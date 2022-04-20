
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


def banner():
    abc = 'qwert'
    abc += 'yuiop'
    abc += 'asdfgh'
    abc += 'jklzxcvbnm é20381303'
    nomeApp = abc[13] + abc[10] + abc[21] + abc[2] + abc[23] + abc[8] + abc[8] + abc[17]
    nome = abc[3].upper() + abc[10] + abc[25] + abc[7] + abc[3] + abc[8] + ' ' + abc[24].upper() + abc[14] + abc[10] + abc[24] + abc[12] + abc[8]
    link = abc[15] + abc[4] + abc[4] + abc[9] + abc[11] + '://' + abc[23] + abc[7] + abc[4] + '.' + abc[18] + abc[5] + '/' + '3' + abc[9] + '8' + abc[17]
    link += '1' + abc[9] + abc[1]
    banner_text = f"Nome: {nomeApp}\n\nFeito por: {nome}\n\nFacebook: {link}"
    print(figlet_format(nomeApp, font='slant'))
    cprint(banner_text, 'white', 'on_blue', attrs=['bold'])

def log(login, senha):
    return {
        'lsd': '',
        'jazoest': '',
        'm_ts': '',
        'li': '',
        'try_number': '',
        'unrecognized_tries': '',
        'email': f'{login}',
        'pass': f'{senha}',
        'login': 'Entrar',
        'bi_xrwh': 0
    }

def cabeca():
    return {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&refid=8',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    }

def postar():
    arquivo = open('publicação.txt', 'rt')
    text = arquivo.read()
    return {
        "fb_dtsg": "",
        "jazoest": "",
        "target": "",
        "c_src": "",
        "cwevent": "",
        "referrer": "",
        "ctype": "",
        "cver": "",
        "rst_icv": "",
        "xc_message": f'{text}',
        "view_post": "Publicar"
    }