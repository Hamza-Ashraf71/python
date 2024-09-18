# #print numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# #print no from 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1


#print the multipication table of level n.
# n = int(input("enter number"))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

#Print the following list using a loop.
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0

# while i < len(nums):
#     print(nums[i])
#     i += 1

    #Search for a number x from tuple using loop.

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36    
# i = 0 #initilaization

# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx", i )
#     else:
#         print("finding...")

#     i += 1    
        

#print the elements of the following list using the for loop

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for el in nums:
#     print(el)



#Search for a number x from tuple using for loop.

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

# x = 49
# i = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", i)

#     i += 1


#print 1 to 100 numbers using range.

# for i in range(1, 101):
#     print(i)
       
#print 100 to 1 numbers using range.

# for i in range(100, 0, -1):
#     print(i)

# print the table of n

# num = int(input("enter number :"))

# for i in range(1, 11):
#     print(num * i)


#WAP to print the sum of n natural numbers using while loop.

n = 9
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print("sum of numbers :", sum)

#WAP to find the factorial of first n numbers using for loop.

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial :", fact)