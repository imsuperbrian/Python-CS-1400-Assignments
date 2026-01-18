# CS1400 Assignment 4: Functions, Strings, and If. By Brian Yang

# Returns the larger of two numbers
def choose_larger(num_1, num_2):
    if num_1 >= num_2:
        return num_1
    else:
        return num_2


# Distinguish the type of triangle based on side lengths
def triangle_type(side_1, side_2, side_3):
    if side_1 == side_2 == side_3:
        return "Equilateral"
    elif side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
        return "Scalene"
    else:
        return "Isosceles"


#Adds the correct word like 'a' or 'an' before a word
def add_a_or_an_to_word(word):
    if word[0] in 'aeiou':
        return 'an ' + word
    else:
        return 'a ' + word


#Adds the correct word like 'a', 'an', or 'any' based on word
def add_a_or_an_or_any_to_word(word):
    if word[-1] == 's':
        return 'any ' + word
    elif word[0] in 'aeiou':
        return 'an ' + word
    else:
        return 'a ' + word


# Replaces a value in a list with another value
def replace_in_list(list, word_or_num_1, word_or_num_2):
    for index in range(len(list)):
        if list[index] == word_or_num_1:
            list[index] = word_or_num_2
    return list


# Returns a synonym for a word if it exists, otherwise returns the original word
def replace_word_with_synonym(word):
    if word == "big":
        return "vast"
    elif word == "important":
        return "noteworthy"
    elif word == "quiet":
        return "tranquil"
    elif word == "nice":
        return "pleasant"
    elif word == "quick" or word == "fast":
        return "prompt"
    elif word == "funny":
        return "humorous"
    elif word == "kind":
        return "benevolent"
    elif word == "fun":
        return "exhilarating"
    elif word == "brave":
        return "courageous"
    elif word == "exciting":
        return "thrilling"
    else:
        return word


# Replaces words in a sentence with their synonyms where applicable
def thesaurus(sentence):
    new_sentence = sentence.split()
    for index in range(len(new_sentence)):
        new_sentence[index] = replace_word_with_synonym(new_sentence[index])
    return " ".join(new_sentence)


#Testing the results:
def main():
    # ----- Testing choose_larger -----
    print("-----Testing choose_larger-----")
    print("choose_larger(5, 10), expected: 10")
    print("Actual:", choose_larger(5, 10))
    print()

    print("choose_larger(20, 15), expected: 20")
    print("Actual:", choose_larger(20, 15))
    print()

    print("choose_larger(7, 7), expected: 7")
    print("Actual:", choose_larger(7, 7))
    print()

    # ----- Testing triangle_type -----
    print("-----Testing triangle_type-----")
    print("triangle_type(5, 5, 5), expected: Equilateral")
    print("Actual:", triangle_type(5, 5, 5))
    print()

    print("triangle_type(5, 5, 3), expected: Isosceles")
    print("Actual:", triangle_type(5, 5, 3))
    print()

    print("triangle_type(3, 4, 5), expected: Scalene")
    print("Actual:", triangle_type(3, 4, 5))
    print()

    # ----- Testing add_a_or_an_to_word -----
    print("-----Testing add_a_or_an_to_word-----")
    print("add_a_or_an_to_word('apple'), expected: an apple")
    print("Actual:", add_a_or_an_to_word('apple'))
    print()

    print("add_a_or_an_to_word('banana'), expected: a banana")
    print("Actual:", add_a_or_an_to_word('banana'))
    print()

    # ----- Testing add_a_or_an_or_any_to_word -----
    print("-----Testing add_a_or_an_or_any_to_word-----")
    print("add_a_or_an_or_any_to_word('apples'), expected: any apples")
    print("Actual:", add_a_or_an_or_any_to_word('apples'))
    print()

    print("add_a_or_an_or_any_to_word('orange'), expected: an orange")
    print("Actual:", add_a_or_an_or_any_to_word('orange'))
    print()

    print("add_a_or_an_or_any_to_word('banana'), expected: a banana")
    print("Actual:", add_a_or_an_or_any_to_word('banana'))
    print()

    # ----- Testing replace_in_list -----
    print("-----Testing replace_in_list-----")
    print("replace_in_list([0, 1, 'hi', 4.7, 1, 1], 1, 'bye'), expected: [0, 'bye', 'hi', 4.7, 'bye', 'bye']")
    print("Actual:", replace_in_list([0, 1, 'hi', 4.7, 1, 1], 1, 'bye'))
    print()

    print("replace_in_list(['apple', 'banana', 'apple'], 'apple', 'orange'), expected: ['orange', 'banana', 'orange']")
    print("Actual:", replace_in_list(['apple', 'banana', 'apple'], 'apple', 'orange'))
    print()

    # ----- Testing replace_word_with_synonym -----
    print("-----Testing replace_word_with_synonym-----")
    print("replace_word_with_synonym('fun'), expected: exhilarating")
    print("Actual:", replace_word_with_synonym('fun'))
    print()

    print("replace_word_with_synonym('nothing'), expected: nothing")
    print("Actual:", replace_word_with_synonym('nothing'))
    print()

    # ----- Testing thesaurus -----
    print("-----Testing thesaurus-----")
    print("thesaurus('this is a big important function'), expected: this is a vast noteworthy function")
    print("Actual:", thesaurus('this is a big important function'))
    print()

    print("thesaurus('you are funny and kind'), expected: you are humorous and benevolent")
    print("Actual:", thesaurus("you are funny and kind"))
    print()

if __name__ == "__main__":
    main()
