import tkinter as Tkinter
from tkinter import *
from datetime import datetime
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ClockAndPlot(Tkinter.Tk):
    def __init__(self):
        super(ClockAndPlot, self).__init__()
        self.geometry('{}x{}'.format(410, 520))
        self.title('Plot Spiral')
        self.resizable(0, 0)
        self.padx = 3
        self.pady = 3

        # clock widget settings
        self.clock_width = 480
        self.clock_height = 50
        self.clock_box_color = 'green'
        self.clock_tick = 1

        # clock frame
        self.top_frame = Frame(self, bg=self.clock_box_color, width=self.clock_width, height=self.clock_height,
                               pady=self.pady, padx=self.padx)
        self.top_frame.grid(row=0)
        self.clock = Label(self.top_frame, text="clock", font=("Courier", 20, 'bold'))
        self.clock.grid(row=0, column=0, columnspan=1)

        # plot widget settings
        self.plot_width = 480
        self.plot_height = 25
        self.plot_box_color = 'gray2'

        # spiral settings
        self.initial_r = 1
        self.delta_r = -0.002
        self.initial_phi = 0.1
        self.delta_phi = 0.1
        self.point_tick = 100

        # plot frame
        self.center_frame = Frame(self, bg=self.plot_box_color, width=self.plot_width, height=self.plot_height,
                                  pady=self.pady, padx=self.padx)
        self.center_frame.grid(row=1,sticky='e')
        self.fig = matplotlib.figure.Figure(figsize=(2, 2), dpi=200)
        #self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.fig, master=self.center_frame)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.center_frame)
        self.canvas.get_tk_widget().grid(row=1, column=0,  sticky='e')
        self.ax = self.fig.add_subplot(111)
        self.ax.axis([-1.5, 1.5, -1.5, 1.5])
        self.ax.set_aspect("equal")

        # button widget settings
        self.button_width = 480
        self.button_height = 50
        self.button_box_color = 'white'

        # button frame
        self.bottom_frame = Frame(self, bg=self.button_box_color, width=self.button_width, height=self.button_height,
                                  pady=self.pady, padx=self.padx)
        self.bottom_frame.grid(row=3)

        # set quit  button function
        self.quit_button = Button(self.bottom_frame, text="Quit", command=self.my_destroy, font=("Courier", 20, 'bold'))
        self.quit_button.grid(row=0, column=1, sticky="s")

        # set sart  button function
        self.start_button = Button(self.bottom_frame, text="Start", command=self.start, font=("Courier", 20, 'bold'))
        self.start_button.grid(row=0, column=0)

    def start(self):
        self.run_clock()
        self.create_plot()

    def my_destroy(self):
        self.update()
        self.destroy()
        self.quit()
        Tkinter.Tk().quit()

    def run_clock(self):
        def print_time():
            self.clock.config(text=self.get_current_time(), font=("Courier", 20, 'bold'))
            self.after(1, print_time)
        print_time()

    @staticmethod
    def get_current_time():
        now = datetime.now()
        return "%s:%s:%s" % (now.hour, now.minute, now.second)

    def create_plot(self):
        global phi, r
        phi = self.initial_phi
        r = self.initial_r

        def plot_point():
            global phi, r
            phi += self.delta_phi
            r += self.delta_r
            x, y = self.circle(phi, r)
            self.ax.plot(x, y, '.')
            self.after(self.point_tick, plot_point)
            self.canvas.draw()
        plot_point()

    @staticmethod
    def circle(phi, r):
        return np.array([r*np.cos(phi), r*np.sin(phi)])


if __name__=="__main__":
    App = ClockAndPlot()
    App.mainloop()