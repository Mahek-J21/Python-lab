import os.path
import sys
fname=input("Enter the file name whose contents are to be sorted")
if not os.path.isfile(fname):
    print("File",fname,"Does not exists")
    sys.exit(0)
infile=open(fname,"r")
my_List=infile.readlines()
line_List=[]
for line in my_List:
    line_List.append(line.strip())
line_List.sort()
outfile=open("sorted.txt","w")
for line in line_List:
    outfile.write(line+"\n")
infile.close()
outfile.close()
if os.path.isfile("sorted.txt"):
    print("\n File containing sorted content sorted.txt createdd successfully")
    print("sorted.txt contains",len(line_List),"lines")
    print("contents of sorted.txt")
    rdfile = open("sorted.txt","r")
for line in rdfile:
    print(line,end="")
rdfile.close()