import string
from collections import Counter

'cifrar mensagem com dada chave'
def cipher(key, message): 
    len_key = len(key)
    cipher = ""
    key = key.lower()
    INICIAL = "a"
    pos = 0
    for letter in message:
        if letter in string.ascii_letters:
            x = (ord(letter.lower()) + ord(key[pos % len_key]) - 2 * ord(INICIAL)) % 26
            x += ord(INICIAL)
            carac = chr(x)
            if letter.isupper():
                carac = carac.upper()
            cipher += carac
            pos += 1
        else:
            cipher += letter
    print(cipher)

'decifrar mensagem com senha'
def decipher(key, message):
    len_key = len(key)
    cipher = ""
    key = key.lower()
    INICIAL = "a"
    FINAL = "z"
    pos = 0
    for letter in message:
        if letter in string.ascii_letters:
            x = (ord(letter.lower()) - ord(key[pos % len_key]))
            if x >=0:
                x += ord(INICIAL)
            else:
                x += ord(FINAL) + 1
            carac = chr(x)
            if letter.isupper():
                carac = carac.upper()
            cipher += carac
            pos += 1
        else:
            cipher += letter
    print(cipher)
    
'descobir tamanho de chave para cifra sem senha conhecida'
def get_key_length(text):
    positions = {} #posição da última sequência de um tipo encontrada
    distances = [] #todas as distâncias entre sequências repetidas
    for i in range(2,len(text)):
        seq3 = text[i-2:i+1]
        if seq3 in positions:
            distances.append(i - positions[seq3])
        positions[seq3] = i
    divisors = {}
    for distance in distances:
        for i in range(2,21): #todos os divisores de cada distância <= 20
            if distance % i == 0:
                if i not in divisors:
                    divisors[i] = 1
                else:
                    divisors[i] += 1
    print("Frequências dos fatores dos trios de letras: \n")
    
    fats = ""
    i = 1
    for valor, fat in sorted(divisors.items(), key=lambda x:x[1], reverse=True):
        fats += f"{valor}: {fat}"
        if (i % 7 != 0):
           fats += " "*6
        else:
           fats += "\n"
        i += 1
    print(fats)

    key_length = int(input("Informe o tamanho da chave que deseja tentar: "))
    return key_length

'Descoberta da senha a partir do seu tamanho'
def attack(cipher):
    found = False
    FREQ_PT = {'a':14.63,'b':1.04,'c':3.88,'d':4.99,'e':12.57,'f':1.02,'g':1.30,'h':1.28,'i':6.18,
        'j':0.40,'k':0.02,'l':2.78,'m':4.74,'n':5.05,'o':10.73,'p':2.52,'q':1.20,'r':6.53,'s':7.81,'t':4.34,'u':4.63,'v':1.67,'w':0.01,'x':0.21,'y':0.01,'z':0.47}
    FREQ_EN = {'a':8.167,'b':1.492,'c':2.782,'d':4.253,'e':12.702,'f':2.228,'g':2.015,'h':6.094,'i':6.966,'j':0.153,'k':0.772,'l':4.025,
        'm':2.406,'n':6.749,'o':7.507,'p':1.929,'q':0.095,'r':5.987,'s':6.327,'t':9.056,'u':2.758,'v':0.978,'w':2.360,'x':0.150,'y':1.974,'z':0.074}
    text = "".join([l.lower() for l in cipher if l in string.ascii_letters]) #caracteres pertences ao alfabeto sem acento
    freq = None
    
    while not freq:
        lan = input("Digite a língua da mensagem que deseja decifrar(en: inglês, pt: português): ")
        if lan == "en":
            freq = FREQ_EN
        elif lan == "pt":
            freq = FREQ_PT
        else:
            print("Língua inválida. Digite novamente!")

    while not found:
        len_key = get_key_length(text)
        text_parts = []
        for i in range(len_key):
            text_parts.append("")
        for i in range(len(text)):
            text_parts[i % len_key] += text[i] #Dividir em partes
        INICIAL = ord('a')
        key = ""
        for part in text_parts:
            count_part = Counter(part)
            freq_part = {}
            for letter in count_part:
                freq_part[letter] = (count_part[letter] / len(part)) * 100
            max_letter = 0
            max_value = 0
            for i in range(26):
                total = 0
                for j in range(26):
                    try:
                        total += freq_part[chr(INICIAL + (i+j) % 26)] * freq[chr(INICIAL + j % 26)]
                    except:
                        pass
                if total > max_value:
                    max_letter = i
                    max_value = total
            key += chr(INICIAL + max_letter)
        print(f"\nChave: {key}\n")
        print("Texto decifrado:\n")
        decipher(key, cipher)

        sair = input("\nA mensagem encontrada corresponde à desejada?(s/n) ")

        if sair.lower() == 's':
            found = True
