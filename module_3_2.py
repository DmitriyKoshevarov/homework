correct_sender = "university.help@gmail.com"

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if not sender.count('@') > 0 or not recipient.count('@') > 0 or not sender.endswith((".com", ".ru", ".net")) or not recipient.endswith((".com", ".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса "{sender}" на адрес "{recipient}"!')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == correct_sender:
        print(f'Письмо успешно отправлено с адреса "{sender}" на адрес "{recipient}".')
    elif sender != correct_sender:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "{sender}" на адрес "{recipient}".')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# После того как решил, закинул код на проверку чату. Он подсказал, что валидность адреса можно было проверить след.образом:

# def is_valid_email(email):
#   return "@" in email and email.endswith((".com", ".ru", ".net"))
#
# def send_email(message, recipient, *, sender="university.help@gmail.com"):
#   if not is_valid_email(sender) or not is_valid_email(recipient):
#       print(f'Невозможно отправить письмо с адреса "{sender}" на адрес "{recipient}".')

# Добавлять в свой код пока не стал,потому что не я придумал =). Записал себе на будущее.