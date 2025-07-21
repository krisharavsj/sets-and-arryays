num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y:x+y,num1,num2)
print(list(result))
num3=[7,8,9,0,8]
def square(n):
    return n*n
square1=list (map(square,num3))
print(square1)