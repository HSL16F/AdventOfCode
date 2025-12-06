total_sum = 0

def string_match(val):
    # Converting to string type
    string = str(val)
    length = len(string)
    # check if even length (hence repeat can occur)
    if not (length % 2):
        mid = length//2
        lower = string[:mid]
        upper = string[mid:]
        if lower == upper:
            return val
        else:
            return 0
    return 0


# Get the file inputs
with open("input.txt", "r") as file:
    data = file.readline().split(",")
    for id in data:
        # print(id)
        string_list = id.split("-")
        min_val = int(string_list[0])
        max_val = int(string_list[1])
        for i in range(min_val,max_val):
            total_sum += string_match(i)

print(total_sum)