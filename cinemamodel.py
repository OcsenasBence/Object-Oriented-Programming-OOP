from functools import total_ordering


@total_ordering
class Film:
    cim: str
    _hossz: int
    __korhatar: bool

    def __init__(self, cim: str, hossz: int, korhatar: bool = True) -> None:
        self.cim = cim
        self._hossz = hossz
        self.__korhatar = korhatar

    def __repr__(self) -> str:
        return f"{self.cim}, {self._hossz}, {self.__korhatar}"

    def __str__(self) -> str:
        return f"{self.cim}: {self._hossz} perces ,{'korhatásros' if self.__korhatar else 'nem korhatáros'}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Film) and self.cim == o.cim and self.hossz == o.hossz and self.korhatar == o.korhatar


    def __lt__(self, other):
        if not isinstance(other, Film):
            return NotImplemented
        return (-self.hossz, self.korhatar, self.cim) < \
                (-other.hossz, other.korhatar, other.cim)
    @property
    def hossz(self):
        return self._hossz

    @property
    def korhatar(self):
        return self.__korhatar
    @korhatar.setter
    def korhatar(self,new:bool)->None:
        self.__korhatar=new

    @staticmethod
    def count_adults(filmek: list,hossz:int) -> list:
        cimlista=[]
        for x in filmek:
            if isinstance(x,Film):
                if x.hossz==hossz:
                    cimlista.append(x.cim)
        return cimlista


@total_ordering
class Series(Film):
    __epi: int

    def __init__(self, cim: str, hossz: int, korhatar: bool, epi: int) -> None:
        super().__init__(cim, hossz, korhatar)
        self.__epi = epi



    @property
    def epi(self) -> int:
        return self.__epi

    @epi.setter
    def epi(self, value: int) -> None:
        self.__epi = value



    def __repr__(self) -> str:
        return super().__repr__() + f" {self.__epi}"

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__epi} részes"


import model
import sys

def main():
    filmekszama=0
    try:
        filmekszama=sys.argv[1]   #elso argumentum
        filmekszama=int(filmekszama) #számmá konvertáltuk
        print(filmekszama)
    except IndexError: #ha nincs megadva argumentum
        print("Nincs elég argumentum")
    except ValueError: #nem egesz szam az arg
        print(f"a {sys.argv[1]} nem egész szám")
    filmlista=[]
    classeslista=[]
    for x in range(filmekszama):
        listaelem=input()
        filmlista.append(listaelem)
    for kitudja in filmlista:
        elvalasztott=kitudja.split(";")


        try:
            if len(elvalasztott) == 3:
                classeslista.append(model.Film(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2])))
            elif len(elvalasztott) == 4:
                classeslista.append(
                    model.Series(elvalasztott[0], int(elvalasztott[1]), bool(elvalasztott[2]), int(elvalasztott[3])))
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