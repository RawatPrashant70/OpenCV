import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
import datetime

class App:
	def __init__(self, window, window_title, video_source=0):
		self.window = window
		self.window.title(window_title)

		self.cap = Myvideocapture(video_source)

		self.canvas = tkinter.Canvas(window, width=self.cap.width, height=self.cap.height)
		self.canvas.pack()

		self.bt = tkinter.Button(window, text="Snapshot", width=90, command=self.snapshot)
		self.bt.pack(anchor=tkinter.CENTER, expand=True)

		self.bt = tkinter.Button(window, text="video_start", width=90, command=self.videosnapshot)
		self.bt.pack(anchor=tkinter.CENTER, expand=True)

		self.bt = tkinter.Button(window, text="video_stop", width=90, command=self.stoprecording)
		self.bt.pack(anchor=tkinter.CENTER, expand=True)

		self.delay = 4
		self.update()

		self.window.mainloop()

	def videosnapshot(self):

		filename = "R:\ new.avi"
		codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
		framerate = 30
		resolution = (640, 480)

		out = cv2.VideoWriter(filename, codec, framerate, resolution)

		while (True):
			ret, frame = self.cap.get_frame()

			img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

			if ret == True:
				out.write(img)
			else:
				break

	def stoprecording(self):

		messagebox.showinfo(title="Capture", message="done")

		out.release()
		cap.release()


		self.window.quit()
		self.window.destroy()

	def snapshot(self):
		ret, frame =self.cap.get_frame()

		if ret:
			img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

			date = datetime.date.today()
			name = "new" + str(date)

			outpath = "P:\ " + name + ".jpg"

			cv2.imwrite(outpath, img)

			messagebox.showinfo(title="Capture", message="done")

	def update(self):
		ret, frame = self.cap.get_frame()

		if ret:

			self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
			self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

		self.window.after(self.delay, self.update)

class Myvideocapture:
	def __init__(self, video_source=0):
		self.cap = cv2.VideoCapture(video_source)

		if not self.cap.isOpened():
			raise ValueError("UnAble to open video source", video_source)

		self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

		print(self.width)
		print(self.height)

	def get_frame(self):
		if self.cap.isOpened():
			ret, frame = self.cap.read()
			if ret:
				return(ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
			else:
				return(ret, None)
		else:
			return(ret, None)

	def __del__(self):
		if self.cap.isOpened():
			self.cap.release()




App(tkinter.Tk(), "OpenCV")