import random
import string


def get_random(length):
    letter =string.ascii_lowercase
    return ''.join(random.choice(letter) 
                   for i in range(length))

st = input("Enter message: ")
words =st.split(" ")
coding = input("1 for coding or 0 for Decoding: ")

if(coding == '1'):

    nwords =[]
    for word in words:

        if(len(word)>=3):

            r1 = get_random(3)
            r2 = get_random(3)
            stnew = r1+word[1:] + word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords =[]
    for word in words:

        if(len(word)>=3):
            stnew = word[3:-3] 
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))