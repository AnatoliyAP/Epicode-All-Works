import socket
import ipaddress

while True:
    try:
        #chiede all'utente l'indirizzo IP
        target = input("Inserisci l'indirizzo IP: ")
        #Valida indirizzo IP
        ipaddress.ip_address(target)
        break
    except ValueError:
        print("Indirizzo IP non valido.")

while True:
    try:
        #chiede all'utente il range delle porte
        portrange = input("Inserisci il range delle porte (0-65535): ")
        #estrae low e highport
        lowport, highport = map(int, portrange.split("-"))
        #controlla che il range sia valido
        if not (0 <= lowport <= highport <= 65535):
            raise ValueError
        break
    except ValueError:
        print("Range porte non valido.")

#stampa IP e range porte
print('Scanning host', target, 'from port', lowport, 'to port', highport)
#itera ogni porta nel range
for port in range(lowport, highport + 1):
    #crea socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #controlla connessione tra IP e port
    status = s.connect_ex((target, port))
    #se lo stato e 0
    if status == 0:
        #stampa porta aperta
        print('*** Port', port, '- OPEN ***')
   #else:
       #print('Port', port, '- CLOSED') #porta chiusa
    #chiude il socket
    s.close()
