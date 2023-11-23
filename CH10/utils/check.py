# utils/check.py
def getLucky():
    from random import random
    # 取1~7之間的亂數
    return int(random() * 7 +1)