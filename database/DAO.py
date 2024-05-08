from database.DB_connect import DBConnect
from model.flight import Flight
from model.rotte import Rotta


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllFlightAggregate():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT T1.ORIGIN_AIRPORT_ID, T1.DESTINATION_AIRPORT_ID, COALESCE(T1.D, 0) + COALESCE(T2.D, 0) as TOT_DISTANCE, COALESCE(T1.N, 0) + COALESCE(T2.N, 0) as N_VOLI
                FROM (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
		            FROM flights f
				    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
				    LEFT JOIN 
				    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N 
				    FROM flights f 
				    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2 
			    ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
			    WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL """

        cursor.execute(query)
        for row in cursor:
            result.append(Rotta(row["ORIGIN_AIRPORT_ID"],
                                row["DESTINATION_AIRPORT_ID"],
                                row["TOT_DISTANCE"],
                                row["N_VOLI"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getFlightByID(id_partenza, id_arrivo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM flights
                    WHERE ORIGIN_AIRPORT_ID = %s and DESTINATION_AIRPORT_ID = %s"""
        cursor.execute(query, (id_partenza, id_arrivo))
        for row in cursor:
            result.append(Flight(row["ID"],
                                 row["ORIGIN_AIRPORT_ID"],
                                 row["DESTINATION_AIRPORT_ID"],
                                 row["DISTANCE"]))

        cursor.close()
        conn.close()
        return result
