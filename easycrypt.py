"""
* Created by JetBrains PhpStorm.
* User: ferron
* Date: 1/3/12
* Time: 5:01 PM
* To change this template use File | Settings | File Templates.
*/

/*
* CopyLeft (c) 2012 Ferron Hanse  All  Rights Reserved.
*
* This software is made available under the terms of the "GPL License"
* A copy of this license is included with this source distribution
* in "license.txt" and is also available at:
* http://www.gnu.org/copyleft/gpl.html
*
* Last Update : 19 February 2012
* Converted to Python, Java, PHP, JavaScript
*
* Welcome to any suggestion : ferronrsmith@gmail.com
*
"""

# Much like a ROT13 shift used in the caesar cipher
# http://en.wikipedia.org/wiki/Caesar_cipher
SHIFT = 3
CIPHER = '@)*%/~^!?z' # cipher : keep this secret ^_^

def encrypt (data) :
    # private variables
    encrypted = "" # default string for storing result
    temp = ""
    j = 0
    for i in range(len(data)):
        compared = ord(data[i]) + SHIFT
        if compared < 100:
            if compared < 10 :
                encrypted += '00' + str(compared)
            else:
                encrypted += '0' + str(compared)
        else:
            encrypted += str(compared)

    for j in range(len(encrypted)):
        if encrypted[j] == '0':
            temp += CIPHER[0]
        elif encrypted[j] == '1':
            temp += CIPHER[1]
        elif encrypted[j] == '2':
           temp += CIPHER[2]
        elif encrypted[j] == '3':
            temp += CIPHER[3]
        elif encrypted[j] == '4':
            temp += CIPHER[4]
        elif encrypted[j] == '5':
            temp += CIPHER[5]
        elif encrypted[j] == '6':
            temp += CIPHER[6]
        elif encrypted[j] == '7':
            temp += CIPHER[7]
        elif encrypted[j] == '8':
            temp += CIPHER[8]
        elif encrypted[j] == '9':
            temp += CIPHER[9]
        else:
            print "Encrypt Error:number out of range"
    encrypted = temp
    return encrypted

def decrypt(data):
    # private variables
    encrypted=""
    result = ""
    temp = 0
    inc = 0
    for j in range(len(data)):
        if data[j] == CIPHER[0]:
            encrypted +='0'
        elif data[j] == CIPHER[1]:
            encrypted += '1'
        elif data[j] == CIPHER[2]:
            encrypted += '2'
        elif data[j] == CIPHER[3]:
            encrypted += '3'
        elif data[j] == CIPHER[3]:
            encrypted += '3'
        elif data[j] == CIPHER[4]:
            encrypted += '4'
        elif data[j] == CIPHER[5]:
            encrypted += '5'
        elif data[j] == CIPHER[6]:
            encrypted += '6'
        elif data[j] == CIPHER[7]:
            encrypted += '7'
        elif data[j] == CIPHER[8]:
            encrypted += '8'
        else:
            encrypted += '9'
    data = encrypted

    while inc < len(data):
        temp = int(data[inc] + data[inc+1] + data[inc+2])
        temp -= SHIFT
        result += chr(temp)
        inc += 3

    return result