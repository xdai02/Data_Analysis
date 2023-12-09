import random

class Hangman:
    def __init__(self):
        self.__HANGMAN_PICS = [
            '''
            +---+
                |
                |
                |
               ===''', '''
            +---+
            O   |
                |
                |
               ===''', '''
            +---+
            O   |
            |   |
                |
               ===''', '''
            +---+
            O   |
           /|   |
                |
               ===''', '''
            +---+
            O   |
           /|\  |
                |
               ===''', '''
            +---+
            O   |
           /|\  |
           /    |
               ===''', '''
            +---+
            O   |
           /|\  |
           / \  |
               ==='''
        ]

        # 创建词库
        self.__words = []
        with open("第1章 Python/综合练习/hangman/words.txt", "r") as file:
            self.__words = file.readlines()
        self.__words = [word.strip() for word in self.__words]
        self.__words = [
            word for word in self.__words 
            if word.isalpha() and word.islower() and len(word) >= 5
        ]
    
    def __choose_word(self):
        # 随机选择一个单词
        self.__secret_word = random.choice(self.__words)

    def __display_status(self):
        # 绞刑架状态
        print(self.__HANGMAN_PICS[self.__wrong_num])

        # 单词状态
        for letter in self.__secret_word:
            if letter in self.__correct_letters:
                print(letter,end=' ')
            else:
                print('_',end=' ')
        print()

        # 错误字母
        print("错误字母:",self.__incorrect_letters)
        print()

    def __check_win(self):
        # 判断玩家是否获胜
        for letter in self.__secret_word:
            if letter not in self.__correct_letters:
                return False
        return self.__wrong_num < 7

    def start(self):
        self.__wrong_num = 0
        self.__correct_letters = []
        self.__incorrect_letters = []

        # 随机选择单词
        self.__choose_word()
        
        while True:
            # 显示游戏界面
            self.__display_status()

            # 用户输入字母
            guess = input("猜1个字母:")
            if len(guess) != 1 or not guess.isalpha():
                print("输入有误")
                continue
            
            # 判断是否正确
            if guess in self.__secret_word:
                if guess not in self.__correct_letters:
                    self.__correct_letters.append(guess)
            else:
                if guess not in self.__incorrect_letters:
                    self.__wrong_num += 1
                    self.__incorrect_letters.append(guess)
            
            if self.__check_win():
                print("猜对了！正确答案是：",self.__secret_word)
                break
            if self.__wrong_num >= 7:
                print("猜错了！正确答案是：",self.__secret_word)
                break

if __name__ == "__main__":
    game = Hangman()
    game.start()
