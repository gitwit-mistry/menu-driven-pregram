import os
import pyttsx3
import datetime
import time
import helper_fn

pyttsx3.speak('Welcome to your miniature menu of an operating system')

while True:
    p = input('what can i do for you?')
    if ('run' in p or 'open') and 'chrome' in p:
        if ('dont' in p or 'do not' in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('chrome')
    elif ('run' in p or 'open') and ('notepad' in p) or ('editor' in p):
        if ('dont' in p or 'do not' in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('notepad')
    elif ('run' in p or 'open') and ('media' in p) or ('player' in p) or ('windows media player' in p):
        if ('dont' in p or 'do not' in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('wmplayer')
    elif ('run' in p or 'open') and ('notebook' in p) or ('jupyter' in p):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('jupyter notebook')
    elif ('run' in p or 'open') and ('spotify' in p):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('spotify')
    
    elif ('time' in p) and ('now' in p):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont show it to you =\ ')
        else:    
            time_now = helper_fn.time()
            pyttsx3.speak(time_now)
            print(time_now)
            
    elif ('date' in p):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont show it to you =\ ')
        else:    
            today = helper_fn.today_date()
            pyttsx3.speak("Today's Date is {}".format(today))
            print("Today's Date is",today)
            
    
    elif ('run' in p or 'open') and (('stopwatch' in p) or ('timer' in p)):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont  start timer for you =\ ')
        else:    
            helper_fn.stopwatch()
            
    elif ('run' in p or 'open' in p or 'search' in p) and ('wikipedia' in p):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            result = helper_fn.wiki()
            print(result)
    
    
    
    elif 'break' in p or 'quit' in p:
        pyttsx3.speak('Goodbye and have a good day')
        break
        
        
    else :
        print("Invalid Function or maybe the function is under development....")
        print('Do you want to write a feed back to me so that i can improve?')
        y_n = input('if yes press y else press any other key')
        while y_n == 'y':
            helper_fn.feedback_fn()
            print('thank you for you feedback')
        
