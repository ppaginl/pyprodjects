class Employee:
    def __init__(self):
        print('employee created')
    def __del__(self):
        print("Destroctor called")
    def create_obj():
        print('making objects ...')
        obj =Employee()
        print('function end ...')
        return obj
print('calling create_obj() function')
obj = Employee.create_obj()
print('program end ...')