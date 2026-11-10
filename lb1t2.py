def unpack_record(record):
    item_id, name, quantity, price = record
    return f"ID: {item_id}, Товар: {name}, Кількість: {quantity}, Ціна: {price}"

def calculate_total_value(records):
    total = 0
    for record in records:
        quantity = record[2]
        price = record[3]
        total += quantity * price
    return total

inventory = [
    (1, "Ноутбук", 5, 25000),
    (2, "Миша", 15, 650),
    (3, "Клавіатура", 10, 1200)
]

print("Початкові записи:", inventory)

print("\nРозпакування першого запису:")
print(unpack_record(inventory[0]))

total_value = calculate_total_value(inventory)
print("\nЗагальна вартість:", total_value)

print("\nДемонстрація імутабельності кортежу (спроба зміни викликає помилку):")
# inventory[0][0] = 99  # Якщо розкоментувати цей рядок, Python видасть TypeError

complex_record = (1, "Ноутбук", [25000, 24500])
print("\nКортеж з мутабельним списком всередині:", complex_record)

complex_record[2].append(24000)
print("Після зміни внутрішнього списку:", complex_record)
