#!/bin/bash
echo "Prueba automática de la API"
curl -i http://localhost:8080/api/status
curl -i http://localhost:8080/api/ping
curl -i http://localhost:8080/api/items
