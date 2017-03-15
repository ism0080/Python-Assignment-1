import re

# ID = "A123"
# GENDER = "M"
# AGE = 12
# SALES = 123
# BMI = "NORMAL"
# SALARY = 10.999
# BIRTHDAY = "24-10-1996"

# file = open("table.txt", "r")
# for line in file:
#     print(line)

with open('table.txt', 'r') as file:
    # data = file.readlines()
    data2 = file.read()
    # print(data)

    line = data2.split()
    dic = dict(e.split('=') for e in line)
    print(dic)
    # print(data.split('='))


class Validator(object):

    def __init__(self):
        self.regDic = {"id": r'[A-Z][1-9]{3}',
                       "gender": r'M|F',
                       "age": r'[0-9]{2}',
                       "sales": r'[0-9]{3}',
                       "bmi": r'(Normal|Overweight|Obesity|Underweight)',
                       "salary": r'[0-9]{2,3}',
                       "birthday": r'[0-3][1-9]-[0-9]{1,2}-[1-9]{4}'}
        # for i, j in reg:
        self.regLi = [r'[A-Z][1-9]{3}',
                      r'M|F',
                      r'[0-9]{2}',
                      r'[0-9]{3}',
                      r'(Normal|Overweight|Obesity|Underweight)',
                      r'[0-9]{2,3}',
                      r'[0-3][1-9]-[0-9]{1,2}-[1-9]{4}']

    def valid(self, input):
        clean = []
        for key, value in input.items():
            match = re.search(self.regDic.get(key), value)
            if match is not None:
                clean.extend(["{} = True".format(key.upper())])
            else:
                clean.extend(["{} = False".format(key.upper())])
        return clean

    # def valid(self, input):
    #     clean = []
    #     i = 0
    #     for key, value in input.items():
    #         match = re.search(self.regLi[i], value)
    #         if match is not None:
    #             clean.extend(["{} = True Validation".format(key.upper())])
    #         else:
    #             clean.extend(["{} = False Validation".format(key.upper())])
    #         i += 1
    #     return clean

    def empid(self, empid):
        match = re.search(r'id=[A-Z][1-9]{3}', empid)
        if match is not None:
            clean = "Id = True Validation"
            new_match = re.search(r'[A-Z][1-9]{3}', match.group(0))
            self.id = new_match.group(0)
        else:
            clean = "Id = False Validation"
        return clean

    def gender(self, gender):
        match = re.search(r'gender=M|F', gender)
        if match is not None:
            clean = "Gender = True Validation"
            new_match = re.search(r'M|F', match.group(0))
            self.gender = new_match.group(0)
        else:
            clean = "Gender = False Validation"
        return clean

    def age(self, age):
        match = re.search(r'age=[0-9]{2}', age)
        if match is not None:
            clean = "Age = True Validation"
            new_match = re.search(r'[0-9]{2}', match.group(0))
            self.age = new_match.group(0)
        else:
            clean = "Age = False Validation"
        return clean

    def sales(self, sales):
        match = re.search(r'sales=[0-9]{3}', sales)
        if match is not None:
            clean = "Sales = True Validation"
            new_match = re.search(r'[0-9]{3}', match.group(0))
            self.sales = new_match.group(0)
        else:
            clean = "Sales = False Validation"
        return clean

    def bmi(self, bmi):
        match = re.search(r'bmi=(Normal|Overweight|Obesity|Underweight)', bmi)
        if match is not None:
            clean = "Bmi = True Validation"
            new_match = re.search(r'(Normal|Overweight|Obesity|Underweight)', match.group(0))
            self.bmi = new_match.group(0)
        else:
            clean = "Bmi = False Validation"
        return clean

    def salary(self, salary):
        match = re.search(r'salary=[0-9]{2,3}', salary)
        if match is not None:
            clean = "Salary = True Validation"
            new_match = re.search(r'[0-9]{2,3}', match.group(0))
            self.salary = new_match.group(0)
        else:
            clean = "Salary = False Validation"
        return clean

    def birthday(self, birthday):
        match = re.search(r'birthday=[0-3][1-9]-[0-9]{1,2}-[1-9]{4}', birthday)
        if match is not None:
            clean = "Birthday = True Validation"
            new_match = re.search(r'[0-3][1-9]-[0-9]{1,2}-[1-9]{4}', match.group(0))
            self.birthday = new_match.group(0)
        else:
            clean = "Birthday = False Validation"
        return clean

    def __str__(self):
        return "id = {id}\n" \
               "gender = {gender}\n" \
               "age = {age}\n" \
               "sales = {sales}\n" \
               "bmi = {bmi}\n" \
               "salary = {salary}\n" \
               "birthday = {birthday}".format(
                id=self.id, gender=self.gender, age=self.age,
                sales=self.sales, bmi=self.bmi, salary=self.salary,
                birthday=self.birthday)

e = Validator()
print(e.valid(dic))
# print(e.empid(data))
# print(e.gender(data))
# print(e.age(data))
# print(e.sales(data))
# print(e.bmi(data))
# print(e.salary(data))
# print(e.birthday(data))

# try:
#     matchObj = re.match(r'[A-Z][1-9]{3}', ID)
#     if matchObj:
#         var_id = ID
#         print(var_id)
# except re.error:
#     print("Enter a valid ID")
#

# ID = "A123"
# re.match(r'[A-Z][1-9]{3}', ID)
