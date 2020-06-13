#apt-get install ffmpeg libavcodec-extra
#pip install pydub

from tkinter import Tk, Label, Button
from tkinter import filedialog
from tkinter.ttk import * 
#from tkinter import font
from tkinter import *
import time
import threading 
from pydub import AudioSegment
from pydub.playback import play
import os

#helv36 = font.Font(family='Helvetica', size=12, weight='bold')
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Voice Style Transfer")
        master.minsize(400,100)
        #canvas = Canvas(self.master,width=100,height=100)
        #photo=PhotoImage(file="voice_wave.gif")
        #img1 = photo.subsample(50, 50) 
  
       
        self.label = Label(master, text="To upload the voice to be converted:")
        self.label.grid(row=0,column=0,pady=3)
        self.to_play=[]
        self.played=[]
        self.threads=[]
        self.output_folder=""
        self.input_button = Button(master, text="Upload audio", fg='#3369ab',activebackground="white",activeforeground="black",borderwidth="3",relief="raised", command=self.upload)
        self.input_button.grid(row=0,column=1,pady=3)
        #gui related threads
        self.t1=""
        self.t2=""
        #main code thread
        self.t3=""
        self.inputf = ""
        self.outputf = ""
        self.stop_threads=False
        self.label2 = Label(master, text="To select the output voice folder:")
        self.label2.grid(row=1,column=0,pady=3)
        self.output_button=Button(master, text="Output folder",fg='#3369ab',activebackground="white",activeforeground="black",borderwidth="3",relief="raised", command=self.select_output)
        self.output_button.grid(row=1,column=1,pady=3)
        
        
        self.convert_button = Button(master, text="Convert",fg='#3369ab',activebackground="white",activeforeground="black",borderwidth="3",relief="raised",command=self.convert_audio)
        self.convert_button.grid(row=2,column=0,pady=5)

        self.close_button = Button(master, text="Play", fg='#3369ab',activebackground="white",activeforeground="black",borderwidth="3",relief="raised",command=self.playing)
        self.close_button.grid(row=2,column=1,padx=5,pady=5)
        self.play_button = Button(master, text="CLOSE", fg='#db0b0b',activebackground="white",activeforeground="black",borderwidth="3",relief="raised",command=self.quit)
        self.play_button.grid(row=3,column=0,padx=5,pady=5)
        #canvas.grid(row=3,column=0,columnspan=100)
        #canvas.create_image(100,100, anchor=NW, image=photo)  
        
        
    def select_output(self):
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory(initialdir = "/home/arpit-mint/Desktop/Voice_Converter_CycleGAN",title = "Select folder")
        self.output_folder= '/home/arpit-mint/Desktop/Voice_Converter_CycleGAN/data/converted_voices'
    
    def upload(self):
        root = Tk()
        root.filename =  filedialog.askdirectory(initialdir = "/home/arpit-mint/Desktop/Voice_Converter_CycleGAN",title = "Select folder")
        print(root.filename)
        self.inputf = root.filename
        #print(self.input)
        root.destroy()


    #to play the sounds as they are generated
    def playing(self):
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = self.output_folder,title = "Select file",filetypes = (("all files","*.*"),("audio files","*.wav")))
        audio1 = AudioSegment.from_file(root.filename)
        play(audio1)
        

    #converting
    def converting(self):
	    print(os.getcwd())
	    #/home/arpit-mint/Desktop/Voice_Converter_CycleGAN/data/evaluation_all/SF1
	    cmd = 'python convert.py --model_dir ./model/sf1_tf2 --model_name sf1_tf2.ckpt --data_dir '+self.inputf+' --conversion_direction A2B --output_dir ./converted_voices'
	    print(cmd)
	    os.system(cmd)	
	    self.stop_threads=True


    def convert_audio(self):
        self.converting()


    def quit(self):
        self.stop_threads=True
        sys.exit()
        #time.sleep(2)
        #self.t1.join()
        #self.t2.join()
        #self.t3.join()
        self.master.destroy()

root = Tk()
root.geometry('400x400')
root.configure(background='#d3d3d3')
my_gui = MyFirstGUI(root)
root.mainloop()
