#*************************************************************************
## CREATO DA ORTU prof. DANIELE
## daniele.ortu@itisgrassi.edu.it

from danielebk import tbk
import os
import subprocess
import glob

class bkFile(tbk):
    def __init__(self,fConf,f):
        super().__init__(fConf)
        self.__f=f
        self._nomeTAR=""
    def __preparaFile(self):
        self.__nomeTAR=self._do+"-"+self._nome+".tar.gz"
    def __log(self,f,msg,mail):
        f.write(msg)
        f.close()
        if mail:
            os.system("mail -s  '"+self._nome+"' server.backup@itisgrassi.edu.it < "+self._fileLOG)    
    def backuppa(self):
        f = open(self._fileLOG, "w")
        f.write("Copio il file "+self._da+"/"+self.__f+" in "+self._tmp+"/")
        r=subprocess.run(["scp",self._da+"/"+self.__f,self._tmp+"/"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #print(r.stderr)
        if r.stderr:
            self.__log(f,"\nERRORE: "+r.stderr.decode("utf-8"),True)
            return
        f.write("\nFile "+self._da+"/"+self.__f+" copiato")
        ls=self._getListaBackup()
        if len(ls)!=0:
            ls.reverse()
            print("da fare: controllare data")
            #return

        f.write("\nCambio directory: "+self._tmp)
        #r=subprocess.call("cd "+self._tmp,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #if r.stderr:
        #    self.__log(f,"\nERRORE: "+r.stderr.decode("utf-8"),True)
        #    return
        r=os.chdir(self._tmp)
        if r:
            self.__log(f,"\nERRORE: cambio directry",True)
            return
        f.write("\nDirectory cambiata")
        
        self.__preparaFile()
        f.write("\nComprimo "+self.__nomeTAR)
        r=subprocess.run(["tar","zfc",self.__nomeTAR,self.__f],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if r.stderr:
            self.__log(f,"\nERRORE: "+r.stderr.decode("utf-8"),True)
            return
        f.write("\nFile compresso")

        f.write("\nCopio file "+self.__nomeTAR+" in "+self._dirBK)
        r=subprocess.run(["cp",self.__nomeTAR,self._dirBK+"/"+self.__nomeTAR],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if r.stderr:
            self.__log(f,"\nERRORE: "+r.stderr.decode("utf-8"),True)
            return
        f.write("\nFile copiato")
        
        f.write("\nPulisco "+self._tmp)
        for i in glob.glob(os.path.join(self._tmp,'*')):
            if os.path.isdir(i):
                shutil.rmtree(path)
            else:
                os.remove(i)
        f.write("\nDirectory ripulita")

        f.write("\nElimina vecchi")
        r=self._rimuoviVecchi()
        f.write(r)
        self.__log(f,"\nPROCESSO ESEGUITO CON SUCESSO",False)
        f.close()
        
        
#c=bkFile("infoschool.json","AXIOSDATABASE.FDB")
c=bkFile("infoschool.json","pipi.txt")
c.backuppa()
