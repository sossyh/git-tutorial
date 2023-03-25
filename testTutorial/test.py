import pytest
from arithmetic_operations import ArithmeticClass

class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArithmeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArithmeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArithmeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArithmeticClass.add("1", "2")
        
        assert expected_output == actual_output
        
    def test_sub(self ):
        # arrange
        x, y = 5.0, 1.0
        expected_output = 4.0
        # act
        actual_output = ArithmeticClass.subtract(x, y)
        # assert
        with pytest.raises(TypeError):
            ArithmeticClass.subtract("5", 1)
        with pytest.raises(TypeError):
            ArithmeticClass.subtract(5, "1")
        with pytest.raises(TypeError):
            ArithmeticClass.subtract("5", "5")
        
        assert expected_output == actual_output
    
    def test_mul(self ):
        # arrange
        x, y = 2.0, 2.0
        expected_output = 4.0
        # act
        actual_output = ArithmeticClass.multiply(x, y)
        # assert
        with pytest.raises(TypeError):
            ArithmeticClass.multiply("2", 2)
        with pytest.raises(TypeError):
            ArithmeticClass.multiply(2, "2")
        with pytest.raises(TypeError):
            ArithmeticClass.multiply("2", "2")
        
        assert expected_output == actual_output
    
    def test_div(self ):
        # arrange
        x, y = 4.0, 2.0
        expected_output = 2.0
        # act
        actual_output = ArithmeticClass.divide(x, y)
        # assert
        with pytest.raises(TypeError):
            ArithmeticClass.divide("4", 2)
        with pytest.raises(TypeError):
            ArithmeticClass.divide(4, "2")
        with pytest.raises(TypeError):
            ArithmeticClass.divide("4", "2")
        with pytest.raises(ZeroDivisionError):
            ArithmeticClass.divide(2, 0)
        
        assert expected_output == actual_output