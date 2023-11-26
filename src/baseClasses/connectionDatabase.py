import pandas as pd
import psycopg2
import sqlalchemy
import asyncio
from sqlalchemy import create_engine
from typing import List, AnyStr

class DatabaseConnector():
    """
    Class to help and work with POSTGRES-SQL Databases

    Attributes
    ----------
        host_adress : str
                contains the IP-Adress of the Database

        database_name : str
                contains the name of the Database

        user_name : str
                contains name of the user to login to the Database

        password: str
                contains the password of the user

        postgres_port : str
                contains the default port for postgres: 5432

        cursor : cursor
                object to execute SQL commands to the Database

        engine : engine
                used to  connect to the Database

    Methods
    -------
        connect()
                starts connection to the Database

        postgresql_to_dataframe(self,select_query, column_names : List) -> pd.DataFrame:
                turns a postgresql Selection into a Pandas Dataframe

        execute_sql(sql_query: AnyStr )
                executres the given SQL Command to the Database
                
        close_connection():
                closes the connection to the Database
    """

    def __init__(self) -> None:
        self.postgres_port = "5342"
        self.cursor, self.engine = None,None
        self.connected_bool = False
        
    def __connect_postgres(self, host_address, database_name, user_name, password) -> None:
        """
            Starts connection to the Database        
        """
        self.host_adress = host_address
        self.database_name = database_name
        self.user_name = user_name
        self.password = password

        url = "postgresql+psycopg2://"+ self.user_name +":"+self.password + "@" + self.host_adress +"/"+ self.database_name
        print("Conecting to database....")
        try:
            self.engine = create_engine(url, echo = False)
            self.connected_bool = True
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            print("Connection failed!")
        self.cursor = self.engine.connect()
        
    def postgresql_to_dataframe(self,select_query, column_names : List[str] = []) -> pd.DataFrame:
        """
        Tranform a SELECT query into a pandas dataframe
        """
        
        try:
            result = self.cursor.execute(sqlalchemy.text(select_query))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)

            return error

        headers = result.keys()

        # Naturally we get a list of tupples
        # We just need to turn it into a pandas dataframe
        if column_names is not None:
            df = pd.DataFrame(result, columns=headers)
        else:
            df = pd.DataFrame(result, columns=column_names)
        return df

    def execute_SQL(self, sql_query: AnyStr ) -> None:
        """
            Executes an SQL-Query and makes the changes persistent
        """
        
        try:
            output = self.cursor.execute(sql_query)
            return output

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)

    def get_all_table_names(self):
        try:
            return self.engine.table_names()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)

    def close_connection(self) -> None:
        """
            Closes the connection to the DB
        """      
        self.cursor.close()
        self.connected_bool = False
        print("!!!Connection closed!!!")
        
    def is_connected(self):
        return self.connected_bool
    
    def connect_any_dialect(self, host_address, database_name, user_name, password) -> None:
        """
            Starts connection to the Database        
        """
        self.host_adress = host_address
        self.database_name = database_name
        self.user_name = user_name
        self.password = password

        dialects = ["mysql", "oracle", "postgresql", "mssql", ]
        for dialect in dialects:
            url = dialect + "://"+ self.user_name +":"+self.password + "@" + self.host_adress +"/"+ self.database_name
            print("Conecting to database....")
            try:
                self.engine = create_engine(url, echo = False)
                self.cursor =  self.engine.connect()
                self.connected_bool = True
                print("Connection succesfull with a " + dialect + "database")
                break
            except BaseException as error:
                # print("Error: %s" % error)
                # print("Connection failed!")
                pass
        