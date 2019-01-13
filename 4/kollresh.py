import itertools, random
from random import randint

class win:
    def __init__(self):
        self.cand = ["a1", "a2", "a3"]
        self.gol = {"a1":0,
                    "a2":0,
                    "a3":0}

    def match(self):
        people = 100
        while people != 0:
            ran = random.randint(0,2)
            self.gol[self.cand[ran]] += 1
            people -= 1

        inverse = [(value, key) for key, value in self.gol.items()]
        print ("Относительного большества:  ", max(inverse)[1])
        print(self.gol)




class Condorcet:

    def __init__(self):
        self.candidates = set()
        self.scores = dict() # score for each permutation of two candidates
        self.results = dict() # winner of each pair of candidates
        self.winner = None # Condorcet winner of the election
        self.voters = vot # ranking of each voter

    def process(self):
        self._build_dict()
        self._matches_candidates()
        self._elect_winner()
        self.coplend()
        self.simpson()
        return self.winner

    def _build_dict(self):
        for voting in self.voters:
            for candidate in voting:
                self.candidates.add(candidate)
            for pair in list(itertools.permutations(voting, 2)):
                if pair not in self.scores:
                    self.scores[pair] = 0
                if voting.index(pair[0]) < voting.index(pair[1]):
                    self.scores[pair] += 1



    def _matches_candidates(self):
        for match in list(itertools.combinations(self.candidates, 2)):
            reverse = tuple(reversed(match))
            if self.scores[match] > self.scores[reverse]:
                self.results[match] = match[0]
            else:
                self.results[match] = match[1]

    def _elect_winner(self):
        for candidate in self.candidates:
            candidate_score = 0
            for result in self.results:
                if candidate in result and self.results[result] == candidate:
                    candidate_score += 1
            if candidate_score == len(self.candidates) - 1:
                self.winner = candidate
        print("Явный победитель:  ", self.winner)

    def coplend(self):
        cond = {}
        for i in self.candidates:
            cond.update({i: 0})
        for voting in self.voters:
            for candidate in voting:
                self.candidates.add(candidate)
            for pair in list(itertools.permutations(voting, 2)):
                if pair not in self.scores:
                    cond[pair[0]] = 0
                if voting.index(pair[0]) < voting.index(pair[1]):
                    cond[pair[0]] += 1
        inverse = [(value, key) for key, value in cond.items()]
        print ("Правило Копленда:  ", max(inverse)[1])

    def simpson(self):
        cond = {}
        for i in self.candidates:
            cond.update({i: 0})
        for i in range(len(list(cond))):
            a= []
            for j in range(len(list(self.scores))):
                if list(cond.keys())[i] in list(self.scores.keys())[j][0]:
                    a.append(list(self.scores.values())[j])
            cond[list(cond.keys())[i]] = a
        for i in list(cond.keys()):
            cond[i] = min(cond[i])
        inverse = [(value, key) for key, value in cond.items()]
        print ("Правило Симпсона:  ", max(inverse)[1])

class Bord():
    def __init__(self):
        self.voters = vot
        self.candidates = set()
        self.results = {}
        self.scores = {}

    def process(self):
        self.variant()
        self.matchs()

    def variant(self):

        for voting in self.voters:
            for candidate in voting:
                self.candidates.add(candidate)
            for pare in list(itertools.permutations(self.candidates, 3)):
                    self.scores[pare] = 0

        for voting in self.voters:
            if voting in list(self.scores.keys()):
                self.scores[voting] += 1



    def matchs(self):
        cond = {}
        for i in self.candidates:
            cond.update({i: 0})
        ball = [i for i in range(len(cond.keys()), 0, -1)]
        print(ball)
        keyscor = list(self.scores.keys())
        keycond =list(cond.keys())
        for keyc in keycond:
            for keys in keyscor:
                for i in range(len(ball)):
                    if keyc == keys[i]:
                        cond[keyc] += (ball[i]+1)*self.scores[keys]
        inverse = [(value, key) for key, value in cond.items()]
        print ("Метод Борда:  ", max(inverse)[1])


vot = [("a1", "a2", "a3"),
       ("a1", "a3", "a2"),
       ("a2", "a1", "a3"),
       ("a1", "a2", "a3")]


Condorcet().process()
Bord().process()
win().match()