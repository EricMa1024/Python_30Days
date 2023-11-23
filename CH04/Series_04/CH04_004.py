# 學習重點：在不同的型別做資料類型的轉換
# 例如：int 跟 bool 互相轉換

# 一、bool(0) = False
print(bool(0))

# 二、bool(1) = True
print(bool(1))

# 三、bool(3) = True，其他數值都會是True
print(bool(3))
print(bool(-2))

# 四、int(True) = 1； int(False) = 0
print(int(True))
print(int(False))