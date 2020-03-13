from exceptions import IllegalCarError


class Car():
    """
    Stores information about a car.

    Attributes:
        pax_count (int): Number of passengers riding the car, driver included.
        car_mass (int): Mass of the empty car in kilograms.
        gear_count (int): Number of gears in the car.
    """
    def __init__(self, pax_count: int, car_mass: int, gear_count: int):

        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    # Getters and setters
    @property
    def pax_count(self):
        """Get pax_count"""
        return self.__pax_count

    @pax_count.setter
    def pax_count(self, pax_count):
        """Set pax_count"""
        if pax_count < 1 or pax_count > 5:
            raise IllegalCarError(
                                'Passenger count cannot be ' +
                                'greater than 5, or less than 1.')
        else:
            self.__pax_count = pax_count

    @property
    def car_mass(self):
        """Get car_mass"""
        return self.__car_mass

    @car_mass.setter
    def car_mass(self, car_mass):
        """Set car_mass"""
        if car_mass > 2000:
            raise IllegalCarError('Car mass cannot be greater than 2000 kg.')
        else:
            self.__car_mass = car_mass

    # Properties
    @property
    def total_mass(self):
        ''' Returns a total mass of car and the passengers in kilograms. '''
        return self.car_mass + self.pax_count * 70


if __name__ == '__main__':

    car = Car(4, 2000, 5)
    print(f'Passenger count: {car.pax_count}')
    print(f'Mass: {car.car_mass} kilograms')
    print(f'Gear count: {car.gear_count}')
    print(f'Total mass {car.total_mass} kilograms')