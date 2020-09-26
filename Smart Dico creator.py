from larousse_api import larousse
import os
def app(motbrut) :
    mot = motbrut.lower()
    file = open("dicoFR1.txt", 'r')
    c = file.read().split('\n')
    file.close()
    position = 0
    for space in c :
        if space == '' :
            del c[position]
        position = position + 1
    if mot in c :
        lo = 0
        #print('Existe deja')
    else :
        c.append(mot)
    tour = 0
    file = open("dicoFR1.txt",'w')
    for word in c :
        if tour == 0 :
            file.write(word)
        else :
            file.write('\n' + word)
        tour = tour + 1
    file.close()
f = os.listdir()
if "dicoFR1.txt" in f :
  print('Doc ok')
else :
  print('Création du doc')
  file = open("dicoFR1.txt","w")
  file.close()
mot = input('Mot : ')
app(mot)
i = True
p = 0
while i :
    file = open("dicoFR1.txt", 'r')
    c = file.read().split('\n')
    file.close()
    mot = c[p]
    print("Le mot _>" + mot)
    deff = larousse.get_definitions(str(mot))
    if deff == [] :
        print('Pad de définition')
    else :
        ldef = deff[0].split(' ')
        print(ldef)
        for w in ldef :
            #print(w)
            app(w)
    p = p + 1