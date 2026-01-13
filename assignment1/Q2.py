def add_order(order_id, orders=None):
    # If orders is None, create a new list
    if orders is None:
        orders = []

    # Add the new order id
    orders.append(order_id)

    # Return the full order list
    return orders
print(add_order(101))
print(add_order(102))
print(add_order(103))   