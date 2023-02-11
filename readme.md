This is exercise for multiple inheritance <br>

### create an application related to an organization which have employees and then divide those employees into admin and manager

create a class named **Employee** <br>
def __init__ method so that Employee instance will get created <br>
employee will have id which is auto increment <br>
def a method called say_id(self) which can say something about that particular instance <br>




create a class named **Admin**  <br>
def __init__ method <br>
Admin should be inherited from class **Employee** but there should be some difference that admin can define <br>


create a class named **User** <br>
def __init__ method with self, username and role as parameters <br>
def say_user_info() method which will describe the user <br>
by default user is the customer so role will be customer as default value <br>

create a class called **Manager** <br>
this class should be inherited from **Employee** and **user** 
which means a manager can be a user of the application and employee of an organization<br>
now describe the id of the manager and role of the manager as a user <br>