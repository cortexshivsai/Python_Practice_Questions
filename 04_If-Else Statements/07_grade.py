#Grade calculator.
print("***ENTER YOUR MARKS OF 3 SUBJECTS***")
sub1=int(input("Enter your marks for subject 1: "))
sub2=int(input("Enter your marks for subject 2: "))
sub3=int(input("Enter your marks for subject 3: "))
total=sub1+sub2+sub3
percent=total/3
if percent>=90 and percent<=100:
    print(f"Your Percentage is: {percent} and your Grade is: Distinction")
elif percent>=80 and percent<90:
    print(f"Your Percentage is {percent} and Your Grade is: A")    
elif percent>=50 and percent<80:
    print(f"Your Percentage is {percent} and Your Grade is: B")    
elif percent>=35 and percent<50:
    print(f"Your Percentage is {percent} and Your Grade is: c")    
else:
    print(f"Your Percentage is {percent} and Your Grade is: Fail")    
    
    

