
# create an employee class
class Employee:
    # new_id will 
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}".format(self.id))

e1 = Employee()


