## Author: Alex Levering
## Date: 04/19/2017

"""Framework & steps:
# 1. Parse XML, retrieve all book titles / authors / 
"""

from os import chdir
import epub_conversion
from epub_conversion.utils import open_book
import zipfile
from lxml import etree

# Set to your e-book root folder
chdir("D:\cygwinfolders\gutenberg-generated")

book = open_book(r'D:\cygwinfolders\gutenberg-generated\25014\pg25014.epub')

lines = epub_conversion.converter.convert_epub_to_lines(book)

# Script retrieved from the following location:
# http://stackoverflow.com/questions/3114786/python-library-to-extract-epub-information
def get_epub_info(fname):
    ns = {
        'n':'urn:oasis:names:tc:opendocument:xmlns:container',
        'pkg':'http://www.idpf.org/2007/opf',
        'dc':'http://purl.org/dc/elements/1.1/'
    }

    # prepare to read from the .epub file
    zip = zipfile.ZipFile(fname)

    # find the contents metafile
    txt = zip.read('META-INF/container.xml')
    tree = etree.fromstring(txt)
    cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path',namespaces=ns)[0]

    # grab the metadata block from the contents metafile
    cf = zip.read(cfname)
    tree = etree.fromstring(cf)
    p = tree.xpath('/pkg:package/pkg:metadata',namespaces=ns)[0]
    return(p)
    
    # repackage the data
    res = {}
    for s in ['title','language','creator','date','identifier']:
        res[s] = p.xpath('dc:%s/text()'%(s),namespaces=ns)[0]

    return res
    
metadata = get_epub_info(r'D:\cygwinfolders\gutenberg-generated\1\pg1.epub')