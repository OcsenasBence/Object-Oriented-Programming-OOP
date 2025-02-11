from functools import total_ordering
import sys

@total_ordering
class Sport:
    nev: str
    __nemzetiseg: str
    __kor: int

    def __init__(self,nev:str,kor:int,nemzetiseg:str = "Hungary") -> None:
        self.nev = nev
        self.__nemzetiseg = nemzetiseg
        self.__kor = kor

    @property
    def nemzetiseg(self) -> str:
        return self.__nemzetiseg

    @property
    def kor(self) -> int:
        return self.__kor

    @nemzetiseg.setter
    def nemzetiseg(self,new:str) -> None:
        self.__nemzetiseg = new

    @kor.setter
    def kor(self,new:int) -> None:
        self.__kor = new

    def __repr__(self) -> str:
        return f"{self.nev}, {self.__nemzetiseg}, {self.__kor}"

    def __str__(self) -> str:
        return f"{self.nev} ({self.__nemzetiseg}, {self.__kor})"

    def __eq__(self, o:object) -> int:
        return isinstance(o,Sport) and (self.nev, self.__nemzetiseg, self.__kor) == (o.nev, o.__nemzetiseg, o.__kor)

    def __lt__(self, other):
        if isinstance(other,Sport):
            return (-self.__kor, self.__nemzetiseg, self.nev) < (-other.__kor, self.__nemzetiseg, self.nev)
        else:
            return NotImplemented

    @staticmethod
    def static(sportolok: list, kor:int)->list:
        sport=[]
        for x in sportolok:
            if isinstance(x,Sport):
                if x.__kor > kor:
                    sport.append(x)
        return sport

@total_ordering
class Focista(Sport):
    _aranylabdakszama: int

    def __init__(self, nev: str, kor: int,aranylabdakszama: int, nemzetiseg: str = "Hungary") -> None:
        super().__init__(nev, kor, nemzetiseg)
        self._aranylabdakszama = aranylabdakszama

    @property
    def aranylabdakszama(self) -> int:
        return self._aranylabdakszama

    @aranylabdakszama.setter
    def aranylabdakszama(self,value:int)->None:
        self._aranylabdakszama = value

    def __repr__(self) -> str:
        return super().__repr__() + f", {self._aranylabdakszama}"

    def __str__(self) -> str:
        return super().__str__() f": {self._aranylabdakszama}"

def main():
    sportolokszama=0
    try:
        sportolokszama=sys.argv[1]   #elso argumentum
        sportolokszama=int(sportolokszama) #számmá konvertáltuk
        print(sportolokszama)
    except IndexError: #ha nincs megadva argumentum
        print("Nincs elég argumentum")
    except ValueError: #nem egesz szam az arg
        print(f"a {sys.argv[1]} nem egész szám")
    sportlista=[]
    classeslista=[]
    for x in range(sportolokszama):
        listaelem=input()
        sportlista.append(listaelem)
    for foci in sportlista:
        elvalasztott=foci.split(";")


        try:
            if len(elvalasztott) == 3:
                classeslista.append(model.Sport(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2])))
            elif len(elvalasztott) == 4:
                classeslista.append(
                    model.Focista(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2]), int(elvalasztott[3])))
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













