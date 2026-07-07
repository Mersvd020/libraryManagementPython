from operationChoose import chooseOperate

def library_Manager():

     def menu_Management():

         y_input = input("======== Library ========\n1 : addbook\n2 : exit\n");
      
         if y_input == "2":
                print("Exiting the library")
                return False  
         if y_input not in ["1","2"]:
                print("Invalid input. Please enter a number between 1 and 2.");
                return menu_Management();
         def menuChoose():
             if(y_input == "1"):
                 chooseOperate("1");

         
             
         menuChoose();
      
     return menu_Management();

library_Manager();

