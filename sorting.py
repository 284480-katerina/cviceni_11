import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def bubble_sort(numbers):

    numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers



def main():
    test = random_numbers(20)
    print (test)

    bubble_1 = (bubble_sort(test))
    print (bubble_1)

    bubble_2 = (bubble_sort([5, 1, 4, 2, 8]))
    print (bubble_2)

if __name__ == '__main__':
    main()