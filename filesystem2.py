# -*- coding: utf-8 -*-
#"""
#Created on Sun Sep 25 06:11:15 2022

#@author: abrah
#"""
import subprocess




#Please undock console when running program to see full
# program output.
#I declared a set of global variables for use in the program
#for the loop exit
QUIT=11


    



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
    print("8. View contents of Directory")
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
            viewcontents()
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
   
   logfile = "~/samplelog.txt"
   subprocess.call(['less', filename], shell=False)
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
    subprocess.call(['ls', '-1'], shell=True) 
    #using the call() function
    print()  
  
  
def writefile():
    filename = input("Enter a Filename: ")
    openfile3 = open(filename, "a")
    writestuff = input("Enter text to write to file: ")
    openfile3.write(writestuff)
    openfile3.close()
    print("Text written to ", filename)
def deletefile():

    print()
    filename=str(input("Enter a filename to delete: "))
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
def copyfile():
   print()
   filename=str(input("Enter the filename you wish to copy: "))
   destination=str(input("Enter the destination for the copy: "))
   subprocess.call(['cp', filename, destination], shell=False)
   print()
   print("File: ", filename, " has been copied to ", destination)
   print()

def downloadfile():
    print("once again not done yet")
def viewcontents():
   
   print("once again, not done yet")
   
def makedirectory():
  
    #lookup how mkdir works in linux for making and renanming 
    print("working on this one still")

def viewlogs():
    print("not done yet either")  
        #create logs by appending to file in each function.
        # save in log file


# 11) Exit the program menu
# a. (* do not use ‘break’)
# the loop breaks when you enter 11. see main() above

if __name__=='__main__':
    main()



