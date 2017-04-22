"""
Contains all scripts that analyze the e-pub file one way or the other
"""

## Script retrieved from the following location:
## http://stackoverflow.com/questions/3114786/python-library-to-extract-epub-information

import zipfile
from lxml import etree

def get_epub_metadata(fname):
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

    # repackage the data
    res = {}
    for s in ['title','language','creator','date','identifier']:
        res[s] = p.xpath('dc:%s/text()'%(s),namespaces=ns)[0]

    return res

def process_text_in_ebook(path):
    import epub_conversion
    from epub_conversion.utils import open_book
    
    book = open_book(path)
    lines = epub_conversion.converter.convert_epub_to_lines(book)
    return lines

if __name__ == "__main__":
    import unittest

    class TestStringMethods(unittest.TestCase):  
        import unittest
        
        def test_title(self):
            self.assertEqual(get_epub_metadata(r'D:\cygwinfolders\gutenberg-generated\1\pg1.epub')['title'], 'The Declaration of Independence of the United States of America')
        def test_creator(self):
            self.assertEqual(get_epub_metadata(r'D:\cygwinfolders\gutenberg-generated\1\pg1.epub')['creator'], 'Thomas Jefferson')
    unittest.main()