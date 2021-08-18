import math
def calcv(s):
    vowels = ["a", "e", "i", "o", "u"]
    
    c = 0
    v = 0
    for i in range(len(s)):
        if s[i] in vowels:
            v += 1
        else:
            c += 1
            
    n = abs(c-v)
    return n

def cv(s):
    if len(s) == 1:
        return calcv(s)
   
    x = math.floor(len(s)/2)
    y = len(s) - math.ceil(len(s)/2)
    
    return calcv(s)+cv(s[:x])+cv(s[y:])
    
print(cv("sample"))
