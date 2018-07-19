
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

PRICE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

PROM = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
}

COMB = {
    'E': (2, 'B', 1),
}


def checkout(skus):
    products = Counter(skus)
    price = 0
    for product, (c, item, reduction) in COMB.items():
        count = products[product]
        if item in products:
            products[item] = max(products[item] - count // c, 0)

    for product, count in products.items():
        if product in PRICE:
            single = PRICE[product]
            if product in PROM:
                remain_count = count
                for prom_th, prom_price in PROM[product]:
                    price += prom_price * (remain_count // prom_th)
                    remain_count = remain_count % prom_th
                price += single * remain_count
            else:
                price += single * count
        else:
            return -1
    return price
