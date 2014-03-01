import base64


def encriptar(texto):
	print texto
	textocodificado = base64.encodestring(texto)
	return textocodificado;

matricula= raw_input("Dame la matricula")

temporal= encriptar(matricula)

print "Encriptado= ", temporal



"""
#!/usr/bin/env python
# coding utf-8
 
import getpass
import crypt
 
semilla = 'sl'
pass_unix = getpass.getpass()
 
def login_user(semilla,pass_unix):
    return crypt.crypt(semilla,pass_unix)
 
print login_user(semilla,pass_unix)"""