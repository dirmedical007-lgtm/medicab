#!/usr/bin/env bash
hostport="$1"
until nc -z $(echo $hostport | cut -d: -f1) $(echo $hostport | cut -d: -f2); do
  echo "En attente de $hostport..."
  sleep 2
done
