import os

app_settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "files"),
    "static_url_prefix": '/files/',
    "xsrf_cookies": False,
    'cookie_secret': '&E)H@MbQeThWmZq4t7w!z%C*F-JaNdRf'
}

KEY = '&E)H@MbQeThWmZq4t7w!z%C*F-JaNdRf'