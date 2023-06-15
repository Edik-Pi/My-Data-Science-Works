#!/usr/bin/env python
# coding: utf-8

# In[1]:


""""1. Дана строка со значениями, которые разделены запятыми:
line = '2019-07-01,organic,4293'
Напишите функцию column_count, которая возвращает число столбцов в такой строке"""

# importing pandas
import pandas as pd
 
# creating dataframe
df = pd.DataFrame({'Line': ['2019-07-01,organic,4293']})
 
print(len(df))
print(len(df.columns))

# obtaining the shape
print("shape of dataframe", df.shape)
 
# obtaining the number of rows
print("number of rows : ", df.shape[0])
 
# obtaining the number of columns
print("number of columns : ", df.shape[1]) 



# In[3]:


""""2.  Создайте класс сотрудника Employee. При инициализации класса задается имя сотрудника name и его текущая зарплата salary. Напишите следующие методы:
1.Метод up, который увеличивает зарплату сотрудника на 100
2.Метод print, который выводит на экран текущую зарплату сотрудника в формате "Сотрудник Иван, зарплата 100"""

class Employee:
    def __init__(self):
        self.name='Ivan'
        self.Salary =5000


    def up(self):
        print('Сотрудник Иван, зарплата:', self.Salary*100)

Employee1=Employee()
Employee1.up()


# In[ ]:


""""3.  Вам нужно помочь секретарю автоматизировать работу. Для этого нужно написать программу, которая будет на основе хранимых данных исполнять пользовательские команды.

Исходные данные имеют следующую структуру:
1.перечень всех документов
documents = [
{‘type’: ‘passport’, ‘number’: ‘2207 876234’, ‘name’: ‘Василий Гупкин’},
{‘type’: ‘invoice’, ‘number’: ‘11-2’, ‘name’: ‘Геннадий Покемонов’},
{‘type’: ‘insurance’, ‘number’: ‘10006’, ‘name’: ‘Аристарх Павлов’}
]
2.перечень полок, на которых хранятся документы (если документ есть в documents, то он обязательно должен быть и в directories)
directories = {
‘1’: [‘2207 876234’, ‘11-2’],
‘2’: [‘10006’],
‘3’: []} """
def people(documents):
    x = input("Номер документа ")
    for i in documents:
        if i["number"] == x:
            return i["name"]


def shelf(directories):
    x = input("Номер документа ")
    for i in directories.items():
        if x in i[1]:
            return i[0]


def lst(documents):
    for i in documents:
        print(i["type"], i["number"], i["name"])


def add(directories, documents):
    # Пример - passport, 123, АА ББ, 3
    x = list(input("Тип, номер, имя и полку(Через запятую").split(","))
    documents.append({"type": x[0], "number": x[1], "name": x[2]})
    directories[x[3]].append(x[1])
    print(documents)
    print(directories)


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

print(people(documents))
print(shelf(directories))
lst(documents)
add(directories, documents)


# In[ ]:




