import time
import random

def bubleSort(num_list):
    for outter in range(len(num_list)-1,0,-1):
        for i in range(outter):
            if num_list[i] > num_list[i+1]:
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp

n = 10000
random_interger = random.sample(range(1,n+1),n)

# num_list = [20,34,17,19,4,26,49,9,30]
# bubleSort(num_list)
# print(num_list)

time_starts = time.time()
bubleSort(random_interger)
end_time = time.time()
print(random_interger)

print("time start =",time_starts)
print("time end =",end_time)
print("result = ",end_time - time_starts)


