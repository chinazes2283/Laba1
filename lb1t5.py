import time

sizes = [1000, 10000, 100000]
repeats = 5

print(f"{'Операція':<35} | {'N = 1 000 (мс)':<15} | {'N = 10 000 (мс)':<15} | {'N = 100 000 (мс)':<15}")
print("-" * 88)

results_list_search = []
results_set_search = []
results_dict_search = []
results_list_accum = []
results_set_accum = []

for n in sizes:
    target = n - 1
    
    data_list = list(range(n))
    t_start = time.perf_counter()
    for _ in range(repeats):
        _ = target in data_list
    t_end = time.perf_counter()
    time_list = ((t_end - t_start) / repeats) * 1000
    results_list_search.append(time_list)

    data_set = set(data_list)
    t_start = time.perf_counter()
    for _ in range(repeats):
        _ = target in data_set
    t_end = time.perf_counter()
    time_set = ((t_end - t_start) / repeats) * 1000
    results_set_search.append(time_set)

    data_dict = {i: True for i in range(n)}
    t_start = time.perf_counter()
    for _ in range(repeats):
        _ = target in data_dict
    t_end = time.perf_counter()
    time_dict = ((t_end - t_start) / repeats) * 1000
    results_dict_search.append(time_dict)

    raw_data = list(range(n)) + list(range(n))
    t_start = time.perf_counter()
    unique_list = []
    for item in raw_data:
        if item not in unique_list:
            unique_list.append(item)
    t_end = time.perf_counter()
    time_list_accum = (t_end - t_start) * 1000
    results_list_accum.append(time_list_accum)

    t_start = time.perf_counter()
    unique_set = set()
    for item in raw_data:
        unique_set.add(item)
    t_end = time.perf_counter()
    time_set_accum = (t_end - t_start) * 1000
    results_set_accum.append(time_set_accum)

print(f"{'Пошук елемента в List':<35} | {results_list_search[0]:<15.4f} | {results_list_search[1]:<15.4f} | {results_list_search[2]:<15.4f}")
print(f"{'Пошук елемента в Set':<35} | {results_set_search[0]:<15.4f} | {results_set_search[1]:<15.4f} | {results_set_search[2]:<15.4f}")
print(f"{'Перевірка ключа в Dict':<35} | {results_dict_search[0]:<15.4f} | {results_dict_search[1]:<15.4f} | {results_dict_search[2]:<15.4f}")
print(f"{'Накопичення унікальних у List':<35} | {results_list_accum[0]:<15.4f} | {results_list_accum[1]:<15.4f} | {results_list_accum[2]:<15.4f}")
print(f"{'Накопичення унікальних у Set':<35} | {results_set_accum[0]:<15.4f} | {results_set_accum[1]:<15.4f} | {results_set_accum[2]:<15.4f}")

print("\nПсевдографіка зростання часу для накопичення унікальних у List (O(N²)):")
max_time = max(results_list_accum)
for i, n in enumerate(sizes):
    bar = "*" * int((results_list_accum[i] / max_time) * 40)
    print(f"N = {n:<6} | {bar} ({results_list_accum[i]:.2f} мс)")
