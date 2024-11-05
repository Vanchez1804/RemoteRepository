from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

regions = {
    "Республика Адыгея":[3, 5],
    "Республика Алтай":[2, 3],
    "Республика Башкортостан":[4, 3],
    "Республика Бурятия":[2, 2],
    "Республика Дагестан":[2, 5],
    "Донецкая Народная Республика":[3, 5],
    "Республика Ингушетия":[2, 5],
    "Кабардино-Балкарская Республика":[2, 5],
    "Республика Калмыкия":[2, 5],
    "Карачаево-Черкесская Республика":[2, 4],
    "Республика Карелия":[3, 3],
    "Республика Коми":[2, 3],
    "Республика Крым":[4, 5],
    "Луганская Народная Республика":[3, 5],
    "Республика Марий Эл":[4, 3],
    "Республика Мордовия":[4, 3],
    "Республика Саха (Якутия)":[2, 2],
    "Республика Северная Осетия — Алания":[2, 4],
    "Республика Татарстан":[5, 3],
    "Республика Тыва":[3, 3],
    "Удмуртская Республика":[3, 3],
    "Республика Хакасия":[3, 3],
    "Чеченская Республика":[3, 5],
    "Чувашская Республика — Чувашия":[3, 3],
    "Алтайский край":[3, 3],
    "Забайкальский край":[3, 3],
    "Камчатский край":[2, 3],
    "Краснодарский край":[4, 5],
    "Красноярский край":[4, 2],
    "Пермский край":[4, 3],
    "Приморский край":[4, 3],
    "Ставропольский край":[4, 4],
    "Хабаровский край":[3, 3],
    "Амурская область":[3, 2],
    "Архангельская область":[4, 3],
    "Астраханская область":[4, 5],
    "Белгородская область":[4, 4],
    "Брянская область":[4, 4],
    "Владимирская область":[4, 3],
    "Волгоградская область":[4, 4],
    "Вологодская область":[4, 3],
    "Воронежская область":[4, 4],
    "Запорожская область":[3, 5],
    "Ивановская область":[4, 3],
    "Иркутская область":[4, 2],
    "Калининградская область":[4, 4],
    "Калужская область":[4, 3],
    "Кемеровская область ":[4, 3],
    "Кировская область":[4, 3],
    "Костромская область":[4, 3],
    "Курганская область":[3, 3],
    "Курская область":[4, 4],
    "Ленинградская область":[4, 3],
    "Липецкая область":[4, 4],
    "Магаданская область":[4, 2],
    "Московская область":[4, 3],
    "Мурманская область":[4, 3],
    "Нижегородская область":[4, 3],
    "Новгородская область":[4, 3],
    "Новосибирская область":[4, 3],
    "Омская область":[4, 3],
    "Оренбургская область":[4, 3],
    "Орловская область":[4, 4],
    "Пензенская область":[4, 4],
    "Псковская область":[4, 4],
    "Ростовская область":[4, 5],
    "Рязанская область":[4, 3],
    "Самарская область":[4, 3],
    "Саратовская область":[4, 4],
    "Сахалинская область":[3, 3],
    "Свердловская область":[4, 3],
    "Смоленская область":[4, 3],
    "Тамбовская область":[4, 4],
    "Тверская область":[4, 3],
    "Томская область":[4, 3],
    "Тульская область":[4, 4],
    "Тюменская область":[4, 2],
    "Ульяновская область":[5, 3],
    "Херсонская область":[5, 5],
    "Челябинская область":[4, 3],
    "Ярославская область":[5, 3],
    "Москва":[5, 4],
    "Санкт-Петербург":[5, 4],
    "Севастополь":[5, 5],
    "Еврейская АО":[5, 4],
    "Ненецкий АО":[3, 2],
    "Ханты-Мансийский АО":[3, 3],
    "Чукотский АО":[3, 2],
    "Ямало-Ненецкий АО":[3, 3],
    
}
# Create your views here.
@login_required(login_url='/accounts/login')
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    region_search = regions.keys
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    color_search = Car.objects.values_list('color', flat=True).distinct()
    drivingw_search = Car.objects.values_list('driving_wheels', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'color_search': color_search,
        'drivingw_search': drivingw_search,
        'transmission_search': transmission_search,
        'region_search': region_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    region_search = regions.keys
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    color_search = Car.objects.values_list('color', flat=True).distinct()
    drivingw_search = Car.objects.values_list('driving_wheels', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

   

    if 'region' in request.GET:
        region = request.GET['region']
        if region:
            reg=regions[region]
            cars = cars.filter(passability__lte=reg[0]).filter(weather=reg[1])

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'region_search': region_search,
        'color_search': color_search,
        'drivingw_search': drivingw_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)
