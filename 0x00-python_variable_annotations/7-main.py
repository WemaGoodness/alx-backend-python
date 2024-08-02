#!/usr/bin/env python3

to_kv = __import__('to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
