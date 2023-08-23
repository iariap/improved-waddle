from water_jud_riddle import Jug


def test_fill():
    jug = Jug(capacity=10)
    jug.fill()
    assert jug.current_level == 10
    assert jug.is_full()


def test_empty():
    jug = Jug(capacity=10)
    jug.fill()
    jug.empty()
    assert jug.current_level == 0
    assert jug.is_empty()


def test_transfer_same_capacity():
    jug_x = Jug(capacity=10)
    jug_y = Jug(capacity=10)
    jug_x.fill()
    jug_x.transfer_to(jug_y)

    assert jug_x.is_empty()
    assert jug_y.is_full()


def test_transfer_diferent_capacity():
    jug_x = Jug(capacity=5)
    jug_y = Jug(capacity=10)
    jug_x.fill()
    jug_x.transfer_to(jug_y)

    assert jug_x.is_empty()
    assert not jug_y.is_empty()
    assert jug_y.current_level == 5
