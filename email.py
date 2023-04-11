import re


class EmailExtractor:

    def __init__(self, email):
        self.email = email
        self.name = None
        self.surname = None
        self.isStudent = None
        self.regex()

    def regex(self):
        regex = r'^([a-zA-Z]+)\.([a-zA-Z]+)[0-9]*@(\bstudent\b\.)?(wat\.edu\.pl)'
        results = re.match(regex, self.email)
        if results:
            self.name = results.group(1)
            self.surname = results.group(2)
            self.isStudent = bool(results.group(3))
        return self.name, self.surname, self.isStudent

    def is_student(self) -> bool:
        return self.isStudent

    def is_male(self) -> bool:
        last_character = self.name[-1]
        if last_character == 'a':
            return False
        else:
            return True

    def get_surname(self) -> str:
        self.surname = self.surname.capitalize()
        return self.surname

    def get_name(self) -> str:
        self.name = self.name.capitalize()
        return self.name