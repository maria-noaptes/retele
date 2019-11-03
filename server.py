from packets import *
import socket
import pickle
parola='1234'


with open("in.txt") as f:
    chei=f.readlines()
chei = [x.strip() for x in chei]

topics = dict.fromkeys(chei, 0)
print(topics)


# Creaza un socket IPv4, TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Asociere la adresa locala, portul 5000
s.bind(('127.0.0.1', 5000))
# Coada de asteptare pentru conexiuni de lungime 1

s.listen(1)
print('2')
# Asteapta conexiuni
print('Asteapta conexiuni')
conn, addr = s.accept()
print ('S-a conectat clientul', addr, ' la serverul ', conn.getsockname())
while 1:
    # Asteapta data, buffer de 1024 octeti
    data_b = conn.recv(1024)
    data=pickle.loads(data_b)
    if type(data) is CONNECT :
        if data.parola == parola:
            c = CONNACK(1)
            c_b = pickle.dumps(c)
            conn.send(c_b)
        else:
            c = CONNACK(128)
            c_b = pickle.dumps(c)
            conn.send(c_b)
    elif type(data) is PUBLISH:
            topics[data.topic]=data.payload
            print(topics)

    elif type(data) is SUBSCRIBE:
            if data.subscriptii in chei:
                pSUBPACK=SUBPACK(data.packetID,0)
                pSUBPACK_b=pickle.dumps(pSUBPACK)
                conn.send(pSUBPACK_b)
                print(str(data.subscriptii))
                print(topics[str(data.subscriptii)])
                if topics[str(data.subscriptii)]!=0:
                    data_b_payload=pickle.dumps(data.subscriptii)
                    conn.send(data_b_payload)
                else:
                    mesaj='Nu exista  mesaje in cadrul topicului'
                    mesaj_b=pickle.dumps(mesaj)
                    conn.send(mesaj_b)
            else:
                pSUBPACK = SUBPACK(data.packetID,128)
                pSUBPACK_b = pickle.dumps(pSUBPACK)
                conn.send(pSUBPACK_b)

    # Daca functia recv returneaza None, clientul a inchis conexiunea
    #if not data:
   #     break
   # print ('Am receptionat: ', data)
    # Trimite datele receptionate
    #conn.sendall(data)
    #conn.close()
t