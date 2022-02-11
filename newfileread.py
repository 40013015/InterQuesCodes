import os
import filecmp
#-------------------------------------------------------
def GetListOfFilesFromFolder(FolderPath, FileTypeList):
        try:
                FileNameList = []
                for FileType in FileTypeList:
                        for root, dirs, files in os.walk(FolderPath):
                                for f in files:
                                        if 'Support_Files' not in root:
                                                if f.endswith(FileType):
                                                       FileNameList.append(os.path.join(f))
        except:
                print('File name collection error!\n')
        return FileNameList

#--------------------------------------------------------
FileTypeList=['.sos']

SyncPath1= r'D:\newfold1(SW)'
filenamelist=GetListOfFilesFromFolder (SyncPath1, FileTypeList)

SyncPath2= r'D:\newfold(reference)'
filenamelist1=GetListOfFilesFromFolder (SyncPath2, FileTypeList)


#--------------------- reading Reference folder files contents------------------
for filename in filenamelist:
    f1 = open(SyncPath1+"\\"+filename,'r')
    #file1=SyncPath1+"\\"+filename
    lines1 = f1.readlines()
    
    for line in lines1:
        if line.startswith("#"):
            pass
        else:
            #newline=line.replace(" ","")
            file3 = open("D:\output_Ref.txt", "w+")
            file3.write(line)
    f3="D:\output_Ref.txt"
            
        
#------------------- reading SW folder files contents-------------------
    for filename1 in filenamelist1:
        #print(filename1)
        #print(filename)
        if(filename==filename1):
            f2 = open(SyncPath2+"\\"+filename1,'r')
            #file2=SyncPath2+"\\"+filename1
            lines2 = f2.readlines()
            break    

            for line1 in lines2:
                if line1.startswith("#"):
                   pass
                else:
                   file4=open("D:\output_SW.txt", "w+")
                   file4.write(line1)
        f4="D:\output_SW.txt"
         
                
#-------------------compare the files--------------------
    print("compared files are")
    print(filename)
    print(filename1)
    
    comp = filecmp.cmp(f3, f4, shallow = True)
    print(comp)
  
f1.close()
f2.close()
##file3.truncate(0)
##file4.truncate(0)
##
