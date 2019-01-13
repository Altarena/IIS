def if_else(answer):
    if answer in ("y", "yes", "да", "ДА", "Да", "Yes", "YES"):
        answer = True
    else:
        answer = False
    return answer
    
def come_exam():
    answer = input("Пришел на экзамен(yes/no)? ")
    answer = if_else(answer)
    return answer
   
def color_textbook():
    answer = input("Знаешь, какого цвета учебник (yes/no)? ")
    answer = if_else(answer)
    return answer

def name():
    answer = input("Знаешь, как зовут препода (yes/no)? ")
    answer = if_else(answer)
    return answer
 
def ticket():
    answer = input("Попался счастливый билет (yes/no)? ")
    answer = if_else(answer)
    return answer

def prompt():
    answer = input("Есть шпаргалки (yes/no)? ")
    answer = if_else(answer)
    return answer

def telephone():
    answer = input("Есть телефон с интернетом (yes/no)? ")
    answer = if_else(answer)
    return answer

def prompt_help():
    answer = input("Поймали со шпаргалкой(yes/no)? ")
    answer = if_else(answer)
    return answer

def attending_lessons():
    answer = input("Посещал занятия (yes/no)? ")
    answer = if_else(answer)
    return answer

def lateness():
    answer = input("Опоздал на экзамен (yes/no)? ")
    answer = if_else(answer)
    return answer
    
def mood():
    answer = input("Настроение у препода (good/neutral/bad)? ")
    return answer

def ready():
    answer = input("Готовность к экзамену (good/medium/bad)? ")
    return answer


##answers = {
##            "come_exam": come_exam(),
##            "color_textbook": color_textbook(),
##            "name": name(),
##            "ticket": ticket(),
##            "prompt": prompt(),
##            "telephone": telephone(),
##            "prompt_help": prompt_help(),
##            "attending_lessons": attending_lessons(),
##            "lateness": lateness(),
##            "mood": mood(),
##            "ready": ready()
##          }

come_exam = come_exam()
color_textbook = color_textbook()
name =name()
ticket =ticket()
prompt = prompt()
telephone = telephone()
prompt_help = prompt_help()
attending_lessons = attending_lessons()
lateness = lateness()
mood = mood()
ready = ready()

