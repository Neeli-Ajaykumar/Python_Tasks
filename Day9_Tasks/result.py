"""Student Result Generator (Method Overloading Concept) 
A school system calculates student results differently depending on available data. 
Create a Result class where a method can calculate the result using either two 
subjects or three subjects."""

class Result:
    def calculate(self, sub1, sub2):
        total = sub1 + sub2
        average = total / 2
        
        print("Result for 2 subjects:")
        print("Total:", total)
        print("Average:", average)
        
    def calculate1(self, sub1, sub2, sub3):
        total = sub1 + sub2 + sub3
        average = total / 3
        
        print("Result for 3 subjects:")
        print("Total:", total)
        print("Average:", average)


r = Result()
r.calculate(50,60)
print("------------------")
r.calculate1(50,60,70)
