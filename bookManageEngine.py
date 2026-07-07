from abc import ABC, abstractmethod
from pathlib import Path
import random
import json;

databasePath=Path("library_project\\Data\\books.json")
"""
file = open(databasePath,"r");
ID = len(file);
file.close();
"""



class AddBook():
    print("addBookStart");
   
    def __init__(self,title,author,year):
        self.title = title;
        self.author = author;
        self.year = year;

    def addbook_action(self):
        global databasePath
        book = {
             "id":2,
             "title":self.title,
             "author":self.author,
             "year":self.year,
             "available":True
            }
        data = json.dumps(book);
        databasePath.write_text(data);
   
    print("addBookFinished");

class ShowBookList():
    pass

class SearchBook():
    pass

class EditBook():
    pass

class RemoveBook():
    pass