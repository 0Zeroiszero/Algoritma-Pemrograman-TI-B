def penambahan(a,b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")

def modulus(a, b):
    return a % b

def fibonacci(n):
    angka = []

    if n <= 1:
        return angka
    else:
        print(n - 1)
        print(n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)