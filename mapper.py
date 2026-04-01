#!/usr/bin/env python3
import sys
for line in sys.stdin:
  fields = line.strip().split(",")
  if len(fields) == 7:  # Ensure proper format
    date, stock, open_price, high, low, close, volume = fields
    if stock != "Stock":  # Skip header row
      print(f"{stock}\t{close}")  # Emit (Stock, Closing Price)