
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


class Admin(Employee):
    def __init__(self):
        super().__init__('Admin')


class User:
    def __init__(self,username,role="customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))


class Manager(Employee,User):
    def __init__(self):
        super().__init__()
        User.__init__(self,self.id,'Manager')
    def say_id(self):
        User.say_user_info(self)


m1 = Manager()
m1.say_id()
