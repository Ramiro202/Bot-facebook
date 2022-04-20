
import requests
from os import system
from time import sleep
from bs4 import BeautifulSoup
from lib.libs import cabeca, log, postar, banner


class Publicar:
    def __init__(self, email, senha):
        self._headers = cabeca()
        self.sessao = log(email, senha)
        self.postar_grupo = postar()
        self._session = requests.Session()
        self._post = "/composer/mbasic/?av"
        self.url = 'https://free.facebook.com/'
        self.path = "/login/device-based/regular/login/"


    def login(self):
        ##############################################################################
        #       		Para entrar em cada grupo que fazis parte                    #
        # :param site: serve para entrar no própri site 							 #
        # :param entrar: serve para mandar as requisições e iniciar sessão			 #
        ##############################################################################
        try:
            site = self._session.get(self.url)
            tags = BeautifulSoup(site.text, "html.parser")
            self.sessao['lsd'] = tags.find("input", attrs={'name': 'lsd'})['value']
            self.sessao['jazoest'] = tags.find("input", attrs={'name': 'jazoest'})['value']
            self.sessao['m_ts'] = tags.find("input", attrs={'name': 'm_ts'})['value']
            self.sessao['li'] = tags.find("input", attrs={'name': 'li'})['value']
            self.sessao['try_number'] = tags.find("input", attrs={'name': 'try_number'})['value']
            self.sessao['unrecognized_tries'] = tags.find("input", attrs={'name': 'unrecognized_tries'})['value']
            self.sessao['bi_xrwh'] = tags.find("input", attrs={'name': 'bi_xrwh'})['value']
            ##############################################################################
            # 						Para entrar na suposta conta                         #
            ##############################################################################
        except:
            print('\033[31mERRO ao iniciar sessao!\033[m')
        else:
            entrar = self._session.post(url=self.url + self.path, headers=self._headers, data=self.sessao)
            sleep(3)
            conta_de = BeautifulSoup(entrar.text, 'html.parser')
            try:
                nome = conta_de.find('div', attrs={'class': 'bu bv bw'}).get_text()
            except (AttributeError):
                nome = conta_de.find('div', attrs={'class': 'bt bu bv'}).get_text()
            print('=='*25)
            try:
                print(f'Conta de: {nome}')
            except (UnboundLocalError):
                print("Não conseguimos pegar o nome!")
            sleep(3)

    def entrar_grupos(self):
        ##############################################################################
        #       		Para entrar em cada grupo que fazis parte                    #
        # :param tags: serve para pegar todos os grupos 							 #
        # :param lista: serve para guardar  nome de todos os grupos 				 #
        # :param url_grupo: serve para pegar o link de todos os grupos 				 #
        ##############################################################################
        self.lista = []
        
        try:
            url = self._session.get(url=self.url + 'groups/?seemore&refid', headers=self._headers)
            tags = BeautifulSoup(url.text, "html.parser")
            ##############################################################################
            #			"li.bx" serve para pegar o nome de todos os grupos               #
            ##############################################################################
            grupos = tags.find_all('li', attrs={'class': 'bx'})
        
        except:
            print('\033[31mERRO na coecção!\033[m')
        
        else:
            for grupo in grupos:
                url_grup = grupo.find('a')
                self.lista.append(url_grup.get('href'))
                sleep(0.5)

            print(f'Será publicado em: {len(self.lista)} GRUPOS')
            print('=='*25)

    def post_grupos(self):
        conta = 0
        for grupo in self.lista:
            conta += 1
            
            try:
                url = self._session.get(grupo, headers=self._headers)
                tags = BeautifulSoup(url.text, 'html.parser')
                self.postar_grupo['fb_dtsg'] = tags.find("input", attrs={'name': 'fb_dtsg'})['value']
                self.postar_grupo['jazoest'] = tags.find("input", attrs={'name': 'jazoest'})['value']
                self.postar_grupo['target'] = tags.find("input", attrs={'name': 'target'})['value']
                self.postar_grupo["c_src"] = tags.find("input", attrs={'name': "c_src"})['value']
                self.postar_grupo["cwevent"] = tags.find("input", attrs={'name': "cwevent"})['value']
                self.postar_grupo["referrer"] = tags.find("input", attrs={'name': "referrer"})['value']
                self.postar_grupo["ctype"] = tags.find("input", attrs={'name': "ctype"})['value']
                self.postar_grupo["cver"] = tags.find("input", attrs={'name': "cver"})['value']

            except:
                print(f'{conta}ª Não foi possivel!')
            else:
                
                self._session.post(self.url + self._post, headers=self._headers, data=self.postar_grupo)
                print(f'Postou no {conta}ª GRUPO')
                nome = f'grupo{conta}.html'
                #arq = open(nome, 'w')
                #arq.write(enviar.text)
            sleep(4)

system("cls || clear")
banner()
print('=='*25)
user = str(input('Email ou número de telefone: '))
senha = str(input('Digite a tua pelavra passe: '))
system('clear') | system('cls')
print('--'*25)
banner()
facebook = Publicar(user, senha)
facebook.login()
sleep(2)
facebook.entrar_grupos()
sleep(2)
facebook.post_grupos()
