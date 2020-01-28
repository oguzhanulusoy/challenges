


list = [-2, -10, 3, 2, 5, 6, 11, 0, 99]

def get_max(list):

    max = 0
    for i in range (0, len(list)):
        if list[i] > max:
            max = list[i]

    return max

def get_min(list):

    min = list[0]

    for i in range (1, len(list)):
        if list[i] <  min:
            min = list[i]

    return min

if __name__ == "__main__":
    get_max(list)