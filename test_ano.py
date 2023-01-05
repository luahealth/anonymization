from anonymisation import main_ano

#path to the thesaurus file, with concepts 
thesaurus_path = "thesaurus.txt"

#string = "april talked yesterday a lot about ibm"
#string = "esto implica un aumento desde del 3,8 % registrado a mediados de febrero , hasta niveles medios del 4,2 % en el 2007 y del 4,3 % en el 2008 ."

lst = ["Hi there Happy Monday! How are you? Did you have a good weekend?", "ack", "Happy Holidays! Have a wonderful time! See you next year!", "Im going to log off now", "Just checking if HR got back", "Do you think they will be able to help backdate the changes?", "Pinging you elvis thank you!!", "Guys volunteer needed to check my code results", "Okay no worries. Just let me know when you validate them", "hi Pri! Is it possible to add GEO filter in the report", "gawd is it happening again?", "Thanks for your help", "Please feel free to review the updates and provide feedback if any. So far we are on track", "Thank you team for today. It was fun working and doing it together.", "Agree it was fun and very informative for me, as I haven't finished the book yet. Thank you team! ", " ", ":naruto: ", ":pakyaw::pakyaw: ", ":hahaha-gago::frog-lightsaber::pam::alyssa::thankyou: ", ":test: ", "Hey how you doin? 👋", "Ack", "Yes need something? ", "Hi all this is a test message for the purposes of Marlyn's study.", "🌲🌲🎊", "ack", "Hi there this is my second testing message", " ", "🌲🎊👍🙂🥹🥳😭", " ", "🤣🥳🥹😀❤️🌲🌟😭", "thanks ", "Hiii", "This is a test", "Ack", "This works ", "Hello. Hope you're well.", "It was nice talking to you today.", "😀", "Likewise", "Good morning.", "Excited for Christmas and the holidays!", "Hiya.", "I hope the weather is good there.", "Have you been feeling down in winter?", "Hey did anything interesting happen in your day?", "Hello there.", "Wishing you happy holidays "]


output = open("test_output_list.txt","w")
for e in lst:
    print(main_ano(e,thesaurus_path))
    output.write(main_ano(e,thesaurus_path)+"\n")


