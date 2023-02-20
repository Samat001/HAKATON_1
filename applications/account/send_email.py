from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail('Bexicano_Shop',#title
    f'http://localhost:8000/api/v1/account/activate/{code}/', #body
    'githubforsam@gmail.com', #from 
    [email] # to
    )


def send_changepassword_code(email, code):
    send_mail('Bexicano_Shop',#title
    f'http://localhost:8000/api/v1/password_reset/confirm/{code}/', #body
    'githubforsam@gmail.com', #from 
    [email] # to
    )