import json


class estado: 
    def __init__(self,id,sigla,nome,regiao):
        self.id = id
        self.sigla = sigla
        self.nome = nome 
        self.idRegiao = regiao['id']
        self.siglaRegiao = regiao['sigla']
        self.nomeRegiao = regiao['nome']
        
        
    @classmethod
    def from_json(cls, json_string):
        json_dict = json_loads(json_string)
        return cls(**json_dict)

     