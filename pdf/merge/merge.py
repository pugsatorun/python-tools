import PyPDF2

count = int(input('ファイル数を入力してください:'))
file = []
for j in range(count):
    file.append(str(input(str(j+1) + 'つ目のファイルを記入してください：')))
merge = PyPDF2.PdfFileMerger()
for i in range(count):
    merge.append(file[i])
#merge.append('GAKUBUseiseki.pdf')
#merge.append('INseiseki.pdf')
merge.write('output.pdf')
merge.close()