# def greet_user(name):
#     print('Hello ' + name)
#     pass
# greet_user('Vincent')

# def difference(a, b):
#     c = b - a
#     print(c)
#     pass
# difference(3,8)

# def concatenate_list(nums):
#     b = nums
#     c = nums + b
#     print(c)
#     pass
# a = [1,2,3,4]
# concatenate_list(a)

def sleep_assessment(hours):
    if hours < 8:
        print('Oof, go back to bed!')
    elif hours >=8 and hours <=10:
        print("You got a good night's rest!")
    elif hours>10:
        print("You're a sleep prodigy!")
    pass
sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)