#!/bin/sh

SERVER_URL="http://server:8080/"

echo "Iniciando cliente. Enviando requisições periódicas para ${SERVER_URL}..."
echo "Pressione Ctrl+C para parar os logs (no host)."

while true; do
  echo "---- $(date) ----"
  curl -s "${SERVER_URL}" || echo "Falha ao conectar ao servidor."
  echo ""
  sleep 5
done
