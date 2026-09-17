def correspond(adresse, reference):
    nouveau = ""
    isHash = False
    for i in range(len(adresse)):
        if adresse[i] == "@":
            isHash = True
        if adresse[i] != "." and not isHash:
            nouveau += adresse[i]
    return reference == nouveau



assert correspond("courspremiere@e-nsi.fr", "courspremiere@e-nsi.fr") == True