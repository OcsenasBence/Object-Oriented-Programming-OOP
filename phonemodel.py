from functools import total_ordering
import sys

@total_ordering
class Mobil:
    gyarto: str
    __tipus: str
    __ev: int

    def __init__(self,gyarto:str,tipus:str,ev:int=2022) -> None:
        self.gyarto = gyarto
        self.__tipus = tipus
        self.__ev = ev

    @property
    def tipus(self) -> str:
        return self.__tipus

    @property
    def ev(self) -> int:
        return self.__ev

    @tipus.setter
    def tipus(self,new:str) -> None:
        self.__tipus = new

    @ev.setter
    def ev(self,new:int) -> None:
        self.__ev = new

    def __repr__(self) -> str:
        return f"{self.gyarto}, {self.__tipus}, {self.__ev}"

    def __str__(self) -> str:
        return f"{self.gyarto} // {self.__tipus} ({self.__ev})"

    def __eq__(self, other):
        return isinstance(other,Mobil) and (self.gyarto, self.__tipus, self.__ev) == (other.gyarto, other.__tipus, other.__ev)

    def __lt__(self, other):
        if isinstance(ohter, Mobil):
            return (self.gyarto, -self.__ev, self.__tipus) < (other.gyarto, -other.__ev, other.__tipus)
        else:
            return NotImplemented

    @staticmethod
    def static(telefonok:list, ev:int) -> list:
        telefon=[]
        for x in telefonok:
            if isinstance(x,Mobil):
                if x.nev == nev:
                    telefon.append(x.nev)
        return telefon

@total_ordering
class   Okosmobil(Mobil):
    __kamera: str

    def __init__(self, gyarto: str, tipus: str,kamera:str, ev: int = 2022) -> None:
        super().__init__(gyarto, tipus, ev)
        self.__kamera = kamera

    @property
    def kamera(self) -> str:
        return self.__kamera

    def __repr__(self) -> str:
        return super().__repr__() + f", {self.__kamera}"

    def __str__(self) -> str:
        return super().__str__() +f": {self.__kamera}"

def main():
    telefonokszama=0
    try:
        telefonokszama=sys.argv[1]   #elso argumentum
        telefonokszama=int(telefonokszama) #számmá konvertáltuk
        print(telefonokszama)
    except IndexError: #ha nincs megadva argumentum
        print("Nincs elég argumentum")
    except ValueError: #nem egesz szam az arg
        print(f"a {sys.argv[1]} nem egész szám")
    telefonlista=[]
    classeslista=[]
    for x in range(telefonokszama):
        listaelem=input()
        telefonlista.append(listaelem)
    for phone in telefonlista:
        elvalasztott=phone.split(";")


        try:
            if len(elvalasztott) == 3:
                classeslista.append(model.Mobil(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2])))
            elif len(elvalasztott) == 4:
                classeslista.append(
                    model.Okosmobil(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2]), int(elvalasztott[3])))
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











