from tkinter import *
from tkinter.ttk import Combobox
import time
root = Tk()
root.title('Nazm')
root.geometry('600x400+0+0')
import requests
import bs4

class poets1:
    def Faiz(self):
        faiz = ["'woh aarhey hain,woh aate Hain,aa-rhey honge Shab-e-firaq yeh kehkar guzar diye humne'", "'Kya khoob likhta h tum'"]
        for i in faiz:
            return i
    def tagore(self):
        pass
    def manto(self):
        pass
    def jaun(self):
        pass
    def ghalib(self):
        faiz = ["'Yaad-e-Mazi Aazab Hai Ya Rab................Cheen Lay Mujh Say Hafiza Mera!!!!!!!!'",
                "'Kya khoob likhta h tum'"]
        for i in faiz:
            return i




p1=poets1()

def contentfaiz():
    Label(f2, text='{}'.format(p1.Faiz()), font="-weight bold", bg='#dfa579', fg='BLACK').grid(
        row=11, column=1)
def contentfaiz1():
    Label(f21, text='{}'.format(scrap1()), font="-weight bold", bg='#dfa579', fg='BLACK').grid(
        row=11, column=1)
    Label(f21, text='Faiz Ahmad Faiz was born into a Tataley Jat family[7] on 13 February 1911, in Kala Qader (present-day Faiz Nagar), District Narowal, Punjab,British India.[8][9] ', font="-weight bold", bg='#dfa579', fg='BLACK').grid(
        row=12, column=1)
def contentghalib():
    Label(f2, text='{}'.format(p1.ghalib()), font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=11, column=0)
    Label(f2, text='{}'.format(p1.ghalib()), font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=11, column=0)




def credit():
    if entry11.get()=='yes':
        return content1()
def credit1():
    if entry12.get()=='Faiz ahmed Faiz':
        return contentfaiz()
    elif entry12.get()=='Mirza ghalib':
        return contentghalib()
def credit2():
    if entry122.get()=='Faiz ahmed Faiz':
        return contentfaiz1()





def shayari():
    global f2
    f2 = Frame(root, bg='#dfa579', relief=SUNKEN)
    f2.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    Label(f2, text='Welcome to the world of Nazm and Shayari', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=1, column=1)
    Label(f2, text='If you have to add filters and preference, Type yes,else no', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=2, column=1)
    global entry11
    entry11 = Entry(f2, bg='white')
    entry11.grid(row=3, column=1, sticky=N + S + E + W)
    Button(f2, text='Submit', command=credit, bg='#dfa579', fg='black').grid(row=8, column=1)
    Button(f2, text='Back', command=main, bg='#dfa579', fg='black').grid(row=13, column=1)


def poet(): #shayari
    v2=['Faiz ahmed Faiz', 'Jaun Eliya','Sadat hasan Manto', 'Agha Shahid Ali','Mirza ghalib','Munshi Premchand']
    Label(f2, text='Which poet do you want to read?', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=9, column=1)
    global entry12
    entry12 = Combobox(f2, value=v2)
    entry12.grid(row=10, column=1, sticky=N + S + E + W)
    Button(f2, text='Submit', command=credit1, bg='#dfa579', fg='black').grid(row=12, column=1)

def poet1(): #scrap
    v2 = ['Faiz ahmed Faiz', 'Jaun Eliya', 'Sadat hasan Manto', 'Agha Shahid Ali', 'Mirza ghalib', 'Munshi Premchand']
    global f21
    f21 = Frame(root, bg='#dfa579', relief=SUNKEN)
    f21.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    Label(f21, text='Which poet life story do you want to know??', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=1,
                                                                                                          column=1)
    global entry122
    entry122 = Combobox(f21, value=v2)
    entry122.grid(row=2, column=1, sticky=N + S + E + W)
    Button(f21, text='Submit', command=credit2, bg='#dfa579', fg='black').grid(row=3, column=1)
    Button(f21, text='back', command=main, bg='#dfa579', fg='black').grid(row=13, column=1)




def scrap1():
    res = requests.get('https://en.wikipedia.org/wiki/Faiz_Ahmad_Faiz')
    type(res)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    a=soup.select('h3')
    return a[0].get_text()


def content1():
    Button(f2, text='Poets', command = poet, bg='#dfa579', fg='black').grid(row=4, column=1)
    Button(f2, text='Poems',  bg='#dfa579', fg='black').grid(row=5, column=1)
    Button(f2, text='Nazm',  bg='#dfa579', fg='black').grid(row=6, column=1)
    Button(f2, text='Shayari', bg='#dfa579', fg='black').grid(row=7, column=1)




def main():
    global f1
    f1 = Frame(root, bg='#dfa579', relief=SUNKEN)
    f1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    Label(f1, text='', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=1, column=1)
    Label(f1, text='', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=2, column=2)
    Label(f1, text='', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=3, column=3)
    Button(f1, text='Shayari',command = shayari, bg='white', fg='black').grid(row=9, column=4)
    Label(f1, text='', font="-weight bold", bg='#dfa579', fg='BLACK').grid(row=9, column=5)
    Button(f1, text='Poets', command=poet1, bg='white', fg='black').grid(row=9, column=6)


def first():
    f4 = Frame(root, bg='#dfa579', relief=SUNKEN)
    f4.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    l1 = Label(f4, text=' ', font="-weight bold", bg='#dfa579', fg='BLACK')
    l1.grid(row=1, column=3)
    l1 = Label(f4, text=' ', font="-weight bold", bg='#dfa579', fg='BLACK')
    l1.grid(row=2, column=3)
    l1 = Label(f4, text=' ----------------NAZM.----------------', font="-weight bold", bg='#dfa579', fg='BLACK')
    l1.grid(row=3, column=3)
    time.sleep(1)
    button1 = Button(f4, text='OPEN', command=main, bg='#dfa579', fg='black').grid(row=4, column=3)



if __name__ == '__main__':
    first()
    root.mainloop()