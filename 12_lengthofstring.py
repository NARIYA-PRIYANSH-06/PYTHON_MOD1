a=str(input("input string: "))
len1=len(a)
print("length width space: ",len1)
count=0
for i in a:
    if i!=' ':
        count=count+1
print("length widthout space: ",count) 