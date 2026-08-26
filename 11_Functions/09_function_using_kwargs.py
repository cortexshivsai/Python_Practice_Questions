#Function using **kwargs 
def student(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Rahul", age=20, marks=85)

#**kwargs → multiple keyword arguments   → dictionary