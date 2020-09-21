from time import gmtime, strftime
import time
def smart_divide(func):
    def inner(a, b):
        time_sec = int(strftime("%S", gmtime())) 
        if time_sec % 2 != 0:
            # print(f"Odd Second {time_sec}")
            return func(a, b), {time_sec}, True
        else:
            return func(a, b), {time_sec}, False
    return inner

def logging_func_details(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        time_detail = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        msg = (f'{fn.__name__} method has been called {cnt} times accessed at {time_detail} with arguments {args}')
        return fn(*args, **kwargs), msg
    return inner









# def set_password():
#     password = ''
#     def inner():
#         nonlocal password
#         if password == '':
#             password = input()
#         return password
#     return inner

# current_password = set_password()
# current_password()

# def authenticate(fn, current_password, user_password):
#     cnt = 0
#     if user_password == current_password():
#         def inner(*args, **kwargs):
#             nonlocal cnt
#             cnt += 1
#             print(f'{fn.__name__} was called {cnt} times')
#             return fn(*args, **kwargs)
#         return inner
#     else:
#         print('You scamster!!')

# def add(a, b):
#     return a + b
# def mult(a, b):
#     return a * b

# auth_add = authenticate(add, current_password, 'secret')
# print(auth_add(2, 3))