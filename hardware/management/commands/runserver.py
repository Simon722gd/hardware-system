import os
import webbrowser
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    def handle(self, *args, **options):
        # Ensure Chrome is used when the server opens a browser
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        if os.path.exists(chrome_path):
            # register chrome with the webbrowser module
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            os.environ['BROWSER'] = chrome_path

        # if addrport provided use that otherwise default
        addr = options.get('addrport') or '127.0.0.1:8000'
        url = 'http://' + addr if not addr.startswith('http') else addr
        try:
            webbrowser.get('chrome').open(url)
        except Exception:
            pass

        super().handle(*args, **options)