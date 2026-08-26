#Count occurrence.
#Method 1: using count function
t = (10, 20, 10, 30, 10, 40)
print(t.count(10))

#Method 2 :Without using count 

t = (10, 20, 10, 30, 10, 40)
count = 0
for num in t:
    if num == 10:
        count += 1
print("Occurrence:", count)