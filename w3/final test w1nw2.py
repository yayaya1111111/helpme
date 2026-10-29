import json


a = input()

def q1(a):
    a_form = a.split()
    a_dict = []
    for _ in a_form:
        a1 = (_,a_form.count(_))
        a_dict.append(a1)

    print(dict(a_dict))

def q2(a):
    a = input().split()
    res = []
    for i in range(len(a)):
        if a.index(a[i])==i:
            res.append(a[i])
        else:
            pass
    return(res)

def q3(a):
    a_form = a.split()
    ml = 0
    cs = ''
    for i in a_form:
        if len(i)>ml:
            ml = len(i)
            cs = i
        else:
            pass
    return(cs)

def q4(a):
    is_palindrome=False
    for i in range(len(a)//2):
        if a[i]==a[-i-1]:
            is_palindrome = True
        else:
            pass
    return(is_palindrome)

def q5(a):
    
    b = {}
    ap = sum(a.values())/len(a)
    for product in a:
        if product[1] > ap:
            b+=product
    return(b)
q5(a)