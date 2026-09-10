def remove_duplicate(d):
    new_dict = {}
    for key, value in d.items():
        if value not in new_dict.values():
            new_dict[key] = value

    return new_dict


d = {}
n = int(input("Enter number of elements: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

result = remove_duplicate(d)

print("Original dictionary:", d)
print("Dictionary after removing duplicate values:", result)
