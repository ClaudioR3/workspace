'''
Created on 29 mag 2016

@author: claudio
'''
import MySQLdb
class Connection:
    '''
    classdocs
    '''


    def __init__(self, host="localhost",user="root",passwd="",db="database"):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
        self.save_in_file()
    
    def run(self):
        try :
            database=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            return database.cursor()
        except (),e:
            print e
            return ""
    
    def save_in_file(self):
        try:
            pass
        except:
            print "DataConfig.txt non creato"
    
    def import_datas_from_file(self):
        try:
            pass
        except():
            print "DataConfig.txt non presente"
    
    def send_query(self,query):
        cursore=self.run()
        try:
            cursore.execute(query)
            return cursore.fetchall()
        except():
            print "Problema della query"
            return ""
    