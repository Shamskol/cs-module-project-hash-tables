# bytes_representation = "hello".encode()

# for byte in bytes_representation:
#     print(byte)

### Print Output
### 104
### 101
### 108
### 108
### 111

def my_hashing_func(str):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum
sum_1 = my_hashing_func("kolade")
print(sum_1)
