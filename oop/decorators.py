# s = "Yuvraj Soni"
# def func():
#     global s
#     s = 50
#     print(s)
#     mylocal = 10
#     print(locals())
#     print(globals())
#
#
#     # return 1
#
# func()
# print(s)


# def hello(name='Yuvraj'):
#     return "Hello "+name
#
# print(hello())
#
#
# my = hello
#
# print(my())


# def hello(name='Yuvraj'):
#     print("THe Hello Function Has been Run")
#
#     def greet():
#         return "This String Is Inside Greet"
#
#     def welcome():
#         return "This String os Inside Welcome"
#
#     # print(greet())
#     # print(welcome())
#     # print("End of Hello()")
#     if name == "Yuvraj":
#         return greet
#     else:
#         return welcome
# x = hello()
# print(x())
#
#
#
# # hello()


#
# def hello():
#     return 'Hi Yuvraj Soni'
#
# def other(func):
#     print("Hello")
#     print(func)
# other(hello())


# Decorators
def new_dec(func):

    def wrap_fun():
        print("Code Here Before Executing Func")
        func()
        print("Func() Has Been Called ")
    return wrap_fun()

def func_need():
    print("This Is need of Decorator ")


func_need = new_dec(func_need())
func_need()





