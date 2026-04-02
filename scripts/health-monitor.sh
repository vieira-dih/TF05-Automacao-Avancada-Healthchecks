#!/bin/bash

STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/health)

if [ "$STATUS" -eq 200 ]; then
  echo "API saudável ✅"
else
  echo "ALERTA: API caiu ❌"
fi