import csv
with open('data.txt', 'r') as f:
  kw_list = f.read().split("\n")
  print(kw_list)

with open('output.csv', 'w') as f:
  writer = csv.writer(f)
  for i in range(len(kw_list)):
    if i % 2 == 0:
      writer.writerow([kw_list[i], kw_list[i+1]])
