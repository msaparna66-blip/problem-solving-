def print_rangoli(size):
    import string

    letters = string.ascii_lowercase

    for i in range(size - 1, -size, -1):
        row = letters[size-1:abs(i):-1] + letters[abs(i):size]
        print("-".join(row).center(4 * size - 3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
