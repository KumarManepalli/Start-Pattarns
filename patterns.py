num=int(input("enter the inputs:"))
# 1.half triangle:
for i in range(num):
    for j in range(i+1):
        print("*",end=" ")
    print()
#2.reverse half right triange:
for i in range(num):
    for j in range(i,num):
        print("*",end=" ")
    print()

#3. reverse right angle triangel:
for i in range(num):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,num):
        print("*",end=" ")
    print()

# peyramid
for i in range(num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

# reverse pyramid:
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,num-1):
        print("*",end=" ")
    for j in range(i,num):
        print("*",end=" ")
    print()

# dimond shap:
for i in range(num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,num-1):
        print("*",end=" ")
    for j in range(i,num):
        print("*",end=" ")
    print()
#butterfly shap:
for i in range(num):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,num-1):
        print(" ",end=" ")
    for j in range(i,num-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(num):
    for j in range(i,num):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,num):
        print("*",end=" ")
    print()
ractangle :
for i in range(num):
    for j in range(num):
        print("*",end=" ")
    print()
