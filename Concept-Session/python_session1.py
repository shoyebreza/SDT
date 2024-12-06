
name = "Hello World"


#for char in name:
#    print(char, end=",")


#for i in range(len(name)):
#    print(name[i])

#for i, char in enumerate(name):
#    print(f"index : {i} value : {char}")


#number = [1,2,3,4,5,6,7,8,8,9]
#for num in number:
#    print(num)



#def result(name, *args):
#    sums =0
#    for num in args:
#        sums +=num
#    print(f"name : {name}, marks : {sums}")

#result("shakib khan", 10,20,30,40)


#conditions


""" a = 5
b = 10

if a > b:
    print('A is bigger')
elif a==0:
    print('A is zero')
elif b==0:
    print('B is zero')
else:
    print('B is bigger') """



""" nums = [10,20,30,40]

if 20 in nums:
    print("Number is present")
else:
    print('Number is not present') """


""" string = "asdbfghjkerct"

if 'asd' in string:
    print('ase')
else:
    print('Nai') """



#function

""" def square(n):
    return n*n

result = square(10)
print(result) """



""" start in 40 min """

#Scope 
""" x = 10
def func():
    global x
    x = 20 #local variable
    print("inside function", x)

func()

print("outside function", x) """


# list comprenshion

#nums = [1,2,3,4,5,67,8,9]
""" for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print(nums) """



""" square_nums = [num**2 for num in nums]
print(square_nums) """

""" nums = [1,2,3,4,5,67,8,9]
odd_nums = []

for num in nums:
    if num % 2 ==1:
        odd_nums.append(num)
print(odd_nums) """


#way 2
""" nums = [1,2,3,4,5,67,8,9]


odd_nums = [num for num in nums if num % 2 ==1]
print(odd_nums) """


# input number

""" n = int(input("Input number "))
2
print(n)
print(type(n))
 """


""" num = []
n   = int(input())

for i in range(n):
    x = int(input())
    num.append(x)
print(num) """

""" n = int(input())
arr = input().split()
print(arr) """


""" for i in range(len(arr)):
    arr[i] = int(arr[i]) """

# way 2




""" 
arr = input()
int_arr = [int(x) for x in arr]
 """

""" def square(x):
    return x*x

nums = [1,2,3,4,5]
square_nums = list(map(square, nums))
print(square_nums) """


""" arr = input().split()
def conv_int(x):
    return int(x)

input_arr = list(map(conv_int, arr))
print(input_arr) """



""" arr = input().split()
input_arr = list(map(int, arr))
print(input_arr)  """


arr = list(map(int, input().split()))
print(arr)








 