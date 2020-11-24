from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
import time

class MyProgram:
    def __init__(self,win):

        self.start_bttn = tk.Button(win,text = 'Start',command = self.start_func)
        self.take_cmmd_bttn = tk.Button(win,text='Command',command = self.take_cmmd)
        self.ss_bttn = tk.Button(win,text = 'Screenshot', command = self.s_shot)
        self.tab1_bttn = tk.Button(win,text = 'Change to Tab 1',command = self.change_tab_1)
        self.tab2_bttn = tk.Button(win,text = 'Change to Tab 2',command = self.change_tab_2)
        self.tab3_bttn = tk.Button(win,text = 'Change to Tab 3',command = self.change_tab_3)
        self.slider_left_bttn = tk.Button(win,text = 'Slider Left',command = self.slider_left)
        self.slider_right_bttn = tk.Button(win,text = 'Slider Right',command = self.slider_right)
        self.l_inc = tk.Label(win,text = 'Increment:')
        self.e_inc = tk.Entry(win)
        self.e_inc.insert(0,'10')
        self.e_inc.bind('<Return>',self.get_inc)
        self.l_time = tk.Label(win,text = 'Waiting Time:')
        self.e_time = tk.Entry(win)
        self.e_time.insert(0,'10')
        self.e_time.bind('<Return>',self.get_time)

        self.start_bttn.grid(row = 0, column = 0, columnspan = 2)
        self.take_cmmd_bttn.grid(row = 1, column = 0, columnspan = 2)
        self.ss_bttn.grid(row = 2, column = 0, columnspan = 2)
        self.tab1_bttn.grid(row = 3, column = 0, columnspan = 2)
        self.tab2_bttn.grid(row = 4, column = 0)
        self.tab3_bttn.grid(row = 4, column = 1)
        self.slider_left_bttn.grid(row = 5, column = 0)
        self.slider_right_bttn.grid(row = 5, column = 1)
        self.l_inc.grid(row = 6, column = 0)
        self.e_inc.grid(row =6, column = 1)
        self.l_time.grid(row = 7, column = 0)
        self.e_time.grid(row =7, column = 1)

        self.get_inc()
        self.get_time()

        self.browser = webdriver.Firefox(executable_path = './geckodriver')
        self.browser.fullscreen_window()
        self.browser.get('https://lms.gazi.edu.tr')

        # Daha hızlı giriş yapabilmek için aşağıda Your school number kısmına numaranızı
        # Your password kısmına şifrenizi yazınız. Program başladığında otomatik
        # giriş yapılır.

        # time.sleep(1)
        # username = self.browser.find_element_by_xpath('//*[@id="UserName"]')
        # username.send_keys('Your school number')
        # username.send_keys(Keys.RETURN)
        # time.sleep(1)
        # paswd = self.browser.find_element_by_xpath('//*[@id="Password"]')
        # paswd.send_keys('your password')
        # paswd.send_keys(Keys.RETURN)

        self.slider_pos = -350
    def slider_left(self):
        self.slider = self.browser.find_element_by_xpath('//*[@id="rec-slider"]')
        move = ActionChains(self.browser)
        self.slider_pos -= self.incrmnt
        move.click_and_hold(self.slider).move_by_offset(self.slider_pos, 0).release().perform()

    def slider_right(self):
        self.slider = self.browser.find_element_by_xpath('//*[@id="rec-slider"]')
        move = ActionChains(self.browser)
        self.slider_pos += self.incrmnt
        move.click_and_hold(self.slider).move_by_offset(self.slider_pos, 0).release().perform()



    def start_func(self):
        self.slider = self.browser.find_element_by_xpath('//*[@id="rec-slider"]')
        move = ActionChains(self.browser)
        move.move_to_element(self.slider)
        move.click_and_hold(self.slider).move_by_offset(self.slider_pos, 0).release().perform()
        time.sleep(self.wait_time)
        while self.slider_pos < 350:
            move = ActionChains(self.browser)
            self.slider_pos += self.incrmnt
            move.move_to_element(self.slider)
            move.click_and_hold(self.slider).move_by_offset(self.slider_pos, 0).release().perform()
            time.sleep(self.wait_time)
            t = time.localtime()
            current_time = time.strftime("%H_%M_%S",t)
            self.browser.save_screenshot('./Images/IMG_'+current_time+'.png')


    def s_shot(self):
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S",t)
        self.browser.save_screenshot('./Images/IMG_'+current_time+'.png')

    def take_cmmd(self):
        cmmd = 'print("Hello")'
        while(cmmd != 'quit'):
            cmmd = input('Command: ')
            exec(cmmd)

    def change_tab_1(self):
        self.browser.switch_to_window(self.browser.window_handles[0])

    def change_tab_2(self):
        self.browser.switch_to_window(self.browser.window_handles[1])

    def change_tab_3(self):
        self.browser.switch_to_window(self.browser.window_handles[2])

    def get_inc(self,*args):
        inc_str = self.e_inc.get()
        inc_int = int(inc_str)
        self.incrmnt = inc_int

    def get_time(self,*args):
        time_str = self.e_time.get()
        time_int = int(time_str)
        self.wait_time = time_int


win = tk.Tk()
win.title('Selenium APP')
prog = MyProgram(win)
win.mainloop()
