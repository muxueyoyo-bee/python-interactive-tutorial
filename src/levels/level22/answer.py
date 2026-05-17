try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零!")
finally:
    print("程序结束")
