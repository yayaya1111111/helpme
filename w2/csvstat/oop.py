import csv,json,statistics,collections

class cli:
    def csvinput(path, column='',out=False):
        data = []
        try:
            with open(rf'{path}', newline='') as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:    
                    data.append(row)
            if len(data)==0:
                print("Empty file!")
                exit()
        except FileNotFoundError:
            print("File not found")
            exit()
        return(data)
    def is_numerical(column,data):
        novalue = 0
        n = 1
        is_num = True
        while n != len(data):
            try:
                data[n][column] = float(data[n][column])
            except ValueError:
                if data[n][column]=='':
                    del data[n]
                    novalue+=1
                    n-=1
                else:   
                    is_num = False
                    return [is_num,novalue]
            except IndexError:
                return [is_num,novalue]
            else: 
                is_num = True
                n+=1
        return [is_num,novalue]
    def sort(column,data):
        testr = cli.is_numerical(column, data)
        if testr[0]==True:
            col = [row[column] for row in data[1:]]
            return  {
            "Количество значений:": len(col),
            "Минимальное значение": min(col),
            "Максимальное значение:": max(col),
            "Среднее арифметическое:": sum(col)/len(col),
            "Медиана:": statistics.median(col),
            "Строк без значений:":testr[1]
            }
        else:
            col = [row[column] for row in data[1:]]
            return {
            "Количество значений:":len(col),
            "Количество уникальных:": len(set(col)),
            "5 самых популярных:": collections.Counter(col).most_common(5),
            "Строк без значений:":testr[1],
            }

 
    def __init__(self,path,kw):
        try:
            data = cli.csvinput(path)
            column = data[0].index(kw)
            global result
            result = cli.sort(column,data)
        except ValueError:
            print("No such index!")
            exit()
a = cli(input(),input())
print(result)