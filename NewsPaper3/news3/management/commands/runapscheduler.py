from django.core.management.base import BaseCommand, CommandError
from news3.models import News, Category
import django.dispatch
import logging

logger = logging.getLogger(__name__)
weekly_mail = django.dispatch.Signal()


def send_digest():
    # Your job processing logic here...
    print("Job started")

    weekly_mail.send('send_digest')
    #   Signal.send('weekly_mail',)
    pass


class Command(BaseCommand):
    help = 'Подсказка вашей команды'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))

        try:
            category = Category.get(name=options['category'])
            News.objects.filter(category == category).delete()
            self.stdout.write(self.style.SUCCESS(
                f'Succesfully deleted all news from category {category.name}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
        except News.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {"category"}'))
