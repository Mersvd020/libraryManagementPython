from abc import ABC, abstractmethod
from pathlib import Path
import random
import json;
import sys;



databasePath=Path("library_project\\Data\\books.json")

class fileHandler:
    def __init__(self):
        self.filePath = databasePath

    def load(self):
        with open(self.filePath, "r") as file:
            return json.load(file)

    def save(self, books):
        with open(self.filePath, "w") as file:
            data=json.dumps(books);
            file.write(data);


class AddBook:
    
    def __init__(self,jsonHandler):
        self.jsonHandler = jsonHandler;
        
    
    def action(self):
        global databasePath

        print("************ fill input ********************")
        title = input("book name:");
        author = input("author name:");
        year = input("year of publication:");

        if not (title and author and year):
           print("please fill all input")
           import main;
           return main.library_Manager();
        else:

            books = self.jsonHandler.load();
            ID = len(books);

            books.append({
                    "id":ID + 1,
                    "title":title,
                    "author":author,
                    "year":year,
                    "available":True
                })

            self.jsonHandler.save(books);
            print("********* books added! **********");
            
           
     

class ShowBookList:
    
    def __init__(self,jsonHandler):
        self.jsonHandler = jsonHandler;

    def action(self):
        books = self.jsonHandler.load();
        print("________books__________")
        for bk in books:
            print(f"{bk["id"]}:\n book name :{bk["title"]}\n author name:{bk["author"]}\n year of publish:{bk["year"]}\n available:{bk["available"]}\n_____________________________ ")
    
       

class SearchBook():
    pass

class EditBook():
    pass

class RemoveBook():
    pass

if __name__ == "__bookManageEngine__" :
    pass