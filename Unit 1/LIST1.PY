# LIST
numbers = [10,20,30,40,50,60]

print("lists:",numbers )

#accessing element

print("First element :", numbers[1])
print("second element :", numbers[4])
print("last element :", numbers[-1])

# ADD ELEMENT

numbers.append(70)
print("adding element:", numbers)

numbers.append(80)
print("adding element:", numbers)

# REMOVE ELEMENT

numbers.remove(10)
print("removeing element :", numbers)

numbers.remove(50)
print("removeing element :", numbers)

# SORTING ELEMENT

numbers.sort()
print("sorted element:", numbers)
