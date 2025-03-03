statement = """hello word
welcome to python
compilied by Lauryn"""
print(statement)


name = "Lauryn"
num = 10
#concutination
print("Hello " + name)
print(name + " is " + str(num) + " years old")
#f formating
print(f"{name}is {num} years old")

print(name + " has " + str(num) + " siblings")
print(f"{name} has {num} siblings")


#math_results = {"name": "John", "score": "45"}
for key, value in math_results.items():
	print(f"{key}: {value}")

def student():
	num = int(input("enter number of entries"))
	capture = {input("enter key:\n"): input("enter value\n")for _index in range(num)}
	print(capture)
student()


#def performance():
	#test1 = 70
	#test2 = 88
#total = test1 + test2
#print(total )