#Amaan Muhammad
#PSID: 1607608

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        ind = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[ind]:
                ind = j
        numbers[i], numbers[ind] = numbers[ind], numbers[i]
        print(' '.join([str(x) for x in numbers]), '')
    return numbers


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)