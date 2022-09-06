"""
Предположим, что книга стоит 249 рублей 50 копеек, при этом книж-
ный магазин предоставляет скидку в 40%. Стоимость доставки состав-
ляет 100 рублей за первый экземпляр и 49 рублей 50 копеек за каждый
дополнительный. В какую сумму обойдется закупка 60 экземпляров?
"""

book_cost = 249.5
first_delivery_cost = 100
delivery_cost = 49.5
sale = 0.4
book_number = 60

cost = (book_cost * book_number * (1 - sale)) + (delivery_cost * (book_number - 1) + first_delivery_cost)
print(cost)
