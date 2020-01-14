list = [2, 4, 5, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def count_unique(list):
    print(len(count_unique_values(list)))

def count_unique_values(list):
    unique_values = []

    for i in range (0, len(list)):
        if not unique_values.__contains__(list[i]):
            unique_values.append(list[i])

    return unique_values

if __name__ == "__main__":
    count_unique(list)