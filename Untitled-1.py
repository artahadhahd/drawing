def draw(x: int):
    format = [i for i in range(1, x+1)]
    # == format = list(range(1, x + 1))
    for i in range(x-1, -1, -1):
        print(format[x-1-i] * ' ' + format[i] * '*')

    for n in range(2,x+1):
        print(x * ' ' + n * '*')

def main():
    draw(10)


if __name__ == '__main__':
    main()
    