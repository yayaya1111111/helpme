import csv
data=[]
path = input()
def csvinput(path, column='',out=False):
    with open(rf'{path}', newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:    
            data.append(row)
csvinput(path)
def val_type():
    numerical = []
    text = []
    for i in range(len(data[1])):
        is_num = False
        for j in range(1,len(data)):
            try:
                float(data[i][j])
            except:
                is_num = False
                pass
            else: 
                is_num = True
        if is_num == True:
            numerical.append(i)
        else:
            text.append(i)
    return numerical, text
def sort_num():
    for index in :
