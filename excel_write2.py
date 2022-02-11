import os
import xlsxwriter
##import openpyxl
#-------------------------------------------------------
def GetListOfFilesFromFolder(FolderPath, FileTypeList):
        try:
                FileNameList = []
                for FileType in FileTypeList:
                        for root, dirs, files in os.walk(FolderPath):
                                for f in files:
                                        if f.endswith(FileType):
                                                FileNameList.append(os.path.join(root,f))
                                        
        except:
                print('File name collection error!\n')
        return FileNameList
#-----------------------------------------------------------------------
    
FileTypeList=['.py']
Path=r"D:\Spetter Network Application P42Q"
filenamelist =GetListOfFilesFromFolder (Path, FileTypeList)
#------------------Create workbook and add worksheet---------------------

row = 0
col = 0
workbook = xlsxwriter.Workbook('D:\Searched_files.xlsx')     
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'FileNames')
worksheet.write(0, 1, 'TPR')

#-----------------writing filesnames and TPR content into excel---------------
for filename in filenamelist:
        fname=filename.split("\\")
        row+=1
        worksheet.write(row, col,fname[-1])
        f1=open(filename,'r')
        line=f1.readlines()
        for ln in line:
           if ln.startswith("report.TPR"):
               newln=ln.split()
##               print newln[2]
               worksheet.write(row, 1,newln[2])
           else:
               pass
       
workbook.close()
f1.close()
print("Search completed")
