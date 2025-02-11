from functools import total_ordering
import sys

@total_ordering
class Allat:
    faj: str
    __suly: float
    __kor: float

    def __init__(self,faj: str, suly: float, kor: float = 0.0) -> None:
        self.faj = faj
        self.__suly = suly
        self.__kor = kor

    @property
    def suly(self) -> float:
        return self.__suly

    @property
    def kor(self) -> float:
        return self.__kor

    @suly.setter
    def suly(self,new:float) -> None:
        self.__suly = new

    @kor.setter
    def kor(self,new: float) -> None:
        self.__kor = new

    def __repr__(self) -> str:
        return f"{self.faj}, {self.__suly}, {self.__kor}"

    def __str__(self) -> str:
        return f"{self.faj}: {self.__kor} év"

    def __eq__(self, o:object):
        return isinstance(o,Allat) and (self.faj, self.__kor) == (o.faj, o.__kor)

    def __lt__(self, other):
        if isinstance(other, Allat):
            return (self.faj, -self.__kor) < (other.faj, -other.__kor)
        else:
            return NotImplemented

    @staticmethod
    def static(allatok: list, faj: str) -> list:
        allatlista=[]
        for x in allatok:
            if isinstance(x,Allat):
                if x.faj == faj:
                    allatlista.append(x.faj)
        return allatlista

@total_ordering
class Emlos(Allat):
    _labakszama: int

    def __init__(self, faj: str, suly: float,labakszama:int, kor: float = 0.0) -> None:
        super().__init__(faj, suly, kor)
        self._labakszama = labakszama

    @property
    def labakszama(self) -> int:
        return self._labakszama

    @labakszama.setter
    def labakszama(self,value:int)->None:
        if value < 0:
            return None
        else:
            self._labakszama = value

    def __repr__(self) -> str:
        return super().__repr__() + f", {self._labakszama}"

    def __str__(self) -> str:
        return super().__str__() + f"(lábak száma: {self._labakszama})"

def main():
    allatokszama=0
    try:
        allatokszama=sys.argv[1]
        allatokszama=int(allatokszama)
        prin(allatokszama)
    except IndexError:
        print("Nincs eleg argumentum")
    except ValueError:
        print(f"a {sys.argv[1]} nem egesz szam")
    allatlista=[]
    classeslista=[]
    for x in range(allatokszama):
        listaelem=inout()
        allatlista.append(listaelem)
    for animal in allatlista:
        elvalasztott=kitudja.split(";")

        try:
            if len(elvalasztott) == 3:
                classeslista.append(model.Allat(elvalasztott[0], float(elvalasztott[1]), float(elvalasztott[2])))
            elif len(elvalasztott) == 4:
                classeslista.append(model.Emlos(elvalasztott[0], float(elvalasztott[1]), float(elvalasztott[2]), int(elvalasztott[3])))
            else:
                raise NotImplementedError
        except ValueError:
            print("Tipuskonvertalasnal hiba merult fel")
        except NotImplementedError:
            print("A megadott sztring nem egyeztetheto")

    classeslista.sort()
    for x in classeslista:
        print(x)
if __name__ == "__main__":
    main()















