import random


calendar = [
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"],
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"],
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"],
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"]
]

sundayNight = input("Who was the night shift for Sunday? ")

class Person:
    def __init__(self, name, logicalCalendar, hoursWorked, numMorning, numAfternoon, numEvening, numNight):
        self.name = name
        self.logicalCalendar = logicalCalendar
        self.hoursWorked = hoursWorked
        self.numMorning = numMorning
        self.numAfternoon = numAfternoon
        self.numEvening = numEvening
        self.numNight = numNight

    def logCalInit(self):
        # check for last week and others' shifts
        if self.name == sundayNight:
            self.logicalCalendar[0][0] = 1
            self.logicalCalendar[1][0] = 1
            self.logicalCalendar[2][0] = 1
            self.logicalCalendar[3][0] = 1
        for i in range(0, 4):
            for j in range(0, 7):
                if calendar[i][j] != "ㅡㅡㅡ":
                    self.logicalCalendar[i][j] = 1
    
    def assign(self):
        timeslot = random.randint(0, 3)
        day = random.randint(0, 6)

        boolPass = True
        while boolPass == True:
            if  (self.logicalCalendar[timeslot][day]==1) or \
                (timeslot==0 and self.numMorning==2) or \
                (timeslot==1 and self.numAfternoon==2) or \
                (timeslot==2 and self.numEvening==2) or \
                (timeslot==3 and self.numNight==2):
                timeslot = random.randint(0, 3)
                day = random.randint(0, 6)
            else:
                boolPass = False
        # morning shift
        if timeslot == 0:
            self.numMorning += 1
            if day > 0:
                self.logicalCalendar[3][day-1] = 1 # last night
            self.logicalCalendar[timeslot][day] = 1 # the shift
            calendar[timeslot][day] = self.name
            self.logicalCalendar[timeslot+1][day] = 1 # afternoon
            self.logicalCalendar[timeslot+2][day] = 1 # evening
        # afternoon shift
        elif timeslot == 1:
            self.numAfternoon += 1
            if day > 0:
                self.logicalCalendar[3][day-1] = 1 # last night
            self.logicalCalendar[timeslot][day] = 1 # the shift
            calendar[timeslot][day] = self.name
            self.logicalCalendar[timeslot-1][day] = 1 # morning
            self.logicalCalendar[timeslot+1][day] = 1 # evening
        # evening shift
        elif timeslot == 2:
            self.numEvening += 1
            if day > 0:
                self.logicalCalendar[3][day-1] = 1 # last night
            self.logicalCalendar[timeslot][day] = 1 # the shift
            calendar[timeslot][day] = self.name
            self.logicalCalendar[timeslot-2][day] = 1 # morning
            self.logicalCalendar[timeslot-1][day] = 1 # afternoon
            self.logicalCalendar[timeslot+1][day] = 1 # night
        # night shift
        else:
            self.numNight += 1
            if day > 0:
                self.logicalCalendar[3][day-1] = 1 # last night
            if day != 6:
                self.logicalCalendar[0][day+1] = 1 # next morning
                self.logicalCalendar[1][day+1] = 1 # next afternoon
                self.logicalCalendar[2][day+1] = 1 # next evening
                self.logicalCalendar[3][day+1] = 1 # next night
            self.logicalCalendar[timeslot][day] = 1 # the shift
            calendar[timeslot][day] = self.name
            self.logicalCalendar[timeslot-1][day] = 1 # evening shift


def fillBlank(personList):
    # print("checking shifts...")
    # if a person's logicalCalendar value == 0 and calendar value == ㅡㅡㅡ
    # then assign that person there
    random.shuffle(personList)
    for i in range(0, 4):
        for j in range(0, 7):
            if calendar[i][j] == "ㅡㅡㅡ":
                for person in personList:
                    print("checking case for " + person.name + " at "+ str(i) + ", " + str(j))
                    if person.logicalCalendar[i][j] == 0:
                        if i == 0 and person.numMorning < 2:
                            calendar[i][j] = person.name
                            person.numMorning += 1
                            break
                        if i == 1 and person.numAfternoon < 2:
                            calendar[i][j] = person.name
                            person.numAfternoon += 1
                            break
                        if i == 2 and person.numEvening < 2:
                            calendar[i][j] = person.name
                            person.numEvening += 1
                            break
                        if i == 3 and person.numNight < 2:
                            calendar[i][j] = person.name
                            person.numNight += 1
                            break
                        print(person.name+" already has too many shifts for that timeslot")
                        continue
                    else:
                        print("logCal of "+person.name+" has no space")
                        continue

                    

logCalMingeunkim = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
logCalYongheekwon = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
logCalJunghoonban = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
logCalJunehyungkim = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
logCalWootaekhong = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
mingeunkim = Person("김민근", logCalMingeunkim, 0, 0, 0, 0, 0)
yongheekwon = Person("권용희", logCalYongheekwon, 0, 0, 0, 0, 0)
junghoonban = Person("반정훈", logCalJunghoonban, 0, 0, 0, 0, 0)
junehyungkim = Person("김준형", logCalJunehyungkim, 0, 0, 0, 0, 0)
wootaekhong = Person("홍우택", logCalWootaekhong, 0, 0, 0, 0, 0)

personList = [mingeunkim, yongheekwon, junghoonban, junehyungkim, wootaekhong]

for i in range(0, 5):
    for person in personList:
        person.logCalInit()
        person.assign()

print("pre-check:")

for i in range(0, 4):
    print(calendar[i])


# run fillBlank until no more ㅡㅡㅡ exists
"""
for i in range(0, 4):
    print(i)
    while "ㅡㅡㅡ" in calendar[i]:
        fillBlank(personList)
        print("blank "+str(i)+" filled")
"""
fillBlank(personList)

print("final:")
for i in range(0, 4):
    print(calendar[i])
