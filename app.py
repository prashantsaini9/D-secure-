import os
import shutil

class FileManager:
    def __init__(self):
        print("File Manager")
        
    def create_file(self,filename,content=""):
        try:
            with open(filename,'w') as f:
                f.write(content)
            print(f"File '{filename}' Created")
        except Exception as e:
            print(f"Error creating file: {e}")
            
    def read_file(self,filename):
        try:
            if os.path.exists(filename):
                with open(filename,'r') as f:
                    print("\n File Content:")
                    print(f.read())
            else:
                print("File Not Found.")
        except Exception as e:
            print(f"Error creating file: {e}")
            
    def append_file(self,filename,content):
        try:
             if os.path.exists(filename):
                with open(filename,'a') as f:
                    f.write(content)
                print(f" Content add to '{filename}'")
             else:
                print("File Not Found.")
        except Exception as e:
            print(f"Error creating file: {e}")
            
    def copy_file(self,src,dest):
        try:
            shutil.copy(src,dest)
            print(f" File copied from '{src}' to '{dest}'. ")
        except Exception as e:
            print(f"Error copying file: '{e}' ")
            
    def move_file(self,src,dest):
        try:
            shutil.move(src,dest)
            print(f" File moved from '{src}' to '{dest}'. ")
        except Exception as e:
            print(f"Error moving file: '{e}' ")
            
    def delete_file(self,filename):
        try:
             if os.path.exists(filename):
                os.remove(filename)
                print(f" File '{filename}' deleted.")
             else:
                print("File Not Found.")
        except Exception as e:
            print(f"Error deleting file: {e}")  
            
    def secure_delete(self,filename,passes=3):
        try:
             if not os.path.exists(filename):
                print(" File Not Found.")
                return
             with open(filename, "ba+", buffering=0) as f:
                 length = f.tell()
                 for _ in range(passes):
                     f.seek(0)
                     f.write(os.urandom(length))
                 os.remove(filename)
                 print(f" File '{filename}' securely deleted.")
        except Exception as e:
            print(f"Error deleting file: {e}")       



class Menu:
    def __init__(self):
        self.manager = FileManager()
        
    def show(self):
        while True:
            print("\n ======File Manager======")
            print("1. Create File: ")
            print("2. Read File: ")
            print("3. Add to File: ")
            print("4. Copy File: ")
            print("5. Move File: ")
            print("6. Delete File: ")
            print("7. Secure Delete File: ")
            print("8. Exit!")
            
            choice = input("Enter Choice:")
            
            if choice == "1":
                name = input("Enter Filename:")
                content = input("Enter Content: ")
                self.manager.create_file(name,content)
                
            elif choice == "2":
                name = input("Enter Filename:")
                self.manager.read_file(name)
                
            elif choice == "3":
                name = input("Enter Filename:")
                content = input("Enter to add more Content : ")
                self.manager.append_file(name,content)
                
            elif choice == "4":
                src = input("Enter Source Filename:")
                dest = input("Enter destination filename: ")
                self.manager.copy_file(src,dest)
                
            elif choice == "5":
                src = input("Enter Source Filename:")
                dest = input("Enter destination filename: ")
                self.manager.move_file(src,dest)
                
            elif choice == "6":
                name = input("Enter Filename:")
                self.manager.delete_file(name)
                
            elif choice == "7":
                name = input("Enter Filename:")
                self.manager.secure_delete(name)
                
            elif choice == "8":
                print("Existing File Manager")
                break
            
            else:
                print("Invalid choice. Try again.")
        
if __name__ == "__main__":
    Menu().show()
        