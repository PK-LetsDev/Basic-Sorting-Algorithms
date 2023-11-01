import time
import random
import matplotlib.pyplot as plt

def bubbleSort(num_list):
    for outter in range(len(num_list)-1,0,-1):
        for i in range(outter):
            if num_list[i] > num_list[i+1]:
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp

def selectionSort(num_list):
    for fillslot in range(len(num_list)-1, 0, -1):  # Fix the step value
        maxpos = 0
        for location in range(1, fillslot+1):
            if num_list[location] > num_list[maxpos]:
                maxpos = location

        temp = num_list[fillslot]
        num_list[fillslot] = num_list[maxpos]
        num_list[maxpos] = temp

def insertionSort(num_list):
    for index in range(1,len(num_list)):
        currenvalue = num_list[index]
        position = index

        while position > 0 and num_list[position-1]>currenvalue:
            num_list[position] = num_list[position-1]
            position = position-1
        num_list[position] = currenvalue

# Initialize lists to store data
sorting_algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
execution_times = {alg: [] for alg in sorting_algorithms}
data_sizes = list(range(2000, 10001, 2000))

# Test and measure execution times for each sorting method 10 times
num_tests = 10
for n in data_sizes:
    average_times = {alg: 0 for alg in sorting_algorithms}

    for _ in range(num_tests):
        random_integer = random.sample(range(1, n + 1), n)

        for algorithm in sorting_algorithms:
            random_copy = random_integer.copy()
            time_start = time.time()

            if algorithm == 'Bubble Sort':
                bubbleSort(random_copy)
            elif algorithm == 'Selection Sort':
                selectionSort(random_copy)
            elif algorithm == 'Insertion Sort':
                insertionSort(random_copy)

            execution_time = time.time() - time_start
            average_times[algorithm] += execution_time

    for algorithm in sorting_algorithms:
        average_times[algorithm] /= num_tests
        execution_times[algorithm].append(average_times[algorithm])

# Create line charts for each sorting algorithm
for algorithm in sorting_algorithms:
    plt.plot(data_sizes, execution_times[algorithm], marker='o', label=algorithm)

plt.xlabel('Data Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Comparison of Sorting Algorithms (Averaged Over 10 Tests)')
plt.legend()
plt.grid(True)
plt.show()