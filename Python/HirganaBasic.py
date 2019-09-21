import random

#array of Hiragana characters, and pronunciations
hiraganaBasic = {
    0:{"char":u"\u3042", "pron":"a"}, # あ
    1:{"char":u"\u3044", "pron":"i"}, # い
    2:{"char":u"\u3046", "pron":"u"}, # う
    3:{"char":u"\u3048", "pron":"e"}, # え
    4:{"char":u"\u304a", "pron":"o"}, # お
    5:{"char":u"\u304b", "pron":"ka"}, # か 
    6:{"char":u"\u304d", "pron":"ki"}, # き
    7:{"char":u"\u304f", "pron":"ku"}, # く
    8:{"char":u"\u3051", "pron":"ke"}, # け
    9:{"char":u"\u3053", "pron":"ko"}, # こ
    10:{"char":u"\u3055", "pron":"sa"}, # さ
    11:{"char":u"\u3057", "pron":"shi"}, # し
    12:{"char":u"\u3059", "pron":"su"}, # す
    13:{"char":u"\u305b", "pron":"se"}, # せ
    14:{"char":u"\u305d", "pron":"so"}, # そ
    15:{"char":u"\u305f", "pron":"ta"}, # た
    16:{"char":u"\u3061", "pron":"chi"}, # ち
    17:{"char":u"\u3064", "pron":"tsu"}, # つ
    18:{"char":u"\u3066", "pron":"te"}, # て	
    19:{"char":u"\u3068", "pron":"to"}, # と
    20:{"char":u"\u306a", "pron":"na"}, # な
    21:{"char":u"\u306b", "pron":"ni"}, # に
    22:{"char":u"\u306c", "pron":"nu"}, # ぬ
    23:{"char":u"\u306d", "pron":"ne"}, # ね
    24:{"char":u"\u306e", "pron":"no"}, # の
    25:{"char":u"\u306f", "pron":"ha"}, # は
    26:{"char":u"\u3072", "pron":"hi"}, # ひ
    27:{"char":u"\u3075", "pron":"fu"}, # ふ
    28:{"char":u"\u3078", "pron":"he"}, # へ
    29:{"char":u"\u307b", "pron":"ho"}, # ほ
    30:{"char":u"\u307e", "pron":"ma"}, # ま
    31:{"char":u"\u307f", "pron":"mi"}, # み
    32:{"char":u"\u3080", "pron":"mu"}, # む
    33:{"char":u"\u3081", "pron":"me"}, # め
    34:{"char":u"\u3082", "pron":"mo"}, # も
    35:{"char":u"\u3084", "pron":"ya"}, # や
    36:{"char":u"\u3086", "pron":"yu"}, # ゆ
    37:{"char":u"\u3088", "pron":"yo"}, # よ
    38:{"char":u"\u3089", "pron":"ra"}, # ら
    39:{"char":u"\u308a", "pron":"ri"}, # り
    40:{"char":u"\u308b", "pron":"ru"}, # る
    41:{"char":u"\u308c", "pron":"re"}, # れ
    42:{"char":u"\u308d", "pron":"ro"}, # ろ
    43:{"char":u"\u308f", "pron":"wa"}, # わ
    44:{"char":u"\u3092", "pron":"o"}, # を
    45:{"char":u"\u3093", "pron":"n/m"} # ん
    }
  

running = True

while (running):
    #grabs random number
    rand = random.randint(0,45)

    #pulls random character and asks about its pronunciation
    testPro = input("What is the pronunciation of the following character:\t"+ hiraganaBasic[rand]["char"] +" ?\n")

    #checks for correct answer, or tells you incorrect and tells you the answer
    if(hiraganaBasic[rand]["pron"] == testPro.lower()):
        print("That is right!")
    else:
        print("Incorrect!\nThe real pronunciation is: "+ hiraganaBasic[rand]["pron"] +"\n")

    #allows for countinued questions or ends the game
    keepPlaying = input("Would you like to keep playing (y/n)?\n")
    if(keepPlaying.lower() == "y"):
        print("\n\n")
    else:
        print("==== Game Over ====\n\n")
        running = False