'''
Created on 01 lug 2016

@author: claudio
'''
import MySQLdb
from Document import Document
class DBlink:
    '''
    classdocs
    '''
    
    def __init__(self):
        self.doc=Document("config.txt")
        
    def config(self,params):
        self.get_doc().update(params)
    
    def get_config_toString(self):
        return self.get_doc().toString()
    
    def del_config(self):
        self.get_doc().delete()
        
    def get_doc(self):
        return self.doc
    
    def get_cursore(self):
        database=MySQLdb.connect(host=self.get_doc().get_host(),
                                 user=self.get_doc().get_user(),
                                 passwd=self.get_doc().get_passwd(),
                                 db=self.get_doc().get_db())
        return database.cursor()
    
    def get_table(self):
        return self.get_doc().get_table()
    
    def get_db(self):
        return self.get_doc().get_db()
        
    def send_query(self,query):
        cursore=self.get_cursore()
        cursore.execute(query)
        return cursore.fetchall()