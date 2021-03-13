from domain.Entity import Entity
from domain.stire import Stire

class Comentariu(Entity):
    """
    se ocupa de comentarii
    """
    def __init__(self,id_com,id_stire,id_com_parinte,continut):
        """
        creeza un comentariu
        :param id_com: id ul comentariului,int
        :param id_stire: id ul stirii la care este atasat comentariul,int trebuie sa existe stire
        :param id_com_parinte: id ul comentariului parinte,int 0 sau un id de comentariu
        :param continut: continutul comentariului, str
        """
        super(Comentariu, self).__init__(id_com)
        self.__id_stire=id_stire
        self.__id_com_parinte=id_com_parinte
        self.__continut=continut
        
    @property
    def id_stire(self):
        return self.__id_stire
    @property
    def id_com_parinte(self):
        return self.__id_com_parinte
    @property
    def continut(self):
        return self.__continut
    
    def __str__(self):
        return f'{self.id_entity}.{self.id_stire}.{self.__id_com_parinte}-{self.continut}'
    
    def __eq__(self, other):
        if type(self)!=type(other):
            return False
        return self.id_entity==other.id_entity