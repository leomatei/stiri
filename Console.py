from repository.RepositoryGeneric import RepositoryError
from service.service_comentarii import ServiceCom
from service.service_stire import ServiceStire

class Console:
    def __init__(self,service_st,service_com):
        self.__service_st=service_st
        self.__service_com=service_com
        
    def __show_menu(self):
        print('1.adaugare stire')
        print('2.adaugare comentariu')
        print('3.generare stiri')
        print('4.afisare comentarii descrescator dupa numarul de cuvinte')
        print('5.afisarea com radacina si a subcomentarilor')
        print('as.afisare stiri')
        print('ac.afisare comenatrii')
        print('x.iesire')
    
    def __show_list(self,lista):
        for object in lista:
            print(object)
            
    def run(self):
        while True:
            self.__show_menu()
            op=input('alegeti optiune: ')
            if op=='1':
                self.__handle_adauga_stire()
            elif op=='2':
                self.__handle_adauga_com()
            elif op=='3':
                self.__handle_random_stiri()
            elif op=='4':
                self.__show_com(self.__service_com.ordonare_com())
            elif op=='5':
                self.__com_rad()
            elif op=='as':
                self.__show_list(self.__service_st.get_all())
            elif op=='ac':
                self.__show_com(self.__service_com.get_all())
            elif op=='x':
                break
            else:
                print("date invalide")
                
    def __handle_random_stiri(self):
        try:
            n=int(input('dati numarul de stiri de adaugat: '))
            self.__service_st.random_stiri(n)
        except ValueError:
            print('date introduse gresit')
                
    def __handle_adauga_stire(self):
        try:
            id_st=int(input('dati id ul stirii: '))
            titlu=input('dati titlul stirii: ')
            continut=input('dati continutul stirii: ')
            autor=input('dati autorul stirii: ')
            if titlu=='' or continut=='' or autor=='':
                raise ValueError
            self.__service_st.adauga(id_st,titlu,continut,autor)
        except ValueError:
            print('date introduse gresit')
        except RepositoryError as re:
            print(re)
            
    def __handle_adauga_com(self):
        try:
            id_com=int(input('dati id ul comentariului: '))
            id_st=int(input('dati id ul stirii'))
            id_com_parinte=int(input('dati id ul comentariului parinte: '))
            continut=input('dati continutl comentariului: ')
            if self.__service_st.da_stire(id_st) is None:
                raise ValueError
            if id_com_parinte!=0:
                if self.__service_com.da_com(id_com_parinte) is None:
                    raise ValueError
            if continut=='':
                raise ValueError
            self.__service_com.adauga(id_com,id_st,id_com_parinte,continut)
        except ValueError:
            print('date introduse gresit')
        except RepositoryError as re:
            print(re)
            
    def __show_com(self,lista_com):
        for com in lista_com:
            print(self.__service_st.da_stire(com.id_stire).titlu, com)

    def __com_rad(self):
        cr=self.__service_com.com_radacina()
        for i in cr:
            print(self.__service_st.da_stire(self.__service_com.da_com(i[0]).id_stire).titlu)
            print(self.__service_com.da_com(i[0]))
            print(f'cu {i[1]} subcomenatrii')




                
    
        