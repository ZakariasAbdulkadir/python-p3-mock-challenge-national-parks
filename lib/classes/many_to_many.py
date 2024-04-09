class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Visitor's name must be a string.")
        if not 1 <= len(value) <= 15:
            print("Visitor's name must be between 1 and 15 characters.")
        else:
            self._name = value

    def trips(self):
        return [trip for trip in Trip.trips if trip.visitor == self]

    def national_parks(self):
        return list(set(trip.national_park for trip in self.trips()))


class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            print("Attribute exists")
        if not isinstance(value, str):
            print("NationalPark's name must be a string.")
        if len(value) < 3:
            print("NationalPark's name must be at least 3 characters long.")
        else:
            self._name = value

    def trips(self):
        return [trip for trip in Trip.trips if trip.national_park == self]

    def visitors(self):
        return list(set(trip.visitor for trip in self.trips()))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visits = {}
        for trip in self.trips():
            visitor = trip.visitor
            visits[visitor] = visits.get(visitor, 0) + 1
        if visits:
            return max(visits, key=visits.get)
        else:
            return None


class Trip:
    trips = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.trips.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise ValueError("Start date must be a string.")
        if len(value) < 7:
            raise ValueError("Start date must be at least 7 characters long.")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise ValueError("End date must be a string.")
        elif len(value) < 7:
            raise ValueError("End date must be at least 7 characters long.")   
        self._end_date = value


    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            print("Visitor must be an instance of Visitor.")
        self._visitor = value

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            print("NationalPark must be an instance of NationalPark.")
        self._national_park = value
