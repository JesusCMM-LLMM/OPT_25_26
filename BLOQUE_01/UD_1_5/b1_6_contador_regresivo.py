try:
    num = int(input("Introduce un número: "))
    while (num >= 0):
        print(f"{num}.. ")
        num = num - 1

except ValueError:
    print("Necesito un valor numérico")