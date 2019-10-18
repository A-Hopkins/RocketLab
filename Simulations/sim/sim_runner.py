#! /usr/bin/python3
"""
Basic sim runs the simulations for a model rocket.

The basic simulator will have functionality required to model the height, velocity, and acceleration of a model rocket.
This file runs the GUI

Created by: alex on 10/17/19
"""
import tkinter


class Window(tkinter.Frame):
    """
    Window class to make the GUI
    """

    def __init__(self, master=None):
        """
        Initializes the Window class. This class handles all the creations of the GUI.

        :param master: Master frame to root the window to

        :return: None
        """

        tkinter.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        """
        Draws the widgets.

        :return: None
        """
        self.master.title("Model Rocket Simulator")
        self.pack(fill=tkinter.BOTH, expand=True)

        simulate_button = tkinter.Button(self, text="Simulate!", command=simulate)
        simulate_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def simulate():
    """
    Simulates stuff

    :return: None
    """
    # TODO: Add functionality to simulate button. Should call the simulator and plotter functions
    print("Feature not added yet!")


def run():
    """
    Runs the main window.

    :return: None
    """

    root = tkinter.Tk()
    root.geometry("640x480")
    Window(root)
    root.mainloop()


if __name__ == "__main__":
    run()
