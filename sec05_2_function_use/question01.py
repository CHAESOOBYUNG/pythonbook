def flatten(example):
    output = []
    for item in example:
        if type(item) == list:
            output.extend(flatten(item))
        else: 
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))