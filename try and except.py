# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:56:20 2026

@author: ASUS
"""
try:
    a=int(input('Enter the first number:'))
    b=int(input('Enter the second number:'))
    c=a/b
    print(c)
except Exception as e:
    print(e)
else:
    print('Operation successfully completed')
finally:
    print('Thank You!!!')




try:
    a=int(input('Enter the first number:'))
    b=int(input('Enter the second number:'))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Attempt to divide a number by 0")
except ValueError:
    raise ZeroDivisionError("Invalid number entered")
else:
    print('Operation successfully completed')
finally:
    print('Thank You!!!')
