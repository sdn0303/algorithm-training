# -*- coding:utf-8 -*-


# 与えられた文字列に重複する文字が含まれているかどうかを判定
def judge(w):
    counter = {}
    flag = False

    for s in w:
        if s not in counter:
            counter[s] = 1
        else:
            counter[s] += 1
            flag = True
    print(flag)

a = "abcdefg"
b = "aadabbfcdfghdggfg"
judge(a)
judge(b)
