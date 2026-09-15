def greet(SAM):
    return f"Hello, {SAM}! Welcome to Git version control demo."

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(greet("Student"))
    result = add_numbers(5, 7)
    print(f"5 + 7 = {result}")
