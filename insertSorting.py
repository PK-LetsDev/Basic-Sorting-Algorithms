import random
import time

def insertionSort(num_list):
    for index in range(1,len(num_list)):
        currenvalue = num_list[index]
        position = index

        while position > 0 and num_list[position-1]>currenvalue:
            num_list[position] = num_list[position-1]
            position = position-1
        num_list[position] = currenvalue


n = 10000
random_integer = random.sample(range(1,n+1),n)


# num_list = [20,34,17,19,4,26,49,9,30]
# insertionSort(num_list)
# print(num_list)

time_starts = time.time()
insertionSort(random_integer)
end_time = time.time()
print (random_integer)

print("time start =",time_starts)
print("time end =",end_time)
print("result = ",end_time - time_starts)