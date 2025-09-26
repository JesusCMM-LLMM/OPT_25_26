try:
    num = int(input("Introduce el número: "))
    for i in range (1,11):
        print(f"({num} multiplicado por {i} es {num * i})")

except ValueError:
    print("Necesito un valor numérico")