import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 2
__filename__ = "TwitchAFK"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("http://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("http://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("http://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

import time, threading, random
from pynput.keyboard import Key, Controller

board = Controller()
voc = ["GG", "Nice!", "Wow", "Good job!", "Come on...", "Let's go", "Yeah!", "Good one!"]

def close_window():
    start.destroy()
    os._exit(1)

start = Tk()
if os.path.exists(__iconpath__):
    start.iconbitmap(__iconpath__)
start.configure(bg="black")
start.protocol("WM_DELETE_WINDOW", close_window)
start.geometry("300x120")
start.title(__filename__)

def message():
    for i in range(sys.maxsize**10):
        board.type(random.choice(voc))
        board.press(Key.enter)
        board.release(Key.enter)
        time.sleep(random.randint(80, 120))

def run():
    time.sleep(5)
    thread = threading.Thread(target=message)
    thread.start()

Button(start, text="Start AFK", command=run, relief=GROOVE, width=20, font="impact 20", fg="black", cursor="cross").pack(pady=30)
start.mainloop()
