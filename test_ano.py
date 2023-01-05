from anonymisation import main_ano

#path to the thesaurus file, with concepts 
thesaurus_path = "thesaurus.txt"

lst = ["april talked yesterday a lot about ibm", "esto implica un aumento desde del 3,8 % registrado a mediados de febrero , hasta niveles medios del 4,2 % en el 2007 y del 4,3 % en el 2008 ."]

# output = open("test_output_list.txt","w")
for e in lst:
    print(main_ano(e,thesaurus_path))
    # output.write(main_ano(e,thesaurus_path)+"\n")


