import random
import time

for i in range(6) :
    print(random.randint(1,45))

start = time.perf_counter()

count = 0 
for i in range(1000000):
    count +=1

end = time.perf_counter()
print(end - start)