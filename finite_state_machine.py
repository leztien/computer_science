

"""
a simple Finite State Machine
for the regular expression "ab+[cde]"

The states must be defined by the client, otherwise this pattern is quite general (?)
"""


other = ... # any other character


class State:
    # each state is aware of the container where all states are placed
    states_container = set()
    
    def __init__(self, state_number,
                 next_states=dict(),
                 accepting_state=False):
        self.state_number = state_number
        self.next_states = next_states
        self.accepting_state = accepting_state
        self.states_container.add(self)
        
    def next_state(self, char):
        """proceed to the next state depending on the current character"""
        assert type(char) is str and len(char) == 1, "a single character is expected"
        
        # decode the user's dictionary of states
        temp_dict = self.next_states.copy()
        for k,v in self.next_states.items():
            if (type(k) is str) and len(k) > 1:
                temp_dict.update({c:v for c in k})
        
        # get the next state 
        next = temp_dict.get(char, temp_dict.get(other, 0))
        
        # if it is of class State then return it
        if type(next) is type(self):
            return next
        
        # otherwise find the state by the number provided by the client
        for state in self.states_container:
            if state.state_number == next:
                return state
    
    def __repr__(self):
        return self.__class__.__name__ + f"({self.state_number})"


            
def search(starting_state, string):
    """immitates the re.search(pattern, string)"""
    match, start = "", None
    state = starting_state
    
    for i,c in enumerate(string):
        match += c
        start = start if start is not None else i
        
        state = state.next_state(c)
        
        if state.state_number == 0:
            match = ""
            start = None
            continue
        
        if state.accepting_state == True:
            return (match, start, i)  # i = end           
        
 
def parse_regex(pattern_as_string):
    """the code is a bit hackinsh but does seem to do the job"""
    splits = []
    
    k = -1
    s = ""
    
    while k < len(pattern) - 1:
        k += 1
        
        if pattern[k] == '[':
            k += 1
            while pattern[k] != ']':
                s += pattern[k]
                k += 1
            splits.append(s)
            s = ""
            continue
        
        if pattern[k] == '+':
            s = "+"
        
        else:
            s += pattern[k]
            splits.append(s)
            s = ""
    if s == '+':
        splits.append('+')  
    return splits



def make_finite_state_machine(splits: "list of strings"):
    
    State.states_container.clear()
    
    states = []
    
    for i,s in enumerate(splits):
        d = dict()
        
        if s[0] == '+':
            d = states[i-1].next_states.copy()
            s = s[1:]
        
        if s:
            d.update({s: i+1})
        
        
        node = State(i, d)
        states.append(node)
    states.append(State(i+1, accepting_state=True))
    return states



def decode_regex(pattern_as_string):
    """wrapper function"""
    splits = parse_regex(pattern_as_string)
    states = make_finite_state_machine(splits)
    return states[0]



#########################################################

pattern = "ab+[cde]"

starting_state = decode_regex(pattern)


string = "...abbabc.."
match = search(starting_state, string)
print(match)



# Test
import re
match = re.search(pattern, string)
if match:
    print( (match.group(), match.start(), match.end()-1) )  # re.macth.end = end + 1 (apparently)








"""
# Here the states are defined manually (ideally it must be done algorithmically - how?)
s0 = State(0, {'a': 1, other: 0}, False)
s1 = State(1, {'b': 2, other: s0}, False)
s2 = State(2, {'b': 2, "cde": 3}, False)  # "forgot" to define the default 'other'
s3 = State(3, accepting_state=True)



#ab+[cde]
# [ab]+c  # ababaabbc

s0 = State(0, {"ab": 1})
s1 = State(1, {"ab":1, 'c':2})
s2 = State(2, accepting_state=True)



pattern = r"ab+[cde]"
pattern = "[ab]+c"



s0 = decode_regex(pattern)
print(s0, pattern)


print("##################")





# Example
string = "...baaaababaabbcXx"

match = search(s0, string)
print(match)


# Test
import re
pattern = r"[ab]+c"
match = re.search(pattern, string)
if match:
    print( (match.group(), match.start(), match.end()) )  # re.macth.end = end + 1 (apparently)

"""




