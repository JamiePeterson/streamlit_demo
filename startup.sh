#!/bin/bash
mkdir -p /home/site/wwwroot
cp -r * /home/site/wwwroot
cd /home/site/wwwroot
streamlit run traffic_accidents.py --server.port=8000 --server.address=0.0.0.0
