import math
def jxM1(red):
    result = 0
    for i in red:
        result+=i
    result = round(result/17)
    while result>0:
        (result,r) = divmod(result,10)
    return r

def jxM2(red):
    result = 0
    for i in red:
        result += i
    result = round(result / 18)
    while result > 0:
        (result, r) = divmod(result, 10)
    return r


