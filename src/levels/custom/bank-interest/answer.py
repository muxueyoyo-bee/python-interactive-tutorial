def compound_interest(principal, rate, years):
    total = principal
    for y in range(1, years + 1):
        total *= (1 + rate)
        print(f"第{y}年: {total:.2f} 元")
    return total

result = compound_interest(10000, 0.03, 5)
print(f"5年总收益: {result - 10000:.2f} 元")
