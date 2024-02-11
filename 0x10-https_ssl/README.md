# 0x10 https ssl
<img align="left" alt="C" style="padding-right;" src="ssl.gif">

<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>



## Setting up your SSL:
Note that you must know how to use these before you can start. Ensure that
Nginx has been installed in your primary server, secondary server, as well
as the load balancer (HAproxy) before you begin
- sudo apt update
- sudo apt install snapd
- sudo apt-get remove certbot
- sudo apt-get install certbot
- sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d example.com
- sudo ls /etc/letsencrypt/live/your_domain_name
- sudo mkdir -p /etc/haproxy/certs
- DOMAIN='example.com' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
- sudo chmod -R go-rwx /etc/haproxy/certs
- sudo nano /etc/haproxy/haproxy.cfg or sudo vim /etc/haproxy/haproxy.cfg

## Most common errors:
If the HAproxy fails to start, check the HAproxy's configuration (/etc/haproxy/haproxy.cfg)
-  before editing it, stop Nginx and HAproxy services
    -  stop Nginx in all the servers
    -  stop HAproxy in load balancer
