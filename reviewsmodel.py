from functools import total_ordering
import sys

@total_ordering
class Oktato:
    nev: str
    _kovetelmeny: int
    __segitokesz: int

    def __init__(self,nev:str,kovetelmeny:int,segitokesz:int=3) -> None:
        self.nev = nev
        self._kovetelmeny = kovetelmeny
        self.__segitokesz = segitokesz

    @property
    def kovetelemeny(self) -> int:
        return self._kovetelmeny

    @property
    def segitokesz(self) -> int:
        return self.__segitokesz

    @kovetelmeny.setter
    def kovetelmeny(self,new:int) -> int:
        self._kovetelmeny = new

    @segitokesz.setter
    def segitokesz(self,new:int) -> int:
        self.__segitokesz = new

    def __repr__(self) -> str:
        return f"{self.nev}, {self._kovetelmeny}, {self.__segitokesz}"

    def __str__(self) -> str:
        return f"{self.nev} ({self._kovetelmeny} / {self.__segitokesz}"

    def __eq__(self, o:object) -> int:
        return isinstance(o,Oktato) and (self.nev, self.kovetelemeny, self.segitokesz) == (o.nev, o.kovetelemeny, o.segitokesz)

    def __lt__(self, other):
        if isinstance(other,Oktato):
            return (self.nev, -self._kovetelmeny, -self.__segitokesz) < (other.nev, -other._kovetelmeny, -other.__segitokesz)
        else:
            return NotImplemented

    @staticmethod
    def static(ertekeles:list, kovetelmeny: int) -> list:
        tanarok=[]
        for x in ertekeles:
            if isinstance(x,Oktato):
                if x.__segitokesz >= 3 and x._kovetelmeny >= 3:
                    tanarok.append(x)
        return tanarok

@total_ordering
class Reszletes(Oktato):
    __szexi: bool

    def __init__(self, nev: str, kovetelmeny: int,szexi: bool, segitokesz: int = 3) -> None:
        super().__init__(nev, kovetelmeny, segitokesz)
        self.__szexi = szexi

    @property
    def szexi(self) -> bool:
        return self.__szexi

    @szexi.setter
    def szexi(self, new:bool) -> None:
        self.__szexi = new

    def __repr__(self) -> str:
        return super().__repr__() + f", {self.__szexi}"

    def __str__(self) -> str:
        return super().__str__() + f": {'szexi' if self.__szexi else 'nem szexi'}"

    tanarokszama = 0
    try:
        tanarokszama = sys.argv[1]  # elso argumentum
        tanarokszama = int(tanarokszama)  # számmá konvertáltuk
        print(tanarokszama)
    except IndexError:  # ha nincs megadva argumentum
        print("Nincs elég argumentum")
    except ValueError:  # nem egesz szam az arg
        print(f"a {sys.argv[1]} nem egész szám")
    tanarlista = []
    classeslista = []
    for x in range(tanarokszama):
        listaelem = input()
        tanarlista.append(listaelem)
    for teacher in filmlista:
        elvalasztott = teacher.split(";")

        try:
            if len(elvalasztott) == 3:
                classeslista.append(model.Oktato(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2])))
            elif len(elvalasztott) == 4:
                classeslista.append(
                    model.Reszletes(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2]), int(elvalasztott[3])))
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

















