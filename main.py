## Author: Alex Levering
## Date: 04/19/2017

"""Framework & steps:
# 1. Parse XML, retrieve all book titles / authors / 
"""

if __name__ == "__main__":
    from os import chdir
    from os import walk
    
    # Set working directory to script location
    chdir("D:\git\gutenberg")
    
    # Script modules
    from lib import analyze_epub
    from lib import alter_database
    
    # Database set-up
    alter_database.create_database("postgres", "gutenberg", "postgres", "")
    
    # Create Gutenberg table
    alter_database.create_postgis_extension("gutenberg", "postgres", "")
    
    alter_database.create_country_table(dbname, user, password, table_name, overwrite = False):
    
    # Note-to-self: Refactor to wrapper later
    subfolders = [directory[0] for directory in walk(r'D:\cygwinfolders\gutenberg-generated')]
    for directory in subfolders[2:3]:
        book_text = analyze_epub.process_text_in_ebook(directory)
        print(book_text)
    

