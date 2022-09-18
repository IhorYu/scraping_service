import os
import sys
import django
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

django.setup()
from scraping.models import Vacancy
from scraping_service.settings import EMAIL_HOST_USER

subject = 'Vacancies'
text_content = 'Vacancies'
from_email = EMAIL_HOST_USER

empty = '<h2>Sorry, there are no new vacancies for today</h2>'
User = get_user_model()
qs = User.objects.filter(send_email=True).values('city', 'language', 'email')
users_dct = {}
for user in qs:
    users_dct.setdefault((user['city'], user['language']), [])
    users_dct[(user['city'], user['language'])].append(user['email'])

if users_dct:
    params = {'city_id__in': [], 'language_id__in': []}
    for pair in users_dct.keys():
        params['city_id__in'].append(pair[0])
        params['language_id__in'].append(pair[1])

    qs = Vacancy.objects.filter(**params).values()
    vacancies = {}
    for i in qs:
        vacancies.setdefault((i['city_id'], i['language_id']), [])
        vacancies[(i['city_id'], i['language_id'])].append(i)
    for keys, emails in users_dct.items():
        rows = vacancies.get(keys, [])
        html = ''
        for row in rows:
            html += f'<h5><a href="{row["url"]}">{row["title"]}</a></h5>'
            html += f'<p> {row["description"]} </p>'
            html += f'<p> {row["company"]} </p><br><hr>'
        _html = html if html else empty
        for email in emails:
            to = email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(_html, "text/html")
            msg.send()
