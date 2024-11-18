import re
from datetime import datetime
import unittest

# Validation Functions
def validate_symbol(symbol):
    """Validates that the stock symbol is all uppercase, alphabetic, and between 1-7 characters."""
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def validate_chart_type(chart_type):
    """Validates that the chart type is either '1' or '2'."""
    return chart_type in {"1", "2"}

def validate_time_series_option(option):
    """Validates that the time series option is a number between '1' and '4'."""
    return option in {"1", "2", "3", "4"}

def validate_date_format(date):
    """Validates that the date is in the format YYYY-MM-DD and is a valid date."""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Unit Tests
class TestStockVisualizerInputs(unittest.TestCase):
    
    # Test symbol validation
    def test_validate_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))  # Valid symbol
        self.assertTrue(validate_symbol("GOOGL"))  # Valid symbol
        self.assertFalse(validate_symbol("aapl"))  # Invalid: lowercase
        self.assertFalse(validate_symbol("AAPL123"))  # Invalid: contains numbers
        self.assertFalse(validate_symbol("A"))  # Invalid: too short


    # Test chart type validation
    def test_validate_chart_type(self):
        self.assertTrue(validate_chart_type("1"))  # Valid option
        self.assertTrue(validate_chart_type("2"))  # Valid option
        self.assertFalse(validate_chart_type("3"))  # Invalid option
        self.assertFalse(validate_chart_type("0"))  # Invalid option

    # Test time series option validation
    def test_validate_time_series_option(self):
        self.assertTrue(validate_time_series_option("1"))  # Valid option
        self.assertTrue(validate_time_series_option("4"))  # Valid option
        self.assertFalse(validate_time_series_option("5"))  # Invalid option
        self.assertFalse(validate_time_series_option("0"))  # Invalid option

    # Test date validation
    def test_validate_date_format(self):
        self.assertTrue(validate_date_format("2023-01-01"))  # Valid date
        self.assertTrue(validate_date_format("2022-12-31"))  # Valid date
        self.assertFalse(validate_date_format("01-01-2023"))  # Invalid format
        self.assertFalse(validate_date_format("2023/01/01"))  # Invalid format
        self.assertFalse(validate_date_format("2023-13-01"))  # Invalid month
        self.assertFalse(validate_date_format("2023-00-01"))  # Invalid month
        self.assertFalse(validate_date_format("2023-02-30"))  # Invalid day

if __name__ == "__main__":
    unittest.main()
