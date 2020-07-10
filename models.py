class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade, cep):
        self.logradouro = logradouro 
        self.numero = numero 
        self.bairro = bairro 
        self.cidade = cidade 
        self.cep = cep


class Cliente:
  def __init__(self, nome='', cpf='', endereco: Endereco = [], telefone=''):
      self.nome = nome
      self.cpf = cpf
      self.endereco: Endereco = endereco
      self.telefone = telefone
      self.clientel = []

  def cadastro_cliente(self):
      print('CADASTRO CLIENTE 1')
      nome = input('NOME: ')
      cpf = input('CFP: ')
      endereco = input('ENDEREÇO: ')
      telefone = input('TELEFONE: ')

      novocliente = Cliente(nome, cpf, endereco, telefone)
      self.clientel.append(novocliente)

      print(novocliente)



class Conta:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.transacoes: Transacao = []

    def depositar(self, valor, descricao):
        self.transacoes.append(Transacao(self, valor, 'deposito', descricao))
    
    def sacar(self, valor):
        if self.tem_limite(valor):
            self.transacoes.append(Transacao(self, valor, 'saque'))

    def tem_limite(valor):
        return get_saldo() >= valor

    def get_saldo(self):
        return sum(map(lambda t: t.valor), self.transacoes)


class Transacao:
    def __init__(self, conta, valor, tipo, descricao=None):
        self.conta = conta
        self.valor = valor
        self.tipo = tipo
        self.descricao = descricao
