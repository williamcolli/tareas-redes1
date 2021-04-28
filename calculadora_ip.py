import ipaddress

Id_Red=input("ingrese la direccion y la mascara:")
ip=ipaddress.IPv4Network(Id_Red)
print("la mascara de subred es:", ip.netmask)
print("la mascara wildcard es:", ip.hostmask)
print("la primera  direccion valida o usable es:", ip.network_address+1)
print("la ultima direccion valida o usable es:", ip.broadcast_address-1)
print("la direccion de broadcast es:", ip.broadcast_address)
print("es una direccion privada:", ip.is_private)
print("total de direcciones ip validas o usables:", ip.num_addresses-2)
q=input("quieres conocer cuales son las ip validas:")
if q== 'si' or q=='si' or q=='si':
        
    for h in ip.hosts():
        print(h)
       
