# Importing necessary packages to be used
from tkinter import *
from PIL import Image as PIL_Image
from PIL import ImageTk
import cv2
from tkinter import messagebox
import sys

def displayOutputInCanvas():
    # Creating 9 sub frames inside the master_frame
    frame1 = Frame(master=master_frame, width=1380, pady=10, bg='white')
    frame2 = Frame(master=master_frame, width=1380, pady=20, bg='white')
    frame3 = Frame(master=master_frame, width=1380, pady=5, bg='lightgrey')
    frame4 = Frame(master=master_frame, width=1380, pady=20, bg='white')
    frame5 = Frame(master=master_frame, width=1380, pady=10, bg='white')
    frame6 = Frame(master=master_frame, width=1380, pady=10, bg='white')
    frame7 = Frame(master=master_frame, width=1380, pady=10, bg='white')
    frame8 = Frame(master=master_frame, width=1380, pady=10, bg='white')
    frame9 = Frame(master=master_frame, width=1380, pady=10, bg='white')

    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack(pady=(30, 0))
    frame5.pack()
    frame6.pack()
    frame7.pack(pady=(30, 0))
    frame8.pack()
    frame9.pack()
    
    title = Label(master=frame1, text='VIRTUAL MEMORY MANAGEMENT SIMULATOR', font='Script 30', fg='#007700', bg='white')
    title.pack()

    subtitle1 = Label(master=frame2, text='Results', font='Script 22', fg='green', bg='white')
    subtitle1.pack(side=LEFT, padx=10)

    height = 6
    width = 2
    data = [['Number of Processes     ', ':  ' + PROCESS_COUNT],
            ['Number of Memory Requests', ':  ' + MEMORY_REQ_COUNT], 
            ['Fetch Policy ', ':  ' + PAGING],
            ['Replacement Policy', ':  ' + REPLACEMENT], 
            ['Page size ', ':  ' + PAGE_SIZE], 
            ['Number of Page Faults ', ':  ' + PAGE_FAULTS]]

    for i in range(height):  # Rows
        for j in range(width):  # Columns
            fgcolor = 'black'
            if j == 1 and i == 5:
                fgcolor = 'red'
            elif j == 1:
                fgcolor = 'orange'

            b = Entry(frame3, fg=fgcolor, font='Script 16', bg='white', highlightthickness=0, borderwidth=0, width=40, disabledbackground='white', disabledforeground=fgcolor)
            b.grid(row=i, column=j)
            b.insert(END, data[i][j])
            b['state'] = DISABLED
    
    subtitle2 = Label(master=frame4, text='Statistics', font='Script 22', fg='green', bg='white')
    subtitle2.pack(side=LEFT, padx=10)

    plottitle1 = Label(master=frame5, text='Plot 1: Number of pagefaults VS Page size', font='Script 18', fg='black', bg='white')
    plottitle1.pack(side=LEFT, padx=10)

    # Displaying plot 1
    canvas1 = Canvas(master=frame6, width=1000, height=560, bg='white')  
    canvas1.pack()

    image = cv2.imread('./Plots/plot1.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (1000, 560))
    image = PIL_Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    canvas1.image = image
    canvas1.create_image(0, 0, anchor=NW, image=image) 

    plottitle2 = Label(master=frame7, text='Plot 2: Number of pagefaults for different combinations of paging and replacement methods', font='Script 18', fg='black', bg='white')
    plottitle2.pack(side=LEFT, padx=10)

    # Displaying plot 2
    canvas2 = Canvas(master=frame8, width=1000, height=560, bg='white')  
    canvas2.pack()

    image = cv2.imread('./Plots/plot2.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (1000, 560))
    image = PIL_Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    canvas2.image = image
    canvas2.create_image(0, 0, anchor=NW, image=image)

def main():
    argData = sys.argv

    global PROCESS_COUNT, MEMORY_REQ_COUNT, PAGING, REPLACEMENT, PAGE_SIZE, PAGE_FAULTS

    PROCESS_COUNT = argData[1]
    MEMORY_REQ_COUNT = argData[2]
    PAGING = argData[3]
    REPLACEMENT = argData[4]
    PAGE_SIZE = argData[5]
    PAGE_FAULTS = argData[6]

    displayOutputInCanvas()

def scrollbar_function(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=1380, height=785)

if __name__ == '__main__':
    root = Tk()
    root.title('Virtual Memory Management - Results')
    root.resizable(False, False)
    root.config(bg='white')

    # Updated window size to 1400x800
    window_height = 800
    window_width = 1400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    # Main frame
    main_frame = Frame(root, relief=GROOVE, bd=1, bg='white')
    main_frame.place(x=0, y=0)

    # Canvas setup
    canvas = Canvas(main_frame, bg='white')
    master_frame = Frame(canvas, bg='white', padx=10, pady=10)

    myscrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=master_frame, anchor='nw')
    master_frame.bind("<Configure>", scrollbar_function)

    main()
    root.mainloop()


'''# Importing necessary packages to be used
from tkinter import *
from PIL import Image as PIL_Image
from PIL import ImageTk
import cv2
from tkinter import messagebox
import sys


def displayOutputInCanvas():
    # Creating 4 sub frames inside the master_frame
    frame1 = Frame(master = master_frame, width = 1530, pady = 10, bg = 'skyblue')
    frame2 = Frame(master = master_frame, width = 1530, pady = 20, bg = 'skyblue')
    frame3 = Frame(master = master_frame, width = 1530, pady = 5, bg = 'aquamarine')
    frame4 = Frame(master = master_frame, width = 1530, pady = 20, bg = 'skyblue')
    frame5 = Frame(master = master_frame, width = 1530, pady = 10, bg = 'skyblue')
    frame6 = Frame(master = master_frame, width = 1530, pady = 10, bg = 'skyblue')
    frame7 = Frame(master = master_frame, width = 1530, pady = 10, bg = 'skyblue')
    frame8 = Frame(master = master_frame, width = 1530, pady = 10, bg = 'skyblue')
    frame9 = Frame(master = master_frame, width = 1530, pady = 10, bg = 'skyblue')

    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack(pady=(30, 0))
    frame5.pack()
    frame6.pack()
    frame7.pack(pady=(30, 0))
    frame8.pack()
    frame9.pack()
    
    title = Label(master=frame1,text='VIRTUAL MEMORY MANAGEMENT SIMULATOR',font='Script 35',fg='#23ff0f',bg='skyblue')
    title.pack()

    subtitle1 = Label(master=frame2, text='Results', font='Script 25',fg='#9932cc',bg='skyblue')
    subtitle1.pack(side=LEFT,padx=10)

    height = 6
    width = 2
    data = [['Number of Processes     ', ':  ' + PROCESS_COUNT],
            ['Number of Memory Requests', ':  ' + MEMORY_REQ_COUNT], 
            ['Fetch Policy ', ':  ' + PAGING],
            ['Replacement Policy', ':  ' + REPLACEMENT], 
            ['Page size ', ':  ' + PAGE_SIZE], 
            ['Number of Page Faults ', ':  ' + PAGE_FAULTS]]

    for i in range(height): #Rows
        for j in range(width): #Columns
            fgcolor = ''

            if j == 0:
                fgcolor = 'black'
            elif i == 5:
                fgcolor = 'red'
            else:
                fgcolor = 'magenta'

            b = Entry(frame3, fg = fgcolor, font='Script 20', bg='skyblue', highlightthickness=0, highlightbackground = "skyblue", borderwidth=0, width=40, disabledbackground='skyblue', disabledforeground=fgcolor)
            b.grid(row=i, column=j)
            b.insert(END, data[i][j])
            b['state'] = DISABLED
    
    subtitle2 = Label(master=frame4, text='Statistics', font='Script 25',fg='light green',bg='skyblue')
    subtitle2.pack(side=LEFT,padx=10)

    plottitle1 = Label(master=frame5, text='Plot 1: Number of pagefaults VS Page size', font='Script 20',fg='black',bg='skyblue')
    plottitle1.pack(side=LEFT,padx=10)

    # Displaying plot 1
    canvas1 = Canvas(master=frame6, width = 1100, height = 619)  
    canvas1.pack()

    image = cv2.imread('./Plots/plot1.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (1100, 619))
    image = PIL_Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    canvas1.image = image
    canvas1.create_image(0, 0, anchor=NW, image=image) 

    plottitle2 = Label(master=frame7, text='Plot 2: Number of pagefaults for different combinations of paging and replacement methods', font='Script 20',fg='black',bg='skyblue')
    plottitle2.pack(side=LEFT,padx=10)

    # Displaying plot 2
    canvas2 = Canvas(master=frame8, width = 1100, height = 619)  
    canvas2.pack()

    image = cv2.imread('./Plots/plot2.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (1100, 619))
    image = PIL_Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    canvas2.image = image
    canvas2.create_image(0, 0, anchor=NW, image=image) 


def main():
    # Arguments
    argData = sys.argv

    global PROCESS_COUNT, MEMORY_REQ_COUNT, PAGING, REPLACEMENT, PAGE_SIZE, PAGE_FAULTS

    PROCESS_COUNT = argData[1]
    MEMORY_REQ_COUNT = argData[2]
    PAGING = argData[3]
    REPLACEMENT = argData[4]
    PAGE_SIZE = argData[5]
    PAGE_FAULTS = argData[6]

    displayOutputInCanvas()


# Configuring the scroll bar widget and canvas widget
def scrollbar_function(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1530,height=795)


if __name__ == '__main__':
    # Declaring root window and specifying its attributes
    root=Tk()
    root.title('Virtual Memory Management - Results')
    root.resizable(False, False)
    root.config(bg = 'skyblue')

    # Defining attributes of root window
    root.resizable(False, False) 
    window_height = 800
    window_width = 1550

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # Creating a main frame inside the root window
    main_frame=Frame(root,relief=GROOVE, bd=1, bg = 'skyblue')
    main_frame.place(x=0,y=0) # Placing the frame at (10, 10)

    # Creating a canvas inside main_frame
    canvas=Canvas(main_frame, bg = 'skyblue')
    master_frame=Frame(canvas, bg = 'skyblue', padx = 10, pady=10)  # Creating master_frame inside the canvas

    # Inserting  and configuring scrollbar widget
    myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=master_frame,anchor='nw')
    master_frame.bind("<Configure>",scrollbar_function)

    main()    

    # Open the root window and loop
    root.mainloop()'''