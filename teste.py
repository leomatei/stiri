from repository.RepositoryGeneric import GenericFileRepository
import os
from domain.stire import Stire
from domain.comentariu import Comentariu
from service.service_comentarii import ServiceCom
from service.service_stire import ServiceStire

repo_st=GenericFileRepository('test_st.pkl')
repo_com=GenericFileRepository('test_com.pkl')

serv_st=ServiceStire(repo_st)
serv_com=ServiceCom(repo_com)

serv_st.adauga(1,'aa1','aaa','aaa')
serv_st.adauga(2,'aaa','aaa','aaa')
serv_st.adauga(3,'aaa','aaa','aaa')

serv_com.adauga(1,1,0,'aa1')
serv_com.adauga(2,1,1,'aaa')
serv_com.adauga(3,2,0,'aaa')

def test_st():
    assert len(serv_st.get_all())==3
    assert serv_st.da_stire(1).titlu=='aa1'
    serv_st.random_stiri(4)
    assert len(serv_st.get_all())==7

def test_com():
    assert len(serv_com.get_all())==3
    assert serv_com.da_com(1).continut=='aa1'
    l=[[1,1],[3,0]]
    assert serv_com.com_radacina()==l
    serv_com.adauga(4, 1, 0, 'aa 1')
    serv_com.adauga(5, 1, 1, 'aa a')
    serv_com.adauga(6, 2, 0, 'a a a')
    a=[serv_com.da_com(6),serv_com.da_com(4),serv_com.da_com(5),serv_com.da_com(1),serv_com.da_com(2),serv_com.da_com(3)]
    assert serv_com.ordonare_com()==a


test_st()
test_com()

os.remove('test_st.pkl')
os.remove('test_com.pkl')
