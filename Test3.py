
# coding: utf-8

# In[46]:
import os
import json
data='''Время от времени мне очень хочется выпить, чтобы расслабиться. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
В свое свободное время я чаще всего смотрю телевизор. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я считаю, что одиночество – это самое страшное в жизни. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я – человек азартный и люблю азартные игры. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Секс – это самое большое удовольствие в жизни. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я довольно часто ем не от голода, а для получения удовольствия. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я соблюдаю религиозные ритуалы. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я все время думаю о работе. о том, как сделать ее лучше. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я довольно часто принимаю лекарства. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я провожу очень много времени за компьютером. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Не представляю свою жизнь без сигарет. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я активно интересуюсь проблемами здоровья. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я пробовал наркотические вещества. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Мне тяжело бороться со своими привычками. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Иногда я не помню произошедшего во время опьянения. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я могу долго щелкать пультом в поисках чего-нибудь интересного по телевизору. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Главное чтобы любимый человек всегда был рядом. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Время от времени я посещаю игровые автоматы. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я не думаю о сексе только когда я сплю. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я постоянно думаю о еде, представляю себе разные вкусности. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я довольно активный член религиозной общины. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я не умею отдыхать, чувствую себя плохо во время выходных. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Лекарства – самый простой способ улучшить самочувствие. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Компьютер – это реальная возможность жить полной жизнью. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Сигареты всегда со мной. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
На поддержание здоровья не жалею ни сил, ни денег, ни времени. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Попробовать наркотик – это получить интересный жизненный урок. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я считаю, что каждый человек от чего то зависим. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Бывает что я чуть чуть перебираю когда выпиваю. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Телевизор включен большее время моего пребывания дома. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Когда я не вместе с любимым человеком, я постоянно думаю о нем. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Игра дает самые острые ощущения в жизни. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я готов идти на « случайные связи», ведь воздержание от секса для меня крайне тяжело. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Если кушанье очень вкусное то я не удержусь от добавки. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Считаю что религия – единственное что может спасти мир. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Близкие часто жалуются, что я постоянно работаю. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
В моем доме много медицинских и подобных препаратов $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Иногда, сидя у компьютера я забываю поесть или о каких то делах. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Сигарета это самый простой способ расслабиться. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я читаю медицинские журналы и газеты, смотрю передачи о здоровье. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Наркотик дает самые сильные ощущения из всех возможных. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Привычка – вторая натура, и избавиться от нее глупо. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Алкоголь в нашей жизни – основное средство расслабления и повышения настроения. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Если сломался телевизор, то я не буду знать чем себя развлечь вечером. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Быть покинутым любимым человеком – самое большое несчастье, которое может произойти. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я понимаю азартных игроков, которые могут в одну ночь выиграть состояние а в другую проиграть два. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Самое страшное это получить физическое увечье которое вызовет сексуальную неполноценность. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
При походе в магазин не могу удержаться что бы не купить что-нибудь вкусненькое. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Самое главное в жизни – жить наполненной религиозной жизнью. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Мера ценности человека заключается в том, на сколько он отдает себя работе. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я довольно часто принимаю лекарства. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
«Виртуальная реальность» более интересна чем обычная жизнь. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я ежедневно курю. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я стараюсь неотступно соблюдать правила здорового образа жизни. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Иногда я употребляю средства, считающиеся наркотическими. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Человек – существо слабое, нужно быть терпимым к его вредным привычкам. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Мне нравится выпить и повеселиться в веселой компании. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
В наше время почти все можно узнать из телевизора. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Любить и быть любимым это главное в жизни. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Игра – это реальный шанс сорвать куш, выиграть много денег. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Секс – это лучшее времяпровождение. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я очень люблю готовить и делаю это так часто, как могу. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я часто посещаю религиозные заведения. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я считаю, что человек должен работать на совесть, ведь деньги это не главное. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Когда я нервничаю, я предпочитаю принять успокоительное. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Если бы я мог то все время занимался бы компьютером. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я – курильщик со стажем. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Я беспокоюсь за здоровье близких, стараюсь привлечь их к здоровому образу жизни. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
По интенсивности ощущений наркотик не может сравниться ни с чем. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да
±
Глупо пытаться показать свою силу воли и отказаться от различных радостей жизни. $$
    Нет
    Скорее нет
    Ни да, ни нет
    Скорее да
    Да'''

vals = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]


# In[47]:

d = (i.decode('utf-8').split("$$") for i in data.split('±'))
questions = [[q.strip(), [i.strip() for i in a.strip().split('\n')]] for q, a in d]


# In[48]:

import datetime
import sys
sys.path.append('/srv/ewok/ewok/settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'production'

import django
django.setup()

from exam.models import *


# In[49]:

test, is_new = Test.objects.get_or_create(title=u"Зависимости")

for idx, item in enumerate(questions):
    text, variants = item
    
    q, is_new = Question.objects.get_or_create(test=test, description=text, number=(idx+1), type=0)

    for value, variant in enumerate(variants):
        Variant.objects.get_or_create(question=q, text=variant, value={vals[idx % 14]: value+1})


# In[ ]:



