from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))
        
    passability_choice = []
    for r in range(1, 6):
        passability_choice.append((r,r))
        
    features_choices = (
        ('Круиз-контроль', 'Круиз-контроль'),
        ('Аудиоподготовка', 'Аудиоподготовка'),
        ('Подушки безопасности', 'Подушки безопасности'),
        ('Кондиционер', 'Кондиционер'),
        ('Подогрев передних сидений', 'Подогрев передних сидений'),
        ('Иммобилайзер', 'Иммобилайзер'),
        ('Парковочный ассистент', 'Парковочный ассистент'),
        ('Усилитель руля', 'Усилитель руля'),
        ('Камера заднего вида', 'Камера заднего вида'),
        ('Start/Stop', 'Start/Stop'),
        ('Мультируль', 'Мультируль'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(('Название'),max_length=255)
    color = models.CharField(('Цвет'),max_length=100)
    model = models.CharField(('Модель'),max_length=100)
    year = models.IntegerField(('Год'), choices=year_choice)
    passability = models.IntegerField(('Проходимость'), choices=passability_choice)
    weather = models.IntegerField(('Погода'), choices=passability_choice)
    price = models.IntegerField(('Цена'))
    description = RichTextField(('Описание'),)
    car_photo = models.ImageField(('Фото'),upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(('Фото 2'),upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(('Фото 3'),upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(('Фото 4'),upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(('Фото 5'),upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(('Конфигурация'),choices=features_choices)
    body_style = models.CharField(('Кузов'),max_length=100)
    engine = models.CharField(('Двигатель'),max_length=100)
    transmission = models.CharField(('Привод'),max_length=100)
    interior = models.CharField(('Интерьер'),max_length=100)
    doors = models.CharField(('Количество дверей'),choices=door_choices, max_length=10)
    passengers = models.IntegerField(('Количество пассажиров'))
    fuel_type = models.CharField(('Тип топлива'),max_length=50)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(('Дата размещения'),default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
