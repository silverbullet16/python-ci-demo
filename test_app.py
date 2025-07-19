from app import add


def test_add():
    assert add(1, 2) == 5
    assert add(2, 3) == 5
    assert add(3, 4) == 7
