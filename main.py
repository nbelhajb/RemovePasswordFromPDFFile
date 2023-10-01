# This is a sample Python script.
import os.path

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pikepdf
import os
from colorama import init, Fore, Style
import sys

def warnMsg(_msg):
    print(Fore.LIGHTYELLOW_EX + _msg + Style.RESET_ALL)

def showCorrectSyntax():
    warnMsg('SYNTAX ERROR - correct syntax is : main.py -f pdf_file_name -p password')

init ()

pdf_file_name=""
_password=""

#if len(sys.argv) < 2:
#    showCorrectSyntax()
#    exit(1)

#i=1
#while i < len(sys.argv)-1:
#    if sys.argv[i] == '-f':
#        pdf_file_name = sys.argv[i+1]
#        i += 1
#    if sys.argv[i] == '-p':
#        _password = sys.argv[i+1]
#        i += 1
#    i += 1

#if pdf_file_name == "":
#    showCorrectSyntax()
#    exit(1)

pdf_file_name = input(Fore.LIGHTWHITE_EX + "PDF file : ")
_password = input(Fore.LIGHTWHITE_EX + "PDF password: ")


if not os.path.isfile(pdf_file_name):
    warnMsg("file not found ({})".format(pdf_file_name))
#    showCorrectSyntax()
    exit(1)

pdf_file_ext = pdf_file_name.split(".")[-1]

if pdf_file_ext.upper() != "PDF":
    warnMsg("This is not a PDF file !")
    exit(1)

if _password == "":
    showCorrectSyntax()
    exit(1)

#print("PDF file name = "+pdf_file_name)
#print("EXT = "+pdf_file_ext)
#print("PASSWORD = "+_password)

pdf_save = os.path.splitext(pdf_file_name)[0]+"_new.pdf"
#print("NEW FILE NAME = "+pdf_save)

pdf = pikepdf.open(pdf_file_name, password=_password)

print("\nProcessing...\n")

#pdf_save = input("Save file as: ")
#pdf_loc2 = input("Save location: ")

pdf.save(pdf_save)

print("The password successfully removed from the PDF")
print("Location: " + pdf_save)

