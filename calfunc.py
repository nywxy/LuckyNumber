import math
def Right(data):
    data = str(data)
    data = data[-1:]
    return int(data)

def jxM1(red):
    result = round(sum(red)/17)
    return Right(result)

def jxM2(red):
    result = round(sum(red) / 18)
    return Right(result)

def jxM3(red):
    result = round(sum(red) / 22)
    return Right(result)

def jxM4(red):
    result = round(sum(red) / 23)
    return Right(result)

def jxM5(red):
    result = int((sum(red) / 100)%10)+int((sum(red) / 10)%10)+int((sum(red) % 10))
    return Right(result)

def jxM6(red):
    return Right(abs(red[3]-12))

def jxM7(red):
    if int((sum(red)-red[0])/red[0])>99:
        result = int((sum(red) - red[0]) / red[0]) - 99
    elif int((sum(red)-red[0])/red[0])>66:
        result = int((sum(red) - red[0]) / red[0]) - 66
    elif int((sum(red) - red[0]) / red[0]) > 33:
        result = int((sum(red) - red[0]) / red[0]) - 33
    else:
        result = int((sum(red) - red[0]) / red[0])
    return Right(result)





#测试数据，已18、19、20数据进行
d18 = [8,12,21,22,27,31]
d19 = [3,13,14,16,25,27]
d20 = [3,4,18,26,27,33]
print(jxM1(d18),jxM2(d18),jxM3(d18),jxM4(d18),jxM5(d18),jxM6(d18),jxM7(d18))
print(jxM1(d19),jxM2(d19),jxM3(d19),jxM4(d19),jxM5(d19),jxM6(d19),jxM7(d19))
print(jxM1(d20),jxM2(d20),jxM3(d20),jxM4(d20),jxM5(d20),jxM6(d20),jxM7(d20))
