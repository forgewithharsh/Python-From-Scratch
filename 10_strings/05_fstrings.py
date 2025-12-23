# String formatting

template = "Dear {}, You are awesome. Take this {}$ bag"

a = "Harsh"
a1 = 100000
b = "Harry"
b1 = 200000

s1 = template.format(a,a1)
print(s1)

print(f"Dear {b}, You are awesome. Take this {b1}$ bag")