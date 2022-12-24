import re
print("Выберите одно из действий: : 1 - Считать имена и фамилии, "
      "2- Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход")
while True:
    try:
        user_input=int(input("Введите ваше действие: "))
    except:
        print("Выберите одно из действий: : 1 - Считать имена и фамилии, "
              "2- Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход")
        continue
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        content=file.read()
        colors_list= re.findall(r'#[a-z0-9]{6}', content)
        email_list= re.findall(r'[a-z0-9]+@[a-z.0-9-]+', content)
        names_surnames_list=re.findall(r"[A-Z][a-z-]+\s+[A-Za-d][A-Za-z- O']+", content)
        file_list = re.findall(r'[A-Z][A-Za-z]*\.[a-z0-9]+', content)
    if user_input == 1:
        with open('name.txt', 'w') as name_file:
            name_file.write(f'{len(names_surnames_list)}\n{names_surnames_list}')
    elif user_input == 2:
        with open('email.txt', 'w') as email_file:
            email_file.write(f'{len(email_list)}\n{email_list}')
    elif user_input == 3:
        with open('file.txt', 'w') as file_file:
            file_file.write(f'{len(file_list)}\n{file_list}')
    if user_input == 4:
        with open('color.txt', 'w') as color_file:
            color_file.write(f'{len(colors_list)}\n{colors_list}')
    elif user_input == 5:

        break
    else:
        print("Выберите одно из действий: : 1 - Считать имена и фамилии, "
              "2- Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход")






