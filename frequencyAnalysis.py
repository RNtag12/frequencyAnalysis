#letters frequency in the alphabet are specified here
ETAOIN='ETAOINSHRDLCUMWFGYPBVKJXQZ'

#letters of the alphabet are specified here
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# the first step is to create a dictionary with keys of single letters and ensure that the values of the
# count of how many times they appear in the message parameter:
def getLetterCount(message):
  letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

for letter in message.upper():
  if letter in LETTERS:
    letterCount[letter] += 1
    return letterCount
  
def getItemAtIndexZero(items):
    return items[0]
  
  #the next function returns an alphabet of letters arranged in order of most frequently occuring in the message parametter
def getFreqOrder(message):
  letterToFreq = getLetterCount(message)
  freqToLetter={}
  for letter in LETTERS:
    if letterToFreq[letter] not in freqToLetter:
      freqToLetter[letterToFreq[letter]] = [letter]
    else:
      freqToLetter[letterToFreq[letter]].append(letter)
  for freq in freqToLetter:
    freqToLetter[freq].sort(key=ETAOIN.find, reverse=true)
    freqToLetter[freq]= '' join(freqToLetter[freq])
    
  #converting the dictionary to a list of tuple pairs and sorting them
  freqPairs= list(freqToLetter.items())
  freqPairs.sort(key=getItemAtIndexZero, reverse=True)

#extracting all the letters for the final string:
  freOrder = []
  for freqPair in freqPairs:
  freqOrder.append(freqPair[1])

  return ''.join(freqOrder)

#this next part is to compare the letter frequency of our ordered dictionary to known letter frequencies in the plaintext language

def englishfreqMatchScore(message):
  freqOrder= getFrequencyOrder(message)

matchScore = 0
for commonLetter in ETAOIN[:6]:
  if commonLetter in freqOrder[:6]:
    matchScore += 1

for uncommonLetter in ETAOIN[-6:]:
  if uncommonLetter in freqOrder[-6:]:
    matchScore += 1

return matchScore

