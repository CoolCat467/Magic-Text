# Magic-Text
Magic Text will Magicify Text (make it shorter) and then later Un-Magicify it back into readable text.

# VERY IMPORTANT NOTES:
This program requires the Maths Module! https://github.com/CoolCat467/maths
DISCLAIMER:
Additinal programs used in this program
may contain code or code based off other code
not owned by Cat Inc.

## About
Magic Text will Magicify Text (make it shorter) and then later Un-Magicify it back into readable text. This is very usefull for say, sending quick messages to a friend without email/etc. You could write a message, like "Meet me at twelve O'Clock", which, Magicified, is "1G5 1G2 1c 1S2 1a3". This is significantly shorter, plus, no one can read it without having both the program and the exact same dictionary file.

### Specs
Magic Text was programmed and tested on a Linux Device.
Some errors MAY occor when running on different operating systems.
If you encounter errors, regardless of operating system, please report it as soon as you can.

### How it works
Magic Text uses a dictionary files, each of which can store up to 9999 words. And it's super easy to add words; just select the option "Add to Selected Dictionary", type in a sentance, and the program will handle the rest!
#### Magicification
Whenever you enter text to be Magicified, the program first splits the text by it's spaces, and stores this spit text as a list.
Then, each word is founds in the dictionary, and the position of that word is stored. If it's not in the dictionary, it ommits the word from the result.
This also causes an effective Whitelist, as any words not in the dictionary are simply not possible to send.
And even if a user did add the word, Both the sender and recever need the same dictionary for it to be sent properly.
The position of the word in the dictionary is then converted into Hexadecimal Code, and if even that is able to be shortened, it will be.
#### Un-Magicification
Pretty much, it's just Magicification in reverse.

### Usage
Download Magic Text and the Maths Module (https://github.com/CoolCat467/maths)
Put the following files from Magic Text into a new folder named "Magic Text":
dict.txt
Magic Text.py
Put the following files from the Maths Module into the folder "Magic Text":
maths.py
Launch the program!

### Interface
When you run the program, you should see the following screen:
Copywrite (c) Cat Inc.
All Rights Reserved.

Programmed by Samuel Davenport, member of Cat Inc.

Welcome to the Magic Text Program v0.0.2!

Please select a dictionary file, or enter the name of a new one.
(Program does not handle non-txt files)

Pre-Existing Dictionaries:

And here, it will list any .txt files found in the Magic Text folder.
Then, it will ask for "Dictionary Number or New Dictionary Filename".
Here, you enter either the number listed for the dictionary you want, or a new dictionary name.

Now, you should see the following screen:

Selected Dictionary "<Dictionary name you choose>.txt"

Please Select An Option:
1. Magicification
2. Un-Magicification
3. Add to Selected Dictionary
4. Sort Selected Dictionary
5. Merge Selected Dictionary and Another Together
6. Stats of Currently Selected Dictionary
7. Credits
8. Quit

Option : 

And then, just enter whatever option you want, and it should be straight forward from there!

Hope you like it!
