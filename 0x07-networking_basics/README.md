# 0x07. Networking basics #0
<img src="OSI Model.png">

## OSI Model
-  What it is
-  How many layers it has
-  How it is organized

## What is a LAN
-  Typical usage
-  Typical geographical size

<img src="OSI model_2.gif">

## What is a WAN
-  Typical usage
-  Typical geographical size

## What is the Internet
-  What is an IP address
-  What are the 2 types of IP address
-  What is localhost
-  What is a subnet
-  Why IPv6 was created

## TCP/UDP
-  What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
-  What is the main difference between TCP and UDP
-  What is a port
-  Memorize SSH, HTTP and HTTPS port numbers
-  What tool/protocol is often used to check if a device is connected to a network
<img src="OSI model_2-2.gif">


## More Info
The second line of all your Bash scripts should be a comment explaining what is the script doing

For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer,
example:</br>
What is the most important position in a software company?

    1. Project manager
    2. Backend developer
    3. System administrator
<br></br>

    sylvain@ubuntu$ cat foo_answer_file
    3
    sylvain@ubuntu$

Source for question 1 here (https://twitter.com/devopsreact/status/831922429215662080)

# Tasks
## 0. OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate
the different parts of what make communication possible.

It is organized from the lowest level to the highest level:
-  The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
-  The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It
is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists
in all communications systems.

In this project we will mainly focus on:
-  The Transport layer and especially TCP/UDP
-  On the Network layer with IP and ICMP
-  The image bellow describes more concretely how you can relate to every level.

Questions:

### What is the OSI model?
    1. Set of specifications that network hardware manufacturers must respect
    2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their
    underlying internal structure and technology
    3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their
    underlying internal structure and technology

### How is the OSI model organized?
    1. Alphabetically
    2. From the lowest to the highest level
    3. Randomly

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x07-networking_basics
    File: 0-OSI_model


## 1. Types of network
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

### What type of network a computer in local is connected to?
    1. Internet
    2. WAN
    3. LAN

### What type of network could connect an office in one building to another office in a building a few streets away?
    1. Internet
    2. WAN
    3. LAN

### What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?
    1. Internet
    2. WAN
    3. LAN

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x07-networking_basics
    File: 1-types_of_network


## 2. MAC and IP address
mandatory

Questions:

### What is a MAC address?
    1. The name of a network interface
    2. The unique identifier of a network interface
    3. A network interface

### What is an IP address?
    1. Is to devices connected to a network what postal address is to houses (There was a typo on this. I simply Ctrl+V'ed)
    2. The unique identifier of a network interface
    3. Is a number that network devices use to connect to networks

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x07-networking_basics
    File: 2-MAC_and_IP_address
    

## 3. UDP and TCP
mandatory

<img src="task-3_0x07-networking-basics.jpg">

Let’s fill the empty parts in the drawing above.

Questions:

### Which statement is correct for the TCP box:
    1. It is a protocol that is transferring data in a slow way but surely
    2. It is a protocol that is transferring data in a fast way and might loss data along in the process

### Which statement is correct for the UDP box:
    1. It is a protocol that is transferring data in a slow way but surely
    2. It is a protocol that is transferring data in a fast way and might loss data along in the process

### Which statement is correct for the TCP worker:
    1. Have you received boxes x, y, z?
    2. May I increase the rate at which I am sending you boxes?

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x07-networking_basics
    File: 3-UDP_and_TCP
    

## 4. TCP and UDP ports
mandatory

Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually
enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like
the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage,
some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:
-  22 for SSH
-  80 for HTTP
-  443 for HTTPS
Note that a specific IP + port = socket.

Write a Bash script that displays listening ports:
-  That only shows listening sockets
-  That shows the PID and name of the program to which each socket belongs

### Tests
-  ./4-TCP_and_UDP_ports

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x07-networking_basics
    File: 4-TCP_and_UDP_ports
    

## 5. Is the host on the network
mandatory

The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other
network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot
issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:
-  Accepts a string as an argument
-  Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
-  Ping the IP 5 times

### Tests
-  ./5-is_the_host_on_the_network 8.8.8.8
-  ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
 
It is interesting to look at the time value, which is the time that it took for the ICMP request to go to the 8.8.8.8 IP and come back to my host.
The IP 8.8.8.8 is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that
the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the ping command to see what is going on!

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x07-networking_basics
    File: 5-is_the_host_on_the_network

<br></br>
## Illustration that summarises the OSI model in networking
<br></br>
<img src="OSI model.gif">


