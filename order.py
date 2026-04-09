names = [[56, 'e'], [78, 's'], [100, 'f'], [199, 'se'], [588, 'ghoe'], [799,'owh'], [993, 'wohww'],[2222, 'cih']]
x = int(input("enter your number "))
def binary_search(names, x):
    left, right = 0, len(names) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = names[mid][0] 
        if mid_value == x:
            return names[mid][1]
        elif mid_value < x:
            left = mid + 1
        else:
            right = mid - 1
    return "not found"
print(binary_search(names, x))
