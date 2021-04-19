def FindChild(input_str):
    res = []
    if len(input_str) % 2 != 0: return False
    for i in range(0, len(input_str), 2):
        num = int(input_str[i]) + int(input_str[i + 1])
        res.append(str(num))
    return Palindrome(''.join(res))

def Palindrome(input_str):
    idx_delta = 1 if len(input_str) % 2 == 0 else 0
    half = int((len(input_str) + (1 - idx_delta)) / 2) - ( 1 - idx_delta )    
    for i in range(half + ( 1 - idx_delta ), len(input_str)):
        if input_str[i] != input_str[half - (i - half) - idx_delta]:
            if len(input_str) > 1: return FindChild(input_str)
            return False
    return len(input_str) > 1


if __name__ == "__main__":
    i = str(501541)
    result = Palindrome(i)
    print(result)
