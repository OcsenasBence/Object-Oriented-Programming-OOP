from functools import total_ordering

@total_ordering
class Ital:
    nev: str
    _kiszereles: str
    __ar: int

    def __init__(self, nev: str, ar: int, kiszereles: str = "5 dl") -> None:
        self.nev = nev
        self.__ar = ar
        self._kiszereles = kiszereles

    @property
    def kiszereles(self) -> str:
        return self._kiszereles

    @property
    def ar(self) -> int:
        return self.__ar

    @kiszereles.setter
    def kiszereles(self,new: str) -> None:
        self._kiszereles=new

    def __repr__(self) -> str:
        return f"{self.nev}, {self.kiszereles}, {self.ar}"

    def __str__(self) -> str:
        return f"{self.nev}, {self.kiszereles}, {self.ar} Ft"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Ital) and (self.nev, self.kiszereles, self.ar) == (o.nev, o.kiszereles, o.ar)

    def __lt__(self, other):
        if isinstance(other, Ital):
            return (-self.ar, self.kiszereles, self.nev) < (-other.ar, other.kiszereles, other.nev)
        else:
            return NotImplemented

    @staticmethod
    def static(italok: list, nev: str)->list:
        itallista=[]
        for x in italok:
            if isinstance(x,Ital):
                if x.nev == nev:
                    itallista.append(x.nev)
        return itallista

@total_ordering
class Szeszesital(Ital):
    __alkohol: float

    def __init__(self, nev: str, ar: int,alkohol: float, kiszereles: str = "5 dl") -> None:
        super().__init__(nev, ar, kiszereles)
        self.__alkohol = alkohol

    @property
    def alkohol(self) -> float:
        return self.__alkohol

    @alkohol.setter
    def alkohol(self, value: float) -> None:
        self.__alkohol = value

    def __repr__(self) -> str:
        return super().__repr__() + f", {self.__alkohol}"

    def __str__(self) -> str:
        return f"{self.__alkohol}% alkoholtartalmú {self.nev}, {self._kiszereles}, {self.__ar} Ft"

def main():
    italokszama=0
    try:
        italokszama=sys.argv[1]
        italokszama=int(italokszama)
        print(italokszama)
    except IndexError:
        print("Nincs elég argumentum")
    except ValueError:
        print(f"a {sys.argv[1]} nem egész szám")
    itallista=[]
    classeslista=[]
    for x in range(italokszama):
        listaelem=input()
        itallista.append(listaelem)
    for drink in itallista:
        szplitelt=drink.split(";")

        try:
            if len(szplitelt) == 3:
                classeslista.append(model.Film(szplitelt[0], int(szplitelt[1]), (szplitelt[2])))
            elif len(szplitelt) == 4:
                classeslista.append(model.Film(szplitelt[0], int(szplitelt[1]), (szplitelt[2]), float(szplitelt[3])))
            else:
                raise NotImplementedError
        except ValueError:
            print("Tipuskonvertalasnal hiba merult fel")
        except NotImplementedError:
            print("A megadott sztring nem egyeztetheto se filmnek se sorozatnak")

    classeslista.sort()
    for x in classeslista:
        print(x)

if __name__ == "__main__":
    main()














