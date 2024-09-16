test_data = [x for x in range(1, 2000)]  # The algorythm works well with big lists which MUST be ordered
target_num = 475


def binary_search(data, target):
    start_index = 0
    steps = 0
    end_index = len(data) - 1
    while start_index <= end_index:
        steps += 1
        middle = (start_index + end_index) // 2
        if data[middle] == target:
            return middle, steps
        elif data[middle] < target:
            start_index = middle + 1
        else:
            end_index = middle - 1

    return -1, steps


result, steps_count = binary_search(test_data, target_num)

if result != -1:
    print(f'Target index: {result}. Steps: {steps_count}')
else:  # if the result is -1 it means that the target is not found in the list
    print('Target not found')
