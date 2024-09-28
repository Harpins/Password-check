from tkinter import *


def has_digit(text):
    return any(symbol.isdigit() for symbol in text)


def has_letter(text):
    return any(symbol.isalpha() for symbol in text)


def has_symbols(text):
    return any(not (symbol.isdigit() or symbol.isalpha()) for symbol in text)


def has_lower_letters(text):
    return any(symbol.islower() for symbol in text)


def has_upper_letters(text):
    return any(symbol.isupper() for symbol in text)


def is_very_long(text):
    return len(text) > 12


def password_score(text):
    score = 0
    functions_list = [
        has_digit,
        has_letter,
        has_symbols,
        has_lower_letters,
        has_upper_letters,
        is_very_long,
    ]

    for function in functions_list:
        if function(text) == True:
            score += 2
    return score


def main():

    def check_password(event):
        score_value = password_score(entry.get())
        label1.config(text='Уровень надежности пароля: ' + str(score_value))
        if score_value <= 4:
            label2.config(text='Слабый пароль')
            entry.configure(background="#FFA07A")
        elif 4 < score_value <= 8:
            label2.config(text='Средний пароль')
            entry.configure(background="#FFFACD")
        else:
            label2.config(text='Надежный пароль')
            entry.configure(background="#98FB98")

    root = Tk()
    root.title("Проверка пароля")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width // 2) - (200 // 2)
    y_coord = (screen_height // 2) - (100 // 2)
    root.geometry(f'200x100+{x_coord}+{y_coord}')
    root.resizable(False, False)

    password = StringVar(root)

    entry = Entry(root, textvariable=password)
    entry.bind('<KeyRelease>', check_password)
    entry.pack(pady=10)

    label1 = Label(root, text='')
    label1.pack()

    label2 = Label(root, text='Введите пароль')
    label2.pack()

    root.mainloop()


if __name__ == '__main__':
    main()

