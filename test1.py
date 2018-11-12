# -*- coding: utf-8 -*-
import math
import json


mu_zero = 4 * math.pi * pow(10, -7)
epsilon_zero = 8.854 * pow(10, -12)

with open("materials.json", "r") as material_file:
    data = json.load(material_file)

print(mu_zero)
print(epsilon_zero)
print(data["material"]["Gold"])
print(data["material"]["Bismuth"])

