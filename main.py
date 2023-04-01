import unittest
import re

from email import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):

    print("aaa")
    email = "anna.kowalska@uw.edu.pl"

    match_result = re.match(r'^([a-zA-Z]+)\.([a-zA-Z]+)@.*(?:student)?.*uw\.edu\.pl$', email)

    if match_result:
        print("Imię:", match_result.group(1))
        print("Nazwisko:", match_result.group(2))
        print("Czy to student:", bool("student" in email))
    else:
        print("Nie znaleziono dopasowania")




    matches = re.match(r'([a-zA-Z]+)\.([a-zA-Z]+)@.*(?:student)?.*uw\.edu\.pl+$', email)
    if matches:
        first_name = matches.group(1)
        last_name = matches.group(2)



    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["anna.kowal@student.wat.edu.pl", True, False, "Anna", "Kowal"],
            ["joanna.kowalczyk@student.wat.edu.pl", True, False, "Joanna", "Kowalczyk"],
            ["justyna.lewandowska@student.wat.edu.pl", True, False, "Justyna", "Lewandowska"],
            ["jan.zamojski@wat.edu.pl", False, True, "Jan", "Zamojski"],
            ["tomasz.pisarek@wat.edu.pl", False, True, "Tomasz", "Pisarek"],
            ["piotr.przybysz@student.wat.edu.pl", True, True, "Piotr", "Przybysz"],
            ["andrzej.nowakowski@wat.edu.pl", False, True, "Andrzej", "Nowakowski"],
            ["magdalena.mazur@student.wat.edu.pl", True, False, "Magdalena", "Mazur"],
            ["katarzyna.bieniek@student.wat.edu.pl", True, False, "Katarzyna", "Bieniek"],
            ["julia.wysocka@wat.edu.pl", False, False, "Julia", "Wysocka"]]


    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                is_male = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_male, extractor.is_male())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())






