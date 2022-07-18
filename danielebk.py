from datetime import date
from os import listdir
from os import remove
from os.path import isfile, join

class tbk:
	
    def __init__(self):
		#print("costruttore")
        self.__nome="bkDaniele"
        self.__dirBK="bk"
        self.__do=str(date.today())
        self.__maxBK=5
    def getDataOggi(self):
        return self.__do
    def __costruisciNome(self,pt,d,nome):
        return pt+"/"+d+"-"+nome
    def generaFileTest(self,d,n):
        for i in range(n):
            open(self.__costruisciNome()+str(i),'a').close()
            #curr_date_temp = date.strptime(self.__do, "%y-%m-%a")
            #new_date = curr_date_temp + datetime.timedelta(days=5)
            #print(new_date)
    def __getListaBackup(self):
        l=[ f for f in listdir(self.__dirBK) if isfile(join(self.__dirBK , f))]
        l.sort()
        return self.__filtraLista(l)
    def __filtraLista(self,l):
        l=[f for f in l if f[len(self.__do)+1:len(self.__do)+1+len(self.__nome)]==self.__nome ]
        #print("2022-07-17-bkDaniele0"[len(self.__do):len(self.__do)+1+len(self.__nome)])
        return l
    def rimuoviVecchi(self):
        l=self.__getListaBackup()
        n=len(l)-self.__maxBK
        print(n)
        if n>0:
            for i in range(n):
                remove(self.__dirBK+"/"+l[i])
                print("Ho rimosso: "+str(l[i]))
c=tbk()
c.rimuoviVecchi();

