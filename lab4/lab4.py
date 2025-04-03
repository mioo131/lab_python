def repeat(times):
    def decorator(func):
        def wrapper(value):
            results = []
            for k in range(times):
                results.append(func(value))
            return results
        return wrapper
    return decorator

def make_calc(operation, initial=0):
    def calc(value):
        nonlocal initial # меняем переменную во внешней функции
        if operation == '+':
            initial += value
        if operation == '-':
            initial -= value
        if operation == '*':
            initial *= value
        if operation == '/':
            if value != 0:
                initial /= value
            else:
                raise ValueError("нельзя делить на 0")
        return initial
    return calc

calculator = make_calc("*", initial=1)

@repeat(3)
def calc(value):
    return calculator(value)

print(calc(5))
print(calc(2))