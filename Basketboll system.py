class Transfer():
    def __init__(self, klub1, klub2, game, narx, yil):
        self.klub1 = klub1
        self.klub2 = klub2
        self.game = game
        self.narxi = narx
        self.__yili = yil

    def get_klub1(self):
        return self.klub1

    def get_klub2(self):
        return self.klub2

    def get_narxi(self):
        return self.narxi

    def get_yili(self):
        return self.__yili

    @property
    def game(self):
        return self.__gamer

    @game.setter
    def game(self, fut):
        self.__gamer = self.get_klub2().yes(fut.split())

    def transfer(self, count):
        if self.get_yili() <= count:
            if self.get_yili() > self.game.get_transfer_muddati():
                    self.get_klub1().transfer_app(self.game)
                    self.game.set_transfer_muddati(self.get_yili())
                    self.get_klub2().transfer_rem(self.game)
            elif self.get_klub2().get_budjet() - (count - self.get_yili()) * self.get_klub2().get_xarajat() > 0:
                if self.get_klub1().get_budjet() - (count - self.get_yili()) * self.get_klub1().get_xarajat() >= self.get_narxi():
                    self.get_klub1().transfer_app(self.game)
                    self.game.set_transfer_muddati(self.get_yili())
                    self.get_klub2().transfer_rem(self.game)
                    self.get_klub1().set_budjet(-self.get_narxi())
                    self.get_klub2().set_budjet(self.get_narxi())
            else:
                self.get_klub1().transfer_app(self.game)
                self.game.set_transfer_muddati(self.get_yili())
                self.get_klub2().transfer_rem(self.game)
                self.get_klub1().set_budjet(-self.get_narxi())
                self.get_klub2().set_budjet(self.get_narxi())


class Klub:
    Klubs = []

    def __init__(self, name, gamer, budjet, yillik_xarajat):
        self.name = name
        self.__gamer= gamer
        self.budjet = budjet
        self.yillik_xarajat = yillik_xarajat
        self.Klubs.append(self)

    def get_name(self):
        return self.name

    def get_gamer(self):
        return self.__gamer

    def get_budjet(self):
        return self.budjet

    def get_xarajat(self):
        return self.yillik_xarajat

    def set_budjet(self, count):
        self.budjet += count

    def transfer_app(self, count):
        self.__gamer.append(count)

    def transfer_rem(self, count):
        a_count = self.get_gamer()
        for i in range(len(a_count)):
            if a_count[i].get_ism() == count.get_ism():
                self.__gamer.pop(i)
                break

    def Gamers(self):
        for i in range(len(self.get_gamer())):
            print(str(i + 1) + " " + self.get_gamer()[i].get_ism())

    def yes(self, count):
        for i in range(len(self.get_gamer())):
            if self.get_gamer()[i].get_ism() == count[1]:
                return self.get_gamer()[i]
        return False

    def info(self):
        return f"\nName :{self.get_name()}\nBudget :${self.get_budjet()} mln\nAnnual cost :${self.get_xarajat()} mln\n"


class Gamerss:
    Klubs = []

    def __init__(self, ism, yosh, transfer_narxi, transfer_muddat):
        self.__ism = ism
        self.__yosh = yosh
        self.__transfer_narxi = transfer_narxi
        self.__transfer_muddat = transfer_muddat
        self.Klubs.append(self)


    def get_ism(self):
        return self.__ism

    def get_yosh(self):
        return self.__yosh


    def get_transfer_narxi(self):
        return self.__transfer_narxi

    def get_transfer_muddati(self):
        return self.__transfer_muddat

    def set_transfer_muddati(self, count):
        self.__transfer_muddat = count

    def info(self):
        return "\nGamer:\n" + f"Name :{self.get_ism()}\
\nAge :{self.get_yosh()}\ntransfer cost :\
${self.get_transfer_narxi()} mln\nDeatline :{self.get_transfer_muddati()}\n"

# Chicago Bulls
t1=Gamerss("Maykl Jordon",36,80.2,2022)
t2=Gamerss("Kyle Anderson",42,88.4,2023)
t3=Gamerss("Coby White",44,58.3,2026)
t4=Gamerss("Jarrett Allen",39,55.76,2024)
t5=Gamerss("Will Borton",21,75,2022)
CHB =Klub("Chicago Bulls",[t1,t2,t3,t4,t5],89000,52000)

#New York Knicks
t1=Gamerss("Scottie Barnes",22,100.89,2025)
t2=Gamerss("Even Mobley",20,65,2026)
t3=Gamerss("Davion Mitchell",21,69.7,2022)
t4=Gamerss("Keon Johnson",26,74.3,2024)
t5=Gamerss("Nemanja Bjelica",25,94.6,2029)
NYK =Klub("New York Knicks",[t1,t2,t3,t4,t5],100000,45000)

#Orlando Magic
t1=Gamerss("Trevor Ariza",25,78.6,2025)
t2=Gamerss("Lonzo Ball",20,90,2024)
t3=Gamerss("Jordon Bell",19,65.4,2022)
t4=Gamerss("Tyler Bey",19,79.2,2023)
t5=Gamerss("Bismack Biyombo",22,88.1,2026)
OM =Klub("Orlando Magic",[t1,t2,t3,t4,t5],950000,55000)

#Milwaukee Bucks
t1=Gamerss("Jrue Holiday",21,74,2027)
t2=Gamerss("Donte DiVincenzo",23,90.9,2025)
t3=Gamerss("Pat Connaughton",19,82.4,2027)
t4=Gamerss("Jordan Nwora",21,79.2,2023)
t5=Gamerss("Brook Lopez",21,79.2,2023)
MB =Klub("Milwaukee Bucks",[t1,t2,t3,t4,t5],860000,49000)

#Phoenix Suns
t1=Gamerss("Ty-Shon Alexander",21,77,2025)
t2=Gamerss(" Devin Booker",22,90,2022)
t3=Gamerss("Mikal Bridges",19,829,2024)
t4=Gamerss(" Cameron Johnson",20,70,2023)
t5=Gamerss("Jalen Smith",22,100,2027)
PS =Klub("Phoenix Suns",[t1,t2,t3,t4,t5],1100000,58000)


count =int(input("New Transfer :"))

t1= Transfer(PS, OM, "Devin Booker", 70, 2023)
t1.transfer(count)
t2= Transfer(MB, NYK, "Jordan Nwora", 50, 2024)
t2.transfer(count)
t3= Transfer(MB, NYK, "Pat Connaughton", 60, 2027)
t3.transfer(count)
t4= Transfer(CHB, MB, "Coby White", 65, 2029)
t4.transfer(count)
t5= Transfer(MB, CHB, "Brook Lopez", 55, 2025)
t5.transfer(count)
t6= Transfer(PS, CHB, "Mikal Bridges", 40, 2026)
t6.transfer(count)
t7= Transfer(OM, NYK, "Trevor Ariza", 50, 2023)
t7.transfer(count)
t8= Transfer(PS, OM, "Jalen Smith", 90, 2024)
t8.transfer(count)
t9= Transfer(NYK, CHB, "Davion Mitchell", 59, 2025)
t9.transfer(count)
t10= Transfer(MB, PS, "Jrue Holiday", 60, 2029)
t10.transfer(count)
t11= Transfer(NYK, MB, "Keon Johnson", 65, 2024)
t11.transfer(count)
t12= Transfer(NYK, CHB, "Keon Johnson", 90, 2026)
t12.transfer(count)
t13= Transfer(OM, PS, "Tyler Bey", 30, 2028)
t13.transfer(count)
t14= Transfer(MB, CHB, "Pat Connaughton", 20, 2028)
t14.transfer(count)
t15= Transfer(OM, NYK, "Bismack Biyombo", 100, 2024)
t15.transfer(count)

arrays=Klub.Klubs
while 1:
    for i in range(len(arrays)):
        print(i+1,arrays[i].get_name())
    print(len(arrays)+1,"exit")
    count_b=int(input("Klubs:"))
    if count_b>0 and count_b<len(arrays)+1:
        klub=arrays[count_b-1]
    elif count_b==len(arrays)+1:
        break
    else:
        continue
    print(klub.info())
    klub.Gamers()
    count_c=int(input("Gamers :"))
    if count_c>0 and count_c<len(klub.get_gamer())+1:
        fut=klub.get_gamer()[count_c-1]
    else:
        continue
    print(fut.info())