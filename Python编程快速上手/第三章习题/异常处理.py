def devid(num):
    try:
        return 24/num
    except ZeroDivisionError:
        print('input error')

print(devid(2))
print(devid(3))
print(devid(0))