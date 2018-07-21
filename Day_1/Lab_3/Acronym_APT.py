def acronym(phrase):
    phraseList = phrase.split()
    acronym = ""
    for word in phraseList:
        acronym = acronym + word[0].upper() + " " +  "." + " "
    return acronym
phrase = input("input a string: " )

print (acronym(phrase))
