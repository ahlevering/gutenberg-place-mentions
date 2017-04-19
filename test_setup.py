## Author: Alex Levering
## Date: 04/19/2017

"""Framework & steps:
# 1. Parse XML, retrieve all book titles / authors / 
"""

from os import chdir
chdir("D:\cygwinfolders\gutenberg-generated")
import epub_conversion
from epub_conversion.utils import open_book

book = open_book(r'D:\cygwinfolders\gutenberg-generated\25014\pg25014.epub')

lines = epub_conversion.converter.convert_epub_to_lines(book)

"""
from ebooklib import epub
book = epub.read_epub(r'D:\cygwinfolders\gutenberg-generated\25014\pg25014.epub')
book._id_html
for i in book.get_items:
    print(i)
"""

"""
import epub
book = epub.open_epub(r'D:\cygwinfolders\gutenberg-generated\25014\pg25014.epub')

for item in book.opf.manifest.values():
    # read the content
    data = book.read_item(item)
"""