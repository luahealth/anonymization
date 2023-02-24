from anonymisation import main_ano
from faker import Faker
fake = Faker()

thesaurus_path = "thesaurus.txt"


while True:
    text = fake.text()
    print('Input:',text)
    print('Output:',main_ano(text,thesaurus_path))
    print('   ')



