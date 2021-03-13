from domain.comentariu import Comentariu
from repository.RepositoryGeneric import GenericFileRepository

class ServiceCom:
    """
    se ocupa de operatii pe comentarii
    """
    def __init__(self,repository):
        """
        creeaz un service de comentarii
        :param repository: colectia de comentarii
        """
        self.__repository=repository
        
    def adauga(self,id_com,id_st,id_com_parinte,continut):
        """
        adauga un comentariu
        :param id_com: id ul comentariului,int
        :param id_stire: id ul stirii la care este atasat comentariul,int trebuie sa existe stire
        :param id_com_parinte: id ul comentariului parinte,int 0 sau un id de comentariu
        :param continut: continutul comentariului, str
        """
        com=Comentariu(id_com,id_st,id_com_parinte,continut)
        self.__repository.creeaza(com)
        
    def da_com(self,id_com):
        """
        :param id_com:id ul comentariului 
        :return: comentariul dat
        """
        return self.__repository.citeste(id_com)

    def ordonare_com(self):
        """
        ordoneaza comentarile descrescator dupa numarul de cuvinte
        :return: lista ordonata de comentarii
        """
        return sorted(self.__repository.citeste(),key=lambda x:len(x.continut.split()),reverse=True)

    def com_radacina(self):
        """
        :return:comentarile radacina si subcomentarile acestora 
        """
        cr=[]
        for com in self.__repository.citeste():
            if com.id_com_parinte==0:
                cr.append([com.id_entity,0])
        for i in cr:
            for com in self.__repository.citeste():
                if com.id_com_parinte==i[0]:
                    i[1]+=1
        return cr
        
            
        
    def get_all(self):
        """
        :return:lista de comentarii 
        """
        return self.__repository.citeste()