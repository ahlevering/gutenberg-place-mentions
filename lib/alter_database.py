"""
Contains all scripts that analyze the e-pub file one way or the other
"""


def create_database(default_dbname, new_dbname, user, password):
    import psycopg2
    try:    
        con = psycopg2.connect("dbname={} user={} password={}".format(default_dbname, user, password))
        con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
    except Exception as e:
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