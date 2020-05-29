# -*- coding: utf-8 -*-
"""digitalroot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19cKRjB8UgVhVvoI7jNhwtQIYO5FKenLL
"""

def digitalroot():
  n=int(input("Enter a number"))
  if n == 0: 
   return 0 
  sum = 0
  while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
  while sum>9:
    if sum==0:
      return 9
    else: 
      return(sum%9)

print(digitalroot())