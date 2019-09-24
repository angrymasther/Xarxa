# Xarxa-
 Busqueda de equipos:
  ping scan: Se hace ping a todas las direcciones IP en un rango definido por el usuario en una misma subred.
  ARP Scan: Se pregunta al broadcast si hay una MAC asociada a una dirección IP y si la hay, devuelve la dirección IP.
 Analisis de puertos:
  Socket scan: Abre una conexión socket con el puerto. Si se consigue considera que hay un servicio escuchando en ese puerto.
  Socket scan UDP: Igual que antes pero en UDP.
  FIN scan: Se envia un paquete TCP con la cabecera en FIN y el servidor envia un ack/rst para intentar reiniciar la conexión si existe               algún programa escuchando en ese puerto, si no, el servidor no envia ninguna respuesta.
  HalfSyn scan: Se inicia una conexión normal enviando un syn y si el servidor responde con un syn/ack, se envia un FIN para terminar la                    conexión.
Ataques:
  MitmDoS: Se hace un hombre en el medio entre la puerta de enlace y el objetivo y se desactiva el ip forwarding, haciendo que el objetivo            pueda acceder a internet.
  Mitm: Se interpone la conexión entre el servidor y la puerta de enlace, permitiendo ver y modificar en tiempo real los paquetes.
