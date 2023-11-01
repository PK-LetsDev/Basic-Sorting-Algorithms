import random
import time

def selectionSort(num_list):
    for fillslot in range(len(num_list)-1, 0, -1):  # Fix the step value
        maxpos = 0
        for location in range(1, fillslot+1):
            if num_list[location] > num_list[maxpos]:
                maxpos = location

        temp = num_list[fillslot]
        num_list[fillslot] = num_list[maxpos]
        num_list[maxpos] = temp

n = 10000
random_integer = random.sample(range(1,n+1),n)

num_list = [7, 1, 6, 8, 2, 33, 11]
selectionSort(num_list)
print(num_list)

time_starts = time.time()
selectionSort(random_integer)
end_time = time.time()
print (random_integer)

print("time start =", time_starts)
print("time end =", end_time)
print("result =", end_time - time_starts)
