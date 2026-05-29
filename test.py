import math

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

# Test cases
def test_calculate_area():
    assert calculate_area(0) == 0
    assert calculate_area(1) == math.pi
    assert calculate_area(2) == 4 * math.pi
    try:
        calculate_area(-1)
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"
if __name__ == "__main__":    
    test_calculate_area()
    print("All tests passed!")

main()