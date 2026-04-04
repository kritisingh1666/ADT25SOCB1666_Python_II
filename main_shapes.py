# main_shapes

import shapes

print("1 : circle")
print("2 : rectangle")
print("3 : triangle")

choice = input("Enter your choice: ")

if choice == '1':
    r = float(input("Enter the radius of the circle: "))
    area = shapes.circle_area(r)
    print(f"The area of the circle is {area} square units")

elif choice == '2':
    l = float(input("Enter length of the rectangle: "))
    b = float(input("Enter the breadth of the rectangle: "))
    area = shapes.rectangle_area(l, b)
    print(f"The area of the rectangle is {area} square units")

elif choice == '3':
    l = float(input("Enter the length of the trianlge: "))
    w = float(input("Enter the width of the triangle: "))
    area = shapes.triangle_area(l, w)
    print(f"The area of the triangle is {area} square units")

else:
    print("choice invalid")


