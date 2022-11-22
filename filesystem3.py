# -*- coding: utf-8 -*-
#"""
#Created on Sun Sep 25 06:11:15 2022

#@author: abrah
#"""
import subprocess
import datetime
from subprocess import check_output
import os


#Please undock console when running program to see full
# program output.
#I declared a set of global variables for use in the program
#for the loop exit
QUIT=11
NOW = datetime.datetime.now()





# create an option menu function that returns the value option
# this function will be called repeatedly in the while loop below
def optionmenu(option):
   # i shortened the menu options and created a return function with a parameter 
    print(' ')
    print("Menu options:")
    print("1. Open a File")
    print("2. View Files")
    print("3. Write to a File")
    print("4. Delete a File")
    print("5. Rename a File")
    print("6. Copy a File")
    print("7. Download a File") 
    print("8. Change Directory")
    print("9. Make a new Directory")
    print("10.View logs")
    print("11. QUIT")
    option=input("Enter a menu option: ")
    return option


def main():
    #use nested loops to read user choices. 
    #and create a while loop
    menu_choice='y'
# create a while loop that repeats the call for the option menu
# after an item has been selected. calls the optionmenu and sends the parameter
# menu_choice to it      
    while menu_choice != QUIT:
        menu_choice=optionmenu(menu_choice)
  # the if clause below repeats the optionmenu function after an invalid choice          
        if int(menu_choice) < 1 or int(menu_choice) > QUIT:
            print("Please enter a valid option!")
            menu_choice=optionmenu(menu_choice)
# the elif clauses evaluate user input menu_choice and call the program functions

        if menu_choice== '1':
            openfile()
        elif menu_choice=='2':
            viewfile()
        elif menu_choice=='3':
            writefile()
        elif menu_choice=='4':
            deletefile()
        elif menu_choice=='5':
            renamefile()
        elif menu_choice=='6':
            copyfile()
        elif menu_choice=='7':
            downloadfile()
        elif menu_choice=='8':
            changedir()
        elif menu_choice=='9':
            makedirectory()
        elif menu_choice=='10':
            viewlogs()
        else:  
            # Note that I used "=" instead of "=="
            # to exit the loop. because i am setting
            # the variable.
            menu_choice=QUIT
            # print("Program Terminated.")
                
 #this print statement is at the end of the loop after the else clause.       
    print("Thank you for using SimpleFileSystem!")
        
def openfile():
   filename = str(input("Enter a filename: "))
   
   #logfile = "samplelog.txt"
   subprocess.call(['less', filename], shell=False)
   #create a log entry
  # log = subprocess.check_output(['stat', filename])
   #file1 = open("samplelog.txt", "a")
   #file1.write(str(log))
   #logging file access read
   #file1.write("\n")
   #file1.write("File ")
   #file1.write(str(filename))
   #file1.write(" has been opened and read by ")
   #new logging system
   phrase = str(" has opened the directory and file ")
   path_bytes = check_output('pwd', shell=True)
   blank = path_bytes.decode('utf-8')
   path_bytes2 = check_output('whoami', shell=True)
   username = path_bytes2.decode('utf-8')
   logwrite(username, phrase, blank, filename)
   #old logging system
   #username = str(subprocess.call(['whoami'], shell=False))
   #blank = str(subprocess.call(["pwd"], shell=False))
   #file1.write(str(username))
   #file1.write("\n")
   #file1.write(str(NOW))
   #file1.close()
   
# Append-adds at last
   #file1 = open("myfile.txt", "a")  # append mode
   #file1.write("Today \n")
   #file1.close()
 
   #subprocess.call(['stat', filename, >>  logfile], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
   #subprocess.call(['stat', filename, '>>', logfile], capture_output=True, shell=False)
   #below line works
   #openfile1 = open(filename, 'r+')
   #print(openfile1.read())
   #
   #openfile1.close()
   #subprocess.call(['less', filename], shell=True)  
def viewfile():
    print()
    print("Files in current directory:  ")
    print()
    subprocess.call(['ls'], shell=False) 
    #using the call() function
    print()  
    
  
def writefile():
    filename = input("Enter a Filename: ")
    openfile3 = open(filename, "a")
    writestuff = input("Enter text to write to file: ")
    openfile3.write(writestuff)
    openfile3.close()
    print("Text written to ", filename)
    #log = subprocess.check_output(['stat', filename])
   # file1 = open("samplelog.txt", "a")
    #file1.write(str(log))
    # logging file write
    #file1.write("\n")
    #file1.write("File ")
    #file1.write(str(filename))
    #file1.write(" has been written to by ")
    #username = subprocess.call(['whoami'], shell=False)
    #file1.write(str(username))
    #file1.write("\n")
    #file1.write(str(NOW))
    phrase = str("has been written to")
    path_bytes = check_output('pwd', shell=True)
    blank = path_bytes.decode('utf-8')
    path_bytes2 = check_output('whoami', shell=True)
    username = path_bytes2.decode('utf-8')
    logwrite(filename, phrase, blank, username)


    #file1.close()
 
def deletefile():

    print()
    filename=str(input("Enter a filename to delete: "))
    #log = subprocess.check_output(['stat', filename])
    file1 = open("samplelog.txt", "a")
    #file1.write(str(log))
    #file1.write("\n File deleted.\n")
    #logging file deletion
    #new log system
    phrase = str("has been deleted from")
    path_bytes = check_output('pwd', shell=True)
    blank = path_bytes.decode('utf-8')
    path_bytes2 = check_output('whoami', shell=True)
    username = path_bytes2.decode('utf-8')
    logwrite(filename, phrase, blank, username)


    # old log system
    #file1.write("\n")
    #file1.write("File ")
    #file1.write(str(filename))
    #file1.write(" has been deleted by ")
    #username = subprocess.call(['whoami'], shell=False)
    #file1.write(str(username))
    #file1.write("\n")
    #file1.write(str(NOW))
    #file1.close()
    print("File deletion logged.")
    subprocess.call(['rm', filename], shell=False)
    print()
    print("File ", filename, "deleted.")
    print()
    
def renamefile():
    print()
    filename1 = str(input("Enter the name of the file you want to rename: "))
    print()
    filename2 = str(input("Enter the new filename: "))
    subprocess.call(['mv', filename1, filename2], shell =False)
    print()
    print("File ", filename1, " has been renamed to ", filename2)
    #new logging system
    phrase = str("has been renamed")
    blank= str(filename2)
    filename=str(filename1)
    path_bytes2 = check_output('whoami', shell=True)
    username = path_bytes2.decode('utf-8')
    logwrite(filename, phrase, blank, username)

    #old logging system
    #log = subprocess.check_output(['stat', filename2])
    #file1 = open("samplelog.txt", "a")
    #file1.write("\n")
    #file1.write("File ")
    #file1.write(str(filename1))
    #file1.write(" has been renamed to ")
    #file1.write(str(filename2))
    #file1.write( " by ")
    #username = subprocess.call(['whoami'], shell=False)
    #file1.write(str(username))
    #file1.write("\n")
    #file1.write(str(NOW))
    #file1.close()
    print("File renaming logged.")
    
    #file1.write(str(log))
    #file1.write(str(filename1))
    #file1.write(" renamed to ")
    #file1.write(str(filename2))
    #file1.close()
 
def copyfile():
   print()
   filename=str(input("Enter the filename you wish to copy: "))
   destination=str(input("Enter the destination file or directory for the copy: "))
   subprocess.call(['cp', filename, destination], shell=False)
   print()
   print("File: ", filename, "has been copied", destination)
   print()
   #new logging system
   phrase = str(" has been copied to ")
   path_bytes2 = check_output('whoami', shell=True)
   username = path_bytes2.decode('utf-8')
   logwrite(filename, phrase, destination, username)

   #old logging system
   #log = subprocess.check_output(['stat', filename])
  # file1 = open("samplelog.txt", "a")
   #file1.write("\n")
   #file1.write("File ")
   #file1.write(str(filename))
   #file1.write(" has been copied to ")
   #file1.write(str(destination))
   #file1.write( " by ")
   #username = subprocess.call(['whoami'], shell=False)
   #file1.write(str(username))
   #file1.write("\n")
   #file1.write(str(NOW))
   print("File copy logged.")
   #file1.write(str(log))
   #file1.close()
 
def downloadfile():
    print("OpenLDAP required to use this function.")
def changedir():
   
   #change to a directory of user's choice
   directoryvar= str(input("Enter the path or name of a directory you want to change to: "))
   #use os module to change current directory while running script, makes other directories searchable
   os.chdir(directoryvar)
   #new logging system
   phrase = str(" has changed current directory to ")
   blank= str(" ")
   
   path_bytes2 = check_output('whoami', shell=True)
   username = path_bytes2.decode('utf-8')
   #use os module to get current directory to print out
   cwd = os.getcwd()
   print("Directory is now ", cwd)
   logwrite(username, phrase, directoryvar, blank)

   
def makedirectory():
  
    #make a directory. can make multiple directories with {dir1,dir2,dir3}
    newdir=input("Enter the path or directory name you wish to create: ")
    subprocess.call(['mkdir', newdir], shell=False)
    #new logging system
    phrase = str("has made a new directory at")
    blank= str(" ")
    path_bytes2 = check_output('whoami', shell=True)
    username = path_bytes2.decode('utf-8')
    logwrite(username, phrase, newdir, blank)
    print("Directory ", newdir, " created.")

def viewlogs():
    #write the log first
    #create logs by appending to file in each function.
        
        # save in log file
    phrase = str("has viewed the logs!")
      #path_bytes = check_output('pwd', shell=True)
    blank = str(" ")
    blank2 = str(" ")
    path_bytes2 = check_output('whoami', shell=True)
    username = path_bytes2.decode('utf-8')
    logwrite(username, phrase, blank, blank2)
    #call the command to view the logs
    subprocess.call(['less', '/var/sfssamplelog.txt'], shell=False)  
     
    
   
#function to write logs
def logwrite(var1, phrase, var2, var3):

   file1 = open("/var/sfssamplelog.txt", "a")
   file1.write("\n")
   #file1.write("File ")
   file1.write(str(var1))
   #file1.write(" has been ")
   file1.write(str(phrase))
   #file1.write( " to ")
   #username = subprocess.call(['whoami'], shell=False)
   file1.write(str(var2))
   #file1.write(" by ")
   file1.write(str(var3))
   file1.write("\n")
   file1.write(str(NOW))
   file1.write("\n")
   file1.write("          -- End of Log --             ")

# 11) Exit the program menu
# a. (* do not use ‘break’)
# the loop breaks when you enter 11. see main() above

if __name__=='__main__':
    main()
