import sys
rep_word = ['temp']
rep_word2 = ["frequency"]

with open(sys.argv[1]) as oldfile, open("temp-out.csv","w") as newfile_temp:
    for line in oldfile:
        if any(bad_word in line for bad_word in rep_word):
            newfile_temp.write(line)
with open(sys.argv[1]) as oldfile, open("frequency.csv","w") as newfile_frequency:
    for line in oldfile:
        if any(bad_word2 in line for bad_word2 in rep_word2):
            newfile_frequency.write(line)