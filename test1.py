# -*- coding: utf-8 -*-
import math
import json


mu_zero = 4 * math.pi * pow(10, -7)

with open("materials.json", "r") as material_file:
    data = json.load(material_file)

print(mu_zero)
print(data["material"]["Gold"])

