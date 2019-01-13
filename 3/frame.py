import json

def openP():
    f=open("frame.txt")
    txt = json.loads(f.read())
    return txt

def conditions():
    frame = openP()
    ekz = frame[0]
    cond = frame[1]
    visit = frame[2]
    res = {}
    for i in range(len(cond)):
        res.update({cond[i]["name"]: 0})
    frstud = list(stud.values())
    for i in range(len(cond)):
        frfr= list(cond[i]["conditions"].values())
        for k in range(len(frstud)):
            if frstud[k] in frfr:
                res[cond[i]["name"]]+=1
    print (res)
    ekz.update(stud)

    if (res["Отличные"] == res["Хорошие"])or (res["Отличные"] == res["Удовлетворительные"]):
        res["Отличные"] += 1
    elif (res["Хорошие"]== res["Удовлетворительные"])or(res["Хорошие"]== res["Плохие"]):
        res["Хорошие"] +=1
    elif res["Удовлетворительные"] == res["Плохие"]:
        res["Удовлетворительные"] += 1

    inverse = [(value, key) for key, value in res.items()]
    ekz["conditions"] = max(inverse)[1]

    return ekz, visit

def visit():
    ekz, visit = conditions()
    visstud = stud["visit"]
    for i in range(len(visit)):
        min = visit[i]["visit"][0]
        max = visit[i]["visit"][1]
        if visstud >= min and visstud <= max:
            ekz["visiting"] = visit[i]["name"]
    return ekz

def ball():
    ekz = visit()
    condition = ekz['conditions']
    visiting = ekz['visiting']
    if (condition == "Отличные" and visiting == "Отличная"):
        ekz["Балл"] = "Отлично"
    elif (condition == "Отличные" and visiting == "Хорошая") or (condition == "Хорошие" and visiting == "Отличная"):
        ekz["Балл"] = "Хорошо"
    elif (condition == "Отличные" and visiting == "Плохая")or(condition == "Хорошие" and visiting == "Хорошая")or(condition == "Удовлетворительные" and visiting == "Отличная"):
        ekz["Балл"] = "Удовлетворительно"
    else:
        ekz["Балл"] = "Неуд"
    if ekz["Балл"] == "Неуд":
        print("Студент "+ekz["Фио"]+" получает оценку "+ekz["Балл"]+" и отправляется на пересдачу")
    else:
        print("Студент " + ekz["Фио"] + " получает оценку " + ekz["Балл"])

stud = {"Фио": "Иванов И.И",
        'prep': 'Добрый',
        'kab': 'Плохая',
        'tich': 'Да',
        "visit" : 80}


ball()