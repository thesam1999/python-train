def hello(name, lang):  # name跟lang稱parameter參數，定義函示時，使用的變數，表示函示會接受什麼樣的輸入，可稱"輸入佔位符"
    # 但如果輸入hello("sam","english")那sam跟english稱為argument引數，呼叫函式時傳遞給參數的實際值，執行函式時提供的具體輸入數據，替換函式定義中的參數。

    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)


if __name__ == '__main__':

    import argparse

    # argumentparser 參數解析器
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet. "
    )  # required=True 必須要需入指令才能執行，否則顯示錯誤
    # metaver 表示在輸入-help後，會顯示要輸入-n name 這裡的name就是metavar賦予的值，提示你要在-n後面輸入name，讓生成的幫助信息更具可讀性和友好性

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"], help="The language of greeting."
    )  # choices代表給使用者規定要輸入什麼值，如果不是輸入裡面的詞，會顯示erro

    args = parser.parse_args()

    hello(args.name, args.lang)

    # msg= f"Hello {args.name}!""

    # print(msg)
