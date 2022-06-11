#https://python.slides.com/colt/generators-and-decorators

# args (*) gathers all arguments as a tuple
def ensure_correct_info(*args):
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt!"
	return "Note sure who you are"

print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

print(ensure_correct_info(1, True, "Steele", "Colt"))


def sum_all_nums(*nums):
	total = 0
	for num in nums:
		total += num
	return total
	
print(sum_all_nums(4,6,9,4,10))
print(sum_all_nums(4,6))

#kwargs (**) gathers arguments as a dictionary, arguments passed should be in the form of key value though

def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="royal deep amazing purple")

"""
Parameter ordering in a function:
1. parameters
2. args
3. default parameters
4. kwargs

"""

# * can also be used to unpack list or tuples or set
def sum_all_values(*args):
	print(args)
	total = 0
	for num in args:
		total += num
	print(total)

# sum_all_values(1,30,2,5,6)

nums = [1,2,3,4,5,6]
sum_all_values(*nums)

# ** is used to unpack dictionaries
def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data)