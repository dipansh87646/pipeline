from operation.main import add , sub
def test_add() -> None:
    assert add(5,3) == 5
    assert add(-1,1) == 0

def test_sub() -> None:
    assert sub(7,3) == 4
    assert sub(4,3) == 1
    assert sub(5,2) == 3
    assert sub(10,5) == 5    
