import os
import img2pdf
import sys
from PIL import Image 

if __name__=='__main__':
    output_Folder = '/home/satoshi/lab/pugpytool/convertpdf/output/TSLDM/' #sys.argv[0] + '.pdf'
    jpg_Folder = '/home/satoshi/lab/pugpytool/convertpdf/output/TSLDM/JPG/'
    png_folder = "/mnt/c/Users/satoshi/OneDrive/研究室/2021年度M2/学会発表/TSLDM/TSLDM-final-ito/" #sys.argv[1]
    extention = '.jpg'
    png_file = [j for j in os.listdir(png_folder)if j.endswith(extention)]
    print( png_file )
    for j in png_file:
        output_FileName = j.replace(extention, '.pdf') #任意の文字列入れ替え
        with open(output_Folder + output_FileName,'wb') as f:
            f.write(img2pdf.convert(Image.open(png_folder + j).filename)) #PDFファイル生成
