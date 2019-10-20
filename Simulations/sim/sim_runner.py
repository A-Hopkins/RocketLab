"""
Basic sim runs the simulations for a model rocket.

The basic simulator will have functionality required to model the height, velocity, and acceleration of a model rocket.
This file runs the GUI

Created by: alex on 10/17/19
"""
import tkinter
import tkinter.ttk


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

        simulate_button = tkinter.Button(self, text="Simulate!", command=self.simulate_window)
        simulate_button.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

        load_button = tkinter.Button(self, text="Load Config", command=self.load_config_window)
        load_button.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

    def load_config_window(self):
        """
        Creates a window to load configurations.

        :return: None
        """

        window = tkinter.Toplevel(self.master)
        window.title("Load configurations")
        window.geometry("330x420")

        # Table text, need a better implementation
        # TODO: Fix bug validate command only works once
        # TODO: Add implementation beyond print value
        table_entry1 = tkinter.Label(window, text="Dry Mass:")
        table_entry1.grid(row=0, column=0)
        dry_mass = tkinter.StringVar()
        table_entry2 = tkinter.Entry(window, textvariable=dry_mass, validate="focusout",
                                     validatecommand=lambda: print(dry_mass.get()))

        table_entry2.grid(row=0, column=1)

        table_entry3 = tkinter.Label(window, text="Motor mass:")
        table_entry3.grid(row=1, column=0)
        motor_mass = tkinter.StringVar()
        table_entry4 = tkinter.Entry(window, textvariable=motor_mass, validate="focusout",
                                     validatecommand=lambda: print(motor_mass.get()))
        table_entry4.grid(row=1, column=1)

        table_entry5 = tkinter.Label(window, text="Impulse:")
        table_entry5.grid(row=2, column=0)
        impulse = tkinter.StringVar()
        table_entry6 = tkinter.Entry(window, textvariable=impulse, validate="focusout",
                                     validatecommand=lambda: print(impulse.get()))
        table_entry6.grid(row=2, column=1)

        table_entry7 = tkinter.Label(window, text="Max Thrust:")
        table_entry7.grid(row=3, column=0)
        max_thrust = tkinter.StringVar()
        table_entry8 = tkinter.Entry(window, textvariable=max_thrust, validate="focusout",
                                     validatecommand=lambda: print(max_thrust.get()))
        table_entry8.grid(row=3, column=1)

        table_entry9 = tkinter.Label(window, text="2nd Engine Fire Time:")
        table_entry9.grid(row=4, column=0)
        engine_fire_time = tkinter.StringVar()
        table_entry10 = tkinter.Entry(window, textvariable=engine_fire_time, validate="focusout",
                                      validatecommand=lambda: print(engine_fire_time.get()))
        table_entry10.grid(row=4, column=1)

    def simulate_window(self):
        """
        Creates a window for simulation display.

        :return: None
        """

        window = tkinter.Toplevel(self.master)
        window.title("Simulations")
        window.geometry("640x480")

        combo_box_value = tkinter.StringVar()
        combo_box = tkinter.ttk.Combobox(window, textvariable=combo_box_value)
        # TODO: Do more than print value
        combo_box.bind("<<ComboboxSelected>>", lambda get_value: print(combo_box.get()))
        combo_box['values'] = ('Height vs Acceleration', 'Velocity vs Time', 'Acceleration vs Time')

        combo_box.current(0)
        combo_box.place(relx=0.30, rely=0.95, anchor=tkinter.SE)


def run():
    """
    Runs the main window.

    :return: None
    """

    x = "480"
    y = "320"

    root = tkinter.Tk()
    root.geometry(x + "x" + y)
    Window(root)
    root.mainloop()


if __name__ == "__main__":
    run()
