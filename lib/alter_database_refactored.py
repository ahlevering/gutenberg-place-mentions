"""
Contains all scripts that analyze the e-pub file one way or the other
"""


def create_database(default_dbname, new_dbname, user, password):
    import psycopg2
    try:    
        con = psycopg2.connect("dbname={} user={} password={}".format(default_dbname, user, password))
        con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
    except:
        print("Unable to connect to the database or set the isolation level")
    try:
        insert_query = """CREATE DATABASE {dbname};""".format(dbname = new_dbname)
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
    except:
        print("Failed to create database. It might already exist or you do not have the rights to make a new database.")
        
def create_postgis_extension(dbname, user, password):
    import psycopg2
    con = psycopg2.connect("dbname={} user={} password={}".format(dbname, user, password))
    cur = con.cursor()
    try:
        insert_query = """CREATE EXTENSION PostGIS;"""
        cur.execute(insert_query)
        con.commit()
    except:
        print("Extension PostGIS already exists, or PostGIS is not installed")
    cur.close()
    con.close()


class database_operations:
    def __init__(self):
        import psycopg2
   
    def set_database_credentials(self,user, password):
        self.user = user
        self.password = password
    
    def connect_to_default_database(self, default_database_name):
        try:    
            self.default_db_con = self.psycopg2.connect("dbname={} user={} password={}".format(default_database_name, self.user, self.password))
            self.default_db_con.set_isolation_level(self.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            self.default_db_cur = self.default_db_con.cursor()
        except:
            print("Unable to connect to the database or set the isolation level")
    
    def set_project_database_name(self, project_database_name):
        self.project_database_name = project_database_name
    
    def create_project_database(self):
        try:
            insert_query = """CREATE DATABASE {dbname};""".format(dbname = self.project_database_name)
            self.default_db_cur.execute(insert_query)
            self.default_db_con.commit()
        except:
            print("Failed to create database. It might already exist or you do not have the rights to make a new database.")
            
    def close_default_db_connection(self):
        self.default_db_cur.close()
        self.default_db_con.close()

    def connect_to_project_database(self):
        self.con = self.psycopg2.connect("dbname={} user={} password={}".format(self.project_database_name, self.user, self.password))
        self.cur = self.con.cursor()
    
    def create_project_database_postgis_extension(self):
        try:
            insert_query = """CREATE EXTENSION PostGIS;"""
            self.cur.execute(insert_query)
            self.con.commit()
        except:
            print("Extension PostGIS already exists, or PostGIS is not installed")
    
    def query_project_database(self, query):
        insert_query = """CREATE DATABASE {dbname};""".format(dbname = self.project_database_name)
        self.cur.execute(insert_query)
        self.con.commit()
    
    def close_project_database_connection(self):
        self.cur.close()
        self.con.close()

def create_country_table(dbname, user, password, table_name, overwrite = False):
    import psycopg2
    con = psycopg2.connect("dbname={} user={} password={}".format(dbname, user, password))
    cur = con.cursor()
    
    if overwrite == True:
        del_table_query = """DROP TABLE IF EXISTS {table_name};""".format(table_name = table_name)
        cur.execute(del_table_query)
    insert_query = """CREATE TABLE IF NOT EXISTS {table_name} (
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
                """.format(table_name = table_name)
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()
    
def create_gutenberg_table(dbname, user, password, table_name, overwrite = False):
    import psycopg2
    con = psycopg2.connect("dbname={} user={} password={}".format(dbname, user, password))
    cur = con.cursor()
    
    if overwrite == True:
        del_table_query = """DROP TABLE IF EXISTS {table_name};""".format(table_name = table_name)
        cur.execute(del_table_query)
    insert_query = """CREATE TABLE IF NOT EXISTS {table_name} (
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
                """.format(table_name = table_name)
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

if __name__ == "__main__":
    import unittest

    class TestStringMethods(unittest.TestCase):  
        import unittest
        
        def test_title(self):
            self.assertEqual(get_epub_metadata(r'D:\cygwinfolders\gutenberg-generated\1\pg1.epub')['title'], 'The Declaration of Independence of the United States of America')
        def test_creator(self):
            self.assertEqual(get_epub_metadata(r'D:\cygwinfolders\gutenberg-generated\1\pg1.epub')['creator'], 'Thomas Jefferson')
    unittest.main()