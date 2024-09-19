#-----------------------Functions and Recursions---------------

#WAF to print the length of the list.
# cities = ["Islamabad","Lahore", "Quetta", "Peshawar", "Karachi"]
# animals = ["cow", "buffalo", "goat", "ox"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(animals)

# #WAF to print the item of the list in single line.
# cities = ["Islamabad","Lahore", "Quetta", "Peshawar", "Karachi"]
# animals = ["cow", "buffalo", "goat", "ox"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cities)
# print_list(animals)

#WAF to find the factorial of n.

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(9)

#WAF to convert USD to RS.

def converterpkr(usd_val):
    pkr_val = usd_val * 278
    print(usd_val, "USD", pkr_val, "PKR")

converterpkr(73)

#WAF to convert USD to RS.
def converterinr(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD", inr_val, "INR")

converterinr(73)

#---------------------------------------------------Recursion--------------------------------

