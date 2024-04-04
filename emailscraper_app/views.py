from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import EmailBlastForm, EmailConfigForm
from .models import EmailOption
from email_send_main import blast
from config import *
import pandas as pd
from datetime import datetime
from emailscraper_app.modules.Sending_Emails import KC_schools

df = KC_schools.read_in()
df = KC_schools.filter_emails_by_sport(df, ['Baseball', 'Softball'])



# views are Python functions or classes that receive HTTP requests and return HTTP responses.
# Views contain the business logic of your application, including data retrieval, processing, and rendering.
# Views interact with MODELS to retrieve or manipulate data and with templates to generate HTML output.






def initial_view(request):
    print('Calling initial view')

    #initialize EmailConfigForm instanc, pass into Homepage
    email_config_form = EmailConfigForm()
    emails_sent = request.session.get('emails_sent', False)

    return render(request, 'emailscraper_django/homepage.html', {'email_config_form': email_config_form, 'emails_sent': emails_sent})


def email_config_view(request):

    excluded_fields = ['EMAIL_PASS', 'db_pass']
    print('Starting email config view')

    if request.method == 'POST':
        print('Was a post')
        form = EmailConfigForm(request.POST)

        if form.is_valid():

            # Convert filter_date string to a date object
            filter_date = form.cleaned_data['filter_date'].strftime('%Y-%m-%d')
            form.cleaned_data['filter_date'] = filter_date

            # Create a new instance of EmailConfig using form data
            request.session['email_config'] = form.cleaned_data

            messages.success(request, 'Email configuration saved successfully.')

            # Redirect to the same page to clear form fields and show success message
            print(form.cleaned_data)
            print('Form was valid')
            # return redirect('email_config_view')
            
            # Render the same template with the success message
            return render(request, 'emailscraper_django/homepage.html', {'email_config_form': form, 'excluded_fields': excluded_fields})
        
        else:

            print('\nForm errors:', form.errors)
            print('\nForm data:', request.POST)


    else:
        # Initialize the form with default values
        form = EmailConfigForm()
        print('Form was not valid')



    return render(request, 'emailscraper_django/homepage.html', {'email_config_form': form, 'excluded_fields': excluded_fields})


# #WHERE WAS THE SMTP COMING FROM PRIOR


def send_emails_view(request):

    email_config = request.session.get('email_config') #get the variables from the session, if saved it will be overwritten
    print('Send emails view has been called')
    print(email_config)

    if request.method == 'POST':

        # Call the blast function from email_send_main.py, df can be configured to be passed in dynamically with the adlibs
        #currently reads df from views file being a global variable
        blast(email_config, df, test=True)

        messages.success(request, 'Emails sent successfully!')
        
        # Redirect to the homepage URL
        #What about altering the query string through and additional param , emails_sent = True
        return redirect('initial_view')
    
    else: #on initial page load
        form = EmailBlastForm()
        
    return render(request, 'emailscraper_django/homepage.html', {'form': form})

    







