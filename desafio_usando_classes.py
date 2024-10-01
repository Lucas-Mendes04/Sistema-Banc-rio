#Desafio de Projeto - Modelando o Sistema Bancário em Classes
from abc import ABC, abstractclassmethod, abstractproperty


class Conta:
    def __init__(self,numero:int, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls,cliente,numero:int):        
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self.saldo
    
    @property
    def numero(self):
        return self.numero
    
    @property
    def agencia(self):
        return self.agencia
    
    @property
    def cliente(self):
        return self.cliente        
    
    @property
    def historico(self):
        return self.historico    

    def sacar(self,valor:float):
        saldo = self.valor
        pass
    #return bool

    def depositar(self,valor:float):
        self.valor = valor
        pass
   #return bool 

class ContaCorrente(Conta):
    def __init__(self,limite:float,limite_saques:int, **kw):
        self.limite = limite
        self.limite_saques = limite_saques
        super().__init__(**kw)
        pass

class Historico(Conta):
    def adicionar_transacao(self,transacao):
        self.transacao = transacao

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass

class Deposito(Transacao):
    def __init__(self,valor,**kw):
        self.valor = valor
        super().__init__(**kw)

class Saque(Transacao):
    def __init__(self,valor,*kw):
        self.valor = valor
        super().__init__(**kw)

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco 
        self.contas = []
    
    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)    

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

