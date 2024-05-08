from dataclasses import dataclass


@dataclass
class Flight:
    _id: int
    _origin_airport_ID: str
    _destination_airport_ID: str
    _distance: int

    def getID(self):
        return self._id

    def getOriginAirportID(self):
        return self._origin_airport_ID

    def getDestinationAirportID(self):
        return self._destination_airport_ID

    def getDistance(self):
        return self._distance

