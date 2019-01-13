
;;;======================================================
;;;   Automotive Expert System
;;;
;;;     This expert system diagnoses some simple
;;;     problems with a car.
;;;
;;;     CLIPS Version 6.3 Example
;;;
;;;     To execute, merely load, reset and run.
;;;======================================================

;;****************
;;* DEFFUNCTIONS *
;;****************

(deffunction ask-question (?question $?allowed-values)
   (printout t ?question)
   (bind ?answer (read))
   (if (lexemep ?answer) 
       then (bind ?answer (lowcase ?answer)))
   (while (not (member ?answer ?allowed-values)) do
      (printout t ?question)
      (bind ?answer (read))
      (if (lexemep ?answer) 
          then (bind ?answer (lowcase ?answer))))
   ?answer)

(deffunction yes-or-no-p (?question)
   (bind ?response (ask-question ?question yes no y n))
   (if (or (eq ?response yes) (eq ?response y))
       then yes 
       else no))

;;;***************
;;;* QUERY RULES *
;;;***************

(defrule determine-come-exam ""
   (not (come-exam ?))
   (not (repair ?))
   =>
   (assert (come-exam (yes-or-no-p "Пришел на экзамен(yes/no)? "))))
   
(defrule determine-color-textbook ""
   (come-exam yes)
   (not (repair ?))
   =>
   (assert (color-textbook (yes-or-no-p "Знаешь, какого цвета учебник (yes/no)? "))))

(defrule determine-name ""
   (come-exam yes)
   (color-textbook yes)
   (not (repair ?))   
   =>
   (assert (name (yes-or-no-p "Знаешь, как зовут препода (yes/no)? "))))
   
(defrule determine-ticket ""
   (come-exam yes)
   (not (repair ?))
   =>
   (assert (ticket(yes-or-no-p "Попался счастливый билет (yes/no)? "))))

(defrule determine-mood ""
   (or(come-exam yes)
   (come-exam no))
   (not (repair ?))
   =>
   (assert (mood
      (ask-question "Настроение у препода (good/neutral/bad)? "
                    good neutral bad))))

(defrule determine-ready ""
   (come-exam yes)
   (not (repair ?))
   =>
   (assert (ready
      (ask-question "Готовность к экзамену (good/medium/bad)? "
                    good medium bad))))

(defrule determine-prompt ""
   (come-exam yes)
   (not (repair ?))
   =>
   (assert (prompt
               (yes-or-no-p "Есть шпаргалки (yes/no)? "))))

(defrule determine-telephone ""
   (come-exam yes)
   (prompt no)
   (not (repair ?))
   =>
   (assert (telephone
              (yes-or-no-p "Есть телефон с интернетом (yes/no)? "))))

(defrule determine-prompt-help ""
   (come-exam yes)
   (prompt no)
   (telephone no)
   (not (repair ?))
   =>
   (assert (prompt-help (yes-or-no-p "Поймали со шпаргалкой(yes/no)? "))))

(defrule determine-attending-lessons ""
   (come-exam yes)      
   (not (repair ?))
   =>
   (assert (attending-lessons
              (yes-or-no-p "Посещал занятия (yes/no)? "))))

(defrule determine-lateness ""
   (come-exam yes)      
   (not (repair ?))
   =>
   (assert (lateness
              (yes-or-no-p "Опоздал на экзамен (yes/no)? "))))

;;;****************
;;;* REPAIR RULES *
;;;****************

(defrule two ""
   (or(and(ticket yes)
          (or(name no)
               (color-textbook no))
          (mood bad))
   (and(come-exam no)
       (mood bad))
   (and(mood bad)
       (prompt-help yes))
   (and(ready bad)
       (telephone no)
       (prompt no))
   )
   (not (repair ?))
   =>
   (assert (repair "2")))

(defrule five ""
   (or(and(ticket yes)
          (name yes)
          (color-textbook yes))
      (and(telephone yes)
          (prompt yes)
          (prompt-help no)
          (ready good))
      (and(ready good)
          (mood good))
      (and(ready good)
          (mood neutral)
          (attending-lessons yes)
          (lateness no))      
   )
   (not (repair ?))
   =>
   (assert (repair "5"))) 

(defrule fo ""
   (or(and(ready good)
          (mood neutral)
          (attending-lessons no)
          (lateness yes))
      (and(telephone no)
          (prompt no)
          (ready good))
      (and(telephone yes)
          (prompt yes)
          (prompt-help no)
          (ready medium))
      (and(ticket no)
          (mood good)
          (name no)
          (color-textbook no))
      (and(ready medium)
          (mood good))
      (and(ready medium)
          (mood neutral)
          (attending-lessons yes)
          (lateness no))
   )
   (not (repair ?))
   =>
   (assert (repair "4")))     

(defrule three ""
   (or(and(come-exam no)
          (mood good))
      (and(ready medium)
          (attending-lessons yes)
          (lateness no))
      (and(ready medium)
          (telephone no)
          (prompt no))
      (and(mood good)
          (prompt-help yes))
      (and(ready bad)
          (prompt-help no))
   )
   (not (repair ?))
   =>
   (assert (repair "3")))


;;;********************************
;;;* STARTUP AND CONCLUSION RULES *
;;;********************************

(defrule system-banner ""
  (declare (salience 10))
  =>
  (printout t crlf crlf)
  (printout t "Expert System")
  (printout t crlf crlf))

(defrule print-repair ""
  (declare (salience 10))
  (repair ?item)
  =>
  (printout t crlf crlf)
  (printout t "Repair:")
  (printout t crlf crlf)
  (format t "%s%n%n" ?item))

