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

def jxM8(red):
    if int((sum(red) - red[1]) / red[1]) > 33:
        result = int((sum(red) - red[1]) / red[1]) - 33
    else:
        result = int((sum(red) - red[1]) / red[1])
    return Right(result)

def jxM9(red):
    return Right(int((sum(red) - red[2]) / red[2]))

def jxM10(red):
    return Right(int((sum(red) - red[3]) / red[3]))

def jxM11(red):
    return Right(int((sum(red) - red[4]) / red[4]))

def jxM12(red):
    return Right(int((sum(red) - red[5]) / red[5]))

def jxM13(red):
    return Right((sum(red) - red[0]) % red[0])

def jxM14(red):
    return Right((sum(red) - red[1]) % red[1])

def jxM15(red):
    return Right((sum(red) - red[2]) % red[2])

def jxM16(red):
    return Right((sum(red) - red[3]) % red[3])

def jxM17(red):
    return Right((sum(red) - red[4]) % red[4])

def jxM18(red):
    return Right((sum(red) - red[5]) % red[5])

def jxM19(red):
    return Right(int(math.pow(red[0]*red[1],1/2)))

def jxM20(red):
    return Right(int(math.pow(red[1]*red[2],1/2)))

def jxM21(red):
    return Right(int(math.pow(red[2]*red[3],1/2)))

def jxM22(red):
    return Right(int(math.pow(red[3]*red[4],1/2)))

def jxM23(red):
    return Right(int(math.pow(red[4]*red[5],1/2)))

def jxM24(red):
    return Right(int(math.pow(red[0]*red[5],1/2)))

def jxM25(red):
    return Right(int(math.pow(red[0]*red[2],1/2)))

def jxM26(red):
    return Right(int(math.pow(red[0]*red[3],1/2)))

def jxM27(red):
    return Right(int(math.pow(red[0]*red[4],1/2)))

def jxM28(red):
    return Right(int(math.pow(red[1]*red[3],1/2)))

def jxM29(red):
    return Right(int(math.pow(red[1]*red[4],1/2)))

def jxM30(red):
    return Right(int(math.pow(red[1]*red[5],1/2)))

def jxM31(red):
    return Right(int(math.pow(red[2]*red[4],1/2)))

def jxM32(red):
    return Right(int(math.pow(red[2]*red[5],1/2)))

def jxM33(red):
    return Right(int(math.pow(red[3]*red[5],1/2)))

def jxM34(red,blue):
    if red[5]+blue <= 33:
        result = red[5]+blue
    else:
        result = red[5]+blue-33
    return Right(result)

def jxM35(red,blue):
    return Right(round((red[1]+red[2]+red[3]+red[4]+blue)/6,0))

def jxM36(red,blue):
    return Right(red[1]+blue)

def jxM37(red):
    return Right(red[5]-red[1]+1)

def jxM38(red):
    if red[1]+red[5]+1 <=33:
        return Right(red[1]+red[5]+1)
    else:
        return Right(red[1]+red[5]+1-33)

def jxM39(red):
    if red[5]-red[1]+10 <=33:
        return Right(red[5]-red[1]+10)
    else:
        return Right(red[5]-red[1]+10-33)

def jxM40(red):
    return Right(red[0]+red[1])

def jxM41(red):
    if red[3]+red[0] > 33:
        return Right(red[3]+red[0] -33)
    else:
        return Right(red[3]+red[0])

def jxM42(red):
    return Right(red[3]-red[0]+7)


def jxM43(red):
    return Right(int(sum(red[2:6])/4))

def jxM44(red):
    return Right(int(sum(red[:3])/3))

def jxM45(red):
    if red[1]+red[2] <= 33:
        return Right(red[1]+red[2])
    else:
        return Right(red[1]+red[2]-33)

def jxM46(red):
    return Right(abs(red[4]-red[3]+10))

def jxM47(red):
    return Right(red[0]+12)

def jxM48(red):
    return Right(red[1]-red[0])

def jxM49(red):
    return Right(red[2]-red[0])

def jxM50(red):
    return Right(red[3]-red[0])

def jxM51(red):
    return Right(red[4]-red[0])

def jxM52(red):
    return Right(red[5]-red[0])



























#测试数据，已18、19、20数据进行
d18 = [8,12,21,22,27,31]
d19 = [3,13,14,16,25,27]
d20 = [3,4,18,26,27,33]
print(jxM1(d18),jxM2(d18),jxM3(d18),jxM4(d18),jxM5(d18),jxM6(d18),jxM7(d18))
print(jxM1(d19),jxM2(d19),jxM3(d19),jxM4(d19),jxM5(d19),jxM6(d19),jxM7(d19))
print(jxM1(d20),jxM2(d20),jxM3(d20),jxM4(d20),jxM5(d20),jxM6(d20),jxM7(d20))
