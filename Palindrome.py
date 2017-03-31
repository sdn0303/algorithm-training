# -*- coding:utf-8 -*-


# 回文かどうかを判定する
def palindrome(string):
    if string == string[::-1]:
        print('True')
    else:
        print('False')

string1 = 'abcdefgfedcba'
string2 = 'asifjvbh'
palindrome(string1)
palindrome(string2)
