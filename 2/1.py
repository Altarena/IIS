import json

def answ():
    inp = None
    while (inp != "Да")or(inp != "Нет"):
        if inp in ('да', "Да", "LF", "ДА", 'lf', 'Lf'):
            res = "Да"
            return (res)
        elif inp in ("нет", "Нет", "НЕТ", "ytn", "YTN","Ytn"):
            res = "Нет"
            return (res)
        inp = input("Да/Нет:   ")

def openP():
    f=open("1.txt")
    txt = json.loads(f.read())
    return txt

def cik():
    for j in range(len(memory)):
        k = []
        for i in range(5):
            if memory[j] in list(txt[i]["condition"].items()):
                k.append(i)
    if (len(k)) == 1:
        explanation.append((txt[k[0]])["Name"])
        print (list(txt[k[0]]["condition"]["execute"].values())[0])
        print("Имена сработавших фактов:  ")
        print(explanation)
    else:
        explanation.append((txt[k[0]]["Name"]))
        us(list(txt[k[1]]["condition"].keys())[1])
    return k

def us(c):
    for i in range(len(txt)):
        t = txt[i]["condition"]
        if c in list(txt[i]["condition"].keys()):
            if t["%s" % c] == "":
                print(list(t["execute"].values())[0])
                b = ("%s" % c, answ())
                memory.append(b)
    cik()
    return memory


memory = []
explanation = []
txt = openP()
t = txt[0]["condition"]
c = "come_exam"
us(c)