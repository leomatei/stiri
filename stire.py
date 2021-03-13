from domain.Entity import Entity

class Stire(Entity):
    """
    se ocupa de stiri
    """
    def __init__(self,id_stire,titlu,continut,autor):
        """
        creeaza o stire
        :param id_stire:id ul stirii,int 
        :param titlu: titlul stirii,str nenul
        :param continut: continutul stirii,str nenul
        :param autor: autorul stirii,str nenul
        """
        super(Stire, self).__init__(id_stire)
        self.__titlu=titlu
        self.__continut=continut
        self.__autor=autor
        
    @property
    def titlu(self):
        return self.__titlu
    @property
    def continut(self):
        return self.__continut
    @property
    def autor(self):
        return self.__autor
    
    def __str__(self):
        return f'{self.id_entity}.{self.titlu}:{self.__continut}- {self.__autor}'