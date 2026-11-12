

import numpy as np
# DNA baser
BASES = ["A", "T", "C", "G"]
def get_random_sequence(n, seed = None):
"""
Returnerar en slumpmässig DNA-sekvens med längden n.
Parameters
----------
n : int
Sekvensens längd.
seed : int, optional
Slumpfrö som kan användas för reproducerbara resultat.
Returns
-------
str
En slumpmässig DNA-sekvens.
"""
np.random.seed(seed)
rand_ids = np.random.randint(0,4,int(n))
seq = ''.join([BASES[idx] for idx in rand_ids])
return seq
def dna_shift_encrypt(seq, key):
"""
Returnerar en krypterad DNA-sträng genom att skifta baserna med key steg.
Parameters
----------
seq : str
Okrypterad DNA-sekvens
key : int
Antalet steg DNA-baserna skiftas
Returns
-------
str
Den krypterade DNA-sekvensen
"""
# Ta bort raden nedan och skriv din kod här
raise NotImplementedError("Implementera funktionen dna_shift_encrypt")
def dna_shift_decrypt(encrypt_seq, key):
"""
Returnerar en dekrypterad DNA-sträng som har krypterats genom att skifta
baserna med key steg.
Parameters
----------
encrypt_seq : str
Krypterad DNA-sekvens
key : int
Antalet steg DNA-baserna skiftas
Returns
-------
str
Den okrypterade DNA-sekvensen
"""
# Ta bort raden nedan och skriv din kod här
raise NotImplementedError("Implementera funktionen dna_shift_decrypt")
def dna_substitution_encrypt(seq, key_word):
"""
Returnerar en krypterad DNA-sträng genom substitution baserad på key_word.
Parameters
----------
seq : str
Okrypterad DNA-sekvens
key_word : str
Nyckelord som definierar substutitionen
Returns
-------
str
Den krypterade DNA-sekvensen
"""
# Ta bort raden nedan och skriv din kod här
raise NotImplementedError("Implementera funktionen dna_substitution_encrypt")
def dna_substitution_decrypt(encrypt_seq, key_word):
"""
Returnerar en dekrypterad DNA-sträng som har krypterats genom substitution
baserad på key_word.
Parameters
----------
encrypt_seq : str
Krypterad DNA-sekvens
key_word : str
Nyckelord som definierar substutitionen
Returns
-------
str
Den okrypterade DNA-sekvensen
"""
# Ta bort raden nedan och skriv din kod här
raise NotImplementedError("Implementera funktionen dna_substitution_decrypt")
def dna_checksum(seq):
"""
Returnerar en kontrollsumma baserad på en DNA-sekvens definierad som 1*antal_A
+ 2*antal_T + 3*antal_C + 4*antal_G.
Parameters
----------
seq : str
DNA-sekvens
Returns
-------
int
Kontrolsumman
"""
# Ta bort raden nedan och skriv din kod här
raise NotImplementedError("Implementera funktionen dna_checksum")
