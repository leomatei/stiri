class Entity:
    """
    se ocupa de o entitate
    """
    def __init__(self, id_entity):
        """
        creeazza o entitate
        id_entity:id ul entitatii,int
        """
        self.__id_entity = id_entity


    @property
    def id_entity(self):
        return self.__id_entity

    @id_entity.setter
    def id_entity(self, id_ent):
        self.__id_entity = id_ent