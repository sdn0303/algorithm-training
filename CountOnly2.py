# -*- coding:utf-8 -*-

# 0~29の間に2がいくつ存在するかを数えて出現回数の合計を出力する
number = [str(n) for n in range(30)]
num = list(filter((lambda x: x in "2"), ''.join(number)))
print(number)
print(num)
print(len(num))
