import  Person
def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    ListPerson = Person_File_Text(phone_book)
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Найти по фамилии: ')
            Search_By_Value(ListPerson,last_name,'')
        elif choice==3:
            new_number=input('Найти по номеру: ')
            Search_By_Value(ListPerson,'',new_number)
        elif choice==4:
            add_user(ListPerson)
        elif choice==5:
            find_by_number(ListPerson, 'phonebook.txt')
        elif choice==6:
            quit()
        Enter=input("Продолжить Enter")
        choice =show_menu()
def show_menu():
    print("\nВыберите необходимые действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice
def read_txt(filename):
    with open(filename, "r",encoding='utf-8') as f:
        phone = f.read()
    return phone
def Person_File_Text(Phone_Book):
    ListPerson=[]
    str(Phone_Book)
    Mas_Phone=Phone_Book.split('\n')
    for i in Mas_Phone:
        str(i)

        Information = i.split(",")
        Name=Information[1]
        LastName=Information[0]
        Phone=Information[2]
        Description=Information[3]
        PersonClient = Person.person(LastName=LastName,Name=Name,Phone=Phone,Description=Description)
        ListPerson.append(PersonClient)
    return ListPerson
def write_txt(filename, phone_book):
    with open('phonebook.txt' ,'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    print(phone_book)
def Search_By_Value(ListPerson,Name="",Number=""):
    if Number=="":
        for i in ListPerson:
            if i.LastName==Name:
                i.ToString()
    if Name=="":
        for i in ListPerson:
            if i.Phone==Number:
                i.ToString()
def delete_by_lastname(phone_book, lastname):
    print()
def find_by_number(ListPerson,txt):
        FullText=""
        for i in ListPerson:
            if i==ListPerson[-1]:
                FullText += i.LastName + "," + i.Name + "," + i.Phone + "," + i.Description
            else:
                FullText+=i.LastName+","+i.Name+","+i.Phone+","+i.Description+"\n"

        open(txt, "w").close()
        f = open(txt,'a',encoding='utf-8')
        f.write(FullText)
        f.close()
        print("Сохранено")
def add_user(phone_book):
    print("Добавить человека:")
    LastName=input("Фамилия: ")
    Name = input("Имя: ")
    Phone = input("Телефон: ")
    Description = input("Описание: ")
    phone_book.append(Person.person(LastName,Name,Phone,Description))
    print("Сохранино")
work_with_phonebook()

