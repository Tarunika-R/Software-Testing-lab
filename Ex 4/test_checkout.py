# test_checkout.py

import pytest
from checkout import checkout_cart

@pytest.fixture
def cart_data():
    return [
        {"item_id": "A1", "quantity": 2, "price": 100},
        {"item_id": "B2", "quantity": 1, "price": 200}
    ]

@pytest.fixture
def stock_data():
    return {"A1": 5, "B2": 2}

def test_checkout_success(cart_data, stock_data):
    result = checkout_cart(cart_data, user_balance=500, available_stock=stock_data)
    assert result["success"] is True
    assert result["final_amount"] == 400
    assert "successful" in result["message"].lower()

def test_checkout_insufficient_balance(cart_data, stock_data):
    result = checkout_cart(cart_data, user_balance=100, available_stock=stock_data)
    assert result["success"] is False
    assert result["message"] == "Insufficient balance"

def test_checkout_out_of_stock(cart_data):
    stock_data = {"A1": 1, "B2": 1}  # A1 required: 2, available: 1
    result = checkout_cart(cart_data, user_balance=1000, available_stock=stock_data)
    assert result["success"] is False
    assert "Not enough stock" in result["message"]

def test_checkout_item_not_in_stock(cart_data):
    stock_data = {"B2": 1}  # A1 not present
    result = checkout_cart(cart_data, user_balance=1000, available_stock=stock_data)
    assert result["success"] is False
    assert "not in stock" in result["message"]

def test_checkout_with_coupon(cart_data, stock_data):
    result = checkout_cart(cart_data, user_balance=500, available_stock=stock_data, coupon_code="DISCOUNT10")
    expected_discount = 0.10 * 400
    assert result["success"] is True
    assert result["final_amount"] == pytest.approx(400 - expected_discount, 0.01)

def test_invalid_coupon_code(cart_data, stock_data):
    result = checkout_cart(cart_data, user_balance=500, available_stock=stock_data, coupon_code="FAKECODE")
    assert result["success"] is True
    assert result["final_amount"] == 400  # no discount applied