from domain.stire import Stire
from repository.RepositoryGeneric import GenericFileRepository

class ServiceStire:
    """
    se ocupa de operatii pentru stiri
    """
    def __init__(self,repository):
        """
        creeaza un service pentru stiri
        :param repository: colectia de stiri
        """
        self.__repository=repository
        
    def adauga(self,id_stire,titlu,continut,autor):
        """
        adauga o stire
        :param id_stire:id ul stirii,int 
        :param titlu: titlul stirii,str nenul
        :param continut: continutul stirii,str nenul
        :param autor: autorul stirii,str nenul 
        """
        st=Stire(id_stire,titlu,continut,autor)
        self.__repository.creeaza(st)
        
    def da_stire(self,id_st):
        """
        :param id_st: id ul stirii 
        :return:stirea ceruta 
        """
        return self.__repository.citeste(id_st)

    def random_stiri(self,n):
        """
        genereaza n stiri random
        :param n: numarul de stiri random de adaugat
        """
        import random
        import string
        a=len(self.__repository.citeste())
        for i in range(n):
            cuv_titlu=random.randint(3,10)
            cuv=random.randint(50,200)
            lit_cuv=random.randint(2,10)
            titlu=''
            for y in range(cuv_titlu):
                q=''.join(random.choice(string.ascii_lowercase) for x in range(lit_cuv))
                titlu=titlu+q+' '
                
            continut='' 
            for y in range(cuv):
                q=''.join(random.choice(string.ascii_lowercase) for x in range(lit_cuv))
                continut=continut+q+' '
            autor=''.join(random.choice(string.ascii_lowercase) for x in range(lit_cuv))
            a+=1
            self.adauga(a,titlu,continut,autor)
            
                


        
    def get_all(self):
        """
        :return: colectia de stiri
        """
        return self.__repository.citeste()