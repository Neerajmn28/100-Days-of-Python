# Encapsulation is the concept of bundling data (variables) and the methods (functions) that operate on that data into a single unit (a class), and restricting direct access to some of that data.

class Person:
    def __init__(self,name,age):
        self.name = name # public variable
        self.age = age # public variable
        
class Person:
    def __init__(self, name, age):
        self.__name = name # private variable
        self.__age = age # private variable
        
class Person:
    def __init__(self,name,age,gender):
        self._name = name # protected variable
        self._age = age # protected variable
        
    
    
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # make it private using __

    def get_marks(self):      # Safe way to read marks
        return self.__marks

    def set_marks(self, new_marks):  # Safe way to update
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")

# Now use it
student = Student("John", 85)

print(student.get_marks())     # Output: 85

student.set_marks(95)          # Updates safely
print(student.get_marks())     # Output: 95

student.set_marks(-20)         # Won’t allow invalid value