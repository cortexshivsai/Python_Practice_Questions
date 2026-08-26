#Find Minimun 
#Method 1
# l=[123,456,231,867,908,453,235,120,871]
# print(f"Maximum Number is: {min(l)}")

#Method 2
l = list(map(int, input("Enter Numbers separated by spaces: ").split()))

minimum = l[0]

for num in l:
    if num < minimum:
        minimum = num

print("Minimum element:", minimum)