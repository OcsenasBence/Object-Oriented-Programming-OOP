from functools import total_ordering
import sys

class Szallas:
    nev: str
    _varos: str
    __ar: int

    def __init__(self, nev:str, ar:int, varos:str = "Debrecen") -> None:
        self.nev = nev
        self._varos = varos
        self.__ar = ar

    @property
    def varos(self) -> str:
        return self._varos

    @property
    def ar(self) -> int:
        return self.__ar

    @ar.setter
    def ar(self,new:int) ->None:
        self.__ar=new

    def __repr__(self) -> str:
        return f"{self.nev}, {self._varos}, {self.__ar}"

    def __str__(self) -> str:
        return f"{self.nev} ({self._varos}): {self.__ar} Ft"

    def __eq__(self, o:object) -> int:
        return isinstance(o,Szallas) and (self.nev, self._varos, self.__ar) == (o.nev, o._varos, o.__ar)

    def __lt__(self, other):
        if isinstance(other, Szallas):
            return (self.varos, self.__ar, self.nev) < (other.varos, other.__ar, other.nev)
        else:
            return NotImplemented

    @staticmethod
    def static(szallas:list, nev:str) -> list:
        szallasok=[]
        for x in szallas:
            if isinstance(x,Szallas):
                if x.nev == nev:
                    szallasok.append(x.nev)
        return szallasok

@total_ordering
class Hotel(Szallas):
    _csillagokszama: int

    def __init__(self, nev: str, ar: int,csillagokszama: int, varos: str = "Debrecen") -> None:
        super().__init__(nev, ar, varos)
        self._csillagokszama = csillagokszama

    @property
    def csillagokszama(self) -> int:
        return self._csillagokszama

    @csillagokszama.setter
    def csillagokszama(self,value:int) -> None:
        if value < 1 and value>5:
            return NotImplemented
        else:
            self._csillagokszama = value

    def __repr__(self) -> str:
        return super().__repr__() + f", {self._csillagokszama}"

    def __str__(self) -> str:
        return f"{self.nev} ({self.varos}): {self.ar} Ft // {self._csillagokszama}"

def main():
    szallasokszama = 0
    try:
        szallasokszama = sys.argv[1]  # elso argumentum
        szallasokszama = int(szallasokszama)  # számmá konvertáltuk
        print(szallasokszama)
    except IndexError:  # ha nincs megadva argumentum
        print("Nincs elég argumentum")
    except ValueError:  # nem egesz szam az arg
        print(f"a {sys.argv[1]} nem egész szám")
    szallaslista = []
    classeslista = []
    for x in range(szallasokszama):
        listaelem = input()
        szallaslista.append(listaelem)
    for hotel in szallaslista:
        elvalasztott = hotel.split(";")

        try:
            if len(elvalasztott) == 3:
                classeslista.append(model.Szallas(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2])))
            elif len(elvalasztott) == 4:
                classeslista.append(
                    model.Hotel(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2]), int(elvalasztott[3])))
            else:
                raise NotImplementedError
        except ValueError:
            print("Tipuskonvertálásnál hiba merult fel")
        except NotImplementedError:
            print("A megadott sztring nem egyeztetheto se filmnek se sorozatnak")

    classeslista.sort()
    for x in classeslista:
        print(x)


if __name__ == "__main__":
    main()












