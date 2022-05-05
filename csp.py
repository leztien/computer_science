
"""
simple CSP - no frills
"""

from operator import and_
from functools import reduce


class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables      # set
        self.domains = domains          # dict
        self.constraints = constraints  # callable
        
    def solve(self, assignment=dict()):   # solve = backtrack
        # BASE CASE
        if len(assignment) == len(self.variables):
            return assignment  # full correct assignment
        
        # RECURSIVE CASE
        unassigned = [var for var in self.variables if var not in assignment]
        
        # Select next variable (e.g. with a heuristic)
        variable = unassigned[0]
        
        # Loop ove each value of the current variable
        for value in self.domains[variable]:
            d = assignment.copy()  # d = current assignment
            d[variable] = value
            
            # check constraints
            if self.constraints(d):
                result = self.solve(d)  # result = None or {full assignment}
                if result is not None:
                    return result  # result = full assignment
        
        # None of the values is OK - backtrack
        else:
            return None

#########################################################################

variables = {'A', 'B', 'C', 'D'}
domains = {'A':{1,2,3}, 'B':{1,2,3}, 'C':{1,2,3}, 'D':{1,2,3,4}}
constraint = (('A' != 'B'), ('A' != 'C'), ('A' != 'D'),
              ('B' != 'C'), ('B' != 'D'),
              ('C' != 'D'),  # all diff
              ('A' > 'C'),   # binary constraint
              ('B' != 3))    # unary constraint

# manually deduce the constraints above into a callable
def check_constraint(assignment):
    return reduce(and_, [
        assignment.get('B', 0) != 3,                                # unary constraint
        assignment.get('A', 1) > assignment.get('C', 0),            # binary constraint
        len(assignment.values()) == len(set(assignment.values())),  # all diff
                        ])


csp = CSP(variables, domains, constraints=check_constraint)
assignment = csp.solve()
print("full assignment =", assignment)

