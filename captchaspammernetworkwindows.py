from selenium import webdriver
import time
from threading import Thread
import socket

botarmycount = 22
basename = 'Bot'
gamepin = ''
executablepath='path2executable4chrome'
# these are the possible combinations for the kahoot anti bot verification
# [('red', 'grn', 'ylw', 'ble'), ('red', 'grn', 'ble', 'ylw'), ('red', 'ylw', 'grn', 'ble'), ('red', 'ylw', 'ble', 'grn'), ('red', 'ble', 'grn', 'ylw'), ('red', 'ble', 'ylw', 'grn'), ('grn', 'red', 'ylw', 'ble'), ('grn', 'red', 'ble', 'ylw'), ('grn', 'ylw', 'red', 'ble'), ('grn', 'ylw', 'ble', 'red'), ('grn', 'ble', 'red', 'ylw'), ('grn', 'ble', 'ylw', 'red'), ('ylw', 'red', 'grn', 'ble'), ('ylw', 'red', 'ble', 'grn'), ('ylw', 'grn', 'red', 'ble'), ('ylw', 'grn', 'ble', 'red'), ('ylw', 'ble', 'red', 'grn'), ('ylw', 'ble', 'grn', 'red'), ('ble', 'red', 'grn', 'ylw'), ('ble', 'red', 'ylw', 'grn'), ('ble', 'grn', 'red', 'ylw'), ('ble', 'grn', 'ylw', 'red'), ('ble', 'ylw', 'red', 'grn'), ('ble', 'ylw', 'grn', 'red')]
# by trying every combo at once we can get bots in on that kahoot and ruin some learning fun

# the stuff up here is to control the program remotely, this would not run on my phone and i wanted to be able to use it on the go
# use port forwarding to use it outside the network
host = '192.168.0.103'
port = 4444     # non privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print host , port
s.listen(1)
conn, addr = s.accept()

def response():
    while True:
        data = conn.recv(1024)
        data.split()
        print('testprint')
        print(data)
        try:
            if data == 'exit':
                conn.close()
                exit()
            elif data == 'start':
                bruteforce()
            else:
                global gamepin
                gamepin = data
        except socket.error:
            print "Error Occured."
            break

# this is just an unused reference function it is never called
# this is a function to connect to a kahoot once without any anti bot 2 step verification

def connecttokahoot():
    objectnm = webdriver.Chrome()
    objectnm.set_window_size(200, 200)
    objectnm.get("https://kahoot.it")
    #making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    objectnm.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    objectnm.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    objectnm.find_element_by_id('username').send_keys(basename)
    objectnm.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1.5)

#the next 4 functions are all to press the individual buttons for the two step verification they are used in the combo fucntions

def red(objectnm):
    objectnm.find_element_by_class_name('two-factor-auth-sequence__card--0').click()

def ble(objectnm):
    objectnm.find_element_by_class_name('two-factor-auth-sequence__card--1').click()

def grn(objectnm):
    objectnm.find_element_by_class_name('two-factor-auth-sequence__card--2').click()

def ylw(objectnm):
    objectnm.find_element_by_class_name('two-factor-auth-sequence__card--3').click()

#you will see the list of combonations as i was two lazy to scroll up and copy and paste so many times
# red ylw grn ble red ylw ble grn red ble grn ylw red ble ylw grn grn red ylw ble grn red ble ylw grn ylw red ble grn ylw ble red grn ble red ylw grn ble ylw red ylw red grn ble ylw red ble grn ylw grn red ble ylw grn ble red ylw ble red grn ylw ble grn red ble red grn ylw ble red ylw grn ble grn red ylw ble grn ylw red ble ylw red grn ble ylw grn red

#this starts every browser window at once so we can bruteforce that goddamn 2 step verification
def bruteforce():
    Thread(target=lambda: combo1execution()).start()
    Thread(target=lambda: combo2execution()).start()
    Thread(target=lambda: combo3execution()).start()
    Thread(target=lambda: combo4execution()).start()
    Thread(target=lambda: combo4execution()).start()
    Thread(target=lambda: combo5execution()).start()
    Thread(target=lambda: combo6execution()).start()
    Thread(target=lambda: combo7execution()).start()
    Thread(target=lambda: combo8execution()).start()
    Thread(target=lambda: combo9execution()).start()
    Thread(target=lambda: combo10execution()).start()
    Thread(target=lambda: combo11execution()).start()
    Thread(target=lambda: combo12execution()).start()
    Thread(target=lambda: combo13execution()).start()
    Thread(target=lambda: combo14execution()).start()
    Thread(target=lambda: combo15execution()).start()
    Thread(target=lambda: combo16execution()).start()
    Thread(target=lambda: combo17execution()).start()
    Thread(target=lambda: combo18execution()).start()
    Thread(target=lambda: combo19execution()).start()
    Thread(target=lambda: combo20execution()).start()
    Thread(target=lambda: combo21execution()).start()
    Thread(target=lambda: combo22execution()).start()
    Thread(target=lambda: combo23execution()).start()
    Thread(target=lambda: combo24execution()).start()

# the flood function is never called this was my first attempt at brute forcing the captcha. I wanted to make one
# function i could call over and over, but it didnt work out, so i wrote them all individually. yay

# quick explanation each execution function completes the actions needed to join the game with a certian code for
# two step verification, it keeps looping until it joins into the selected game. The functions that enter the code are
# the combo functions

def flood(combonumber, botname):
    try:
        confirmed = webdriver.Chrome()
        confirmed.get("https://kahoot.it")
        basename = 'bot'
        for i in range(1, 25):
            basename + str(i)
            # making sure the browser loads lol hey future me u dumb fuck
            time.sleep(1)
            confirmed.find_element_by_css_selector('#inputSession').send_keys(gamepin)
            confirmed.find_element_by_css_selector('.btn-greyscale').click()
            time.sleep(.5)
            confirmed.find_element_by_id('username').send_keys(botname)
            confirmed.find_element_by_css_selector('.btn-greyscale').click()
            time.sleep(.5)
            combonumber(confirmed)
            time.sleep(2)
            confirmed.execute_script("window.open('https://kahoot.it')")
    except Exception:
        pass

def combo1(proc):
    red(proc)
    grn(proc)
    ylw(proc)
    ble(proc)

def combo1execution():
    basename = 'bot1'
    combo1proc = webdriver.Chrome(executable_path=executablepath)
    print combo1proc.title
    combo1proc.set_window_size(500, 500)
    combo1proc.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    combo1proc.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    combo1proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    combo1proc.find_element_by_id('username').send_keys(basename)
    combo1proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo1(combo1proc)
            time.sleep(5)
            try:
                combo1proc.find_element_by_css_selector('status-bar')
                time.sleep(3)
                flood(combo1(combo1proc))
            except Exception:
                combo1(combo1proc)
                time.sleep(5)
        except Exception:
            pass

def combo2(proc):
    red(proc)
    grn(proc)
    ble(proc)
    ylw(proc)

def combo2execution():
    basename = 'bot2'
    combo2proc = webdriver.Chrome(executable_path=executablepath)
    print combo2proc.title
    combo2proc.set_window_size(500, 500)
    combo2proc.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    combo2proc.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    combo2proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    combo2proc.find_element_by_id('username').send_keys(basename)
    combo2proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:

        try:
            combo2(combo2proc)
            time.sleep(5)
            while True:
                try:
                    combo2proc.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo2(combo2proc))
                except Exception:
                    combo2(combo2proc)
                    time.sleep(5)
        except Exception:
            pass

def combo3(proc):
    red(proc)
    grn(proc)
    ble(proc)
    ylw(proc)

def combo3execution():
    basename = 'bot3'
    combo3proc= webdriver.Chrome(executable_path=executablepath)
    print combo3proc.title
    combo3proc.set_window_size(500, 500)
    combo3proc.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    combo3proc.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    combo3proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    combo3proc.find_element_by_id('username').send_keys(basename)
    combo3proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo3(combo3proc)
            time.sleep(5)
            while True:
                try:
                    combo3proc.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo3(combo3proc))
                except Exception:
                    combo3(combo3proc)
                    time.sleep(5)
        except Exception:
            pass

def combo4(proc):
    red(proc)
    grn(proc)
    ble(proc)
    ylw(proc)

def combo4execution():
    basename = 'bot4'
    combo4proc= webdriver.Chrome(executable_path=executablepath)
    print combo4proc.title
    combo4proc.set_window_size(500, 500)
    combo4proc.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    combo4proc.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    combo4proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    combo4proc.find_element_by_id('username').send_keys(basename)
    combo4proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo4(combo4proc)
            time.sleep(5)
            while True:
                try:
                    combo4proc.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo4(combo4proc))
                except Exception:
                    combo4(combo4proc)
                    time.sleep(5)
        except Exception:
            pass

# red ble grn ylw red ble ylw grn grn red ylw ble grn red ble ylw grn ylw red ble grn ylw ble red grn ble red ylw grn ble ylw red ylw red grn ble ylw red ble grn ylw grn red ble ylw grn ble red ylw ble red grn ylw ble grn red ble red grn ylw ble red ylw grn ble grn red ylw ble grn ylw red ble ylw red grn ble ylw grn red

def combo5(proc):
    red(proc)
    grn(proc)
    ble(proc)
    ylw(proc)

def combo5execution():
    basename = 'bot5'
    combo5proc= webdriver.Chrome(executable_path=executablepath)
    print combo5proc.title
    combo5proc.set_window_size(500, 500)
    combo5proc.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    combo5proc.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    combo5proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    combo5proc.find_element_by_id('username').send_keys(basename)
    combo5proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo5(combo5proc)
            time.sleep(5)
            while True:
                try:
                    combo5proc.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo5(combo5proc))
                except Exception:
                    combo5(combo5proc)
                    time.sleep(5)
        except Exception:
            pass

def combo6(objectnm):
    ble(objectnm)
    ylw(objectnm)
    grn(objectnm)
    grn(objectnm)

def combo6execution():
    try:
        execution = webdriver.Chrome()
        basename = 'bot6'
        print execution.title
        execution.set_window_size(200, 200)
        execution.get("https://kahoot.it")
        # making sure the browser loads lol hey future me u dumb fuck
        time.sleep(1)
        execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
        time.sleep(1.5)
        execution.find_element_by_css_selector('.btn-greyscale').click()
        time.sleep(1)
        execution.find_element_by_id('username').send_keys(basename)
        execution.find_element_by_css_selector('.btn-greyscale').click()
        time.sleep(1.5)
        combo6(execution)
        time.sleep(1)
        flood(combo6(execution))
        while True:
            try:
                execution.find_element_by_css_selector('screen__main')
                flood(combo6(execution))
            except Exception:
                combo6(execution)
                time.sleep(5)
    except Exception:
        pass

def combo7(objectnm):
    red(objectnm)
    ble(objectnm)
    grn(objectnm)
    ylw(objectnm)

def combo7execution():
    basename = 'bot7'
    combo7proc= webdriver.Chrome(executable_path=executablepath)
    print combo7proc.title
    combo7proc.set_window_size(500, 500)
    combo7proc.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    combo7proc.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    combo7proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    combo7proc.find_element_by_id('username').send_keys(basename)
    combo7proc.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo7(combo7proc)
            time.sleep(5)
            while True:
                try:
                    combo7proc.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo7(combo7proc))
                except Exception:
                    combo7(combo7proc)
                    time.sleep(5)
        except Exception:
            pass

def combo8execution():
    basename = 'bot8'
    execution= webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo8(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo8(execution))
                except Exception:
                    combo8(execution)
                    time.sleep(5)
        except Exception:
            pass


def combo8(objectnm):
    red(objectnm)
    ble(objectnm)
    ylw(objectnm)
    grn(objectnm)

# grn ylw red ble grn ylw ble red grn ble red ylw grn ble ylw red ylw red grn ble ylw red ble grn ylw grn red ble ylw grn ble red ylw ble red grn ylw ble grn red ble red grn ylw ble red ylw grn ble grn red ylw ble grn ylw red ble ylw red grn ble ylw grn red

def combo9(objectnm):
    grn(objectnm)
    red(objectnm)
    ylw(objectnm)
    ble(objectnm)

def combo9execution():
    basename = 'bot9'
    execution= webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo9(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo8(execution))
                except Exception:
                    combo9(execution)
                    time.sleep(5)
        except Exception:
            pass


def combo10(objectnm):
    grn(objectnm)
    red(objectnm)
    ble(objectnm)
    ylw(objectnm)

def combo10execution():
    basename = 'bot10'
    execution= webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo10(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo10(execution))
                except Exception:
                    combo10(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo11(objectnm):
    grn(objectnm)
    ylw(objectnm)
    red(objectnm)
    ble(objectnm)
# ylw grn ble red ylw ble red grn ylw ble grn red ble red grn ylw ble red ylw grn ble grn red ylw ble grn ylw red ble ylw red grn ble ylw grn red

def combo11execution():
    basename = 'bot11'
    execution= webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo11(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo11(execution))
                except Exception:
                    combo11(execution)
                    time.sleep(5)
        except Exception:
            pass


def combo12(objectnm):
    grn(objectnm)
    ble(objectnm)
    red(objectnm)
    ylw(objectnm)

def combo12execution():
    basename = 'bot12'
    execution= webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo12(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo8(execution))
                except Exception:
                    combo12(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo13(objectnm):
    grn(objectnm)
    ble(objectnm)
    ylw(objectnm)
    red(objectnm)

def combo13execution():
    basename = 'bot13'
    execution= webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo13(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo13(execution))
                except Exception:
                    combo13(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo14(objectnm):
    ylw(objectnm)
    red(objectnm)
    grn(objectnm)
    ble(objectnm)

def combo14execution():
    basename = 'bot14'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo14(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo14(execution))
                except Exception:
                    combo14(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo15(objectnm):
    ylw(objectnm)
    red(objectnm)
    ble(objectnm)
    grn(objectnm)

def combo15execution():
    basename = 'bot15'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo15(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo15(execution))
                except Exception:
                    combo15(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo16(objectnm):
    ylw(objectnm)
    grn(objectnm)
    red(objectnm)
    ble(objectnm)

def combo16execution():
    basename = 'bot16'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo16(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo16(execution))
                except Exception:
                    combo16(execution)
                    time.sleep(5)
        except Exception:
            pass
# ble red ylw grn ble grn red ylw ble grn ylw red ble ylw red grn ble ylw grn red

def combo17(objectnm):
    ylw(objectnm)
    ble(objectnm)
    red(objectnm)
    grn(objectnm)

def combo17execution():
    basename = 'bot17'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo17(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo13(execution))
                except Exception:
                    combo17(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo18(objectnm):
    ylw(objectnm)
    ble(objectnm)
    grn(objectnm)
    red(objectnm)

def combo18execution():
    basename = 'bot18'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo18(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo18(execution))
                except Exception:
                    combo18(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo19(objectnm):
    ble(objectnm)
    red(objectnm)
    grn(objectnm)
    ylw(objectnm)

def combo19execution():
    basename = 'bot19'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo19(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo19(execution))
                except Exception:
                    combo19(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo20(objectnm):
    ble(objectnm)
    red(objectnm)
    ylw(objectnm)
    grn(objectnm)

def combo20execution():
    basename = 'bot20'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo20(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo20(execution))
                except Exception:
                    combo20(execution)
                    time.sleep(5)
        except Exception:
            pass
# ble red ylw grn ble grn red ylw ble grn ylw red ble ylw red grn ble ylw grn red

def combo21(objectnm):
    ble(objectnm)
    grn(objectnm)
    red(objectnm)
    ylw(objectnm)

def combo21execution():
    basename = 'bot21'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo21(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo21(execution))
                except Exception:
                    combo21(execution)
                    time.sleep(5)
        except Exception:
            pass
def combo22(objectnm):
    ble(objectnm)
    grn(objectnm)
    ylw(objectnm)
    red(objectnm)

def combo22execution():
    basename = 'bot22'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo22(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo22(execution))
                except Exception:
                    combo22(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo23(objectnm):
    ble(objectnm)
    ylw(objectnm)
    red(objectnm)
    grn(objectnm)

def combo23execution():
    basename = 'bot23'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo23(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo23(execution))
                except Exception:
                    combo23(execution)
                    time.sleep(5)
        except Exception:
            pass

def combo24(objectnm):
    ble(objectnm)
    ylw(objectnm)
    grn(objectnm)
    red(objectnm)

def combo24execution():
    basename = 'bot24'
    execution = webdriver.Chrome(executable_path=executablepath)
    print execution.title
    execution.set_window_size(500, 500)
    execution.get("https://kahoot.it")
    # making sure the browser loads lol hey future me u dumb fuck
    time.sleep(1)
    execution.find_element_by_css_selector('#inputSession').send_keys(gamepin)
    time.sleep(5)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(1)
    execution.find_element_by_id('username').send_keys(basename)
    execution.find_element_by_css_selector('.btn-greyscale').click()
    time.sleep(3)
    while True:
        try:
            combo24(execution)
            time.sleep(5)
            while True:
                try:
                    execution.find_element_by_css_selector('status-bar')
                    time.sleep(3)
                    flood(combo24(execution))
                except Exception:
                    combo24(execution)
                    time.sleep(5)
        except Exception:
            pass

response()
