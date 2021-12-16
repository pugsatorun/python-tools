import os
import pathlib
import img2pdf
import sys
from PIL import Image 

if __name__=='__main__':
    output_Folder = pathlib.Path('./output/') #sys.argv[0] + '.pdf'
    output_Folder = str(output_Folder.resolve())
    print("output_Folder :",output_Folder)
    jpg_Folder = pathlib.Path(input("相対パスを入力:"))
    jpg_Folder = str(jpg_Folder.resolve())
    print("jpg_Folder :",jpg_Folder)
    extention = '.jpg'
    jpg_file = [j for j in os.listdir(jpg_Folder)if j.endswith(extention)]
    print( jpg_file )
    for j in jpg_file:
        output_FileName = j.replace(extention, '.pdf') #任意の文字列入れ替え
        with open(output_Folder + '/' + output_FileName,'wb') as f:
            f.write(img2pdf.convert(Image.open(jpg_Folder + '/' + j).filename)) #PDFファイル生成
