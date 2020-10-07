import math

math_one = abs(int(input()))
math_two = abs(int(input()))
math_three = abs(int(input()))

desks = (math_one // 2 + math_one % 2 + math_two // 2 + math_two % 2 + math_three // 2 + math_three % 2)
upd_desks = math.ceil(desks)

if isinstance(desks, int):
    print(desks)
elif isinstance(desks, float):
    print(upd_desks)
else:
    print("Error")
