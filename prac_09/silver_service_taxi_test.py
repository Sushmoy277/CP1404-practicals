"""
CP1404 Practical
Test SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare calculations."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)

    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18 km: ${fare:.2f}")

    assert round(fare, 2) == 48.78


main()
