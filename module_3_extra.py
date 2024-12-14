data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]

def calculate_structure_sum(data_structure):
    total_ = 0
    for i in data_structure:
        if isinstance(i, int):
            total_ += i
        elif isinstance(i, str):
            total_ += len(i)
        elif isinstance(i, list):
            total_ += calculate_structure_sum(i)
        elif isinstance(i, tuple):
            total_ += calculate_structure_sum(i)
        elif isinstance(i, set):
            total_ += calculate_structure_sum(i)

        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, int):
                    total_ += key
                elif isinstance(key, str):
                    total_ += len(key)

                if isinstance(value, int):
                    total_ += value
                elif isinstance(value, str):
                    total_ += len(value)
                elif isinstance(value, (list, tuple, dict)):
                    total_ += calculate_structure_sum(value)
    return total_

result = calculate_structure_sum(data_structure)
print(result)


