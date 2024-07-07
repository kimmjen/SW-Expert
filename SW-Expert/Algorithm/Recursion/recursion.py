def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():
    test_cases = [9, 12, 20]

    for i, n in enumerate(test_cases, start=1):
        print(f"Test case {i}: {n}! = {factorial(n)}")


if __name__ == "__main__":
    main()