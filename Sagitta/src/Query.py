'''
Created on 01 lug 2016

@author: claudio
'''
from DBlink import DBlink
import sys

class Query:
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.dblink=DBlink()
        
    def confronta(self,n1,n2):
        n1=str.lower(n1)
        n2=str.lower(n2)
        return n1==n2
        
    def is_defined(self,name,describe):
        nameDefined=""
        for e in describe:
            if self.confronta(name,e):
                nameDefined=name
        if nameDefined=="":
            nameDefined=self.is_alias(name)
        return nameDefined
    
    def is_alias(self,name):
        return ""
        
    def build_where(self,args):
        s=""
        describe=self.do_describe()
        for name in args.keys():
            nameDefined=self.is_defined(name,describe)
            if nameDefined!="":
                if s!="":
                    s+=" and "
                s+= " "+nameDefined+" = '"+args[name]+"' "
        if s!="":
            s=" where "+s
        return s
        
    def do_query(self,args):
        query="select * from "+self.dblink.get_table()+" "+self.build_where(args)
        try :
            tupla=self.dblink.send_query(query)
            return "%d risultati"%len(tupla)
        except ():
            return sys.exc_info()[0]
    
    def do_describe(self):
        query="describe MEDCORDEX"
        describe=self.dblink.send_query(query)
        l=""
        for elem in describe:
            l+=elem[0]+" "
        return l
    
    def get_config_toString(self):
        return self.dblink.get_config_toString()
    
    def config_dblink(self,params):
        self.dblink.config(params)
        
    def del_config(self):
        self.dblink.del_config()
                