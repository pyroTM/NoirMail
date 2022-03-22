import threading
import time
import requests
import ctypes 
import os
import random

ctypes.windll.kernel32.SetConsoleTitleW(f"NoirMail | Sent: 0")
os.system("cls")

NOIRMAIL = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    
                                                                 
                                                                 
              
"""
NOIRMAIL1 = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    


                                                    Beaming
                                                                 
                                                                 
              
"""
NOIRMAIL2 = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    


                                                    Beaming.
                                                                 
                                                                 
       
"""
NOIRMAIL3 = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    


                                                    Beaming..
                                                                 
                                                                 
              
"""
NOIRMAIL4 = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    


                                                    Beaming...
                                                                 
                                                                 
              
"""
NOIRMAIL5 = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    


                                                    Beaming..
                                                                 
                                                                 
              
"""
NOIRMAIL6 = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    


                                                    Beaming.
                                                                 
                                                                 
              
"""
NOIRMAIL7 = """[40;35m
                                                                                                    [40;34mv 1.0.0[40;35m

                             /$$   /$$           /$$           /$$      /$$           /$$ /$$
                            | $$$ | $$          |__/          | $$$    /$$$          |__/| $$
                            | $$$$| $$  /$$$$$$  /$$  /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$
                            | $$ $$ $$ /$$__  $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$| $$| $$
                            | $$  $$$$| $$  \ $$| $$| $$  \__/| $$  $$$| $$  /$$$$$$$| $$| $$
                            | $$\  $$$| $$  | $$| $$| $$      | $$\  $ | $$ /$$__  $$| $$| $$
                            | $$ \  $$|  $$$$$$/| $$| $$      | $$ \/  | $$|  $$$$$$$| $$| $$
                            |__/  \__/ \______/ |__/|__/      |__/     |__/ \_______/|__/|__/
                                                                                                    


                                                    Beaming
                                                                 
                                                                 
              
"""



print(NOIRMAIL)

for i in range(3):
    print('')

EMAIL = str(input("                                               [40;36mUsername => "))

for i in range(2):
    print('')

DOMAIN = str(input("                                               [40;32mDomain => "))

for i in range(2):
    print('')

THREAD_COUNT = int(input("                                                   [40;31mThreads => "))

for i in range(5):
    print('')
    
global SENT



def dot_trick(username):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@" + (DOMAIN))
    return emails
    
def spammer(EMAIL):
    SENT = 0
    emails = dot_trick(EMAIL)

    for i in emails:

        URL = "https://www.vox.com/newsletter_form"

        payload = {
            
            "source": "Presto::Site::NewsletterSignupBox__/__/",
            "list_id": "The Weeds",
            "signup_source": "sidebar",
            "provider": "sailthru",
            "email": f"{random.choice(emails)}"

        }
        
        payload2 = {
            
            "source": "Presto::Site::NewsletterSignupBox__/__/",
            "list_id": "VoxCare",
            "signup_source": "sidebar",
            "provider": "sailthru",
            "email": f"{random.choice(emails)}"

        }


        
        payload3 = {"email":f"{random.choice(emails)}","newsletters":["breaking_news","five_things","good_stuff","race","what_matters","reliable_sources","health","vault","point","meanwhile","china","global_briefing","coronavirus","markets_now","btb","nightcap","provoke_persuade","pop_life","underscored","science","royal_news","esp_five_things","esp_breaking_news","arabic_breaking_news","travel_weekly","travel_italy","keep_watching","ten","stress","fitness","sleep","five_things_sunday","eat_med","life","events_citizen","wisdom_project"],"userProfileRequest":{"attributes":{"newsletters":{"acquisition_country":"US","breaking_news_source":"subhub","breaking_news_user_score":"1.00","five_things_source":"subhub","five_things_user_score":"1.00","good_stuff_source":"subhub","good_stuff_user_score":"1.00","race_source":"subhub","race_user_score":"1.00","what_matters_source":"subhub","what_matters_user_score":"1.00","reliable_sources_source":"subhub","reliable_sources_user_score":"1.00","health_source":"subhub","health_user_score":"1.00","vault_source":"subhub","vault_user_score":"1.00","point_source":"subhub","point_user_score":"1.00","meanwhile_source":"subhub","meanwhile_user_score":"1.00","china_source":"subhub","china_user_score":"1.00","global_briefing_source":"subhub","global_briefing_user_score":"1.00","coronavirus_source":"subhub","coronavirus_user_score":"1.00","markets_now_source":"subhub","markets_now_user_score":"1.00","btb_source":"subhub","btb_user_score":"1.00","nightcap_source":"subhub","nightcap_user_score":"1.00","provoke_persuade_source":"subhub","provoke_persuade_user_score":"1.00","pop_life_source":"subhub","pop_life_user_score":"1.00","underscored_source":"subhub","underscored_user_score":"1.00","science_source":"subhub","science_user_score":"1.00","royal_news_source":"subhub","royal_news_user_score":"1.00","esp_five_things_source":"subhub","esp_five_things_user_score":"1.00","esp_breaking_news_source":"subhub","esp_breaking_news_user_score":"1.00","arabic_breaking_news_source":"subhub","arabic_breaking_news_user_score":"1.00","travel_weekly_source":"subhub","travel_weekly_user_score":"1.00","travel_italy_source":"subhub","travel_italy_user_score":"1.00","keep_watching_source":"subhub","keep_watching_user_score":"1.00","ten_source":"subhub","ten_user_score":"1.00","stress_source":"subhub","stress_user_score":"1.00","fitness_source":"subhub","fitness_user_score":"1.00","sleep_source":"subhub","sleep_user_score":"1.00","five_things_sunday_source":"subhub","five_things_sunday_user_score":"1.00","eat_med_source":"subhub","eat_med_user_score":"1.00","life_source":"subhub","life_user_score":"1.00","events_citizen_source":"subhub","events_citizen_user_score":"1.00","wisdom_project_source":"subhub","wisdom_project_user_score":"1.00"}}},"emailAddress":f"{random.choice(emails)}"}


        r = requests.post(url=URL, params=payload)
        r = requests.post(url=URL, params=payload2)
        SENT += 2
        ctypes.windll.kernel32.SetConsoleTitleW(f"NoirMail | Sent: {SENT}")



for i in range(THREAD_COUNT):
    threading.Thread(target=spammer(EMAIL))

