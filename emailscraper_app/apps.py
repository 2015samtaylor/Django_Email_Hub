from django.apps import AppConfig

# The AppConfig subclass can be used to configure various settings for your app. You can define additional attributes or 
# override methods as needed to customize the behavior of your app. For example, you can define a ready() method in your 
# AppConfig subclass to perform initialization tasks when your app is ready. You can also specify other settings or metadata related to your app.


class EmailscraperAppConfig(AppConfig):
    name = "emailscraper_app"
