# Source: https://www.reddit.com/r/learnpython/comments/42dqv4/python_module_to_fetch_book_info_from_google_books/

import requests
import re

class gbooks():
    def __init__(self):
        self.earliest_year = 9999
        self.earliest_entry = None
        self.maturity_rating = None
        self.categories = None
        
        self.googleapikey="AIzaSyDiUD6qk39iMWSQ3Yo8Jmmnk5F0uoKFYbw"

    def search(self, title, author):
        search_value = title + author
        parms = {"q":search_value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        response = r.json()
        self.retrieve_earliest_publication_date(response, title)
        
    def retrieve_earliest_publication_date(self, search_results, title):
        self.earliest_date = 9999 
        
        for current_result in search_results["items"]:
            print(current_result["volumeInfo"])
            year = repr(current_result["volumeInfo"]["publishedDate"])
            matched_year = re.match(r'.*([1-3][0-9]{3})', year)
            
            if 'title' in current_result["volumeInfo"].keys() and matched_year is not None:
                if title in current_result["volumeInfo"]["title"]:
                    year = int(matched_year.group(1))

            if not isinstance(year,int): year = 9999
            if self.earliest_year > year:
                self.earliest_year = year
                self.earliest_entry = current_result
            
        self.set_entry_metadata()

    def set_entry_metadata(self):
        if 'maturityRating' in self.earliest_entry["volumeInfo"].keys(): self.maturity_rating = self.earliest_entry["volumeInfo"]["maturityRating"]
        if 'categories' in self.earliest_entry["volumeInfo"].keys(): self.categories = self.earliest_entry["volumeInfo"]["categories"]
        if 'pageCount' in self.earliest_entry["volumeInfo"].keys(): self.pageCount = self.earliest_entry["volumeInfo"]["pageCount"]
        


if __name__ == "__main__":
    bk = gbooks()
    # bk.search("The Poetical Works of Addison; Gay's Fables; and Somerville's Chase / With Memoirs and Critical Dissertations, by the Rev. George Gilfillan Joseph Addison")
    bk.search("The First Men in the Moon",  "H. G. Wells")