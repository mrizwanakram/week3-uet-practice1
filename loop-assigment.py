#tray to diffrentiate between covid19,fever and malariya by using loops

coughtsimptoms = ["Difficulty breathing","Shallow", "rapid breathing","Wheezing"]
feversimtoms   = ["Chest pain","Fever","headache","extreme tiredness","dry cough"]
covid19 = ["sore throat","headache","pains","diarrhoea","a rash on skin""discolouration of fingers","red eyes"]

# print our lists of disses
print(coughtsimptoms)
print(feversimtoms)
print(covid19)

#getting simpom from user
sym1 = input( "input your simptom you have : ")

if sym1 in coughtsimptoms:
    print("cought")
elif sym1 in feversimtoms:
    print("fever")
elif sym1 in covid19:
    print("covid")
else:
    print("Congratulations!,You are healthy")








