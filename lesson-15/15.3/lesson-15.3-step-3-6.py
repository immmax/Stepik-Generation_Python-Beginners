#-----------------------------------------------#
# DATE: 2023.07.05                              #
# AUTHOR: Maxim Datskiy                         #
# GitHub: https://github.com/immmax             #
#-----------------------------------------------#
# Курс "Поколение Python": Курс для начинающих  #
#                                               #
# Модуль 15 - Работа над мини-проектом          #
# Урок 15.3 - Магический шар                    #
# Шаг 3-6                                       #
#-----------------------------------------------#

import random

answers = ['Бесспорно',
           'Предрешено',
           'Никаких сомнений',
           'Определённо да',
           'Можешь быть в этом уверен',

           'Мне кажется - да',
           'Вероятнее всего',
           'Хорошие перспективы',
           'Знаки говорят - да',
           'Да',

           'Пока неясно, попробуй снова',
           'Спроси позже',
           'Лучше не рассказывать',
           'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять',

           'Даже не думай',
           'Мой ответ - нет',
           'По моим данным - нет',
           'Перспективы не очень хорошие',
           'Весьма сомнительно']

print('Привет, Мир! Я - магический шар, и я знаю ответ на любой твой вопрос.')

username = input('Давай познакомимся! Как тебя зовут?\n')
print(f'Привет, {username.capitalize()}!')

while True:
    question = input('Какой у тебя вопрос?\n')
    print(random.choice(answers))

    if input('У тебя есть ещё вопросы? да/нет: ').lower() == 'нет':
        print('Возвращайся, если возникнут вопросы!')
        break