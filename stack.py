## Using built in function

from collections import deque 

# stack = deque()
# # print(dir(stack)) 

# stack.append('one')
# stack.append('two')
# stack.append('three')
# stack.append('four')
# # print(stack)
# # print(stack.pop())
# print(stack)



## Create using class
## Stack Implementation 

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    

## Exercise 1 : Reverse the string    

def reverse_string(string):
    # for 
    s = Stack()
    for ch in string:
        s.push(ch)

    rev_str = ''
    # for _ in range(s.size()):
    #     rev_str += s.pop()

    while s.size() != 0:
        rev_str += s.pop()


    return rev_str



## Exercise 2 : Match the brackets

def is_match(ch1, ch2):
    match_dict = {
        "}" : "{",
        "]" : "[",
        ")" : "(",
    }

    return match_dict[ch1] == ch2


def validate_paranthesis(string):
    s = Stack()

    for ch in string:
        if ch == "{" or ch == "[" or ch == "(":
            s.push(ch)

        if ch == "}" or ch == "]" or ch == ")":
            if s.size() == 0:
                return False 
            
            if not is_match(ch, s.pop()):
                return False 
    
    return s.size() == 0
        
    # for ch in s.container




if __name__ == "__main__":
    # r = reverse_string("This is example of Reverse string using Stack!")
    # print(r)
    print(validate_paranthesis("({a+b})"))
    print(validate_paranthesis("))((a+b}{"))
    print(validate_paranthesis("((a+b))"))
    print(validate_paranthesis("((a+g))"))
    print(validate_paranthesis("))"))
    print(validate_paranthesis("[a+b]*(x+2y)*{gg+kk}"))

# s = Stack()
# s.push(2)
# s.push(10)
# s.push(8)
# s.push(15)

# print(s.peek())
# print(s.pop())
# print(s.container)


    

