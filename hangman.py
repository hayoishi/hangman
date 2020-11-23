def hangman(word):
    wrong = 0
    stages =  ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = [""] * len(word)
    win = False
    print("ハングマンへようこそ！")

    # 負けこむまでループ
    while wrong < len(stage) -1:
        print("\n")
        msg = print("一文字を予想してね")
        char = input(msg)
        if char in retters:
            cind = rletters.index(char)
            board[cind] = '$'
        else:
            wrong +=1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stage[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print("".join(board))
            win = true
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))
