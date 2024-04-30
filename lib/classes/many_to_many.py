# def proper_format(date):
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#     parts = date.split(" ")

#     if len(parts) != 2:
#         return False
#     if parts[0] not in months:
#         return False
    
#     else:
#         return True


class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in Trip.all if trip.national_park is self})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        # return max(self.visitors(), key=lambda visitor: visitor.total_visits_at_park(self))
        best = None
        visits = 0
        visitor_visits = {}
        for trip in Trip.all:
            if trip.national_park is self:
                if best is None:
                    best = trip.visitor
                    visits = 1
                    visitor_visits[trip.visitor] = 1
                if visitor_visits.get(trip.visitor):
                    visitor_visits[trip.visitor] += 1
                    if visitor_visits[trip.visitor] > visits: 
                        best = trip.visitor
                        visits = visitor_visits[trip.visitor]
                else:
                    visitor_visits[trip.visitor] = 1
        return best

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2 and not hasattr(self, "_name"):
            self._name = name

    @classmethod
    def most_visits(cls):
        return max(cls.all, key=lambda park: park.total_visits())

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.__class__.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) > 6:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) > 6:
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park

class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in Trip.all if trip.visitor is self})
    
    def total_visits_at_park(self, park):
        return len([trip for trip in Trip.all if trip.visitor is self and trip.national_park is park])

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name