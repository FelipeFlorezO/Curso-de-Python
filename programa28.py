def increment(x):
    return x + 1

increment_v2 = lambda x: x+1

def higher_order_function(x, func):
    return x + func(x)
higher_order_function_v2 = lambda x, func: x + func(x)
result = higher_order_function(2, increment)

print(result)

result = higher_order_function_v2(2, increment_v2)
print(result)
result = higher_order_function_v2(2, lambda x: x+2)
print(result)


    