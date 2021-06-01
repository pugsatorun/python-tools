import os
import img2pdf
import cv2
import sys
from PIL import Image
import numpy as np

if __name__=='__main__':
    output_Folder = '/home/satoshi/lab/pugpytool/convertpdf/output/TSLDM/' #sys.argv[0] + '.pdf'
    jpg_Folder = '/home/satoshi/lab/pugpytool/convertpdf/output/TSLDM/JPG/'
    png_folder = "/mnt/c/Users/satoshi/OneDrive/研究室/2021年度M2/学会発表/TSLDM/TSLDM-final-ito/" #sys.argv[1]
    extention = '.png'
    png_file = [j for j in os.listdir(png_folder)if j.endswith(extention)]
    #print( png_file )
    for j in png_file:
        output_FileName = j.replace(extention, '.pdf') #任意の文字列入れ替え
        with open(output_Folder + output_FileName,'wb') as f:
            #白画像生成
            height = 1000
            width = 2000
            white = np.zeros((height, width, 3))
            white += 255 # たさなかったら黒色
            # ここまでが生成
            x_offset=0 #重ねるときの基準値を設定
            y_offset=0 #重ねるときの基準値を設定
            jpg_file_name = j.replace(extention, '.jpg') #jpg保存時拡張子を変換
            jpg_file = cv2.imread(png_folder + j, -1)
            jpg_msk = jpg_file[:,:, 3]
            white = white[:, :, :3]
            jpg_msk_RGB = 255 - cv2.merge((jpg_msk, jpg_msk, jpg_msk))
            white = cv2.resize(white, jpg_file.shape[1::-1]) #画像サイズを合わせるためのリサイズ
            jpg_file = cv2.bitwise_and(white, jpg_msk_RGB)
            jpg_file = cv2.bitwise_or(jpg_file, jpg_msk)
            cv2.imwrite(jpg_Folder + jpg_file_name, jpg_file, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            f.write(img2pdf.convert(Image.open(jpg_Folder + jpg_file_name).filename)) #PDFファイル生成
