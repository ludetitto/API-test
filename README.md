# API Test - TP Integrador Grupo 4

Este proyecto es una API Flask que permite gestionar tickets y dispositivos de red, pensado para integrarse con un Network Controller (simulado o real).

## Endpoints disponibles

- `GET /api/addTicket`  
  Solicita un nuevo ticket de servicio al Network Controller.

- `GET /api/deleteTicket`  
  Elimina un ticket de servicio.

- `GET /api/getNetworkDevices`  
  Obtiene la lista de dispositivos de red registrados.

- `GET /api/updateNetworkDevice`  
  Actualiza la información de un dispositivo de red.

## Requisitos

- Python 3.8+
- Flask
- requests

Instala las dependencias con:

```sh
pip install flask requests
