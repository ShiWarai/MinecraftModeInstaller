import socket,threading,requests, dropbox,zipfile,os,sys

'''class LocalConnection():
    def __init__(self,queue,port,ip=socket.gethostbyname(socket.gethostname()),output_=print,input_=input,bit_rate=1024,isServer=True): # Создание соединения
        super(LocalConnection,self).__init__()
        self.IP=ip
        self.bitrate=bit_rate
        self.PORT=int(port)
        self.output=output_
        self.input=input_
        self.queue=queue
        self.stop=threading.Event()
        self.stop.clear()
        if isServer:
            waiting_socket=socket.socket()
            waiting_socket.bind((ip,int(port)))
            waiting_socket.listen(queue)
            self.socket_,self.IP_Client=waiting_socket.accept()
        else:
            try:
                self.socket_=socket.socket()
                self.socket_.connect((ip,int(port)))
            except:
                return 0

    def __sending(self): # Отправка сообщения
        while self.stop.isSet()==False:
            message=self.input()
            if type(message) != bytes:
                message=str(message).encode(encoding="utf-8")
            try:
                self.socket_.sendall(message)
            except:
                break
        return 0 # Конец работы отправки

    def __getting(self): # Получение сообщения
        while self.stop.isSet()==False:
            message=self.socket_.recv(self.bitrate)
            if not message:
                self.stop.set()
                break
            self.output(message)

    def send(self): # Запускает отправку сообщений
        try:
            thr1=threading.Thread(target=self.__sending)
            thr1.start()
            return self.stop
        except:
            return 0
    def get(self): # Запускает получение сообщений
        try:
            thr1=threading.Thread(target=self.__getting)
            thr1.start()
            return self.stop
        except:
            return 0

class GlobalConnection():
    def __init__(self,queue,ip,port,output_=print,input_=input,bit_rate=1024,isServer=True): # Создание соединения
        super(LocalConnection,self).__init__()
        self.IP=ip
        self.bitrate=bit_rate
        self.PORT=int(port)
        self.output=output_
        self.input=input_
        self.queue=queue
        self.stop=threading.Event()
        self.stop.clear()
        if isServer:
            waiting_socket=socket.socket()
            waiting_socket.bind((ip,int(port)))
            waiting_socket.listen(queue)
            self.socket_,self.IP_Client=waiting_socket.accept()
        else:
            try:
                self.socket_=socket.socket()
                self.socket_.connect((ip,int(port)))
            except:
                return 0

    def __sending(self): # Отправка сообщения
        while self.stop.isSet()==False:
            message=self.input()
            if type(message) != bytes:
                message=str(message).encode(encoding="utf-8")
            try:
                self.socket_.sendall(message)
            except:
                break
        return 0 # Конец работы отправки

    def __getting(self): # Получение сообщения
        while self.stop.isSet()==False:
            message=self.socket_.recv(self.bitrate)
            if not message:
                self.stop.set()
                break
            self.output(message)

    def send(self): # Запускает отправку сообщений
        try:
            thr1=threading.Thread(target=self.__sending)
            thr1.start()
            return self.stop
        except:
            return 0
    def get(self): # Запускает получение сообщений
        try:
            thr1=threading.Thread(target=self.__getting)
            thr1.start()
            return self.stop
        except:
            return 0'''

class UpdateFromDropbox():
    def __init__(self,key,data_name,installer=None):
        self.key=key; self.data_name=data_name; self.install=installer;
        try:
            self.dropfolder=dropbox.Dropbox(self.key)
        except:
            return 0
    def check(self):
        meta,res=self.dropfolder.files_download(path='/versions.txt')
        return res.content.decode("utf-8")[1:len(res.content.decode("utf-8"))]
    def last(self):
        versions=self.check()
        num=versions.index('|')
        return versions[0:num]
    def download(self,version=None):
        if version==None:
            version=self.last()
        meta,arch=self.dropfolder.files_download(path='/versions/'+version+'/'+self.data_name+'.zip')
        way=os.path.abspath(sys.argv[0]).split('\\')
        way.pop(len(way)-1);way_=''
        for x in way:
            way_+=x+'\\'
        way=way_;del way_
        with open(way+self.data_name+'.zip','wb') as file:
            file.write(arch.content)
        if self.install!=None:
            self.install(way,way+self.data_name+'.zip')
            return way

'''def DownloadSiteFile(web,file):
    filereq = requests.get(web,stream = True)
    with open(file,"wb") as receive:
        receive.write(filereq.content)
    del filereq
    return True

def DownloadDropbox(key,path_,file_path):
    from dropbox import Dropbox
    dbx = Dropbox(key);
    with open(file_path, "wb") as f:
        metadata, res = dbx.files_download(path='/'+path_)
        f.write(res.content)
        f.close()
        return metadata
    return 0'''
    