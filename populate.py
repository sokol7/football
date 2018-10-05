import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_project.settings')
import django
django.setup()
from football.models import Country, NewsPage

countries = ['England', 'Spain', 'Germany', 'Italy', 'France']

def populate():
    for country in countries:
        add_country(country)


def add_country(title):
    c = Country.objects.get_or_create(title = title)[0]
    c.save()
    return c

if __name__ == '__main__':
    populate()

