from mcrcon import MCRcon
import subprocess,time,socket

a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
location = ("127.0.0.1",25565)
result_of_check = a_socket.connect_ex(location)
if result_of_check == 0:
    a_socket.close()
    print("server gia\' avviato")
    time.sleep(5)
else:
    a_socket.close()
    print("server in avvio")
    processo = subprocess.Popen(["java","-jar","spigot-1.16.3.jar"],
                            stdout=subprocess.PIPE)
    for i in range(30):
        print(".", end='')
        time.sleep(1)

mcr = MCRcon("127.0.0.1","password")
mcr.connect()
resp ="Connessione"
print("\n"+resp)
while resp != "Stopping the server" or resp=="":
    comando = input('>')
    resp = mcr.command(comando)
    print(resp)
mcr.disconnect()