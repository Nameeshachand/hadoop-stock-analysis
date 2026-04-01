#!/usr/bin/env python3
import sys

current_stock = None
max_price = 0

for line in sys.stdin:
    stock, price = line.strip().split("\t")
    price = float(price)

    if current_stock == stock:
        max_price = max(max_price, price)
    else:
        if current_stock is not None:
            print(f"{current_stock}\t{max_price}")
        current_stock = stock
        max_price = price

# last stock print
if current_stock is not None:
    print(f"{current_stock}\t{max_price}")
