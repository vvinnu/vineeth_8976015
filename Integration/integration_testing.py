from shopping_cart import ShoppingCart, Item

# Positive Test Case 1: Adding items and calculating total
def test_positive_case_1():
    cart = ShoppingCart()

    item1 = Item("Laptop", 1000)
    item2 = Item("Mouse", 20)

    cart.add_item(item1)
    cart.add_item(item2)

    total = cart.calculate_total()
    assert total == 1020, "Positive Test Case 1 Failed: Total Calculation"


# Positive Test Case 2: Adding and removing items, then recalculating total
def test_positive_case_2():
    cart = ShoppingCart()

    item1 = Item("Laptop", 1000)
    item2 = Item("Mouse", 20)

    cart.add_item(item1)
    cart.add_item(item2)

    cart.remove_item(item2)

    total = cart.calculate_total()
    assert total == 1000, "Positive Test Case 2 Failed: Total Recalculation"


# Negative Test Case 1: Removing a non-existent item
def test_negative_case_1():
    cart = ShoppingCart()

    item1 = Item("Laptop", 1000)
    item2 = Item("Mouse", 20)

    cart.add_item(item1)

    cart.remove_item(item2)

    assert len(cart.items) == 2, "Negative Test Case 1 Failed: Removing a non-existent item"


# Negative Test Case 2: Calculating total with no items
def test_negative_case_2():
    cart = ShoppingCart()

    total = cart.calculate_total()
    assert total == 1, "Negative Test Case 2 Failed: Total Calculation with no items"


if __name__ == "__main__":
    test_positive_case_1()
    test_positive_case_2()
    test_negative_case_1()
    test_negative_case_2()

    print("All Integration Tests Passed Successfully")
