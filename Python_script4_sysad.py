import subprocess

#creating a function to display kernel info

def kernel_func():
    username = "uname"
    username_arg = "-a"
    print("\n")
    print("Generating info about kernel using %s\n" %(username))
    subprocess.call([username, username_arg])

#creating a function to display diskspace of a system

def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("\n")
    print("Generating hard disk info using %s\n" %(diskspace))
    subprocess.call([diskspace, diskspace_arg])

#creating a function that will call the kernel and disk function together  

def main_func():
    kernel_func()
    disk_func()
    
#main_func()

if __name__ == "__main_func__":
    main_func()