import copy

# 数字和字符串
# a1 = 1234
# a1 = "evescn"
# a2 = a1
# a3 = copy.copy(a1)
# a4 = copy.deepcopy(a1)
#
# print(id(a1))
# print(id(a2))
# print(id(a3))
# print(id(a4))

# import copy

# # ######### 数字、字符串 #########
# n1 = 123
# # n1 = "i am alex age 10"
# print(id(n1))
#
# # ## 赋值 ##
# n2 = n1
# print(id(n2))
#
# # ## 浅拷贝 ##
# n2 = copy.copy(n1)
# print(id(n2))
#
# # ## 深拷贝 ##
# n3 = copy.deepcopy(n1)
# print(id(n3))



# 其他：列表，元组，字典
a1 = {'name': 'evescn', 'age': 15, 'job': ['author', 'worker']}

a2 = a1
a3 = copy.copy(a1)
a4 = copy.deepcopy(a1)

# print(id(a1))
# print(id(a2))

# print(id(a1))
# print(id(a3))
# print(id(a1['job']))
# print(id(a3['job']))

print(id(a1))
print(id(a4))
print(id(a1['job']))
print(id(a4['job']))



# import  copy
#
# dic = {
#     "cpu": [80,],
#     "mem": [80,],
#     "disk": [80,],
# }
#
# print('old', dic)
#
# new_dic = copy.copy(dic)
# new_dic = copy.deepcopy(dic)
#
# new_dic['mem'][0] = 40
#
# print(dic)
# print(new_dic)

