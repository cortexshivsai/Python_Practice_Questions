#Find index.
#Method 1:Using index function
t = (10, 20, 30, 40, 50)
print(t.index(30))

#Method 2:Without using index function
t = (10, 20, 30, 40, 50)
for i in range(len(t)):
    if t[i] == 30:
        print("Index:", i)