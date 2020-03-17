# haaukins_crack_cipher

**Description**

This cipher crack CTF challenge was created for Haaukins platform. The main goal of the project is decrypting cipher text which is provided in .pcapng file by bruteforce attack and getting the username and password information to login the website. In this project, an Apache2 server created and website is published on the server. PHP is used for back-end of the website. This application is containerized with Docker. 

**Prerequisite**

- Docker
- Wireshark
- Basic understanding of RSA cryptology
- Basic understanding of analyzing network traffic

**How to Run?**

1- git clone https://github.com/lambdavary/haaukins_crack_cipher.git

2- cd haaukins_crack_cipher/

3- docker build -t haaukins_crack_cipher .

4- docker run -d -p 80:80 -e FLAG="FLAG=I thought that I saw a pretty cat. Yes, I did I did!" haaukins_crack_cipher

5- Browse localhost:80/

**Solution**
