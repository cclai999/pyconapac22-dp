from classic_strategy import *


def test_promotion():
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    joe_order = Order(joe, cart, FidelityPromotion())
    assert joe_order.total() == 42.0
    assert joe_order.due() == 42.0

    ann_order = Order(ann, cart, FidelityPromotion())
    assert ann_order.total() == 42.0
    assert ann_order.due() == 39.9