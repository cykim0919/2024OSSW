def compute_y(a, b, x):
    return a ** 2 * x + b

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    max_x = int(input("Max: "))
    for x in range(0, max_x + 1):
        y = compute_y(a, b, x)
        print(f"{a}x{a}x{x} + {b} = {y}")
if __name__ == "__main__":
    main()
