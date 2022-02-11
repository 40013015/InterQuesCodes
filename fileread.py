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

SyncPath1= r'D:\Noice_Tuning\Reference\Y2BC_UQH_RHD_LT2_NPP_FLW'
filenamelist=GetListOfFilesFromFolder (SyncPath1, FileTypeList)

SyncPath2= r'D:\Noice_Tuning\SW\Y2BC_UQH_RHD_LT2_NPP_FLW'
filenamelist1=GetListOfFilesFromFolder (SyncPath2, FileTypeList)


#--------------------- reading Reference folder files contents------------------
for filename in filenamelist:
    #print(filename)
    f1 = open(SyncPath1+"\\"+filename,'r')
    file1=SyncPath1+"\\"+filename
    lines1 = f1.readlines()
    
    for line in lines1[5:]:
            newline=line.replace(" ","")
            file3 = open("D:\output_Ref.txt", "w+")
            file3.write(newline)
            f3="D:\output_Ref.txt"

        
        
#------------------- reading SW folder files contents-------------------
    for filename1 in filenamelist1:
        #print(filename1)
        #print(filename)
        if(filename==filename1):
            f2 = open(SyncPath2+"\\"+filename1,'r')
            file2=SyncPath2+"\\"+filename1
            lines2 = f2.readlines()
            break

    for line1 in lines2:
            newline2=line1.replace(" ","")
            file4=open("D:\output_SW.txt", "w+")
            file4.write(newline2)
            f4="D:\output_SW.txt"
                
#-------------------compare the files--------------------
    print("compared files are")
    print(filename)
    print(filename1)
    
    comp = filecmp.cmp(f3, f4, shallow = True)
    print(comp)
  
f1.close()
f2.close()
