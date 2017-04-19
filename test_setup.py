## Author: Alex Levering
## Date: 04/19/2017

"""Framework & steps:
# 1. Parse XML, retrieve all book titles / authors / 
"""

import rdflib
from os import chdir
import epub
chdir("D:\cygwinfolders\gutenberg-generated")

book = epub.open_epub(r'D:\cygwinfolders\gutenberg-generated\25060\pg25060.epub')

for item in book.opf.manifest.values():
    # read the content
    data = book.read_item(item)
"""
g=rdflib.Graph()
g.load(r'D:\cygwinfolders\gutenberg-generated\25060\pg25060.rdf')

print("graph has %s statements." % len(g))


import pprint
for stmt in g:
    pprint.pprint(stmt)

for subj, pred, obj in g:
   if (subj, pred, obj) not in g:
       raise Exception("It better be!")
   print("{} ###### {}".format(pred,obj))
 """