List =[2,4,5,6,7,8,8,9,767,5,45,5478,3,3,45,56,8,767,7]
#print(List)
max_score = 0
for score in List:
    if score > max_score:
        max_score = score

print(max_score)