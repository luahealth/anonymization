from anonymisation import main_ano

#path to the thesaurus file, with concepts 
thesaurus_path = "thesaurus.txt"

#string = "april talked yesterday a lot about ibm"
string = "esto implica un aumento desde del 3,8 % registrado a mediados de febrero , hasta niveles medios del 4,2 % en el 2007 y del 4,3 % en el 2008 ."

print(main_ano(string,thesaurus_path))
