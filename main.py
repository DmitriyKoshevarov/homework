fruits = ['apple', 'banana', 'cherry']
for one in fruits:
    print(one)

    names = ['Alice', 'Bob', 'Charlie']
    scores = [85, 90, 95]

    combined = zip(names, scores)
    x = list(combined)
    print(x)