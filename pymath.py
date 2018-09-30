#PyMath

from types import FunctionType

def gcd(a:int,b:int)->int:
    return b if a%b==0 else gcd(b,a%b)

def lcm(a:int,b:int)->int:
    return int(a*b/gcd(a,b))

def inverse(array:list)->list:
    return [array[i] for i in range(len(array)-1,-1,-1)]

def array(dim:tuple)->list:
    dim=inverse(dim)
    for i in range(len(dim)):
        out=[0 if i==0 else out for j in range(dim[i])]
    return out

def copy(array:list)->list:
    return [copy(i) if type(i)==list else i for i in array]

def div(a:int,b:int)->tuple:
    return (int(a/b),a%b)

def reduce(func:FunctionType,target:list)->list:
    return target[0] if len(target)==1 else reduce(func,[func(target[0],target[1])]+target[2:])
