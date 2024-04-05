
import copy
class Something:
    def __init__(self, str_1, int_1, arr_1):
        self.str_1 = str_1
        self.int_1 = int_1
        self.arr_1 = arr_1


x = Something("string_1", 3, [1,2,3,4])
y = copy.deepcopy(x)
print(f'object x: {x.str_1}, {x.int_1}, {x.arr_1}')
print(f'object y: {y.str_1}, {y.int_1}, {y.arr_1}')
y = copy.deepcopy(x)
y.str_1 = "string_2"
y.int_1 = 4
y.arr_1[1] = 1111111
print('----------------')
print(f'object x: {x.str_1}, {x.int_1}, {x.arr_1}')
print(f'object y: {y.str_1}, {y.int_1}, {y.arr_1}')