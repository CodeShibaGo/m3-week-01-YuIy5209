txt = "aeiou."


def processString5(txt):
    transTable = txt.maketrans("aeiou", "AEIOU")
    txt = txt.translate(transTable)
    print(txt)


processString5(txt)