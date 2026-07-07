from bookManageEngine import *
import sys

from bookManageEngine import fileHandler


def chooseOperate(num):
    jsonHandler = fileHandler();
    print(num + "num value");
    menu ={
       1:ShowBookList(jsonHandler),
       2:AddBook(jsonHandler),

    }
    menu[int(num)].action();

    def menuHandler():
        Inp = input("retun main menu? (y/n)");

        if Inp.lower() == "y":
            import main
            return main.library_Manager();
        elif Inp.lower() == "n":
            print("exiting book management")
            sys.exit();
        else:
            return menuHandler();
    
    menuHandler();    
  
        
 
     
 
     
    

    

