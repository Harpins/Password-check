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
        label1.config(text='Рейтинг этого пароля: ' + str(score_value))

    root = Tk()
    root.title("Проверка пароля")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width // 2) - (200 // 2)
    y_coord = (screen_height // 2) - (100 // 2)
    root.geometry(f'220x80+{x_coord}+{y_coord}')
    root.resizable(False, False)

    password = StringVar(root)

    label0 = Label(root, text='Введите пароль:')

    entry = Entry(root, show='*', textvariable=password)
    entry.bind('<KeyRelease>', check_password)

    label0.grid(row=0, column=0)
    entry.grid(row=0, column=1)

    label1 = Label(root, text='')
    label1.grid(row=1, column=0, columnspan=2, sticky='w')

    root.mainloop()


if __name__ == '__main__':
    main()


