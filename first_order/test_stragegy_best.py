from strategy_best import *


def test_promotion():
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    joe_order = Order(joe, cart, fidelity_promotion)
    assert joe_order.total() == 42.0
    assert joe_order.due() == 42.0

    ann_order = Order(ann, cart, fidelity_promotion)
    assert ann_order.total() == 42.0
    assert ann_order.due() == 39.9

    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    joe_bulk_order = Order(joe, banana_cart, bulk_item_promotion)
    assert joe_bulk_order.total() == 30.0
    assert joe_bulk_order.due() == 28.5

    long_oder = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    joe_long_oder = Order(joe, long_oder, large_order_promotion)
    assert joe_long_oder.total() == 10.0
    assert joe_long_oder.due() == 9.3

    joe_best_promo1 = Order(joe, long_oder, best_promotion)
    assert joe_best_promo1.total() == 10.0
    assert joe_best_promo1.due() == 9.3

    joe_best_promo2 = Order(joe, banana_cart, best_promotion)
    assert joe_best_promo2.total() == 30.0
    assert joe_best_promo2.due() == 28.5

    ann_best_promo3 = Order(ann, cart, best_promotion)
    assert ann_best_promo3.total() == 42.0
    assert ann_best_promo3.due() == 39.9
