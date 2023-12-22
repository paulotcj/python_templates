from datetime import datetime
t1 = datetime.now()
n = 0
for _ in range(1_000_000_000):
    n += 1

print(n)
t2 = datetime.now()
t_delta = t2 - t1
print(f"time delta:{t_delta}")