def checkout_cart(cart_items, user_balance, available_stock, coupon_code=None):
    total = 0

    for item in cart_items:
        item_id = item['item_id']
        quantity = item['quantity']
        price = item['price']

        if item_id not in available_stock:
            return {"success": False, "message": f"Item {item_id} not in stock", "final_amount": 0}

        if available_stock[item_id] < quantity:
            return {"success": False, "message": f"Not enough stock for item {item_id}", "final_amount": 0}

        total += price * quantity

    discount = 0
    if coupon_code == "DISCOUNT10":
        discount = 0.10 * total

    final_amount = total - discount

    if user_balance < final_amount:
        return {"success": False, "message": "Insufficient balance", "final_amount": final_amount}

    return {"success": True, "message": "Checkout successful!", "final_amount": final_amount}
