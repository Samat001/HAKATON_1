from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail('Bexicano_Shop',#title
    f'http://localhost:8000/api/v1/account/activate/{code}/', #body
    'githubforsam@gmail.com', #from 
    [email] # to
    )


def send_resset_code(email, code):
    send_mail('Bexicano_Shop',#title
    f'Для смены пароля пройдите по ссылке {"http://localhost:8000/api/v1/account/confirm/"}\n {code} и вставьте этот код в поле Токкен', #body
    'githubforsam@gmail.com', #from 
    [email] # to
    )