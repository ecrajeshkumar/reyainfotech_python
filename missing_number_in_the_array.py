

def find_missing(input_list):
    sum_of_elements = sum(input_list)
    n = len(input_list) + 1
    actual_sum = (n * (n + 1)) / 2
    return int(actual_sum - sum_of_elements)

list_1 = [1,5,6,3,4]

print("Missing number: ", find_missing(list_1)) # 2
