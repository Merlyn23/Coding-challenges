str=input("enter a string:")
u=0
l=0
for i in str:
  if(i.isupper()):
    u+=1
  elif(i.islower()):
    l+=1
print("No of uppercase letters:",u)
print("No of lowercase letters:",l)