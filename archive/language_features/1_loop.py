from datetime import datetime
from numba import njit
#------------------------------------------------------------
def func_test():
    t1 = datetime.now()
    n = 0
    for _ in range(1_000_000_000):
        n += 1

    print(n)
    t2 = datetime.now()
    t_delta = t2 - t1
    print(f"time delta:{t_delta}")    

#------------------------------------------------------------
#------------------------------------------------------------
t1 = datetime.now()
n = 0
for _ in range(1_000_000_000):
    n += 1

print(n)
t2 = datetime.now()
t_delta = t2 - t1
print(f"time delta:{t_delta}")
#------------------------------------------------------------
n=0
t1 = datetime.now()
[ i for i in range(1_000_000_000)]
t2 = datetime.now()
print(n)
t_delta = t2 - t1
print(f"list compreension time delta:{t_delta}")
#------------------------------------------------------------