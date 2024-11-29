def send_email(message,recipient,*,sender = "university.help@gmail.com"):
    sender_key = False
    recipient_key = False
    for i in range(2):
        if i == 0:
            mail = recipient
        else:
            mail = sender
        string_ = []
        string_.extend(mail)
        mail_key = False
        mail_key_2 = False
        for a in range(len(string_)):
            if  string_[a] == "@":
                mail_key = True
                break
        mail_4 = mail[(len(string_) - 4) : ]
        mail_3 = mail[(len(string_) - 3) : ]
        if  mail_4 == ".com" or mail_3 == ".ru"  or mail_4 == ".net":
            mail_key_2 = True
        if i == 0 and mail_key and mail_key_2:
            recipient_key = True
        if i == 1 and mail_key and mail_key_2:
            sender_key = True
    if recipient_key == False or sender_key == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')