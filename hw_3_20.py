# Задача 20 В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Пример: Ввод:ноутбук; Вывод: 12


 
w = input = 'НОУТБУК'.upper()

list_1 = ['А', 'В', 'Е', 'И', 'Н','О', 'Р', 'С', 'Т']
list_2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
list_3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
list_4 = ['Й', 'Ы']
list_5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
list_6 = ['Ш', 'Э', 'Ю']
list_7 = ['Ф', 'Щ', 'Ъ']

scrable_1={}
scrable_2={}
scrable_3={}
scrable_4={}
scrable_5={}
scrable_6={}
scrable_7={}

for i in list_1:
    scrable_1.setdefault (i, 1)

for i in list_2:
    scrable_2.setdefault (i, 2)

for i in list_3:
    scrable_3.setdefault (i, 3)

for i in list_4:
    scrable_4.setdefault (i, 4)

for i in list_5:
    scrable_5.setdefault (i, 5)

for i in list_6:
    scrable_6.setdefault (i, 8)

for i in list_7:
    scrable_7.setdefault (i, 10)

scrable_1.update(scrable_2)
scrable_1.update(scrable_3)
scrable_1.update(scrable_4)
scrable_1.update(scrable_5)
scrable_1.update(scrable_6)
scrable_1.update(scrable_7)
print(scrable_1)

su=0
for i in w:
    su += scrable_1[i]
print(su)