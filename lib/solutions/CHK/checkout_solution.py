
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

PRICE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,

}

PROM = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
    'H': [(10, 80), (5, 45)],
    'K': [(2, 150)],
    'P': [(5, 200)],
    'Q': [(3, 80)],
    'V': [(3, 130), (2, 90)],

}

COMB = {
    'E': (2, 'B', 1),
    'F': (2, 'F', 1),
    'N': (3, 'M', 1),
    'R': (3, 'Q', 1),
    'U': (3, 'U', 1),
}


def checkout(skus):
    products = Counter(skus)
    price = 0
    for product, (c, item, reduction) in COMB.items():
        count = products[product]
        if item in products:
            if item != product:
                products[item] = max(products[item] - count // c, 0)
            else:
                products[item] = products[item] // (c + reduction) * c + products[item] % (c + reduction)

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
