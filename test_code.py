import unittest
import code

class TestCase(unittest.TestCase):
    
    def test_add_fun(self):
        number1 = 1
        number2 = 2
        result = code.add_function(number1, number2)
        self.assertEquals(result, 3)
        
if __name__ == '__main__':
    unittest.main()