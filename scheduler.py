import math, openpyxl, random


calendar = [
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"],
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"],
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"],
    ["ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ", "ㅡㅡㅡ"]
]

wb = openpyxl.load_workbook("schedule.xlsx")
sheet1 = wb.get_sheet_by_name("Sheet1")
empytyCellCount = 28

for i in range(0, 4):
    for j in range(0, 7):
        if sheet1.cell(row=i+1, column=j+1).value != None:
            empytyCellCount -= 1
            calendar[i][j] == sheet1.cell(row=i+1, column=j+1).value

sundayNight = sheet1["I3"].value


def addPerson(pathToFile):
    personFile = open(pathToFile, "r")
    personNameList = personFile.read().splitlines()
    return personNameList
    personFile.close()
    

personNameList = addPerson("./people.txt")
print(personNameList)


class Person:
    def __init__(self, name, logicalCalendar, hoursWorked, lostTime, numMorning, numAfternoon, numEvening, numNight):
        self.name = name
        self.logicalCalendar = logicalCalendar
        self.hoursWorked = hoursWorked
        self.lostTime = lostTime
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
    

    def calcTime(self):
        morningTime = 4 * self.numMorning
        afternoonTime = 6 * self.numAfternoon
        eveningTime = 5 * self.numEvening
        nightTime = 9 * self.numNight
        self.hoursWorked = morningTime + afternoonTime + eveningTime + nightTime
        
        for i in range(5, 7):
            if calendar[0][i] == self.name:
                self.lostTime += 4
            if calendar[1][i] == self.name:
                self.lostTime += 6
            if calendar[2][i] == self.name:
                self.lostTime += 5


def fillBlank(personList):
    random.shuffle(personList)
    for i in range(0, 4):
        for j in range(0, 7):
            if calendar[i][j] == "ㅡㅡㅡ":
                for person in personList:
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
                        continue
                    else:
                        continue


personDict = {}

for i, person in enumerate(personNameList):
    personDict["person{0}".format(i)] = Person(
        personNameList[i],
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ],
        0, 0, 0, 0, 0, 0
    )

for i in range(0, math.floor(empytyCellCount / len(personNameList))):
    for person in personDict.values():
        person.logCalInit()
        person.assign()

fillBlank(list(personDict.values()))

# write final results into the Excel sheet
for i in range(0, 4):
    for j in range(0, 7):
        sheet1.cell(row=i+8, column=j+1) == calendar[i][j]


print("final:")
for i in range(0, 4):
    print(calendar[i])
for person in personDict.values():
    person.calcTime()
    print(person.name + ": hours worked = " + str(person.hoursWorked) + ", lost free time = " + str(person.lostTime))
