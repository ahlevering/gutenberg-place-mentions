## Author: Alex Levering
## Date: 04/19/2017

"""Framework & steps:
# 1. Parse XML, retrieve all book titles / authors / 
"""

if __name__ == "__main__":
    import os
    
    # Set working directory to script location
    os.chdir("D:\git\gutenberg")
    
    # Script modules
    from lib import analyze_epub
       
    analyze_book_directories("D:\cygwinfolders\gutenberg-generated")
    subfolders = [directory[0] for directory in os.walk("D:\cygwinfolders\gutenberg-generated")]

