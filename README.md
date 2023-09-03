# Flask-MongoDB-App
This code is for illustration to build dockerized Flask + MongoDB app.

<img src="https://img.shields.io/badge/Parag%20Pallav%20Singh-ED225D?style=for-the-badge&logo=pug&logoColor=C0FFF4"/>
<img src="https://img.shields.io/badge/Flask Mongo DB App-ffff33?style=for-the-badge&logo=docker"/>

## Tools used
<img src="https://img.shields.io/badge/Flask-000334?logo=flask"/> <img src="https://img.shields.io/badge/MongoDB-ffff33?logo=mongodb"/> <img src="https://img.shields.io/badge/Docker-B25F25?logo=docker"/>

# How to: Steps
1. Setup an EC2 instance
2. Clone this repository
```
git clone https://github.com/paragpallavsingh/Flask-MongoDB-App.git
cd Flask-MongoDB-App/
```
<kbd>![image](https://github.com/paragpallavsingh/Flask-MongoDB-App/assets/40052830/c3db2381-06da-4750-acdf-440f9d1b78d9)</kbd>

3. Install Docker and setup user permission
```
sudo apt install -y curl wget apt-transport-https
sudo apt install -y docker.io
sudo usermod -aG docker $USER && newgrp docker
```
<kbd>![image](https://github.com/paragpallavsingh/Flask-MongoDB-App/assets/40052830/9b363f7d-ef7c-427b-b65c-ae6f5bc5dc2e)</kbd>

4. Install Docker Compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```
5. Run Docker Compose
```
docker-compose up -d
```
<kbd>![image](https://github.com/paragpallavsingh/Flask-MongoDB-App/assets/40052830/cb807547-d43f-440a-9b63-666897737d22)</kbd>

## Sample Homepage Output
<kbd>![image](https://github.com/paragpallavsingh/Flask-MongoDB-App/assets/40052830/14a21035-c987-4901-aa17-3c95530ce39c)</kbd>

Here you can see the homepage of the app.

## Sample Tasks Output
<kbd>![image](https://github.com/paragpallavsingh/Flask-MongoDB-App/assets/40052830/2d1b08ea-835a-4e4d-a9a9-7251ad9c8716)</kbd>

Here, the app is showing the list of tasks from the database

Source: [Youtube](https://youtu.be/RuaKvPq0Fzo)

Special Credits: [@Namg04](https://www.linkedin.com/in/namratakumari04/)
