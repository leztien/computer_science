



from collections import UserList



class Stack_(UserList):  # backup
    def push(self, item):
        self.data.append(item)


def load_from_github(url):
    from urllib.request import urlopen
    from os import remove
    
    obj = urlopen(url)
    assert obj.getcode()==200,"unable to open"

    s = str(obj.read(), encoding="utf-8")
    NAME = "_temp.py"
    with open(NAME, mode='wt', encoding='utf-8') as fh: fh.write(s)
    module = __import__(NAME[:-3])
    remove(NAME)
    return module


###############################################################

try:
    #raise ConnectionError   # comment this line out
    path = r"https://raw.githubusercontent.com/leztien/computer_science/main/linked_list.py"
    module = load_from_github(path)
    Stack = module.Stack
except:
    Stack = Stack_

###############################################################




def check_parantheses_balance(string):
    stack = Stack()
    for c in string:
        
        if c in "{[(":
            stack.push(c)
        elif c in "}])":
            try:
                popped = stack.pop()
            except IndexError:
                return False
            if popped != {')':"(", ']':"[", '}':"{"}.get(c):
                return False
    return not bool(stack)
    


s = "[(233+4+5)*(2+3)]  -({2*3})(234)"

b = check_parantheses_balance(s)
print(b)
