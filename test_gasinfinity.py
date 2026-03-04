# test_gasinfinity.py
"""
Tests for GasInfinity module.
"""

import unittest
from gasinfinity import GasInfinity

class TestGasInfinity(unittest.TestCase):
    """Test cases for GasInfinity class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GasInfinity()
        self.assertIsInstance(instance, GasInfinity)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GasInfinity()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
