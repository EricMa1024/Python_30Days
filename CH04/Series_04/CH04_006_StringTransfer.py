# 把其他型態  int, float, bool轉換成string

print(str(9))
print(str(97.1))
print(str(True))
print(str(0o11)) #八進位，會先轉換成10進位，再轉成String

#底下是把字串轉回其他型態

print(int('9'))

# print(int('9.1'))，這種方式不對，要轉換成float
print(float('9.1'))

print(bool('3'))

# 想要印出 'We are the world'，而且單引號還要留著，就要用\
# 底下是範例

print('\'We are the world\'')

# 想要換行，就利用\n

print('還君明珠雙淚垂\n恨不相逢未嫁時')

# 同時印出多個字串，需要利用,

print('I\n', 'like', 'music')