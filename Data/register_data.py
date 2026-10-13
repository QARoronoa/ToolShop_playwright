import faker
from faker import Faker

faker = Faker(locale="FR_fr")
class register:

    @staticmethod
    def register_formulaire():
        return {
            "fist_name" : faker.first_name(),
            "last_name" : faker.last_name(),
            "dob" :  "1990-05-15",
            "email" : faker.email(),
            "pwd" : "$4d9ZZVSXp$fA"

        }

    @staticmethod
    def fail_register_formulaire():
        return {
            "fist_name": faker.first_name(),
            "last_name": faker.last_name(),
            "dob": "1990-05-15",
            "email": "fail.fail.fail",
            "pwd": faker.password()

        }