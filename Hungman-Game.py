def import_word():

    word = input("Choose the word\n").lower()
    return word

tries = 6 
letters = [] 
word=import_word()

def hide():
    hidden=''
    for letter in word:
        if letter in letters:
            hidden+=letter
        else:
            hidden+="_"
    return hidden


while tries>0:
    hidden_word=hide()
    if hidden_word == word:
        print("Congratulations you found the word",word )
        exit()

    print(hidden_word)
    letter= input("Give a letter\n").lower()
    
    
    if letter in letters:
        print ("you have already tried this letter")

    letters.append(letter)
    if letter in word:
        print("You have found a letter")
    else:
        print("This letter is not in the word")
        tries-=1
    print("You have ",tries," tries left")

    if(tries==0):
        print("You lost the game")
        