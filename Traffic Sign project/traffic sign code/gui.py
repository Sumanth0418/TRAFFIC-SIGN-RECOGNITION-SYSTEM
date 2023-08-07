import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_classifier.h5')

#dictionary to label all traffic signs class.
classes = { 1:'All Motor vehicles Prohibited',
            2:'Pedestrians prohibited',      
            3:'Bullock and handcart prohibited',       
            4:'Priority Oncoming Traffic',      
            5:'Truck prohibited',    
            6:'Speed limit (50km/h)',      
            7:'Pedestrians prohibited',     
            8:'Speed limit (100km/h)',    
            9:'Length limit',     
           10:'Overtaking prohibited',   
           11:'No passing veh over 3.5 tons',     
           12:'Man on work',     
           13:'Stop',    
           14:'Give a way',     
           15:'Right turn',       
           16:'No vehicles',       
           17:'Truck Prohibited',       
           18:'Turn left',       
           19:'No Entry',     
           20:'Dangerous curve left',      
           21:'Dangerous curve right',   
           22:'Double curve',      
           23:'Bumpy road',     
           24:'Y intersection',       
           25:'Narrow road ahead',  
           26:'Road work',    
           27:'Traffic signals',      
           28:'Pedestrians',     
           29:'Children crossing',     
           30:'Bicycles crossing',       
           31:'Guarded level crossing',
           32:'Wild animals crossing',      
           33:'Handcart Prohibited',      
           34:'Compulsory Ahead',     
           35:'Hospital',       
           36:'Ahead only',      
           37:'Go straight or right',      
           38:'Resting place',      
           39:'Minimum speed',     
           40:'First aid ',      
           41:'Park both sides',     
           42:'End of no passing',      
           43:'End no passing veh > 3.5 tons'}
                 
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict(image)[0]
    sign_class = numpy.argmax(pred)
    sign = classes[sign_class+1]
    print(sign)
    label.configure(foreground='#011638', text=sign)

   

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Know Your Traffic Sign",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
