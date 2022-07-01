import serial
import tkinter as tk
from tkinter import ttk
import modul2

def com_changed():
    return selected_com.get()

def button_clicked():
    global arduino
    arduino = serial.Serial(com_changed(), baudrate=9600)

def led_on():
    arduino.write(b'1')
    print('led_on')
def led_off():
    arduino.write(b'0')
    print('led_off')

app=tk.Tk()
app.title('combobox')
app.geometry('600x200')

selected_com = tk.StringVar()
com_cb = ttk.Combobox(app, textvariable=selected_com)
com_cb['values'] = modul2.serial_ports()
com_cb['state'] = 'readonly'
com_cb['height'] = 5
com_cb['width'] = 25
com_cb.grid()
com_cb.bind('<<ComboboxSelected>>', com_changed)

button=tk.Button(app,text='connect',command=button_clicked)
button.grid()

bt1=tk.Button(app,text='bat',command=led_on)
bt2=tk.Button(app,text='tat',command=led_off)

bt1.grid()
bt2.grid()

app.mainloop()