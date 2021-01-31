import datetime
import time
import pyttsx3
feed_back_list = []
import wikipedia

def time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def today_date():
    today = datetime.date.today()
    return today


def stopwatch():
    watch = int(input('for how many seconds\t'))
    counter = watch
    n = 0
    while watch>n-1:
        print(counter)
        pyttsx3.speak(counter)
        n += 1
        counter -= 1
    pyttsx3.speak('Your time is up!!!')
    
    
def feedback_fn():
    feed_back = input('please enter your valuable input')
    feed_back_list.append(feed_back)
    
    with open('f1.txt','w') as f:
        f.write('\n'.join(feed_back_list))
        
        
def wiki():
    search = input('enter the word or phrase to search')
    
    result = wikipedia.summary(search, sentences = 2)
    
    return result


def testingfuntion():
    """
    This function is created by jerry
    """
    print("Tester")
