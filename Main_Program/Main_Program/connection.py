import dropbox,os,sys

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

    