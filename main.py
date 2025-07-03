# 1. Запись текста

# Условие:
# Попроси пользователя ввести предложение и запиши его в файл text1.txt.
# Если файл уже есть — перезапиши.
# Чавоб:
# a= input('Enter sentense: ')
# with open("text1.txt", "w") as myfile:
#     b=myfile.write(a)





# ✅ 2. Чтение всего файла

# Условие:
# Открой файл text1.txt и выведи весь текст на экран.
# Чавоб:
# with open('text1.txt','r') as myfile:
#     b=myfile.read()
#     print(b)


# ✅ 3. Чтение построчно

# Условие:
# Открой файл text2.txt и выведи каждую строку с её номером (нумерация с 1).
# Чавоб:
# with open('text2.txt','r') as file:
#     b=file.readlines()
#     for i in range(len(b)):
#         print(f'{i+1}: {b[i]}')




# ✅ 4. Подсчёт символов

# Условие:
# Подсчитай, сколько всего символов (включая пробелы и переносы) в файле text3.txt.
# Чавоб:
# with open('text3.txt','r') as file:
#     b=file.read()
#     print(len(b))

# ✅ 5. Подсчёт слов

# Условие:
# Подсчитай количество всех слов в файле text4.txt.
# Чавоб:
# with open('text4.txt', 'r') as myfile:
#     txt=myfile.read()
#     lst=txt.split()
#     print(len(lst))


  

# ✅ 6. Поиск строки

# Условие:
# Попроси пользователя ввести слово.
# Открой text5.txt и выведи все строки, где встречается это слово.
# Чавоб:
# search=input('Enter word for search: ')
# with open('text5.txt', 'r') as myfile:
#     txt=myfile.readlines()
#     for i in txt:
#         if search in i:
#             print(i)

# ✅ 7. Добавление в файл

# Условие:
# Попроси пользователя ввести строку и добавь её в конец файла text6.txt.
# Чавоб:
# a=input('Enter sentense: ')
# with open('text6.txt','a') as myfile:
#     b=myfile.write(a)



# ✅ 8. Копирование

# Условие:
# Скопируй содержимое text7.txt в новый файл text7_copy.txt.
# Чавоб:
# with open('text7.txt', 'r') as myfile:
#     a=myfile.read()
# with open('text7_copy.txt', 'w') as myfile2:
#     b=myfile2.write(a)




# ✅ 9. Замена слова

# Условие:
# Замени все вхождения слова bad на good в файле text8.txt и сохрани в text8_new.txt.
# Чавоб:
# with open('text8.txt', 'r') as myfile:
#     txt=myfile.read()
#     a=txt.replace('bad','good')

# with open('text8.txt', 'w') as myfile:
#     myfile.write(a)





# ✅ 10. Удаление пустых строк

# Условие:
# Открой файл text9.txt, удали все пустые строки и сохрани результат в text9_clean.txt.
# Чавоб:
# with open('text9.txt', 'r') as myfile:
#     lines=myfile.readlines()
#     for i in lines:
#         if i=='\n':
#             lines.remove(i)
# with open('text9_clean.txt', 'w') as myfile2:
#     myfile2.writelines(lines)
