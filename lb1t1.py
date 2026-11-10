data = [10, 20, 30, 40, 50, 60, 70, 80]

print("Початковий список:", data)

print("Додатний індекс [1]:", data[1])
print("Від'ємний індекс [-1]:", data[-1])

print("Зріз 1 [1:6]:", data[1:6])
print("Зріз 2 [-6:-2]:", data[-6:-2])
print("Зріз 3 [::2] (з кроком 2):", data[::2])

data.append(90)
print("Після append(90):", data)

data.insert(2, 25)
print("Після insert(2, 25):", data)

data.pop(3)
print("Після pop(3):", data)

data[1:4] = [99, 100]
print("Після заміни діапазону data[1:4] = [99, 100]:", data)
