def nextNumber(number):
    num_arr = [int(x) for x in str(number)]
    first_idx = 0
    next_highest = 10
    second_idx = 0
    for idx in reversed(range(len(num_arr) - 1)):
        if num_arr[idx] < num_arr[idx+1]:
            first_idx = idx
            break
    for idx in range(first_idx + 1, len(num_arr)):
        if num_arr[idx] > num_arr[first_idx] < next_highest:
            next_highest = num_arr[idx]
            second_idx = idx    
    num_arr[second_idx], num_arr[first_idx] = num_arr[first_idx], num_arr[second_idx]
    num_arr[first_idx + 1:] = sorted(num_arr[first_idx + 1:])
    str_arr = [str(i) for i in num_arr]
    return int(''.join(str_arr))


if __name__ == "__main__":
    number = 65365326543
    print(nextNumber(number))
