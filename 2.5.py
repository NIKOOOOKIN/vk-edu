def map(func, seq):
    for item in seq:
        yield func(item)

# Пример использования
func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
    print(x)