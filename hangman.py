from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as mb
import random as r

#to install pip use 'pip install Pillow'

root = Tk()
#title of tkinter 
root.title('HangMan') 
#icon of tkinter
root.iconbitmap("HG-icon.ico") #icon of tkinter

l0 = Label(root, text="")
l0.grid(row = 0, column = 1)
l1 = Label(root, text="")
l1.grid(row = 0, column = 2)

#placing images 
hangman_text = Image.open("hangman_title.jpeg") #defining the image 
hangman_text = hangman_text.resize((1165,230)) #(height, width)
image1 = ImageTk.PhotoImage(hangman_text)
l_title = Label(image = image1) #storing the image 
l_title.grid(row = 0, column = 3)  #displaying the image on the screen
Bollywood = 'BOLLYWOOD'
Hollywood = 'HOLLYWOOD'
Places = 'PLACES'
General = 'GENERAL'

chosen_c = ''

def game(cat):    
    global l_underscore,chosen_c,l6_page3,l_dummy_page3,l1_hanging,b1_page3,b2_page3,b3_page3,b4_page3,b5_page3
    chosen_c = cat
    
    count = 1
    
    l6_page3.grid_forget()
    l_dummy_page3.grid_forget()
    b1_page3.grid_forget()
    b2_page3.grid_forget()
    b3_page3.grid_forget()
    b4_page3.grid_forget()
    b5_page3.grid_forget()
    
    
    #default image 
    l1_hanging.grid(row = 0, column = 0)
    
    ltrial1_dummy_game = Label(root, text='')
    ltrial1_dummy_game.grid(row=0,column=1)
    
    ltrial2_dummy_game = Label(root, text='')
    ltrial2_dummy_game.grid(row=1,column=0)
    

    #words=['movie','table','laptop','paper']
    if cat=="HOLLYWOOD":
        words = ['TENET','AVENGERS','AVATAR','THOR','IRONMAN','JOKER','JUMANJI','CONJURING','FROZEN','INSIDIOUS','GRAVITY','SPIDERMAN','DEADPOOL','LUCY','ANNABELLE','SKYFALL','BUMBLEBEE','HELLBOY','SALT','TITANIC','PARASITE','TANGLED','AQUAMAN','SHAZAM','MADAGASCAR','OBLIVION','ALADDIN','TWILLIGHT']
    
    if cat=="BOLLYWOOD":
        words = ['WAR','DANGAL','GULLYBOY','CHHAPAAK','BAHUBALI','DRISHYAM','KICK','RAAZI','URI','BAAGHI','PADMAAVAT','KRRISH','DHOOM','ANDHADHUN','TOILET','BHARAT','PADMAN','KALANK','DILWALE','SHOLAY','BARFI','LAGAN','GHAJINI','CHEF','TANHAJI','ABCD','SAAHO','GOLMAAL','KABHIL','SANJU','GOLDMEDAL','KESARI','PANGA','BHOOT']
    
    if cat=="PLACES":
        words = ['ROME','ITALY','HAWAII','KENYA','CANADA','ISTHANBUL','TURKEY','CAMBODIA','LONDON','ENGLAND','MANHATTAN','PARIS','FRANCE','MOROCCO','BALI','INDONESIA','IRELAND','SYDNEY','AUSTRALIA','ASIA','EUROPE','JAIPUR','VARANASI','MANALI','MUNNAR','GOA','JODHPUR','SHIMLA','BANGALORE','MANGALORE','JAISALMER','KOLKOTA','KOVALAM','MYSURU','MUSSORIE','AMRITSAR','GANGTOK','HYDERABAD','WAYANAD','KODAIKANAL','LADAKH','SRINAGAR','OOTY','COORG','TOKYO','VENICE','BEIJING','TIBET','AMSTERDAM','BARCELONA','BERLIN','VIENNA','ICELAND','ISTANBUL','ATHENS','FLORENCE','MUNICH','MILAN','MOSCOW','FRANKFURT','SALZBUG','BRUSSELS','PISA','MELBOURNE','PERTH','DARWIN','CANBERRA','TOWNSVILLE','DUBAI','OMAN','IRAQ','SINGAPORE','BORNEO','JAPAN','EGYPT','MEXICO','IRAN','PERU','HASSAN','CHENNAI','SURAT','KOCHI','KOLLAM','GWALIOR','UJJAIN','INDORE','JHANSI','JABALPUR','SANCHI','PATNA','LEPAKSHI','KURNOOL','NELLORE','SALEM','THANJAVUR','PUNE','MATHERAN','NASHIK']
    
    if cat=="GENERAL":
        words = ['COP','GEM','DIM','FLY','VEX','JOB','YAM','OAK','USE','ZIP','WET','TON','IVY','MUG','OPT','AGE','KIT','NIL','RAP','INCH','ACED','CALM','BOND','DISH','EELS','GAZE','JINX','LOAN','KITE','MEGA','JAZZ','ZINC','YOKE','ZERO','QUIZ','HUNT','POUT','SAGE','FUZZ','HOOD','SLOT','ALIGN','WRECK','QUACK','LUCID','CLIFF','PIZZA','ETHER','GROWL','PROBE','CHOKE','TEARS','ABODE','BANGS','BARES','DAIRY','DANCE','DATED','DEVIL','EBONY','EAGLE','FABLE','FAITH','FAKER','GAUGE','GLAND','ISSUE','ICONS','HAWKS','HEDGE','KNOCK','LAUGH','LEARN','MARRY','MAYOR','NAVAL','NINJA','OASIS','OPERA','PEACH','PASTA','YUMMY','VIVID','VILLA','VENUE','YOUNG','GNOME','AMENDS','BUSTLE','BRUISE','KIDNAP','TRAUMA','LEAGUE','POUNCE','VOYEUR','BUZZER','NEWELS','SHEWED','ABACUS','ABIDED','BACONS','BAGDES','CACTUS','CANALS','DECENT','DEEMED','FALCON','FABRIC','HARBOR','HASSLE','JUNIOR','JERSEY','KNIGHT','KNIVES','LOBOUR','LADDER','LAWYER','LAPTOP','MARVEL','MANUAL','MARINE','NAUSEA','NOVELS','ONIONS','ORACLE','OUNCES','PANTRY','PATRON','PIXELS','PLAQUE','PRAYER','PYTHON','QUARTZ','RUSTIC','SENSOR','SOCCER','SQUASH','STEREO','SUMMON','SYNTAX','TACTIC','TEAMED','TENDER','THESIS','TOXIC','TUNNEL','VACCUM','VIOLIN','VOYAGE','VISION','WALNUT','WEAPON','WHILST','WISDOM','WORTHY','YOGURT','ZOMBIE','HANDOUT','BISCUIT','ANTIQUE','FOREIGN','WRIGGLE','PSYCHIC','DECENT','BATTERY','ECONOMY','GADGETS','GLIMPSE','IMMENSE','LICENSE','MAXIMUM','KEYNOTE','HOUSING','FINACES','FOCUSED','REVERE','SEAGULL','PENGUIN','ISOLATE','TORNADE','BOYCOTT','MINIMUM','NOMINEE','NUCLEUS','NEEDLES','PICTURE','PAYMENT','PATTERN','RELEASE','REGIONS','SCIENCE','SESSION','UNKNOWN','TRAFFIC','THEATRE','TEXTURE','VITAMIN','VACCINE','WESTERN','UNAWARE','WEBSITE','CILANTRO','RENEGADE','QUIZZING','PICKLOCK','REBUKING','FOGGIEST','LUTETIUM','PULPWOOD','JUNKYARD','MATCHBOX','CLOUDILY','CUFFLINK','DISGUISE','CHLORINE','ASPHYXIA','VIBRATOR','STRUMPET','CALENDER','CONCRETE','DISCOUNT','DOMINATE','ESTIMATE','EVIDENCE','FEEDBACK','FRONTIER','HUMANITY','JUDICIAL','MAGAZINE','MEDIEVAL','MORTGAGE','OPTIMISM','OVERSEAS','PETITION','PORTABLE','RIGOROUS','SCHEDULE','SPECTRUM','SYNDROME','TAXATION','WARRANTY','UNLAWFUL','YOURSELF','PULVERIZE','WORKHOUSE','ANCHORAGE','VALUATION','TESTIMONY','OXYGENISE','QUIBBLING','SOVKHOZES','ZOOGRAPHY','COLOPHONY','HELPFULLY','POLYMORPH','WOLFHOUND','RECITATION','CIRTUITRY','OBSESSION','RESTRAINT','RASPBERRY','SUNFLOWER','ALLOTMENT','DEMOCRACY','KNOWLEDGE','PROSTHETICS','IMMORTALITY','STIPULATION','RECITATION','DISQUALIFY','CHEQUEBOOK','HODGEPODGE','DOUBTFULLY','FLAVOURING','DECLASSIFY','BROTHERHOOD','YOUTHFULLY','DYSPROSIUM','SEQUENTIAL','SNOWFLAKES','COMPELLING','BULLDOZING','CONSCIENCE','RESUSCITATE','PHOTOGRAPH','PUZZLEMENT','NARCISSISM','PUZZLEMENT','ADVANTAGES','APPLICANTS','ATTACHMENT','BLINDFOLDS','CANDIDATES','CEREMONIES','COLLECTORS','COMPLIMENT','CURRENCIES','DESIGNATORS','DELIMITERS','DIMENSIONS','DISTORTION','ENCOUNTER','FORECASTLE','HARDCOPIES','INCREMENT','INJECTION','INVESTMENT','LONGITUDE','MILESTONE','NEGLIGENCE','PARTISION','POSSESSION','PRIORITIES','POPORTION','RECOVERIES','RESEARCHER','REVOLUTION','STATEMENT','SUBROUTINE','TACHOMETER','TOLERANCE','VALIDATION','WHOLESALE']
    
    word_chosen=r.choice(words)  #choosing random word
    print(word_chosen)  #printing random word (in command prompt) for reference
        
    
    hint = list(word_chosen) #variable for hint 
    count_vowels = set()
    for i in hint:
        if i in ['A','E','I','O','U']:
            count_vowels.add(i)
            
    len_vowels = len(count_vowels)
    
    def hint():
        hint_label.grid(row=0,column=11) #displays number of vowels
        
    hint_label = Label(root, text = str(len_vowels)+" vowel(s)", font = ("Gill Sans",20),fg='white',bg='black') 
    hint_button = Button(root, text="HINT",command = hint, bg="black",fg = "white",font=('Lemon Milk Bold',12), width=5).grid(row=4,column = 10)
    
    l1_text=list('_'*len(word_chosen)) #stores the list of underscores depending on length of word_chosen
    l1=StringVar() #tkinter variable used to modify label's text
    l1.set(' '.join(l1_text))
    l_underscore = Label(root, textvariable = l1, font=('Lemon Milk Bold',25))
    l_underscore.grid(row=0, column=3, columnspan=4, padx=10)
    
    def guess(ch): #guess is used to update underscore label if the letter is present in word_chosen, otherwise updates the hangman image
        global name_page2,l_underscore,disp,l2_hanging, l3_hanging, l4_hanging, l5_hanging, l6_hanging, l7_hanging
        nonlocal hint_label,count
        disp=l1.get()     #stores text in label l_underscore (l1)
        guessed=disp.split(' ')                
        if word_chosen.count(ch)>0:
            for c in range(len(word_chosen)):
                    if word_chosen[c]==ch: 
                        guessed[c]=ch
                        l1.set(' '.join(guessed))
                        if guessed==list(word_chosen):
                            mb.showinfo("End","YOU WON")
                            result = mb.askyesno(
                            title = 'HangMan',
                            message = 'Try Again ?')
                            if result:
                                l2_hanging.grid_forget()
                                l3_hanging.grid_forget()
                                l4_hanging.grid_forget()
                                l5_hanging.grid_forget()
                                l6_hanging.grid_forget()
                                l7_hanging.grid_forget()
                                l_underscore.destroy()
                                hint_label.destroy()
                                game(chosen_c)     #chosen_c is the category chosen by the user
                            elif not result:
                                exit()
                    
                        
        elif count==1:
            count = 2
            l1_hanging.grid_forget()
            l2_hanging.grid(row = 0, column = 0)
        elif count==2:
            count=3
            l2_hanging.grid_forget()
            l3_hanging.grid(row = 0, column = 0)
        elif count==3:
            count=4
            l3_hanging.grid_forget()
            l4_hanging.grid(row = 0, column = 0)
        elif count==4:
            count=5
            l4_hanging.grid_forget()
            l5_hanging.grid(row = 0, column = 0)
        elif count==5:
            count=6
            l5_hanging.grid_forget()
            l6_hanging.grid(row = 0, column = 0)
        elif count==6:
            l6_hanging.grid_forget()
            l7_hanging.grid(row = 0, column = 0)
            m_gameover = mb.showinfo("GAME OVER","The word was "+word_chosen)
            result = mb.askyesno(title = 'HangMan', message = 'Try Again ?')
            
            if result:
                l7_hanging.grid_forget()
                l_underscore.destroy()
                hint_label.destroy()
                game(chosen_c)
            elif not result:
                exit()
    
    def vkeypad():   #creates keypad on the game window
        Button(root, text='Q', command=lambda: guess('Q'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=2)
        Button(root, text='W', command=lambda: guess('W'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=3)
        Button(root, text='E', command=lambda: guess('E'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=4)
        Button(root, text='R', command=lambda: guess('R'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=5)
        Button(root, text='T', command=lambda: guess('T'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=6)
        Button(root, text='Y', command=lambda: guess('Y'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=7)
        Button(root, text='U', command=lambda: guess('U'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=8)
        Button(root, text='I', command=lambda: guess('I'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=9)
        Button(root, text='O', command=lambda: guess('O'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=2, column=10)
        Button(root, text='P', command=lambda: guess('P'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=2)
        Button(root, text='A', command=lambda: guess('A'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=3)
        Button(root, text='S', command=lambda: guess('S'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=4)
        Button(root, text='D', command=lambda: guess('D'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=5)
        Button(root, text='F', command=lambda: guess('F'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=6)
        Button(root, text='G', command=lambda: guess('G'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=7)
        Button(root, text='H', command=lambda: guess('H'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=8)
        Button(root, text='J', command=lambda: guess('J'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=9)
        Button(root, text='K', command=lambda: guess('K'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=3, column=10)
        Button(root, text='L', command=lambda: guess('L'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=2)
        Button(root, text='Z', command=lambda: guess('Z'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=3)
        Button(root, text='X', command=lambda: guess('X'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=4)
        Button(root, text='C', command=lambda: guess('C'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=5)
        Button(root, text='V', command=lambda: guess('V'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=6)
        Button(root, text='B', command=lambda: guess('B'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=7)
        Button(root, text='N', command=lambda: guess('N'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=8)
        Button(root, text='M', command=lambda: guess('M'), width=5,font=('Lemon Milk Bold',12), bg='red',relief = RIDGE).grid(row=4, column=9)
    vkeypad()

def page2():
    global l_dummy1_page2,l_2_page2,l_dummy2_page2,l3_page2,l4_page2,l5_page2,l6_page2,l7_page2,l8_page2,l9_page2,b_name_page2,name_page2 
    l_dummy1_page2.grid(row = 1) #dummy row
    l_2_page2.grid(row = 2) #label instruction
    l_dummy2_page2.grid(row = 3) #dummy row
    l3_page2.grid(row = 4) #inst1
    l4_page2.grid(row=5) #inst2
    l5_page2.grid(row=6) #inst3
    l6_page2.grid(row=7) #inst4
    l7_page2.grid(row=8) #inst5
    l8_page2.grid(row=9) #white space 
    l9_page2.grid(row=11)#ENTER PLAYER NAME LABEL
   
    b_name_page2.grid(row=13)

def page3():
    global l_dummy1_page2,l_2_page2,l_dummy2_page2,l3_page2,l4_page2,l5_page2,l6_page2,l7_page2,l8_page2,l9_page2,l_dummy,b_name
    l_dummy1_page2.destroy() #dummy row
    l_2_page2.destroy() #label instruction
    l_dummy2_page2.destroy() #dummy row
    l3_page2.destroy() #inst1
    l4_page2.destroy() #inst2
    l5_page2.destroy() #inst3
    l6_page2.destroy() #inst4
    l7_page2.destroy() #inst5
    l8_page2.destroy() #dummy row
    l9_page2.destroy() #dummy row
      
    b_name_page2.destroy() #next page button
    
    l_dummy_page3.grid(row = 1)
    l6_page3.grid(row = 1)
    b1_page3.grid(row=1,column=1)#movies
    b2_page3.grid(row=1,column=2)#places
    b3_page3.grid(row=1,column=3)#general

#page 2 widgets
l_dummy1_page2 = Label(root, text = "") 
l_2_page2 = Label(root, text = "INSTRUCTIONS", font = ("Sorta",85),fg="white",bg="black",width=20)
l_dummy2_page2 = Label(root,text = "")
l3_page2 = Label(root, text = "1. Your GOAL is to guess the word to save the HANGMAN from hanging.", font = ("Gill Sans",22))
l4_page2 = Label(root, text = "2. Fill in the blanks by guessing one letter at a time to see if it’s in the word.", font = ("Gill Sans",22))
l5_page2 = Label(root, text = "3. Click on the letter to guess it.", font = ("Gill Sans",22))
l6_page2 = Label(root, text = "4. If you have guessed correctly, the letter will appear in the blank spaces.", font = ("Gill Sans",22))
l7_page2 = Label(root, text = "5. You can also use the HINT button.", font = ("Gill Sans",22))

#dummy spaces below instructions
l8_page2 = Label(root, text = "")
l9_page2 = Label(root, text = "")

b_name_page2 = Button(root, text = "NEXT PAGE", font = ("LEMON MILK BOLD",15), command = page3,relief = RIDGE)

#page3 widgets
def Movies():
    global b4_page3, b5_page3
    b4_page3.grid(row = 2, column = 1)#bollywood button
    b5_page3.grid(row = 3, column = 1)#hollywood button

l_dummy_page3 = Label(root, text = "") #WHITE SPACE
l6_page3 = Label(root, text = "CHOOSE CATEGORY", font = ("Rogueland Bold",22))

b1_page3 = Button(root, text = "MOVIES", font = ("Gill Sans",20),command = Movies,width=11)
b2_page3 = Button(root, text = "PLACES", font = ("Gill Sans",20),width=11,command = lambda : game(Places))
b3_page3 = Button(root, text = "GENERAL", font = ("Gill Sans",20),width=11,command = lambda :  game(General))
b4_page3 = Button(root, text = "BOLLYWOOD",font = ("Gill Sans",20),command = lambda : game(Bollywood))
b5_page3 = Button(root, text = "HOLLYWOOD",font = ("Gill Sans",20),command = lambda : game(Hollywood))

#game function widgets 
#default image 
hanging1 = Image.open("hangman1.jpeg") #defining the image 
hanging1  = hanging1.resize((387,383)) #(height, width)
image1_game = ImageTk.PhotoImage(hanging1)
l1_hanging = Label(image = image1_game) #storing the image

#image2 
hanging2 = Image.open("hangman2.jpeg") #defining the image 
hanging2  = hanging2.resize((387,383)) #(height, width)
image2_hanging = ImageTk.PhotoImage(hanging2)
l2_hanging = Label(image = image2_hanging) #storing the image

#image3
hanging3 = Image.open("hangman3.jpeg") #defining the image 
hanging3  = hanging3.resize((387,383)) #(height, width)
image3_hanging = ImageTk.PhotoImage(hanging3)
l3_hanging = Label(image = image3_hanging) #storing the image

#image4
hanging4 = Image.open("hangman4.jpeg") #defining the image 
hanging4  = hanging4.resize((387,383)) #(height, width)
image4_hanging = ImageTk.PhotoImage(hanging4)
l4_hanging = Label(image = image4_hanging) #storing the image

#image5
hanging5 = Image.open("hangman5.jpeg") #defining the image 
hanging5  = hanging5.resize((387,383)) #(height, width)
image5_hanging = ImageTk.PhotoImage(hanging5)
l5_hanging = Label(image = image5_hanging) #storing the image

#image6
hanging6 = Image.open("hangman6.jpeg") #defining the image 
hanging6  = hanging6.resize((387,383)) #(height, width)
image6_hanging = ImageTk.PhotoImage(hanging6)
l6_hanging = Label(image = image6_hanging) #storing the image

#image7
hanging7 = Image.open("hangman7.jpeg") #defining the image 
hanging7  = hanging7.resize((387,383)) #(height, width)
image7_hanging = ImageTk.PhotoImage(hanging7)
l7_hanging = Label(image = image7_hanging) #storing the image



def delete_label():
    global l_dummy1_page1,l_dummy2_page1,b1,l0,l1,l_title
    l_dummy1_page1.destroy()
    l_dummy2_page1.destroy()
    l0.destroy()
    l1.destroy()
    l_title.destroy()
    b1.destroy()
    page2()

l_dummy1_page1 = Label(root, text = "")
l_dummy1_page1.grid(row = 1,column = 1)

l_dummy2_page1 = Label(root, text = "")
l_dummy2_page1.grid(row = 1,column = 2)


page3_count = 1
b1 = Button(root, text = "Click here to PLAY",font = ("Gill Sans",20), command = delete_label,relief = RIDGE)
b1.grid(row = 1, column = 3)

root.mainloop()