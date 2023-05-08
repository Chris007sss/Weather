import tkinter as tk
import requests
from PIL import Image ,ImageTk


root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")

#key : 1c7909c2c990c435378abccd80827df9
#api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
def format_response(wet):
    try:
        city=(wet['name'])
        condition=wet['weather'][0]['description']
        temp=wet['main']['temp']
        final_str='City%s\nCondition:%s\nTemprature:%s'%(city,condition,temp)
    except:
        final_str='There was a problem retrieving that information'
    return final_str       
     



def get_weather(city):
    weather_key='1c7909c2c990c435378abccd80827df9'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    # print(response.json())

    wet=response.json()

    # print(wet['name'])
    # print(wet['weather'][0]['description'])
    # print(wet['main']['temp'])

    result['text']=format_response(wet)

    # icon_name=wet['weather'][0]['icon']
    # open_image(icon_name)


# def open_image(icon_name):
#     size=int(frame_two.winfo_height()*0.25)
#     # img=ImageTk.PhotoImage(Image.open('./img/'+ icon +'.png').resize((size,size)))
#     img=ImageTk.PhotoImage(Image.open('./img/'+icon +'.png')).resize((size,size))
#     weather_icon.delete('all')
#     weather_icon.create_image(0,0,anchor='nw',image=img)
#     weather_icon.image=img


img=Image.open('./weather.png')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

weather_lbl=tk.Label(root,image=img_photo)
weather_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(weather_lbl,text='Get Weather info for over 150 lakh cities',fg='yellow',bg='purple',font=('times new roman',17,'bold'))
heading_title.place(x=80,y=15)

frame_one=tk.Frame(weather_lbl,bg="sky blue",bd=7)
frame_one.place(x=100,y=50,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',20),width=19)
txt_box.grid(row=0,column=0,sticky='w')


btn=tk.Button(frame_one,text='Show Weather',fg='Red',font=('times new roman',13,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two=tk.Frame(weather_lbl,bg="sky blue",bd=7)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=30,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

# weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
# weather_icon.place(xrel=.75,yrel=0,relwidth=1,relheight=0.5)

root.mainloop()