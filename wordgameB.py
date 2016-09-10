from wordgameA import *
import time

def isvalidassume(word, hand, wordList):
    word_list=getFrequencyDict(word)
    for i in word_list.keys():
        if hand.get(i,0)>=word_list[i]:
            pass
        else:
            return False
    return True
#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score=0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word=''
    # For each word in the wordList
    for word in wordList:
    
        if isvalidassume(word , hand , wordList):
                
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            score=getWordScore(word,n)
            # Find out how much making that word is worth
            if score > max_score:
            # If the score for that word is higher than your best score
                max_score=score
                best_word=word
                # Update your best score, and best word accordingly
    if max_score==0:
        return None
    else:
        return best_word

    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total=0
    score=0
    new_hand=hand.copy()
    m=calculateHandlen(new_hand)
    while m>0:         
        print "Current Hand: ",
        displayHand(new_hand)
        word=compChooseWord(new_hand, wordList, n)
        if word==None:
            print
            break
        score=getWordScore(word, n)
        total=total+score
        print
        print '"'+word+'"','earned',str(score),'points.','Total: '+str(total),'points.'
        new_hand=updateHand(new_hand, word)
        m=calculateHandlen(new_hand)
        if m==0:
            break
        print
    print "Total score:",str(total),"points."
#   
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    isGameGoing = True
    hand = {}
 
    while isGameGoing == True:
        inp = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
 
        if inp == 'n':
            hand = dealHand(HAND_SIZE)
            while True:
                inp = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if inp == 'u':
                    playHand(hand.copy(), wordList, HAND_SIZE)
                    break
                elif inp == 'c':
                    compPlayHand(hand.copy(), wordList, HAND_SIZE)
                    break
                else:
                    print ('Invalid command.')
                    print
        elif inp == 'r':
            if hand != {}:
                while True:
                    inp = raw_input('Enter c to give this hand to a computer or u to play by yourself: ')
                    if inp == 'u':
                        playHand(hand.copy(), wordList, HAND_SIZE)
                        break
                    elif inp == 'c':
                        compPlayHand(hand.copy(), wordList, HAND_SIZE)
                        break
                    else:
                        print ('Invalid command.')
                        print
            else:
                print ('No hand have been played yet. Please play a new hand first!')
                print
        elif inp == 'e':
            isGameGoing = False
        else:
            print ('Invalid command.')


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
