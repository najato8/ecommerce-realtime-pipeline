# -*- coding: utf-8 -*-
import subprocess
import ast
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter

result = subprocess.check_output([
    'hdfs', 'dfs', '-cat', '/ecommerce/orders/*/part-00000'
])
orders = []
for line in result.strip().split('\n'):
    if line:
        try:
            order = ast.literal_eval(line)
            orders.append(order)
        except:
            pass

print("Total orders: " + str(len(orders)))

countries = Counter(o['country'] for o in orders)
products = Counter(o['product'] for o in orders)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(countries.keys(), countries.values(), color='steelblue')
ax1.set_title('Orders by country')
ax1.set_xlabel('Country')
ax1.set_ylabel('Count')

ax2.bar(products.keys(), products.values(), color='coral')
ax2.set_title('Orders by product')
ax2.set_xlabel('Product')
ax2.set_ylabel('Count')

plt.tight_layout()
plt.savefig('/home/cloudera/ecommerce_stats.png')
print("Done: /home/cloudera/ecommerce_stats.png")
