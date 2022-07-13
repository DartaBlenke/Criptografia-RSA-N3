import random as rd

def mdc(n1, n2):
    while(n2 != 0):
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1


def public_key(n):
    while True:
        e = rd.randrange(2, n)
        if(mdc(n, e) == 1):
            return e

def private_key(totiente, e):
    d = 0
    while((d * e) % totiente != 1):
        d += 1
    return d


def encode(message, e, n):
    encoded_msg = ""
    for letter in message:
        k = (ord(letter) ** e) % n
        encoded_msg += chr(k)
    return encoded_msg

file = open("mensagem.txt", "r")
line = file.readlines()
for msg in line:
    print(msg)

# file = open("encrypted.txt", "w+")
# for line in encryptedMsg:
#     file.write(line)

def rsa():
  message = msg
  p = 23
  q = 29
  n = p * q
  y = p - 1
  x = q - 1
  totiente = x * y
  e = public_key(totiente)

  print(f"Chave Publica: ({n},{e})")

  d = private_key(totiente, e)
  print(f"Chave Privada: ({n},{d})")

  encrypted = encode(message, e, n)
  print("Mensagem Encoded: " + encrypted)
  return encrypted

encryptedMsg = rsa()

print(encryptedMsg)

encryptedMsg = open("encrypted.txt", "w+")
for line in encryptedMsg:
    file.write(line)
