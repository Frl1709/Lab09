from dataclasses import dataclass


@dataclass
class Rotta:
    _origin_airport_ID: str
    _destination_airport_ID: str
    _tot_distance: int
    _nVoli : int

    def getOriginAirportID(self):
        return self._origin_airport_ID

    def getDestinationAirportID(self):
        return self._destination_airport_ID

    def getTotalDistance(self):
        return self._tot_distance

    def getNVoli(self):
        return self._nVoli
