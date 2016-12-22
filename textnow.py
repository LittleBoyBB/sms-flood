# coding: utf-8
try:
	import requests
	import json
except:
	print('Algumas bibliotecas nao foram carregadas')

class TextNow:
	"""
	Cria a acesso a API REST do textnow permitindo realizar
	tarefas como exclusão, envio e visualização de mensagens
	"""
	def __init__(self,own,cookie):
		self.proxy = {}
		self.owner = own
		self.cookie = cookie
		self.header = {
			'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.3) Gecko/20100402 Prism/1.0b4',
			'Host':'www.textnow.com',
			'Cookie': self.cookie,
			'Content-Type': 'application/json'
		}
		self.data = {
			"json":{
				"contact_value":None,
				"contact_type":'2',
				"message":None,
				"read":'1',
				"message_direction":'2',
				"message_type":'1',
				"from_name":self.owner
			}
		}
		self.url = "https://www.textnow.com/api/users/{0}/messages"

	def send(self,number=None,message="Mensagem invalida ou vazia"):
		"""
		Envia uma mensagem para o numero requisitado

		ex: send('5511984442233','Ola mundo')

		Retorna False -> se number nao for passado ou nao for uma string
		Retorna False -> Se a resposta da API for diferente de OK (200)
		Retorna True  -> Se a resposta for OK (200)
		"""
		if not number or type(number) != str:
			return False 

		payload = self.data.copy()

		payload['json']['contact_value'] = '+' + number
		payload['json']['message'] = message

		payload = json.dumps(payload)

		url = self.url.format(self.owner)

		req = requests.post(url,data=payload,headers=self.header,proxies=self.proxy)

		if req.status_code == 200:
			return True

		return False

	def proxies(self, list_prox):
		"""
		Defini uma lista de proxys para serem usadas

		Return True -> Sempre
		"""

		self.proxy = list_prox
		return True

	def change_cookie(self,cookie):
		"""
		Alterar o cookie usado nas requisições

		Retorna False -> Se nenhum cookie for passado
		Retorna True  -> Se cookie setado corretamente
		"""
		if not cookie:
			return False

		self.cookie = cookie
		self.header['Cookie'] = self.cookie
		return True

	def change_owner(self,owner):
		"""
		Altera o SENDER da mensagem, porém não tem tanto impacto no
		funcionamento do script.

		Return True -> Sempre
		"""
		self.owner = owner
		self.data['json']['from_name'] = self.owner
		return True

	def messages(self):
		"""
		Retorna todas as mensagens enviadas e recebidas

		Return False -> Se a resposta do servidor for diferente de OK (200)
		Return JSON  -> Se a resposta for OK (200)
		"""
		req = requests.get(self.url,headers=self.header)

		if req.status_code == 200:
			return req.json()

		return False

	def delete_conversation(self,number):
		"""
		Deleta toda a conversa com um determinado numero

		Return False -> Se o numero nao for especificado ou nao for uma string
		Return False -> Caso a resposta do servidor for diferente de OK(200)
		Return True  -> Se tudo ocorrer bem
		"""
		if not number or type(number) != str:
			return False

		url = "https://www.textnow.com/api/users/{0}/conversations/%2B".format(self.owner) + number
		req = requests.delete(url, headers=self.header)

		if 200 == req.status_code:
			return True

		return False

	def delete_message(self, id_message):
		"""
		Remove pelo id, uma mensagem enviada para um numero especifico

		Retorna False -> se ID nao for passado ou nao for uma string
		Retorna False -> Se a resposta da API for diferente de OK (200)
		Retorna True  -> Se a resposta for OK (200)
		"""
		if not id_message or type(id_message) != str:
			return False

		url = "https://www.textnow.com/api/users/{0}/messages/".format(self.owner) + id_message[:-1]
		req = requests.delete(url,headers=self.header)

		if 200 == req.status_code:
			return True

		return False

	def block(self,number):
		"""
		Bloqueia um numero

		Retorna False -> se number nao for passado ou nao for uma string
		Retorna False -> Se a resposta da API for diferente de OK (200)
		Retorna True  -> Se a resposta for OK (200)
		"""
		if not number or type(number) != str:
			return False

		url = "https://www.textnow.com/api/blocks?contact_value=%2B" + number
		req = requests.put(url, headers=self.header)

		if 200 == req.status_code:
			return True

		return False

	def unblock(self,number):
		"""
		Desbloqueia um numero bloqueado

		Retorna False -> se number nao for passado ou nao for uma string
		Retorna False -> Se a resposta da API for diferente de OK (200)
		Retorna True  -> Se a resposta for OK (200)
		"""
		if not number or type(number) != str:
			return False

		url = "https://www.textnow.com/api/blocks/%2B" + number
		req = requests.delete(url,headers=self.header)

		if 200 == req.status_code:
			return True

		return False

if __name__ == '__main__':
	print('Iae, Beleza?')