from repository.RepositoryGeneric import GenericFileRepository
from ui.Console import Console
from domain.comentariu import Comentariu
from domain.stire import Stire
from service.service_stire import ServiceStire
from service.service_comentarii import ServiceCom

repo_st=GenericFileRepository('stiri.pkl')
repo_com=GenericFileRepository('comentarii.pkl')

service_st=ServiceStire(repo_st)
service_com=ServiceCom(repo_com)


cons=Console(service_st,service_com)

cons.run()