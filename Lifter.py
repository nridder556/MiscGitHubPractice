
import math
class Lifter:

    def __init__(self, firstname, lastname, weight_lb, height_in, bench_lb, squat_lb, deadlift_lb):
        self.firstname = firstname
        self.lastname = lastname
        self.weight = weight_lb
        self.height = height_in
        self.bench = bench_lb
        self.squat = squat_lb
        self.deadlift = deadlift_lb



    def getTotal(self):
        total = self.bench + self.squat+self.deadlift
        return total


    def getBMI(self):
        bmi = self.weight/math.pow(self.height, 2)*703
        return bmi


    def getWilks(self):
        a =-216.0475144
        b = 16.2606339
        c = -0.002388645
        d = -0.00113732
        e = 7.01863E-06
        f = -1.291E-08

        return (self.getTotal()*500)/(a + b * self.weight + c*math.pow(self.weight, 2)
                                      + d * math.pow(self.weight, 3)+e*math.pow(self.weight, 4) +
                                      f * math.pow(self.weight, 5))

class OlympicLifter(Lifter):
    def __init__(self,fn,ln,wt,ht,sntch,cnj):
        super().__init__(self,fn,ln,wt,ht,None,None)
        self.snatch = sntch
        self.cj = cnj






