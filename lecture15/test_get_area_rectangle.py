import pytest
from rectangle import Rectangle

class TestGetAreaRectangle:
    def test_normal_case(self):
        """Test case to check normal positive area calculation"""
        rectangle = Rectangle(2, 3)
        assert rectangle.get_area() == 6, "incorrect area calculation"

    def test_negative_case(self):
        """Test case to check handling of negative dimensions"""
        with pytest.raises(AssertionError):
            rectangle = Rectangle(-1, 2)
            rectangle.get_area()

if __name__ == "__main__":
    pytest.main()
