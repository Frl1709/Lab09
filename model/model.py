from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._flight = DAO.getAllFlightAggregate()
        self.grafo = nx.Graph()

    def buildGraph(self, distance):
        # airport = set()
        """for flight in self._flight:
            v1 = flight.getOriginAirportID()
            v2 = flight.getDestinationAirportID()
            weight = self.weight(v1, v2)
            if weight is not None and weight > 0 and weight > distance:
                if v1 not in airport:
                    airport.add(v1)
                if v2 not in airport:
                    airport.add(v2)
                self.grafo.add_edge(v1, v2)"""
        for flight in self._flight:
            v1 = flight.getOriginAirportID()
            v2 = flight.getDestinationAirportID()
            weight = float(flight.getTotalDistance()/flight.getNVoli())
            if weight > distance:
                self.grafo.add_edge(v1, v2, weight=weight)
        return self.grafo

    @staticmethod
    def weight(id_partenza, id_destinazione):
        w = 0
        count = 0
        voli = DAO.getFlightByID(id_partenza, id_destinazione) + DAO.getFlightByID(id_destinazione, id_partenza)
        for f in voli:
            """if (f.getDestinationAirportID() == id_partenza and f.getDestinationAirportID() == id_destinazione) or (
                    f.getDestinationAirportID() == id_destinazione and f.getDestinationAirportID() == id_partenza):"""
            w += f.getDistance()
            count += 1
        return w / count
