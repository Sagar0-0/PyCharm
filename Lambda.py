# Lambda functions or anonymous functions
# def add(a, b):
#     return a + b
#
# minus = lambda x, y: x - y
#
# # def minus(x, y):
# #     return x-y
#
# print(minus(9, 4))
def mysort(x):
    return x[2]
a = [[1,3,5],[35,7,8],[0,5,3],[45,2,5],[34,23,6],[512,65,26],[4,2,7]]
a.sort(key=mysort)
print(a)
