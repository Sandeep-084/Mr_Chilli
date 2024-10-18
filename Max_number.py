import random

number = (12,34,3,34,45,56,6,1,35,6,0,98,78,67,54,34,1,26,37,7,4,87)
max_number = 0
for score in number:
    if score > max_number:
        max_number = score
print(max_number)

