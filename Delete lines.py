import glob   
path ='/Users/Matthew/Desktop/College Work/Text/*.txt'   #change this code to match location of path
files=glob.glob(path)
min = int(input("1st line to stop deleting: "))
max = int(input("2nd line to start deleting after: "))
for file in files: 
    print(file)
    infile = open(file,'r').readlines()
    with open(file,'w') as outfile:
        for index,line in enumerate(infile):
            if index >= min and index <max:
                outfile.write(line)
