#!/bin/bash
sudo docker-compose down
git pull origin main
sudo docker-compose up -d
