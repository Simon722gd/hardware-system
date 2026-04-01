#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hardware.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Auto-open browser only on the main process during runserver
    if 'runserver' in sys.argv and os.environ.get('RUN_MAIN') != 'true':
        import threading
        import webbrowser
        import time

        def open_browser():
            """Wait for server to start and then open the default browser."""
            time.sleep(2.5)
            url = 'http://127.0.0.1:8000'
            try:
                # Optimized path for Microsoft Windows Chrome installation
                chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                if os.path.exists(chrome_path):
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                    webbrowser.get('chrome').open(url)
                else:
                    webbrowser.open(url)
            except Exception:
                webbrowser.open(url)
        
        # Start open_browser in a daemon thread to avoid blocking server shutdown
        threading.Thread(target=open_browser, daemon=True).start()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
