from bookManageEngine import *
import sys
#from main import library_Manager;

def chooseOperate(num):

  def add_book():
    
    title = input("book name:");
    author = input("author name:");
    year = input("year:");
    

    if title and author and year:
        AddBook(title,author,year);
        
    else:
        print("please fill all input");
        sys.exit();

  if num == "1":
      add_book();
 
     
    

    

