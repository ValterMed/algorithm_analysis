#First we import the libraries random, time and matplotlib
import random
import time
import matplotlib.pyplot as plt

def main():
    #We declare the main set as a set of 1000 random integers from -100 and 100, then we declare the 3 subsets we'll use and the sum variables to compare
    mainset = [random.randint(-100, 100) for _ in range(1000)]
    lastsubset = []
    greatestsubset = []
    negativesubset = []
    sumay = 0
    sumaz = 0
    #We print the main set to check if our code works
    print(mainset)
    #We declare our axes for graphing later
    execution_times = []
    elements_read = []
    #Now we iterate for each item on our main set and append the positive values to our lastsubset, the negative values are ignored and every time one appears, we compare our lastsubset with our greatestsubset
    #If the lastsubset is greater, it replaces the greatestsubset
    #When we find a negative value, the lastsubset is deleted, except in the case that we find more than 1 negative value in a row, we don't compare again
    #The code also measures the time it takes for each iteration (in microseconds)
    for i in range(len(mainset)):
        start_time = time.time()* 1e6
        if mainset[i] >= 0:
            lastsubset.append(mainset[i])
            sumay = sum(lastsubset)
            del negativesubset[:]
        elif mainset[i] < 0:
            negativesubset.append(mainset[i])
            if len(negativesubset) > 1:
                if i == 0:
                    execution_times.append((end_time - start_time))
                else:
                    execution_times.append((end_time - start_time + execution_times[i - 1]))
                elements_read.append(i + 1)
                continue
            if sumay > sumaz:
                greatestsubset = lastsubset.copy()
                sumaz = sum(greatestsubset) 
            del lastsubset[:] 
        end_time = time.time()* 1e6
        if i == 0:
            execution_times.append(end_time - start_time)
        else:
            execution_times.append(end_time - start_time + execution_times[i - 1])
        elements_read.append(i + 1)
    #We graph the elements read against the time of execution
    plt.plot(elements_read, execution_times)
    plt.xlabel('Number of elements read')
    plt.ylabel('Time (microseconds)')
    plt.title('Execution Time vs. Number of Elements Read')
    plt.show()
    #Finally, we print our results
    print("Greatest Subset:", greatestsubset)
    print("Sum of Greatest Subset:", sum(greatestsubset))

if __name__ == "__main__":
    main()