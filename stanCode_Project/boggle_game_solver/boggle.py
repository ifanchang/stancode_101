"""
File: boggle.py
Name: CHANG I FAN
----------------------------------------
TODO:
"""

# from campy.gui.events.timer import pause

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic_word = []
row_list = []
word_count = [0]


def main():
    """
    This is a boggle game
    """
    if input_and_check() == "out":
        pass

    else:
        read_dictionary()
        for x in range(4):
            for y in range(4):
                combine_the_word("", x, y, row_list, [])
        print("There are", word_count[0], "word in total")


def combine_the_word(current_word, position_x, position_y, row_list_func, found_list):
    # Check the word in the list(dic_word)
    # 如果偵測到現有的字母組合已經沒有機會，就直接return不要繼續往下跑。
    if len(current_word) > 3:
        if current_word in dic_word:
            if current_word not in found_list:
                found_list.append(current_word)
                print("found", current_word)
                word_count[0] += 1
        if not has_prefix(current_word):
            return
    # --------------------------------------

    # choose
    # 如果字母位置為空，直接return掉。
    if row_list_func[position_x][position_y] == "":
        return

    # 將字母加到文字組合中
    temp_word = row_list_func[position_x][position_y]
    current_word += str(temp_word)

    # explore
    # 將選取到的字母位置改為空
    row_list_func[position_x][position_y] = ""
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= position_x+i <= 3:
                position_x_next = position_x + i
            else:
                continue
            if 0 <= position_y+j <= 3:
                position_y_next = position_y + j
            else:
                continue
            combine_the_word(current_word, position_x_next, position_y_next, row_list_func, found_list)

    # un-choose
    row_list_func[position_x][position_y] = current_word[len(current_word) - 1]
    current_word = current_word[:len(current_word) - 1]


def input_and_check():
    for i in range(4):
        row = str(input(str(i + 1) + " row of letters: ")).lower()
        row_list.append([])

        # Add a new list in the list(row_list)
        if len(row) != 7:
            print("Illegal input")
            return "out"
        for row_index in [1, 3, 5]:
            if row[row_index] != " ":
                print("Illegal input")
                return "out"
        for row_index in [0, 2, 4, 6]:
            if not row[row_index].isalpha():
                print("Illegal input")
                return "out"
            else:
                row_list[i] += row[row_index]


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open("dictionary.txt", "r")as f:
        for line in f:
            dic_word.append(line[0:len(line) - 1])


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dic_word:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
