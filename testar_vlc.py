# Tentando portas alternativas que cameras Anyka costumam liberar
ID = "CFEO-945311-LDUZR"
IP = "192.168.100.100"

print("--- TENTE ESTES LINKS NO VLC ---")
print(f"Opcao 1 (Padrao): rtsp://admin:admin@{IP}:554/live/ch0")
print(f"Opcao 2 (Porta 8080): rtsp://admin:admin@{IP}:8080/live/ch0")
print(f"Opcao 3 (HTTP): http://{IP}:80/livestream/11.m3u8")
print("-------------------------------")
