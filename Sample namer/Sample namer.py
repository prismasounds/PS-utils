import tkinter as tk

def delete_on_click(event):
    event.widget.delete(0, "end")

def update_text(text):

    display.configure(state="normal")
    display.delete(1.0, tk.END)
    display.insert(1.0, text[:-1])
    display.configure(state="disabled")

    display.clipboard_clear()
    display.clipboard_append(text[:-1])

def name_samples():

    dyn_range = dyn.get()

    if RR.get():
        n_rr = RR.get()
    else:
        n_rr = 1

    text = ""
    for note in range (int(lownote.get()), int(hinote.get())+1):
        for rr in range (1, int(n_rr)+1):
            text += str(note) + "_" + dyn_range + "_rr" + str(rr) + ","

    update_text(text)

# GUI

window = tk.Tk()
window.geometry("600x450")
window.title("Automatically name samples")
window.resizable(False, False)

container = tk.Frame(window)
container.pack(side=tk.BOTTOM)

canvas = tk.Canvas(window, width = 400, height = 100)
canvas.pack()

# Lower note
lownoteLabel = "Lowest note"
lownoteLabel= tk.Label(window, text=lownoteLabel)
canvas.create_window(50, 30, window=lownoteLabel)

lowtut = tk.StringVar() 
lowtut.set('(MIDI value)') 

lownote = tk.Entry(window, textvariable=lowtut)
canvas.create_window(200, 30, window=lownote)

lownote.bind("<Button-1>", delete_on_click)

# Higher note
hinoteLabel = "Highest note"
hinoteLabel= tk.Label(window, text=hinoteLabel)
canvas.create_window(50, 50, window=hinoteLabel)

hitut = tk.StringVar() 
hitut.set('(MIDI value)') 

hinote = tk.Entry(window, textvariable=hitut)
canvas.create_window(200, 50, window=hinote)

hinote.bind("<Button-1>", delete_on_click)

# n of RR
RRLabel = "Round Robins"
RRLabel= tk.Label(window, text=RRLabel)
canvas.create_window(50, 70, window=RRLabel)

rrtut = tk.StringVar() 
rrtut.set('(N. of round robins)') 

RR = tk.Entry(window, textvariable=rrtut)
canvas.create_window(200, 70, window=RR)

RR.bind("<Button-1>", delete_on_click)

# Dynamic range
dynLabel = "Dynamic range"
dynLabel= tk.Label(window, text=dynLabel)
canvas.create_window(50, 90, window=dynLabel)

dyn = tk.StringVar() 
dyn.set('(e.g. "dyn1" or "1-127")')

dyn = tk.Entry(window, textvariable=dyn)
canvas.create_window(200, 90, window=dyn)

dyn.bind("<Button-1>", delete_on_click)

# Start button
start_button = tk.Button(window,text="Start", command=name_samples)
canvas.create_window(375, 50, window=start_button)

# Instructions
instruct = 'Insert the range, the number of RR and the dynamic range, then hit "Start".\nThe names will be automatically copied to your clipboard separated by commas.'
tuto = tk.Label(window, text=instruct)
tuto.pack()

# display results
results = tk.Canvas(window, width = 600, height = 300)
results.pack( expand=True)

display = tk.Text(results)
display.configure(state="disabled")
display.configure(inactiveselectbackground=display.cget("selectbackground"))
display.pack()

if __name__ == "__main__":
    window.mainloop()