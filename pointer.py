print("Integer pointer, the address value is immutable")

num1 = 11
num2 = num1 

print("Value Num1 = ",num1)
print("Value Num2 = ",num2)

print("Address Num1 = ",id(num1))
print("Address Num2 = ",id(num2))

num1 = 22

print("Num1 = ",num1)
print("Num2 = ",num2) 

print("Address Num1 = ",id(num1))
print("Address Num2 = ",id(num2))

print("Dictionaries, the address value is mutable")

dict1 = {
    'value' : 11
}

dict2 = dict1

print("Value dict1 = ",dict1)
print("Value dict2 = ",dict2)

print("Address Num1 = ",id(num1))
print("Address Num2 = ",id(num2))