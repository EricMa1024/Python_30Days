#字串的各式用法

#一、字串相加，conca
print('a'+'b'+'c')

#二、重複使用字串
print('drum'*3)

#三、取出字串的某一個字
player = 'wembanyama'
print(player[1])

#四、字串切割，以0開始，以4結束，每次跳1
print(player[0:4:1])

#四-1、字串切割，以0開始，以4結束，每次跳2
print(player[0:4:2])

#五、取得字串的長度len
print(len(player))

#五-1、取得字串的長度len，切出來的長度是4
print(len(player[0:4:1]))

Quote = 'Good love is on the way'

#六、用括號內的字串來分割，預設是空白字元
print(Quote.split())

#六-1、用括號內的字串來分割，用逗號來分割
print(Quote.split(','))

#六-2、用括號內的字串來分割，因為.的右邊沒東西，所以會多一個空字串
print(Quote.split('.'))

#七、把Quote的字串切割給CombinedQuotes
CombinedQuotes=Quote.split()
print(CombinedQuotes)

#八、印出來的時候就知道\\是拿來join
d='\\'.join(CombinedQuotes)
print(d)