from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar behaviour over many drives."""
    low_reliability = UnreliableCar("Low reliability", 100, 30)  # 30% reliable
    high_reliability = UnreliableCar("High reliability", 100, 90)  # 90% reliable

    number_of_trials = 100
    distance_per_attempt = 1

    low_drives = count_successful_drives(low_reliability, number_of_trials, distance_per_attempt)
    print(f"{low_reliability.name}:")
    print(f"Attempts: {number_of_trials}")
    print(f"Times it actually drove: {low_drives}")
    print(f"Final fuel: {low_reliability.fuel}")
    print()

    high_drives = count_successful_drives(high_reliability, number_of_trials, distance_per_attempt)
    print(f"{high_reliability.name}:")
    print(f"Attempts: {number_of_trials}")
    print(f"Times it actually drove: {high_drives}")
    print(f"Final fuel: {high_reliability.fuel}")


def count_successful_drives(car, number_of_trials, distance_per_attempt):
    """Return how many times the unreliable car actually drives."""
    drives = 0
    for i in range(number_of_trials):
        distance_driven = car.drive(distance_per_attempt)
        if distance_driven > 0:
            drives += 1
    return drives


main()
