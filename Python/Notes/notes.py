# Parsing Parameter
# I/O Stream
from sys import argv
import argparse

parsing = argparse.ArgumentParser(description='Program Processing note',usage='%(prog)s [options]',argument_default='--help')
parsing.add_argument('option',help='addnote,delnote,listnotes')
#parsing.add_argument('other',const='wew',default='defaultvalue',nargs='?',help='Testing')

if len(argv) < 2:
    parsing.print_help()
    quit(1)
else:
    args = parsing.parse_args()

#fungsi add note
def addnote(Judul,Isi,Tag):

    return 1

#fungsi del note
def delnote(Judul):

    return 1

#fungsi list notes
def listnotes():

    return 1

if args.option == "addnote":
    print("Disini proses menambah note")
    addnote("A","A","A")
elif args.option == "delnote":
    print("Disini proses delete note")
elif args.option == "listnotes":
    print("Disini proses list note")
else:
    parsing.print_help()