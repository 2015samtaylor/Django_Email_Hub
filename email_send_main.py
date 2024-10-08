#class variables are initialized in config
from config import *
import pandas as pd
import numpy as np
from datetime import datetime
import time
import logging
import os
from emailscraper_app.modules.Sending_Emails.sends import SendMail



#create log dir and file
logpath_creation = os.getcwd() + '\\Logs'
if not os.path.exists(logpath_creation):
    os.makedirs(logpath_creation)

# logging.basicConfig(filename= logpath_creation + '\\Email_Sender.log', level=logging.INFO,
#                     format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', force=True)



# ---------------------------

def blast(email_config, df, user, test):

    print('Blast has been called')
    # Get the next 50 emails iteratively and send every 60 seconds with a new SMTP connection
    # get_next_50 is what ends this function. It will break once end_point has surpassed.
    while len(df) >= 1:

        print(df.head())
        print(f'Here is the email config passed into blast func {email_config}')

        # next_50 = SendMail.get_next_50(df, email_config)

        # print(f'Here is the next_50 frame {next_50.head()}')

        # try:
        #     new_point = next_50.index[0]
        #     end_point = next_50.index[-1]   
        #     print(new_point, end_point) 
        #     logging.info(f'\n\nStarting email send at index {new_point}, and ending at index {end_point}')
        # except IndexError:
        #     print('List has been fully iterated through')

        #  # Check if the end_point surpasses 1500
        # if end_point >= 1500:
        #     logging.info('Reached the end_point limit of 1500. Exited the loop.')
        #     print('Reached the end_point limit of 1500. Exited the loop.')
        #     break
        
        # SMTP conn populates directly in process, & if test is True it will only send two emails to personal accounts
        # email_history = SendMail.process(next_50, email_config, test)
        email_history = SendMail.process(df, email_config, user, test) 

        if test:
            logging.info('Breaking loop after sending to personal emails due to test')
            break  # Terminate after one iteration if test=True
        else:
            logging.info('Test is false')
        
        interval_seconds = 30
        # Wait for the specified interval before the next iteration
        try:
            time.sleep(interval_seconds)
            logging.info(f'Sleeping for {interval_seconds} seconds completed')
            print(f'Sleeping for {interval_seconds} seconds')
        except:
            logging.info('Issue with the sleep')
            print('Issue with the sleep')


