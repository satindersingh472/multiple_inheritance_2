
# create an employee class
class Employee:
    # new_id will 
    new_id = 1
    # it will set the id of an employee to employee.new_id
    # and auto increment the id everytime the code runs
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    # method say_id will define the instance 
    def say_id(self):
        print("My id is {}".format(self.id))

# Admin is inherited from Employee
class Admin(Employee):
    def __init__(self):
        super().__init__('Admin')

# User is the user of an application
class User:
    def __init__(self,username,role="customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))

# in manager class it is assumed that manager is employee and user 
# So manager class is inheriting Employee and user
class Manager(Employee,User):
    def __init__(self):
        super().__init__()
        User.__init__(self,self.id,'Manager')
    def say_id(self):
        super().say_id()
        User.say_user_info(self)


m1 = Manager()
m1.say_id()
