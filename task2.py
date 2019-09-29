from collections import Counter

'''using counter for easy counting words in text'''
def get_most_popular_word(text):
    words = text.split()
    most_popular = Counter(words).most_common(2)
    if not most_popular or (len(most_popular) == 2 and most_popular[0][1] == most_popular[1][1]):
        return '—'
    return most_popular[0][0]


def main():
    s = input("please enter da text: ")
    '''input str by str but if u wanna to copy full text from somewhere, u will need to click enter one more time'''
    s_ = input()
    while s_!='':
        s += s_
        s_ = input()
    print(get_most_popular_word(s))
    return 0

if __name__ == '__main__':
    main()