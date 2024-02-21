from datetime import datetime

l = []
start = datetime.now()
for i in range(10001):
    l.append(i)
time = datetime.now() - start
print(time.total_seconds())
