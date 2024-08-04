#!/usr/bin/python3
"""
Unit tests for the Booking model class
"""

import unittest
from datetime import datetime
from models.booking import Booking  # Adjust import as per your project structure

class TestBooking(unittest.TestCase):
    """Test cases for the Booking class"""

    def setUp(self):
        """Set up test methods"""
        self.new_booking = Booking(start="2024-01-01", end="2024-01-05")

    def test_instance_creation(self):
        """Test for proper instance creation"""
        self.assertIsInstance(self.new_booking, Booking)

    def test_initial_attributes(self):
        """Test initial attribute values"""
        self.assertEqual(self.new_booking.start, datetime(2024, 1, 1))
        self.assertEqual(self.new_booking.end, datetime(2024, 1, 5))

    def test_duration(self):
        """Test calculation of booking duration"""
        self.assertEqual(self.new_booking.duration(), 4)

    def test_overlap(self):
        """Test the overlap check between two bookings"""
        other_booking = Booking(start="2024-01-04", end="2024-01-07")
        self.assertTrue(self.new_booking.overlaps(other_booking))

if __name__ == '__main__':
    unittest.main()

