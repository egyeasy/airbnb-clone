## 4.0 TimeStampedModel

#### settings.py

```python
PROJECT_APPS = [
    "users.apps.UsersConfig", "rooms.apps.RoomsConfig"
]
```



#### models.py

```python
from django.db import models

# Create your models here.
class Room(models.Model):

    """ Room Model Definition """

    pass
```





#### admin.py

```python
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass

```



`django-admin startapp core`

core안에 재사용가능한 common 파일을 만들 것이다.



#### settings.py

```python
PROJECT_APPS = [
    "core.apps.CoresConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig"
]
```



#### models.py

```python
from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
```

abstract 모델은 모델이지만 데이터베이스에는 드러나지 않는 것

확장을 하려고 사용한다.

user에도 abstractUser가 있다 -> 코드에서만 쓰인다.(추상 모델)



#### reservations/models.py

```python
from django.db import models
from core import models as core_models

# Create your models here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    pass

```



## 4.1 Room Model part One

country는 django-countries를 설치해서 넣도록 한다.

`pipenv install django-countries`

 

#### settings.py

```python
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = ["django_countries"]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig"
]

# Application definition

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
```



import는 주로 python lib, django, third_party, my app 순으로

#### models.py

```python
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)


```

timefield는 하루 내의 시간을 의미. 0~24시



호스트를 연결해줘야 한다.

```python
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

```



### auto now, auto add

auto_now : save 할 때 date와 time을 기록(**수정**)

auto_now_add : model을 생성할 때마다 업데이트(**생성**)



#### core/models.py

```python
from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```



migrate



## 4.2 Foreign Keys like a Boss













































