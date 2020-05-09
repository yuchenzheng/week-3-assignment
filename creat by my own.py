import random


def main():
    lenth = get_lenth()
    compare(lenth)


# get the lenth of word from user and a random number
def get_lenth():
    lenth_1 = random.randint(2, 8)
    lenth_2 = int(input('choose a lenth of word.(2-8)'))
    # set these two number as a tuple to return
    lenth = (lenth_1, lenth_2)
    return lenth


# compare the number of word and print the result out
def compare(lenth):
    # open the words file
    with open('words.txt', 'r') as rf:
        words = rf.readlines()
        random_result = []
        user_result = []
        # compare which lenth has more words base on words file
        for word in words:
            if len(word) == lenth[0]:
                random_result.append(word)
            if len(word) == lenth[1]:
                user_result.append(word)

    # caompare the result and print it out
    if len(random_result) > len(user_result):
        print('You lost! The random lenth has more words than lenth you choosed')
    elif len(random_result) == len(user_result):
        print('TIE! The random lenth has same number of words as lenth you choosed')
    else:
        print('You win! The lenth you choosed has more words than random lenth')
    # print out the number of each lenth's word
    print('There are ' + str(len(random_result)) + ' ' + str(lenth[0]) + ' letter words')
    print('There are ' + str(len(user_result)) + ' ' + str(lenth[1]) + ' letter words')


main()




