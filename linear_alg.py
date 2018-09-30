#linear_alg

from types import FunctionType

def copy(array:list)->list:
    return [copy(i) if type(i)==list else i for i in array]

def matrix(dim:tuple,default=0)->list:
    return copy(default) if len(dim)==0 else matrix(dim[:-1],[default for i in range(dim[-1])])

def shape(array:list,rec:list=[])->tuple:
    return tuple(rec+[len(array)]) if type(array[0])!=list else shape(array[0],rec+[len(array)])

def flatten(array:list,total:bool=False)->list:
    return (array if total else [array]) if len(array)==0 or type(array[0])!=list else sum([flatten(i,total) for i in array],[])

def reshape(array:list,toShape:tuple)->list:
    out=matrix(toShape);flat=flatten(out);ref=flatten(array,True)
    for i,value in enumerate(ref):
        flat[i//shape(flat)[1]][i%shape(flat)[1]]=value
    return out

def operate(func:FunctionType,array_1:list,array_2:list)->list:
    if shape(array_1)!=shape(array_2): raise ValueError('Matrices must be the same size')
    out=matrix(shape(array_1));op=flatten(out);a_1=flatten(array_1,True);a_2=flatten(array_2,True)
    for i in range(len(a_1)): op[i//shape(op)[1]][i%shape(op)[1]]=func(a_1[i],a_2[i])
    return out

def log(array:list,indent:int=0):
    if len(shape(array))>1:
        print(indent*'\t'+'[')
        for i in array: log(i,indent+1)
        print(indent*'\t'+'],')
        return
    print(indent*'\t'+str(array))
