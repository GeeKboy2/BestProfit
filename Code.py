class Person:
    def __init__(self, person_id, quantity, price):
        self.id = person_id
        self.quantity = quantity
        self.price = price


def calculate_profits(budget, buyers_list, sellers_list):
    starting_budget = 0
    buyers = sorted(buyers_list, key=lambda person: person.price)
    sellers = sorted(sellers_list, key=lambda person: person.price, reverse=True)
    transactions = []   
    while buyers and sellers and buyers[-1].price > sellers[-1].price and budget // buyers[-1].price > 0:
        quantity = min(buyers[-1].quantity, sellers[-1].quantity, budget // buyers[-1].price)
        profit_margin = buyers[-1].price - sellers[-1].price
        budget += quantity * profit_margin
        transactions.append(f'Buying {quantity} products from seller {sellers[-1].id} for {sellers[-1].price}')
        transactions.append(f'Selling {quantity} products to seller {buyers[-1].id} for {buyers[-1].price}')
        buyers[-1].quantity -= quantity
        sellers[-1].quantity -= quantity
        if buyers[-1].quantity == 0:
            buyers.pop()
        if sellers[-1].quantity == 0:
            sellers.pop()

    return budget - starting_budget, transactions


budget = 40
buyers = [Person(0, 10, 2), Person(111, 100, 1.2), Person(222, 900, 1.0)]
sellers = [Person(123, 10, 0.9), Person(456, 90, 1.0)]

profit, transactions = calculate_profits(budget, buyers, sellers)
print(f'{profit = }')
for trans in transactions:
    print(trans)
