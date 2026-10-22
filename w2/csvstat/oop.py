import csv,json,statistics
data = []
class cli:
    def csvinput(path, column='',out=False):
        with open(rf'{path}', newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:    
                data.append(row)
    def is_numerical(column):
        is_num = True
        for j in range(1,len(data)):
            try:
                data[j][column] = float(data[j][column])
            except ValueError:
                is_num = False
                return False
            else: 
                is_num = True
        if is_num == True:
            return is_num
    def sort(column):
        if cli.is_numerical(column)==True:
            col = [row[column] for row in data[1:]]
            print("Количество значений:",len(col))
            print("Минимальное значение:", min(col))
            print("Максимальное значение:", max(col))
            print("Среднее арифметическое:",(sum(col)/len(col)))
            print("Медиана:",statistics.median(col))
    def __init__(self,path,kw):
        cli.csvinput(path)
        try:
            column = data[0].index(kw)
        except:
            print("wrong index")
        cli.sort(column)
a = cli(input(),input())
