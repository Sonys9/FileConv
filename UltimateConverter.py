from pathlib import Path
import threading

print('Запуск... Пожалуйста, подождите')

try:

    try: 
        from tkinter import filedialog
        from customtkinter import *                                                                                                                                                                                                                                                                                                                                                                                            ; print('TG: @M5STICKHACK')

    except:

        print('Устанавливаем модуль CustomTkinter...')                                      

        os.system('pip install setuptools')
        os.system('pip install tkinter')
        os.system('pip install customtkinter')

        try: 

            from customtkinter import * 
            from tkinter import filedialog

            print('Модуль CustomTkinter установлен!')                                                                                                                                                                                                                                                                                                                                         ; print('TG: @M5STICKHACK')

        except: 

            input('Не удалось установить модуль CustomTkinter.')

except Exception as e: input('Ошибочка вышла: '+e)

fileee=None
fileee2=None

def choicefile(s):

    global infoo, fileee, infoo2, fileee2

    file_path = filedialog.askopenfilename()
    if file_path: 
        filename = file_path.split('/')[-1]
        if len(filename) > 18:res = filename[:20]+'...'
        else:res = filename

        if s==1:
            infoo.configure(text=res)
            fileee=file_path
        else: 
            infoo2.configure(text=res)
            fileee2=file_path

dirr = None

def choicedir():

    global dirr, infoo3

    dir_path = filedialog.askdirectory()
    if dir_path: 
        filename = dir_path.split('/')[-1]
        if len(filename) > 18:res = filename[:20]+'...'
        else:res = filename
        
        dirr = dir_path
        infoo3.configure(text=res)

def get_all_files(directory):return [file for file in Path(directory).rglob('*') if file.is_file()]

def save():

    file_path = filedialog.asksaveasfilename(
        title="Сохранить файл",
        defaultextension=".bin", 
        filetypes=(("IR файл", "*.ir"), ('RF файл', '*.sub'), ("Все файлы", "*.*"))
    )
    
    return file_path

                
def go(i):
    global ress, start
    with open(i, 'r') as ff: 
        print(i)
        con = ff.read()
        if 'Filetype' in con:
            for i, v in enumerate(con.split('\n')):
                if 'Filetype' in v and 'Filetype' not in start: start+=v+'\n'
                elif 'Version' in v and 'Version' not in start: start+=v+'\n'
                elif 'name' in v and con.split('\n')[i-1]!='#': ress+='#'+'\n'+v
                #Filetype: Flipper SubGhz RAW File
                #Version: 1
                #Frequency: 433920000
                #Preset: FuriHalSubGhzPresetOok650Async
                #Protocol: RAW
                elif 'Frequency' in v and 'Frequency' not in start: start+=v+'\n'
                elif 'Preset' in v and 'Preset' not in start: start+=v+'\n'
                elif 'Protocol' in v and 'Protocol' not in start: start+=v+'\n'
                else: ress+=v+'\n'

def dircomp(): 

    global dirr, ress, start

    #dir = r'C:\Users\SystemX\Downloads\irs'
    if dirr:

        allfiles = get_all_files(dirr)

        ress = []
        start = ''
        res = ''
        thrs = []

        for i in allfiles:

            if str(i).endswith('.ir') or str(i).endswith('.sub'):

                thr = threading.Thread(target=go, args=(i,))
                thr.start()
                thrs.append(thr)

                add_log(f'Совмещаем {i}...')

            else: add_log(f'Пропускаем {i}...')

        for thr in thrs: thr.join()

        for resss in ress: res+=resss

        for i in range(10): 
            ress=res.replace('# \n#\nname:', '#\nname:')
            ress=res.replace('#\n#\nname:', '#\nname:')

        dirrr = save()
        
        if dirrr and dirrr!='':

            with open(dirrr, 'w') as f:

                f.write(start+res)

def compill():

    global fileee, fileee2
    
    if fileee and fileee2:

        res = ''
        start = ''

        for i in [fileee,fileee2]:

            if str(i).endswith('.ir') or str(i).endswith('.sub'):
                
                with open(i, 'r') as ff: 
                    print(i)
                    add_log(f'Совмещаем {i}...')
                    con = ff.read()
                    if 'Filetype' in con:
                        for i, v in enumerate(con.split('\n')):
                            if 'Filetype' in v and 'Filetype' not in start: start+=v+'\n'
                            elif 'Version' in v and 'Version' not in start: start+=v+'\n'
                            elif 'name' in v and con.split('\n')[i-1]!='#': res+='#'+'\n'+v
                            #Filetype: Flipper SubGhz RAW File
                            #Version: 1
                            #Frequency: 433920000
                            #Preset: FuriHalSubGhzPresetOok650Async
                            #Protocol: RAW
                            elif 'Frequency' in v and 'Frequency' not in start: start+=v+'\n'
                            elif 'Preset' in v and 'Preset' not in start: start+=v+'\n'
                            elif 'Protocol' in v and 'Protocol' not in start: start+=v+'\n'
                            else: res+=v+'\n'
            else: add_log(f'Пропускаем {i}...')
        for i in range(10): 
            res=res.replace('# \n#\nname:', '#\nname:')
            res=res.replace('#\n#\nname:', '#\nname:')

        dirrr = save()

        if dirrr and dirrr!='':

            with open(dirrr, 'w') as f:

                f.write(start+res)

def add_log(text):
    try:
        global log_text
        log_text.configure(state='normal')
        log_text.insert(END, text + '\n') 
        log_text.see(END)
        log_text.configure(state='disabled')
    except:...

window = CTk()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ;sys.stdout.write("\nТ̷G̵:̷ ̷М̶5̶S̴Т̴I̶С̷К̵Н̶А̶С̴К̴\n")
window.title('IR&RF Files comp')
window.geometry('300x510')
window.resizable(False, False)
set_appearance_mode("dark")

fg = '#008E63'
hover = '#225244'
bg = '#2B2B2B'

CTkFrame(window, width=280, height=130).place(x=10,y=10)

choiceafile = CTkButton(window, text='Выбрать файл', width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: choicefile(1))
choiceafile.place(x=20, y=20)

infoo = CTkLabel(window, text='Файл не выбран', bg_color=bg, font=('Calibri', 15))
infoo.place(x=130, y=20)

choiceafile2 = CTkButton(window, text='Выбрать файл', width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: choicefile(2))
choiceafile2.place(x=20, y=60)

infoo2 = CTkLabel(window, text='2 файл не выбран', bg_color=bg, font=('Calibri', 15))
infoo2.place(x=130, y=60)

compf = CTkButton(window, text='Совместить', width=260, fg_color=fg, bg_color=bg, hover_color=hover, command=compill)
compf.place(x=20, y=100)


CTkFrame(window, width=280, height=90).place(x=10,y=150)

choiceadir = CTkButton(window, text='Выбрать папку', width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=choicedir)
choiceadir.place(x=20, y=160)

infoo3 = CTkLabel(window, text='Папка не выбрана', bg_color=bg, font=('Calibri', 15))
infoo3.place(x=130, y=160)

compf = CTkButton(window, text='Совместить файлы в папке', width=260, fg_color=fg, bg_color=bg, hover_color=hover, command=dircomp)
compf.place(x=20, y=200)


CTkFrame(window, width=280, height=250).place(x=10,y=250)

log_text = CTkTextbox(window, width=260, height=230)
log_text.configure(state='disabled', font=('Calibri', 13))
log_text.place(x=20, y=260)

add_log('Логи будут здесь')

window.mainloop()