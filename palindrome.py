#takes words from a text file and returns only those words that are palindromes.

def palindrome(list_words):
    '''returns the palindrome of a word to a list '''

    for word in list_words:
        reverse_word = word.lower()[::-1]
        if len(word)>1 and word.lower() == reverse_word :
            final_list.add(word)

list_words = set()
final_list = set()
#for line in open('trial_paldata.txt','r'):
for line in open('anagram.txt','r'):
    list_words.add(line.strip().lower())

palindrome(list_words)
print(sorted(final_list))



