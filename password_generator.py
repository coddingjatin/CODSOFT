from graphics import GraphWin, Entry, Text, Point, Rectangle
import string
import random

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    win = GraphWin("Password Generator", 400, 250)
    win.setBackground("#f0f0f0")

    text_username = Text(Point(100, 50), "Username:")
    text_username.draw(win)

    entry_username = Entry(Point(250, 50), 20)
    entry_username.draw(win)
    entry_username.setFill("#e6e6e6")

    text_password_length = Text(Point(100, 100), "Password Length:")
    text_password_length.draw(win)

    entry_password_length = Entry(Point(250, 100), 10)
    entry_password_length.draw(win)
    entry_password_length.setFill("#e6e6e6")

    button_generate = Text(Point(200, 150), "Generate Password")
    button_generate.draw(win)
    button_generate.setStyle("bold")
    button_generate.setFill("#4caf50")

    password_box = Rectangle(Point(100, 180), Point(300, 220))
    password_box.draw(win)
    password_box.setFill("#e6e6e6")

    password_text = Text(Point(200, 200), "")
    password_text.draw(win)

    reset_box = Rectangle(Point(310, 190), Point(380, 230))
    reset_box.draw(win)
    reset_box.setFill("#ff7043")

    reset_text = Text(Point(345, 210), "Reset")
    reset_text.draw(win)
    reset_text.setTextColor("white")
    reset_text.setStyle("bold")

    win.getMouse()

    try:
        username = entry_username.getText()
        password_length = int(entry_password_length.getText())

        if password_length <= 0:
            raise ValueError

        generated_password = generate_password(password_length)
        password_text.setText(generated_password)

    except ValueError:
        error_text = Text(Point(200, 230), "Invalid input. Please enter a positive integer for password length.")
        error_text.setTextColor("red")
        error_text.draw(win)

    while True:
        click_point = win.getMouse()
        x, y = click_point.getX(), click_point.getY()
        if 310 <= x <= 380 and 190 <= y <= 230:
            entry_username.setText("")
            entry_password_length.setText("")
            password_text.setText("")
            if "error_text" in locals():
                error_text.undraw()
            break

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
