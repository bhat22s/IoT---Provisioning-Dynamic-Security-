# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 15:35:38 2021

@author: emily
"""

import time 
import sys 
import random
import binascii
import trivium 

def bytes_to_hex(b):
    return b.hex()

def demo_print(data):
    maxlen = max([len(text) for (text, val) in data])
    for text, val in data:
        print("{text}:{align} 0x{val} ({length} bytes)".format(text=text, align=((maxlen - len(text)) * " "), val=bytes_to_hex(val), length=len(val)))

def E_and_db(KEY, IV, message):
    t1 = trivium.Trivium(KEY, IV)
    t2 =trivium.Trivium(KEY, IV)
    
    start1 = time.time()
    encryptb = t1.encrypt(message,"b")
    end1 = time.time()
    #print("Encryption1b message: " + encryptm1b)
    start2 = time.time()
    decryptb = t2.decrypt(encryptb)
    end2 = time.time()
    #print("Decryption1b message: " + decryptm1b)
    
    key_str = ""
    for i in KEY:
        key_str += str(i)
        
    demo_print([("plaintext", message.encode("utf-8")),
                ("ciphertext", encryptb.encode("utf-8"))
               ])
    
    print("Encryption1b time:" + str(end1 - start1))
    print("Decryption1b time:" + str(end2 - start2))
    
def E_and_dh(KEY, IV, message):
    t1 = trivium.Trivium(KEY, IV)
    t2 =trivium.Trivium(KEY, IV)
    
    start1 = time.time()
    encrypth = t1.encrypt(message,"b")
    end1 = time.time()
    #print("Encryption1b message: " + encryptm1b)
    start2 = time.time()
    decrypth = t2.decrypt(encrypth)
    end2 = time.time()
    #print("Decryption1b message: " + decryptm1b)
    
    key_str = ""
    for i in KEY:
        key_str += str(i)
        
    demo_print([("plaintext", message.encode("utf-8")),
                ("ciphertext", encrypth.encode("utf-8")),
               ])
    
    print("Encryption1b time:" + str(end1 - start1))
    print("Decryption1b time:" + str(end2 - start2))

def main():
    message1 = "liaqbpxxlhqvboaywjxjnqnbaoqaomhl"
    message2 = "licfumnlvebfmdpfjdacztrcjnqcuhvlhxwljkmiebirzfpafoployzyfgbgmncseepivjirpuivhxzfcghrfistfgedpdvzksmnrwmfxkfhhpafmxcrxrvmewcosoedidwwasgkiihkyxzsevhizwk"
    message3 = "rzzcybfdyyammaailezszamvkhegazdybtysgnweamjrcutfbihwmarifazgpfpxwsjjpxgovaidiyxfjdndevbytwgkxohbgvibiguqourqrvpdpybjyrubdnmecmlfqlmhiunzxjzxzixxqhpaychkalxykghrlwgzhkegqsmzprgwhzfbrbzienzyqgeejgvuoogelmtfiwxjhyyptmxvgusqptyxvlreeyhinmifjbgcjixckvmsxhwlnwddxvgtutvjewpsqfnlxxnkptxvixwgtmhiviyhoasqxfkdwfvoemlxzxzxzgaefrnmmrwyfrhsiwnkknvhfrjcdyvzlbgdbaxbwngdfrhdpscalgtfizfksesosszpyeolznhtbgcuuhpcudwfouazcncffwiofvratbhqsxpdhymtghrgupbkvtxhohefuifldxybldfsxwjyswallmsozuampiuaoxwnjhyghwgcjjiujhfrrnmgclqmonbcuaqtnfkxcldsaqnpfkztbhmmredvxkubgtrpxlgwqwavuvdbxucfwwrtlakxtvcsyodfsuirlwsqhfltaumfeastifmh" 

    # choose a cryptographically strong random key and a nonce that never repeats for the same key:
    og_key = str(random.randint(10000, 1000000))
    og_iv = "8"
    
    # associateddata = b"Hello World"
    # plaintext      = b"Hello World"
    key_hex = binascii.hexlify(og_key.encode('utf-8')).decode('utf-8').upper()
    iv_hex =  binascii.hexlify(og_iv.encode('utf-8')).decode('utf-8').upper()
    
    KEY = trivium.hex_to_bits(key_hex)[::-1]
    IV = trivium.hex_to_bits(iv_hex)[::-1]
    
    if len(KEY) < 80:
        for k in range (80-len(KEY)):
            KEY.append(0)
    if len(IV) < 80:
        for i in range (80-len(IV)):
            IV.append(0)
            
    if len(KEY) > 81 or len(IV) > 81:
        print("wrong size")
        sys.exit()
	
    
    E_and_db(KEY, IV, message1)
    E_and_dh(KEY, IV, message1)
    
    E_and_db(KEY, IV, message2)
    E_and_dh(KEY, IV, message2)
    
    E_and_db(KEY, IV, message3)
    E_and_dh(KEY, IV, message3)
	
    
    
    
    """
    start = time.time()
    encryptm1b = t1.encrypt(message1,"b")
    end = time.time()
    #print("Encryption1b message: " + encryptm1b)
    print("Encryption1b time:" + str(end - start))
    start = time.time()
    decryptm1b = t2.decrypt(encryptm1b)
    end = time.time()
    #print("Decryption1b message: " + decryptm1b)
    print("Decryption1b time:" + str(end - start))
    
    start = time.time()
    encryptm1h = t1.encrypt(message1, "h")
    end = time.time()
    #print("Encryption1h message: " + encryptm1h)
    print("Encryption1h time: " + str(end - start))
    start = time.time()
    decryptm1h = t2.decrypt(encryptm1h)
    end = time.time()
    #print("Decryption1h message: " + decryptm1h)
    print("Decryption1h time: " + str(end - start))
    
    print("----------------------")
    
    
    start = time.time()
    encryptm2b = t1.encrypt(message2,"b")
    end = time.time()
    #print("Encryption2b message: " + encryptm2b)
    print("Encryption2b time: " + str(end - start))
    start = time.time()
    decryptm2b = t2.decrypt(encryptm2b)
    end = time.time()
    #print("Decryption2b message: " + decryptm2b)
    print("Decryption2b time: " + str(end - start))
  
    start = time.time()
    encryptm2h = t1.encrypt(message2, "h")
    end = time.time()
    #print("Encryption2h message: " + encryptm2h)
    print("Encryption2h time: " + str(end - start))
    start = time.time()
    decryptm2h = t2.decrypt(encryptm2h)
    end = time.time()
    #print("Decryption2h message: " + decryptm2h)
    print("Decryption2h time: " + str(end - start))
    
    print("----------------------")
    
    start = time.time()
    encryptm3b = t1.encrypt(message3,"b")
    end = time.time()
    #print("Encryption3b message: " + encryptm3b)
    print("Encryption3b: " + str(end - start))
    start = time.time()
    decryptm3b = t2.decrypt(encryptm3b)
    end = time.time()
    #print("Decryption3b message: " + decryptm3b)
    print("Decryption3b time: " + str(end - start))
    
    start = time.time()
    encryptm3h = t1.encrypt(message3, "h")
    end = time.time()
    #print("Encryption3h message: " + encryptm3h)
    print("Encryption3h time: " + str(end - start))
    start = time.time()
    decryptm3h = t2.decrypt(encryptm3h)
    end = time.time()
    #print("Decryption3h message: " + decryptm3h)
    print("Decryption3h time: " + str(end - start))
    """
    
if __name__ == "__main__":
    main()
