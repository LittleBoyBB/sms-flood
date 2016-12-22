# coding: utf-8
try:
	from textnow import TextNow 
	from random import randrange, random
	from colorama import Fore, Back, Style
except:
	print(Fore.RED + Style.DIM + '[X] Uma ou mais libs nao foram carregadas!!')

__cookie = {
	'fsouza':str("unsupported_browsers_notif=true; language=pt; express:sess=eyJ1c2VybmFtZSI6ImZzb3V6YSIsInNlc3Npb25JZCI6Ijg3YmE5MzVmMmQzZmNiMjhhNzg2YmY3YTE3NGI5NTZiMzRhMzYwYzE2YTRmYjg4Y2IzNjg5MjUwMTZmNTBkMGMiLCJzZXR0aW5ncyI6eyJzb3VuZHNFbmFibGVkIjp0cnVlLCJjYWxsaW5nRW5hYmxlZCI6ZmFsc2V9LCJyZW1lbWJlciI6ZmFsc2UsImhhc1N1YnNjcmlwdGlvbiI6ZmFsc2V9; express:sess.sig=wy_qWg0aEv3oP85KSu7Lg98268s; paidUser=false; interstitial_%2Fcommon%2Fpublic%2Fimages%2FHolidaySale2016%2FWeb_Interstitial.jpg_shown=true; fsouzaNotifPermissionsGranted=false; UserDidVisitApp=true; FirehoseSession-messaging=true; H1:9a6351cc748972b8f9f0328ac014d=1; sm_dapi_session=1"),
	'alejandro_martins':str("unsupported_browsers_notif=true; _gat=1; language=pt; _ga=GA1.2.861620014.1482343914; express:sess=eyJ1c2VybmFtZSI6ImFsZWphbmRyb19tYXJ0aW5zIiwic2Vzc2lvbklkIjoiN2FiNzE5NjA5MzFkNjJmNjZlNzk2NTY2YzE5OTY4ZTgyN2I3NDEzOTI0ZTk3MTE2YTMyMjRiNjE5OTM4ZDJlMyIsInNldHRpbmdzIjp7InNvdW5kc0VuYWJsZWQiOnRydWUsImNhbGxpbmdFbmFibGVkIjpmYWxzZX0sInJlbWVtYmVyIjpmYWxzZSwiaGFzU3Vic2NyaXB0aW9uIjpmYWxzZX0=; express:sess.sig=6gbT_RTZ-jTO7ChkfLG5-SyXJfc; paidUser=false; interstitial_%2Fcommon%2Fpublic%2Fimages%2FHolidaySale2016%2FWeb_Interstitial.jpg_shown=true; alejandro_martinsNotifPermissionsGranted=false; UserDidVisitApp=true; FirehoseSession-messaging=true; H1:be12c4285404c3ad7578705581e22=1; sm_dapi_session=1"),
	'araujo_junior':str("unsupported_browsers_notif=true; language=pt; express:sess=eyJ1c2VybmFtZSI6ImFyYXVqb19qdW5pb3IiLCJzZXNzaW9uSWQiOiIyODNkOTc3M2MzNjM2YWE3NjFhYTYxYjI2NDQyZjMwYzlhNzcwN2FjMmY5M2I0YzZkOTRhOTkyNjAyYWQ1OTA1Iiwic2V0dGluZ3MiOnsic291bmRzRW5hYmxlZCI6dHJ1ZSwiY2FsbGluZ0VuYWJsZWQiOmZhbHNlfSwicmVtZW1iZXIiOmZhbHNlLCJoYXNTdWJzY3JpcHRpb24iOmZhbHNlfQ==; express:sess.sig=SUFgJEfjiCr-eQuLlm2683wHp2Y; paidUser=false; interstitial_%2Fcommon%2Fpublic%2Fimages%2FHolidaySale2016%2FWeb_Interstitial.jpg_shown=true; araujo_juniorNotifPermissionsGranted=false; UserDidVisitApp=true; FirehoseSession-messaging=true; H1:e82417c278de0f613431cfdd48097=1; sm_dapi_session=1"),
	'arnaldo_sarcomani': str("unsupported_browsers_notif=true; language=pt; newUser.arnaldo_sarcomani=new; express:sess=eyJ1c2VybmFtZSI6ImFybmFsZG9fc2FyY29tYW5pIiwic2Vzc2lvbklkIjoiMzhjZDQ0NTcwYjVhMGJhN2YzMjA0YjYyNTVlNmNiOWMxZGQ1OTk3MjM3NjY4ZDZiZjlmOWRlNTE2ZDc4ZWZmOSIsInNldHRpbmdzIjp7InNvdW5kc0VuYWJsZWQiOnRydWUsImNhbGxpbmdFbmFibGVkIjpmYWxzZX0sImhhc1N1YnNjcmlwdGlvbiI6ZmFsc2V9; express:sess.sig=1ZLBiiXdZUarkK9Mn8JxtiKGyQo; paidUser=false; interstitial_%2Fcommon%2Fpublic%2Fimages%2FHolidaySale2016%2FWeb_Interstitial.jpg_shown=true; arnaldo_sarcomaniNotifPermissionsGranted=false; UserDidVisitApp=true; H1:a2693ccbb3d576536874de8acf666=1; sm_dapi_session=1; FirehoseSession-messaging=true"),
	'gzuis_cristis': str("unsupported_browsers_notif=true; language=pt; newUser.gzuis_cristis=new; express:sess=eyJ1c2VybmFtZSI6Imd6dWlzX2NyaXN0aXMiLCJzZXNzaW9uSWQiOiIyZTlkNzA5OTkxZTE3Y2EwMmMzZTFhN2U4MDVhYTBmNGEzMGE1MzBjNzM5MmZiNWEwYmNjMTI5ZTE3N2Q3MTcyIiwic2V0dGluZ3MiOnsic291bmRzRW5hYmxlZCI6dHJ1ZSwiY2FsbGluZ0VuYWJsZWQiOmZhbHNlfSwiaGFzU3Vic2NyaXB0aW9uIjpmYWxzZX0=; express:sess.sig=uCEsH73Ls6vBgU0tjjgewT7fLIY; paidUser=false; interstitial_%2Fcommon%2Fpublic%2Fimages%2FHolidaySale2016%2FWeb_Interstitial.jpg_shown=true; gzuis_cristisNotifPermissionsGranted=false; UserDidVisitApp=true; H1:d322f20f2e1033a7440b660ad8b8a=1; sm_dapi_session=1; FirehoseSession-messaging=true")
}

__proxys = {
	'http': '178.62.88.50:8118',
	'http': '124.88.67.20:81',
	'http': '124.88.67.34:843',
	'http': '163.158.216.152:80',
	'http': '58.176.46.248:80',
	'http': '124.88.67.17:82',
	'http': '168.63.20.19:8119',
	'http': '137.74.254.198:3128'
}
__banner = """
  ██████  ███▄ ▄███▓  ██████      █████▒██▓     ▒█████   ▒█████  ▓█████▄ 
▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒    ▓██   ▒▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
░ ▓██▄   ▓██    ▓██░░ ▓██▄      ▒████ ░▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
  ▒   ██▒▒██    ▒██   ▒   ██▒   ░▓█▒  ░▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
▒██████▒▒▒██▒   ░██▒▒██████▒▒   ░▒█░   ░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ 
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░    ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ 
░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░    ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ 
░  ░  ░  ░      ░   ░  ░  ░      ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ 
      ░         ░         ░                ░  ░    ░ ░      ░ ░     ░    
                                                                  ░      
@LittleBoy_BB
"""

def main(): 
	print(__banner)
	
	print('[*] O numero precisa conter o codigo do pais,ddd e sem espacos')
	number 	 = input('[*] Digite o numero de envio:')

	qnt 	 = int(input('[*] Digite quantas mensagens devem ser enviadas[Tente nao exagerar xeroque]:')) 
	mensagem = input('[*] Digite uma mensagem(Digite mesmo!!):')

	if not mensagem:
		print(Fore.RED + '[X] Nenhuma mensagem foi inserida...')
		print('\n[*] Deixando o script....' + Fore.RESET)
		exit()

	send(qnt,number,mensagem)

def send(quantidade,number,message):
	if quantidade <= 0:
		print(Fore.RED +'[X] A quantidade precisa ser um numero inteiro maior que zero!!'+ Fore.RESET)
		exit()

	Text = TextNow('','')
	Text.proxies(__proxys)

	for tent in range(quantidade):
		shuffle_cookies = sorted(__cookie.items(), key=lambda x: random())
		random_accounts = shuffle_cookies[ randrange(len(shuffle_cookies) - 1) ]
		Text.change_cookie( random_accounts[1] )
		Text.change_owner( random_accounts[0] )
		
		print(Fore.CYAN+ Style.BRIGHT +'[!] Randomize number'+ Style.RESET_ALL)

		if Text.send(str(number), message):
			print(Fore.GREEN + Style.BRIGHT +'[*] Num:{0} - Mensagem enviada...'.format(tent) + Style.RESET_ALL)
		else:
			print(Back.RED + Fore.WHITE +'[*] Num:{0} - Falhou...'.format(tent) + Style.RESET_ALL)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(Fore.RED +'\n[*] Deixando o script....'+ Fore.RESET)
		exit()