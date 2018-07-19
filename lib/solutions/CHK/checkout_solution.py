
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

PRICE = {
    'A': (50, 3, 130),
    'B': (30, 2, 45),
    'C': (20, None, None),
    'D': (15, None, None),
}


def checkout(skus):
    products = Counter(skus)
    price = 0
    for product, count in products.items():
        if product in PRICE:
            single, prom, prom_price = PRICE[product]
            if prom:
                price += (single * (count % prom) + prom_price * (count // prom))
            else:
                price += single * count
        else:
            return -1
    return price
