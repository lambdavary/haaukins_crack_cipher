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

1- Analyzing the network_traffic.pcapng with Wireshark

2- Investigating the POST request

3- There is a POST request which contains "username=1874&pub_rsa=10&password=1874". This line means that the username and password fields are encrypted with RSA by using "Public Key" which value is "10" and their values are "1874"

4- Write a code for decrypting username and password. In this step, bruteforce approach can be used which is using numbers between 1 to 10 for "Private key".

5- Using all possible username password pairs to login the system. In this step, POST requests which includes username and password pairs are generated by "curl". By analyzing the output of the POST request we obtain the decryption key and the FLAG.

Solution video: https://youtu.be/Zf25ernqIS4
