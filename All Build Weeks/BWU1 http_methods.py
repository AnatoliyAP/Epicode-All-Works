import requests # Libreria contentente le richieste HTTP
#enumera i metodi HTTP, parametro è indirizzo di destinazione
def enumerare_metodi_http(url_destinazione):
    metodi = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'TRACE', 'PATCH'] #metodi HTTP
    
    for metodo in metodi:
        try:
            #per ogni metodo controlla il codice di stato
            risposta = requests.request(metodo, url_destinazione)
            #Se il codice di stato è 200
            if risposta.status_code == 200: #richiesta e metodo consentito
                print(f"Il metodo HTTP '{metodo}' è consentito")
            #Se il codice di stato è 405  
            elif risposta.status_code == 405: #richiesta e metodo non consentito
                print(f"Il metodo HTTP '{metodo}' non è consentito")
            #Se il codice non è 202 e 405
            else: #stampa il metodo ed il suo codice di stato
                print(f"Il metodo HTTP '{metodo}' - Codice di stato: {risposta.status_code}")
        #Se viene colta un'eccezione durante la richiesta
        except requests.exceptions.RequestException as e:
            print(f"Si è verificato un errore durante l'invio della richiesta con il metodo '{metodo}': {str(e)}")

while True: 
    #Chiede all'utente di inserire l'URL
    destinazione = input("Inserisci l'URL di destinazione (senza http://) o digita 'x' per uscire: ")
    #Possiamo digitare x o X per uscire dal programma
    if destinazione.lower() == 'x': 
    #esce dal loop
        break
    #chiama la funzione inserendo http://
    url_destinazione = f"http://{destinazione}"
    enumerare_metodi_http(url_destinazione)