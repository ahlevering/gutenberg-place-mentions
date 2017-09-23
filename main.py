## Author: Alex Levering
## Date: 04/19/2017

"""Framework & steps:
# 1. Parse XML, retrieve all book titles / authors / 


Get books from Gutenberg (desc)
wget geonames (wget -r -np -k -nd http://download.geonames.org/export/dump/)
"""
if __name__ == "__main__":
    from os import chdir
    from os import walk
    import logging
    import psycopg2
    
    # Set working directory to script location
    chdir("D:\git\gutenberg")
    
    # Script modules
    from lib import analyze_epub
    from lib import alter_database_refactored as alter_db
    
    gutenberg_db = alter_db.database_operations()
    gutenberg_db.set_database_credentials(user = "postgres", password = "postgres")
    gutenberg_db.connect_to_default_database(default_database_name = "postgres")
    gutenberg_db.set_project_database_name(project_database_name = "gutenberg")
    gutenberg_db.create_project_database()
    gutenberg_db.close_default_db_connection()
    gutenberg_db.connect_to_project_database()
    gutenberg_db.create_project_database_postgis_extension()
    
    ## Create database for location data ##
    gutenberg_db.set_location_table_name(location_table_name = "location_lut_1000")
    gutenberg_db.create_location_table(overwrite = False)
    gutenberg_db.insert_location_file(location_file_name = "D:/git/gutenberg/data/cities1000.txt")
    
    
    
    
    
"""       
    # Note-to-self: Refactor to wrapper later
    subfolders = [directory[0] for directory in walk(r'D:\cygwinfolders\gutenberg-generated')]
    for directory in subfolders[2:3]:
        book_text = analyze_epub.process_text_in_ebook(directory)
        print(book_text)
"""

