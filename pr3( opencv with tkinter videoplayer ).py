
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import cv2

class videoplayer:

    def __init__(self, window, window_name):
        self.window = window
        self.window.title(window_name)

        top_frame = Frame(self.window)
        top_frame.pack(side=TOP, pady=5)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM, pady=5)

        self.canvas = Canvas(top_frame)
        self.canvas.pack()

        self.btn1=Button(bottom_frame, text="select video file", width=20, command= self.open_file)
        self.btn1.grid(row=0, column=0 )

        self.btn2 = Button(bottom_frame, text="Play", width=20, command=self.play)
        self.btn2.grid(row=0, column=1)

        self.btn3 = Button(bottom_frame, text="Pause", width=20, command=self.pause)
        self.btn3.grid(row=0, column=2)

        self.delay = 10

        self.window.mainloop()

    def open_file(self):
        
        self.pause = False

        self.file = filedialog.askopenfilename(title="Select file", filetypes=(("MP4 files","*.mp4"),("WMV files", "*.wmv"), ("AVI files", "*.avi")))

        print(self.file)

        self.cap = cv2.VideoCapture(self.file)

        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.canvas.config(width = self.width, height=self.height)

    def get_frame(self):   # get only one frame

        try:

            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        except:
            messagebox.showerror(title='Video file not found', message='Please select a video file.')

    def play(self):

        ret, frame= self.get_frame()

        if ret :
            self.photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor=NW)

        if not self.pause:
            self.window.after(self.delay, self.play)

    def pause(self):
        self.pause = True

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

videoplayer(Tk(), "player")
