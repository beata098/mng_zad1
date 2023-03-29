import re


class EmailExtractor:
    def __init__(self, email):
        self.email = email

    def is_student(self) -> bool:
        x = re.compile("")
        x.match(self.email)
        return False

    def get_surname(self) -> str:
        return str

    def get_name(self) -> str:
        return str