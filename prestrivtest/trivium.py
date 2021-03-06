#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trivium-lab2-cenfotec.py
#  
#  Copyright 2016 Johnny Pan <codeskill@gmail.com>
#  Copyright 2016 Mario Zamora <mortasoftgmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from collections import deque
from itertools import repeat
from sys import version_info
import unicodedata
import subprocess
import codecs
import binascii

# Funciones globales de conversion HEX2BYTES, HEX2BITS y BITS2HEX
# Convert strings of hex to strings of bytes and back, little-endian style
_allbytes = dict([("%02X" % i, i) for i in range(256)])


def _hex_to_bytes(s):
    return [_allbytes[s[i:i+2].upper()] for i in range(0, len(s), 2)]


def hex_to_bits(s):
    return [(b >> i) & 1 for b in _hex_to_bytes(s)
            for i in range(8)]


def bits_to_hex(b):
    return "".join(["%02X" % sum([b[i + j] << j for j in range(8)])
                    for i in range(0, len(b), 8)])


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[33m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Trivium:
    def __init__(self, key, iv):
        """in the beginning we need to transform the key as well as the IV.
        Afterwards we initialize the state."""
        self.state = None
        self.counter = 0
        self.key = key  # self._setLength(key)
        self.iv = iv  # self._setLength(iv)
        
        # Initialize state
        # len 100
        init_list = list(map(int, list(self.key)))
        init_list += list(repeat(0, 20))
        # len 84
        init_list += list(map(int, list(self.iv)))
        init_list += list(repeat(0, 4))
        # len 111
        init_list += list(repeat(0, 108))
        init_list += list([1, 1, 1])
        self.state = deque(init_list)

		# Se realizan 4 corridas y se descarta su salida
        # Do 4 full cycles, drop output
        for i in range(4*288):
            self._gen_keystream()

	#=========================================================
	# Metodo para encriptar, recibe el mensaje en texto plano
    #=========================================================
    def encrypt(self, message, output):
        plaintext = remove_accents(message).upper()
        plaintext_hex = binascii.hexlify(plaintext.encode('utf-8')).decode('utf-8').upper()
        plaintext_bin = hex_to_bits(plaintext_hex)
		# Imprime mensaje en bits
		# print "Plaintext="+str(plaintext_bin)
		# Imprime cantidad de items del mensaje en bits
		# print "Tama??o de plaintext="+str(range(len(plaintext_bin)))
        ciphertext = []
        for i in range(len(plaintext_bin)):
            ciphertext.append(self._gen_keystream() ^ plaintext_bin[i])

		# Imprime texto cifrado en bits
		# print "Texto cifrado"+str(ciphertext)		
		# Imprime texto cifrado en hexadecimal
		# print(bits_to_hex(ciphertext))
        if output == 'b' or output == 'B':
			# Retorna texto cifrado en bits
            return ''.join(map(str,ciphertext))
        else:
			# Retorn texto cifrado en hexadecimal
            return bits_to_hex(ciphertext)

	#==========================================================
    # Metodo para desencriptar, recibe el texto en hexadecimal o bits
    #==========================================================
    def decrypt(self, cipher):
        ciphertext_bin = []
        plaintext_bin = []
        if (any(c.isalpha() for c in cipher)):
            ciphertext_bin = hex_to_bits(cipher)
            for i in range(len(ciphertext_bin)):
                plaintext_bin.append(self._gen_keystream() ^ ciphertext_bin[i])
        else:
            ciphertext_bin = list(str(cipher))
            for i in range(len(ciphertext_bin)):
                plaintext_bin.append(self._gen_keystream() ^ int(ciphertext_bin[i]))
                
        plaintext_hex = bits_to_hex(plaintext_bin)
        plaintext = binascii.unhexlify(plaintext_hex.encode('utf-8')).decode('utf-8')
        return plaintext

    def keystream(self):
        """output keystream
        only use this when you know what you are doing!!"""
        while self.counter < 2**64:
            self.counter += 1
            yield self._gen_keystream()

    def _setLength(self, input_data):
        """we cut off after 80 bits, alternatively we pad these with zeros."""
        input_data = "{0:080b}".format(input_data)
        if len(input_data) > 80:
            input_data = input_data[:(len(input_data)-81):-1]
        else:
            input_data = input_data[::-1]
        return input_data
	
	#====================================
	# Metodo para generar los keystreams
	#====================================
    def _gen_keystream(self):
        """this method generates triviums keystream"""

        a_1 = self.state[90] & self.state[91]
        a_2 = self.state[181] & self.state[182]
        a_3 = self.state[292] & self.state[293]

        t_1 = self.state[65] ^ self.state[92]
        t_2 = self.state[168] ^ self.state[183]
        t_3 = self.state[249] ^ self.state[294]

        out = t_1 ^ t_2 ^ t_3

        s_1 = a_1 ^ self.state[177] ^ t_1
        s_2 = a_2 ^ self.state[270] ^ t_2
        s_3 = a_3 ^ self.state[68] ^ t_3

        self.state.rotate(1)

        self.state[0] = s_3
        self.state[100] = s_1
        self.state[184] = s_2

        return out

def remove_accents(input_str):
	input_str = input_str.replace(u"\u2018", "\"").replace(u"\u2019", "\"").replace(u"\u201c","\"").replace(u"\u201d", "\"")
	nkfd_form = unicodedata.normalize('NFKD', str(input_str))
	return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

def main():
	# Limpia la pantalla
	cmd = subprocess.call('cls', shell = True)
	print(cmd)
	print(color.OKBLUE)
	print ('+-----------------------------------------------+')
	print ('| MSEG-02 - PRINCIPIOS DE CRIPTOGRAFIA          |')
	print ('| LABORATORIO DE TRIVIUM                        |')
	print ('| JOHNNY.PAN | ESTEBAN.CASTILLO | MARIO.ZAMORA  |')
	print ('+-----------------------------------------------+')
	print(color.ENDC)

	# Se ingresa el mensaje en texto plano o cifrado
	print(color.OKYELLOW + 'TYPE THE MESSAGE (PLAIN TEXT OR CIPHER TEXT)' + color.ENDC)
	mensaje = input()
	print
	# Se ingresa la llave
	print(color.OKYELLOW + 'TYPE THE KEY' + color.ENDC)
	llave = input()
	print
	# Se ingresa el vector de inicializacion
	print(color.OKYELLOW + 'TYPE THE INITIALIZATION VECTOR' + color.ENDC)
	vector_inicializacion = input()

	# Se codifican las variables ingresadas
	key_hex = binascii.hexlify(llave.encode('utf-8')).decode('utf-8').upper()
	iv_hex =  binascii.hexlify(vector_inicializacion.encode('utf-8')).decode('utf-8').upper()
	# Se pasan las variables de hexadecimal a bits
	KEY = hex_to_bits(key_hex)[::-1]
	IV = hex_to_bits(iv_hex)[::-1]
	# Si es mejor de 80 bits se completa con ceros
	if len(KEY) < 80:
		for k in range (80-len(KEY)):
			KEY.append(0)
	if len(IV) < 80:
		for i in range (80-len(IV)):
			IV.append(0)
	
	# Se crea el objeto Trivium
	trivium = Trivium(KEY, IV)
    

	# Pregunta si se desea encriptar o desencriptar el mensaje
	print(color.OKYELLOW)
	opcion = input('SELECTION [E] ENCRYPTION | [D] DECRYPTION: ')
	print(color.ENDC)
	if opcion == 'e' or opcion == 'E':
		print(color.OKYELLOW)
		salida = input('ENCRYPTION OUTPUT FORMAT [B] BINARY | [H] HEXADECIMAL: ')
		print(color.ENDC)
		if salida == 'b' or salida == 'B' or salida == 'h' or salida == 'H':
			print(color.BOLD + 'MESSAGE ENCRYPTED' + color.ENDC)
			print(color.OKGREEN)
			print(trivium.encrypt(mensaje,salida))
			print(color.ENDC)
		else:
			main()
	elif opcion == 'd' or opcion == 'D':
			print(color.BOLD + 'MESSAGE DECRYPTED' + color.ENDC)
			print(color.OKGREEN)
			print(trivium.decrypt(mensaje))
			print(color.ENDC)
	else:
		main()

if __name__ == "__main__":
    main()
	
