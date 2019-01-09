import os
import time

if __name__ == "__main__":
   if os.name == "nt":
      print("This machine is running MS Windows. Running taskmgr...")
      time.sleep(3)
      os.system("taskmgr")    
   if os.name == "posix":
      print("This machine is running Linux. Running top...")
      time.sleep(3)
      os.system("top")
   
            
      
