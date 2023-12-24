


def main1():
 print("2023/09/24 00:00|Практическая работа по уроку Организация программ и методы строк.")

 my_string = "Something Interesting"
 print("длина строки -", len(my_string))
 print("Верхний -", my_string.upper())
 print("Нижний -", my_string.lower())
 print("без пробелов -", my_string.replace(" ", ""))
 print("первый символ -", my_string[0])
 print("последний символ -", my_string[-1])
 print("Конец этой практической")
 print(" ")

def main2():
 print("2023/09/24 00:00|Практическое задание по теме: Неизменяемые и изменяемые объекты. Кортежи")

 immutable_var = (2, "yes", [5, 6, 7])
 print(immutable_var)
 """ immutable_var(1) = "no" """ "так как кортеж это неизменяемая структура данных, его эелементы нельзя изменить"

 mutable_list = [15, "prise", ["no", "yes", "maybe"]]
 mutable_list[2] = "yes"
 print(mutable_list)
 print("конец этой практической")
 print(" ")


def main3():
 print("2023/09/25 00:00|Практическое задание по теме: Списки и словари")
 my_list = ["apple", "orange", "banana", "grapefruit", "lemon"]
 print("список - ", my_list)
 print("первый и последний элементы - ", my_list[1], my_list[-1])
 print("элементы с 3 по 5 - ", my_list[3:5])
 my_list[3] = "lime"
 print("изменённый список - ", my_list)

 my_dict = {'apple': 'яблоко', 'game': 'игра', 'water': 'вода', 'genius': 'гений', 'etc': 'и так далее'}
 print(my_dict)
 print(my_dict['genius'])
 my_dict['apple'] = 'огурец'
 print(my_dict)
 print("конец этой практической")
 print(" ")


main1()
main2()
main3()
