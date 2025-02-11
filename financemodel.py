from functools import total_ordering
import sys

@total_ordering
class Valuta:
    nev: str
    jeloles: str
    __arfolyam: float

    def __init__(self,nev:str,jeloles:str,arfolyam:float) -> None:
        self.nev = nev
        self.jeloles = jeloles
        self.__arfolyam = arfolyam

    @property
    def arfolyam(self) -> float:
        return self.__arfolyam

    @arfolyam.setter
    def arfolyam(self,new:float) -> None:
        self.__arfolyam = new

    def __repr__(self) -> str:
        return f"{self.nev}, {self.jeloles}, {self.__arfolyam}"

    def __str__(self) -> str:
        return f"{self.jeloles} ({self.nev}): ${self.__arfolyam}"

    def __eq__(self, other):
        return isinstance(other,Valuta) and (self.nev, self.jeloles, self.__arfolyam) == (other.nev, other.jeloles, other.__arfolyam)

    def __lt__(self, other):
        if isinstance(other,Valuta):
            return (-self.__arfolyam, self.nev, self.jeloles) < (-other.__arfolyam, other.nev, other.jeloles)
        else:
            return NotImplemented

    @staticmethod
    def static(valutak: list,arfolyam: float) -> list:
        valuta=[]
        for x in valutak:
            if isinstance(x, Valuta):
                if x.__arfolyam > arfolyam:
                    valuta.append(x.__arfolyam)
        return valuta

@total_ordering
class Kripto(Valuta):
    __tervezoneve: str

    def __init__(self, nev: str, jeloles: str, arfolyam: float, tervezoneve:str) -> None:
        super().__init__(nev, jeloles, arfolyam)
        self.__tervezoneve = tervezoneve

    @property
    def tervezoneve(self) -> str:
        return self.__tervezoneve

    @tervezoneve.setter
    def tervezoneve(self,value: str) -> None:
        self.__tervezoneve = value

    def __repr__(self) -> str:
        return super().__repr__() + f", {self.__tervezoneve}"

    def __str__(self) -> str:
        return super().__str__() + f", @{self.__tervezoneve}"

def main():
    valutakszama=0
    try:
        valutakszama=sys.argv[1]   #elso argumentum
        valutakszama=int(valutakszama) #számmá konvertáltuk
        print(valutakszama)
    except IndexError: #ha nincs megadva argumentum
        print("Nincs elég argumentum")
    except ValueError: #nem egesz szam az arg
        print(f"a {sys.argv[1]} nem egész szám")
    valutalista=[]
    classeslista=[]
    for x in range(valutakszama):
        listaelem=input()
        filmlista.append(listaelem)
    for finance in filmlista:
        elvalasztott=finance.split(";")


        try:
            if len(elvalasztott) == 3:
                classeslista.append(model.Valuta(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2])))
            elif len(elvalasztott) == 4:
                classeslista.append(
                    model.Kripto(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2]), int(elvalasztott[3])))
            else:
                raise NotImplementedError
        except ValueError:
            print("Tipuskonvertálásnál hiba merult fel")
        except NotImplementedError:
            print("A megadott sztring nem egyeztetheto se filmnek se sorozatnak")

    classeslista.sort()
    for x in classeslista:
        print(x)
if __name__=="__main__":
    main()










