"""
Contains all scripts that analyze the e-pub file one way or the other
"""
from importlib import import_module

class database_operations:
    def __init__(self):
        self.psycopg2 = import_module('psycopg2')
        self.logging = import_module('logging')
        
        self.user = ""
        self.password = ""
        self.default_db_con = ""
        self.default_db_cur = ""
        self.cur = ""
        self.con = ""        
   
        self.location_table_name = ""
        self.gutenberg_table_name = ""
        
    def set_database_credentials(self,user, password):
        self.user = user
        self.password = password
    
    def connect_to_default_database(self, default_database_name):
        try:
            self.default_db_con = self.psycopg2.connect("dbname={} user={} password={}".format(default_database_name, self.user, self.password))
            self.default_db_con.set_isolation_level(self.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            self.default_db_cur = self.default_db_con.cursor()
        except BaseException as e:
            print("Failed to access default database: " + str(e))
    
    def set_project_database_name(self, project_database_name):
        self.project_database_name = project_database_name
    
    def create_project_database(self):
        try:
            insert_query = """CREATE DATABASE {dbname};""".format(dbname = self.project_database_name)
            self.default_db_cur.execute(insert_query)
            self.default_db_con.commit()
        except BaseException as e:
            print("Failed to create database: " + str(e))
            
    def close_default_db_connection(self):
        self.default_db_cur.close()
        self.default_db_con.close()
        
    def execute_query(self, query, query_values = False):
        try:
            if query_values != False:
                self.cur.execute(query, query_values)
                self.con.commit()
            else:
                self.cur.execute(query)
                self.con.commit()
        except BaseException as e:
            print("Failed to perform query: " + str(e))
            self.close_project_database_connection()
            self.connect_to_project_database()
            print("database connection has been reset")
    
    def close_project_database_connection(self):
        self.cur.close()
        self.con.close()        

    def connect_to_project_database(self):
        self.con = self.psycopg2.connect("dbname={} user={} password={}".format(self.project_database_name, self.user, self.password))
        self.cur = self.con.cursor()
    
    def create_project_database_postgis_extension(self):
        try:
            insert_query = """CREATE EXTENSION PostGIS;"""
            self.cur.execute(insert_query)
            self.con.commit()
        except BaseException as e:
            print("Could not create PostGIS extension: " + str(e))
            self.close_project_database_connection()
            self.connect_to_project_database()
            print("database connection has been reset")

    def set_location_table_name(self, location_table_name):
        self.location_table_name = location_table_name
        
    def create_location_table(self, overwrite = False):   
        """
            Create the country table by the struture listed in http://download.geonames.org/export/dump/readme.txt
            Hardcoded table structure because Geonames structure has not changed for a long time
        """
        if overwrite == True:
            del_table_query = """DROP TABLE IF EXISTS {table_name};""".format(table_name = self.location_table_name)
            self.cur.execute(del_table_query)
            
        country_lut_query = """CREATE TABLE IF NOT EXISTS {table_name} (
                            geonameid           bigint,
                            name                varchar(200),
                            normalizedname      varchar(200),
                            alternatenames      varchar(10000),
                            latitude            decimal,
                            longitude           decimal, 
                            featureclass        varchar(1),
                            featurecode         varchar(10),
                            countrycode	        varchar(2),
                            alternatecc         varchar(200),
                            admin1code	        varchar(80),
                            admin2code	        varchar(40),
                            admin3code	        varchar(20),
                            admin4code	        varchar(20),
                            elevation           integer,
                            dem                 integer,
                            population          integer,
                            timezone            varchar(40),
                            modificationdate    date,
                            CONSTRAINT geoidentifier PRIMARY KEY(geonameid)
                            );""".format(table_name = self.location_table_name)
        self.execute_query(country_lut_query)
    
    def insert_location_file(self, location_file_name):
        with open (location_file_name, encoding="utf-8") as country_Data:
            for line in country_Data:
                location_row = line.split("	")
                self.insert_location_row(location_row)
        
    def insert_location_row(self, location_table_row):
        location_row_query =  """INSERT INTO {tablename} VALUES(""".format(tablename = self.location_table_name)
        syntaxed_entries = [str("'" + str(entry) + "',") for entry in location_table_row]
        for i,entry in enumerate(syntaxed_entries):
            if entry == "'',":
                entry = "DEFAULT,"
            location_row_query += entry
        location_row_query = location_row_query[:-1] + ") ON CONFLICT (geonameid) DO NOTHING;" #Stripping last comma
        self.execute_query(location_row_query)
            
            
            
            
            
            
            
            
            
            
            
    def set_gutenberg_table_name(self, gutenberg_table_name):
        self.gutenberg_table_name = gutenberg_table_name
        
    def create_gutenberg_table(self, overwrite = False):
        if overwrite == True:
            del_table_query = """DROP TABLE IF EXISTS {table_name};""".format(table_name = self.gutenberg_table_name)
            self.cur.execute(del_table_query)
            
        gutenberg_table_query = """CREATE TABLE IF NOT EXISTS {table_name} (
                        id  	bigint,
                        time	varchar(50),
                        latitude	decimal,
                        longitude	decimal,
                        selfrepcity varchar(500),    
                        lang	varchar(10),
                        source	varchar(250),
                        countrycode	varchar(10),
                        countryname	varchar(250),
                        location	varchar(250),
                        url	varchar(100),
                        text        varchar(500),
                        loclat   decimal,
                        loclong  decimal);
                    """.format(table_name = self.gutenberg_table_name)
        self.execute_query(gutenberg_table_query)

if __name__ == "__main__":
    import unittest

    class TestStringMethods(unittest.TestCase):  
        import unittest
        
        def test_title(self):
            self.assertEqual(get_epub_metadata(r'D:\cygwinfolders\gutenberg-generated\1\pg1.epub')['title'], 'The Declaration of Independence of the United States of America')
        def test_creator(self):
            self.assertEqual(get_epub_metadata(r'D:\cygwinfolders\gutenberg-generated\1\pg1.epub')['creator'], 'Thomas Jefferson')
    unittest.main()