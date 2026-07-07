from operationChoose import chooseOperate

def library_Manager():

     def menu_Management():

         y_input = input("======== Library ========\n1 : show Books\n2 : add book\n3 :exist\n");
      
         if y_input == "3":
                print("Exiting the library")
                return False  
         elif y_input not in ["1","2","3","4"]:
                print("Invalid input. Please enter a number between 1 and 2.");
                return menu_Management();
         else:
           chooseOperate(y_input);

     return menu_Management();

 # باعث می شود فایل اگر جایی دیگری ایمپورت شد دو بار اجرا نشود یا باعث اجرایی ناخواسته نشود
if __name__ == "__main__":  # اسم ان براساس نام فایل ولی نباید برابر با نام فایل باشد مثل روبرو
    library_Manager()

