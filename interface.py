"""
tkinter based Python program to test
python skills and library learning

author: davidlao (n3x4z @ GitHub)

objective:
- Practice learning Python concepts
- Learning about libraries (tkinter, random, requests, PIL)
"""
import random
import requests
import tkinter as tk
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

def show_about():
    """Shows the About window of the tkinter app"""
    # instance & configure window
    about = Tk()
    about.title("About the app")
    about.geometry("320x240")
    about.configure(bg="#222222")
    about.grid()

    # display the app description
    tk.Label(about, text="This is just a test application made in Python with tkinter", font="sans-serif", justify="left", wraplength=320, background="#222222", foreground="#EEEEEE").pack(fill="x", padx=5, pady=5)
    # display an OK button to close window
    tk.Button(about, text="OK", command=about.destroy).pack()

    # shows window
    about.mainloop()


greetings: tuple = ("Hey", "Hi", "Howdy", "Hello")
def get_random_greeting() -> str:
    """
    Gives a random greeting from ``greetings``
    :return: Greeting string
    """
    # choose a random greeting from the fixed tuple
    return greetings[random.randint(0, len(greetings) - 1)]


def show_list_test() -> Tk:
    """
    Returns window for basic list test (pre-add, add, remove)
    :return: :class:`Tk` window
    """
    # instance & configure window
    list_test = Tk()
    list_test.title("List")
    list_test.geometry("640x480")
    list_test.configure(bg="#222222")
    list_test.grid()

    # list for items to be shown
    list_widget = tk.Listbox(list_test, bg="#222222", fg="#EEEEEE")

    # programatically pre-add "Element n" items
    for i in range(1,6):
        list_widget.insert(i, f"Element {i}")

    # button to add new element (random greeting)
    tk.Button(list_test, text="Add", command=lambda: list_widget.insert(tk.END, get_random_greeting())).pack()

    # button to remove last element of list
    tk.Button(list_test, text="Remove", command=lambda: list_widget.delete(tk.END)).pack()

    # add window components
    list_widget.pack()

    # return final window state to be shown
    return list_test


def fetch_endpoint(url: str):
    """
    Fetches URL and shows data in ``messagebox``
    If the fetch fails, it also shows the exception in ``messagebox`` style
    :param url:
    """
    try:
        # show the fetch response in a messagebox
        result: str = requests.get(url).text
        messagebox.showinfo(message=f"{result}", title="Fetched")
    except requests.exceptions.MissingSchema as e:
        # warn the user an invalid URL was input
        messagebox.showinfo(message=f"Error: {e}", title="Failed")


def show_fetch_test() -> Tk:
    """
    Returns HTTP fetcher window
    :return: :class:`Tk` window
    """
    # instance & configure window
    fetch_test = Tk()
    fetch_test.title("JSON Fetch test")
    fetch_test.geometry("640x480")
    fetch_test.configure(bg="#222222")
    fetch_test.grid()

    # URL to fetch JSON from
    fetch_url = tk.Text(fetch_test, height=1, width=20)

    # button to fetch URL data
    tk.Button(fetch_test, text="Fetch", command=lambda: fetch_endpoint(fetch_url.get('1.0', 'end-1c'))).pack()

    # add window components
    fetch_url.pack()

    # return final window state to be shown
    return fetch_test


def choose_image(widget: tk.Label, canvas: Tk):
    """Opens file selection dialog and changes image from input ``widget``"""
    # ask for new image file
    path: str = askopenfilename()

    try:
        # try loading in the new image
        new_image_data = Image.open(path).resize((128,128))
        new_image = ImageTk.PhotoImage(new_image_data, master=canvas)

        # update the visual side of things
        widget.configure(image=new_image)
        # must keep reference (otherwise python drops it and we get no image)
        widget.image = new_image
    except Exception as e:
        messagebox.showinfo(message=f"Error: {e}", title="Failed")


def show_image_test() -> Tk:
    """
    Returns image test and picker window
    :return: :class:`Tk` window
    """
    # instance & configure window
    image_test = Tk()
    image_test.title("Image test")
    image_test.geometry("320x240")
    image_test.configure(bg="#222222")
    image_test.grid()

    try:
        # attempt loading in default image
        image_original_data = Image.open("default.png").resize((128,128))
        image_data = ImageTk.PhotoImage(image_original_data, master=image_test)
        image_widget = tk.Label(image_test, image=image_data)
        image_widget.image = image_data # must keep reference (otherwise python drops it and we get no image)

        # add window components
        tk.Button(image_test, text="Choose image", command=lambda: choose_image(image_widget, image_test)).pack()
        image_widget.pack()
    except tk.TclError as e:
        messagebox.showinfo(message=f"Error: {e}", title="Failed")

    # return final window state to be shown
    return image_test


def show_windows():
    """Function whose sole purpose is to launch a few windows for the ``Hi!`` button"""
    # get window objects
    win1 = show_list_test()
    win2 = show_fetch_test()
    win3 = show_image_test()

    # show them
    win1.mainloop()
    win2.mainloop()
    win3.mainloop()

def main():
    # init Tkinter
    root = Tk()

    # set window parameters
    root.title("Simple tkinter app")
    root.geometry("640x480")
    root.configure(bg="#222222")
    root.grid()

    # add window components
    tk.Label(root, text = "Hello there!", font=("sans-serif", 24), background="#222222", foreground="#EEEEEE").pack()
    tk.Button(root, text="Click me", command=lambda: messagebox.showinfo(message="i\'m just a message", title="HEY!")).pack(pady=5)
    tk.Button(root, text="Hi!", command=show_windows).pack(pady=5)
    tk.Button(root, text="About", command=show_about).pack(pady=5)
    tk.Button(root, text="Quit", command=exit).pack(pady=5)

    # show the window
    root.mainloop()

# run program
main()