
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output.extend(flatten(item))
        else:
            output.append(item)
    return output

data = [[1, 2, 3], 
        [4, [5, 6]],
        [7, [[[[[1, 2, 3], 4]]]]],
        [8, 9]]
print(flatten(data))