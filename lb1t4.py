group_a = [101, 102, 103, 104, 105, 102, 101]
group_b = [103, 104, 105, 106, 107]
group_c = [103, 104]

set_a = set(group_a)
set_b = set(group_b)
set_c = set(group_c)

print("Множина A (унікальні ідентифікатори):", sorted(set_a))
print("Множина B (унікальні ідентифікатори):", sorted(set_b))

intersection_result = set_a.intersection(set_b)
print("\nПеретин множин (A та B):", sorted(intersection_result))

union_result = set_a.union(set_b)
print("Об'єднання множин (A та B):", sorted(union_result))

symmetric_diff = set_a.symmetric_difference(set_b)
print("Симетрична різниця (A та B):", sorted(symmetric_diff))

is_sub_true = set_c.issubset(set_a)
print(f"\nЧи є C підмножиною A: {is_sub_true}")

is_sub_false = set_b.issubset(set_a)
print(f"Чи є B підмножиною A: {is_sub_false}")

frozen_container = frozenset([1, 2, 3])
items_dict = {frozen_container: "Набір першої категорії"}
print("\nВикористання frozenset як ключа у словнику:", items_dict)
