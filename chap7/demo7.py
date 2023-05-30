items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 120  ]

d = {item.upper():price for item, price in zip(items, prices)}
print(d)