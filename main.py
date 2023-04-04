class Enigma:
    def __init__(self,plugboard):
        self._Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        self._rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        self._rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        self._reflector = 'AY BR CU DH EQ FS GL IP JX KN MO TZ VW'
        self._plugboard = plugboard
        #Ring settings
        self._rs1 = self._Alphabet.find('I')
        self._rs2 = self._Alphabet.find('J')
        self._rs3 = self._Alphabet.find('S')
        #Initial Positions
        self._pos1 = (self._Alphabet.find('B') - self._rs1) % 26
        self._pos2 = (self._Alphabet.find('B') - self._rs2) % 26
        self._pos3 = (self._Alphabet.find('C') - self._rs3) % 26
        #Turnover Positions
        self._turn_1 = (self._Alphabet.find('R')  - self._rs1) % 26 
        self._turn_2 = (self._Alphabet.find('F')  - self._rs2) % 26
        self._turn_3 = (self._Alphabet.find('W')  - self._rs3) % 26
        

    
    def decode_msg(self,Message):
        strip_message = Message.replace(' ','')
        Plaintext = strip_message.upper()
        print(Plaintext)
        Ciphertext = ''
        for letter in Plaintext:
            #Stepping
            self._pos3 = (self._pos3 + 1) % 26
            if(self._pos3 == self._turn_3):
                self._pos2 = (self._pos2 + 1) % 26
            if(self._pos2 == self._turn_2):
                self._pos1 = (self._pos1 + 1) % 26
                #Double Stepping
                self._pos2 = (self._pos2 + 1) % 26  
            print('Letter in: ' + letter)
            
            #Plugboard initial
            letter_in = letter
            for pair in self._plugboard.split(' '):
                if letter in pair:
                    letter_in = (pair.replace(letter,''))   

            index_in = self._Alphabet.find(letter_in)
            #Forwards bit
            index_1_in = (index_in + self._pos3) % 26
            letter_1 = self._rotor3[index_1_in]
            index_1_out = (self._Alphabet.find(letter_1) - self._pos3) % 26
            print("L1: " + self._Alphabet[index_1_out])
            index_2_in = (index_1_out + self._pos2) % 26
            letter_2 = self._rotor2[index_2_in]
            index_2_out = (self._Alphabet.find(letter_2) - self._pos2) % 26
            print("L2: " + self._Alphabet[index_2_out])
            index_3_in = (index_2_out + self._pos1) % 26
            letter_3 = self._rotor1[index_3_in]
            index_3_out = (self._Alphabet.find(letter_3) - self._pos1) % 26
            print("L3: " + self._Alphabet[index_3_out])
            #Reflector
            reflected_letter = 'A' #Default value should never be used
            for pair in self._reflector.split(' '):
                if self._Alphabet[index_3_out] in pair:
                    reflected_letter = pair.replace(self._Alphabet[index_3_out],'')
            index_r_out = self._Alphabet.find(reflected_letter)
            print("Reflect: " + reflected_letter)
            #Backwards bit
            index_4_in = (index_r_out + self._pos1) % 26
            letter_4 = self._Alphabet[index_4_in]
            index_4_out = (self._rotor1.find(letter_4) - self._pos1) % 26
            print("L4: " + self._Alphabet[index_4_out])

            index_5_in = (index_4_out + self._pos2) % 26
            letter_5 = self._Alphabet[index_5_in]
            index_5_out = (self._rotor2.find(letter_5) - self._pos2) % 26
            print("L5: " + self._Alphabet[index_5_out])

            index_6_in = (index_5_out + self._pos3) % 26
            letter_6 = self._Alphabet[index_6_in]
            index_6_out = (self._rotor3.find(letter_6) - self._pos3) % 26
            print("L6: " + self._Alphabet[index_6_out])
            letter_out = self._Alphabet[index_6_out]
            #Plugboard final
            for pair in self._plugboard.split(' '):
                if letter_out in pair:
                    letter_out = (pair.replace(letter_out,''))

            if(len(Ciphertext) % 6 == 5 and len(Ciphertext) != 0):
                Ciphertext += ' '
            Ciphertext += letter_out
            print("Rotors: " + str(self._pos1) + ',' + str(self._pos2) + ',' + str(self._pos3))
            

        return Ciphertext
