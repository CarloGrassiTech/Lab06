from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def get_anno():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT g.Date 
                        FROM go_daily_sales g"""

        cursor.execute(query)

        res = ["non scelto"]
        for row in cursor:
            res.append(row["Date.YEAR"])
        # processa res

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_brand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT g.Product_brand
                    FROM go_products g
                """

        cursor.execute(query)

        res = ["non scelto"]
        for row in cursor:
            # res.append(Corso(codins=row["codins"],
            #                  crediti = row["crediti"],
            #                  nome = row["nome"],
            #                  pd = row["pd"]))
            res.append(Corso(**row))
        # processa res

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_retailers(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT *
                        FROM corso c
                        WHERE c.pd = %s"""

        cursor.execute(query, (pd,))

        res = ["non scelto"]
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res