
import json

class node:
    data=[]
    linkedTo=[]

    def __init__(self, name, id, label, data, type, linkedTo):
        self.name=name
        self.id=id
        self.label=label
        self.data=data
        self.type=type
        self.linkedTo=self.__gettingLinkedTo__(linkedTo)


    def __gettingLinkedTo__(linkedTo):
        aux=[]
        
        for i in linkedTo:
            x=i.get[0]
            y=i.get[1]
            aux.append((x,y))
        return aux


    