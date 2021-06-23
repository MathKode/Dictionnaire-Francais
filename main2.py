print(" ____  _  ____       ____      _____     _____     ____  \n|  _ \(_)/ ___|___  / ___|_ __| ____|__ |_   _|__ |  _ \ \n| | | | | |   / _ \| |   | '__|  _| / _` || |/ _ \| |_) |\n| |_| | | |__| (_) | |___| |  | |__| (_| || | (_) |  _ < \n|____/|_|\____\___/ \____|_|  |_____\__,_||_|\___/|_| \_\ ")
try :
    from larousse_api import larousse
except:
    import os
    os.system("pip install larousse-api-sunbro")
    print("------\nRESTART THE CODE\n------")
    exit(0)
print("ATTENTION : Si vous avez un fichier nommez dico.txt, il sera supprimé")

def create(w,p,ms,ls,f,a):
    maxx = ls
    if p == 0:
        file = open("dico.txt","w")
        file.write(w)
        file.close()
    while True:
        file = open("dico.txt","r")
        ls = file.read().split('\n')
        file.close()
        mot = ls[p]

        print("Mot ->",mot)
        def_ = "".join(larousse.get_definitions(mot)).lower().split(' ')
        if def_ == ['']:
            print('Pas de def')
        else :
            print('Def Find')

        #print(def_)
        def_final = []
        #Supp les nombres, points...
        for word in def_:
            go = True
            for lettre in word:
                if lettre in list(',;:=?./+ù%$!$^¨12345()6789 0°_@#&"*') or lettre == "'" or lettre in f.split(';'):
                    go = False
                    #print("0",word)
            if len(word) > ms:
                #print("1",word)
                go = False
            if len(word) < maxx:
                go = False
                #print("2",word)
            if word in f.split(';'):
                go = False
                #print("3",word)
            if word in a.split(';'):
                go = True
                #print("4",word)
            if word == '': go = False
            if go:
                def_final.append(word)
        
        #print(def_final)
        
        for word in def_final:
            if word not in ls:
                ls.append(word)
        
        file = open("dico.txt","w")
        file.write("\n".join(ls))
        file.close()
        p += 1

print("START : Do help to access to the command\nSTOP : ctrl + c")

w = "bonjour"
p = 0
ms = 20
ls = 0
f = ""
a = ""
while True:
    command = input("-> ").lower()
    if command == "help":
        print("                    Command list\ncreate <w> <n> <ms> <ls> <f> <a>\n   -w (word) -> specify the first word of the list\n   -n (number) -> specify the line of begin\n   -ms (max_size) -> size max of a word\n   -ls (little_size) -> least size of a word\n   -f (forbidden) -> Forbid words\n   -a (autorise) -> autorise word\nEXAMPLE :\ncreate -w hello -ms 3 -ls 10 -f lol;hi -a dick\n\nOTHER :\nstart <- To start | code\nshow | print the settings")
    if command.split()[0] == "create":
        c = command.split('-w ')
        if len(c) > 1:
            w = c[1].split(' ')[0]
        
        c = command.split('-n ')
        if len(c) > 1:
            p = int(c[1].split(' ')[0]) -1
        
        c = command.split('-ms ')
        if len(c) > 1:
            ms = int(c[1].split(' ')[0])

        c = command.split('-ls ')
        if len(c) > 1:
            ls = int(c[1].split(' ')[0])
        
        c = command.split('-f ')
        if len(c) > 1:
            f = c[1].split(' ')[0]

        c = command.split('-a ')
        if len(c) > 1:
            a = c[1].split(' ')[0]
    if command == "start":
        create(w,p,ms,ls,f,a)
    if command == "show":
        print("create -w",w,"-n",p,"-ms",ms,"-ls",ls,"f",f,"a",a)
