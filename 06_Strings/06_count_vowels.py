string = input("Enter a string: ")
count=0
for i in string:
    if 'a' or 'e' or 'i' or 'o' 'u' or 'A' or 'E' or 'I' or 'O' or 'U' in string:
        count=count+1
    else:
        pass    
print("No.of vowels are: ",count)        
