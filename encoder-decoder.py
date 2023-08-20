'''
## Message Encoder-Decoder


```
def encode(text):
    # Generate a random key for slicing the text
    key = random.randint(1, len(text) - 1)

    # Slice the text using the key
    sliced_text = text[key:] + text[:key]

    # Convert the sliced text into a list of ASCII codes using ord()
    ascii_codes = []
    for c in sliced_text:
       ascii_codes.append(ord(c))

    # Add 10*key to 5*ASCII code for each ASCII code in the list
    encoded_codes = []
    for code in ascii_codes:
      encoded_codes.append((5*code) + (10*key))

    # Convert the encoded ASCII codes back into a string
    encoded_text = ''
    for code in encoded_codes:
      encoded_text += chr(code)

    return encoded_text, key
```

It takes as input a `secret_message` that is to be encrypted so that no one can understand it, and returns the encrypted message, along with a key.

It does so by processing the `secret_message` in 4 steps. Each step adds extra complexity and makes it more incomprehensible.

Your task is to understand how it works and implement the `decoder()` function to decode the encoder's output i.e. extract the original secret message by implementing a reverse-inverse of the encoder. For example:
```
# define the message to be encrypted
secret_message = 'Hush! This is a secret message, sent from a very secretive group of people to some other very secretive people'

# do the encryption
encrypted_message, key = encode(secret_message)

# do the decryption
decrypted_message = decode(encrypted_message, key)

print(decrypted_message) # should print 'Hush! This is a secret message, sent from a very secretive group of people to some other very secretive people'
```

To implement the decoder, you need to implement the encoder steps in reverse order, and implement the inverse at each step:
* Convert the encoded text into a list of ASCII codes using `ord()`
* Subtract 10*key from the ASCII codes, and divide by 5 to undo the encoding
* Convert the decoded ASCII codes back into a string using `chr()`
* Slice the text using the key

Note that the `ord()` function converts a character to its ASCII representation and the `char()` function converts and ASCII representation to its corresponding character:
For example:
* `ord('!')` is `33`
* `chr(33)` is `'!'`

'''

import random


def encode(text):
    # Generate a random key for slicing the text
    key = random.randint(1, len(text) - 1)

    # Slice the text using the key
    sliced_text = text[key:] + text[:key]

    # Convert the sliced text into a list of ASCII codes using ord()
    ascii_codes = []
    for c in sliced_text:
        ascii_codes.append(ord(c))

    # Add 10*key to 5*ASCII code for each ASCII code in the list
    encoded_codes = []
    for code in ascii_codes:
        encoded_codes.append((5 * code) + (10 * key))

    # Convert the encoded ASCII codes back into a string
    encoded_text = ''
    for code in encoded_codes:
        encoded_text += chr(code)

    return encoded_text, key


def decode(encoded_text, key):
    ##########################
    ### START OF YOUR CODE ###
    ##########################

#use ascii ord()

    encoded_asc = [ord(c) for c in encoded_text]

    decoded_asc = [(code - 10 * key) // 5 for code in encoded_asc]
#convert ascii

    decoded_text = ''.join(chr(code) for code in decoded_asc)
#slice text use key

    o_text = decoded_text[-key:] + decoded_text[:-key]
    return o_text


    ##########################
    ###  END OF YOUR CODE  ###
    ##########################


if __name__ == '__main__':
    # test your solution here
    secret_message = 'Hush! This is a secret message, sent from a very secretive group of people to some other very secretive people'
    encrypted_message, key = encode(secret_message)
    print(decode(encrypted_message, key))
    # should print 'Hush! This is a secret message,
    # sent from a very secretive group of people
    # to some other very secretive people'
