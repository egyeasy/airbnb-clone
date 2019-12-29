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

### 1 대 N 관계

Room의 foreign key는 user. 하나의 필드인데 다른 모델의 id를 가리키고 있음





## 4.3 ManyToMany like a Boss

django에서는 model의 이름을 string으로 바꾼다. 그걸 커스터마이즈 할 수 있다.

```python
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

    def __str__(self):
        return self.name
```



### Many to Many relationship

형제자매가 서로 형제자매를 N명 가질 수 있다.



일단 house type model부터 만들어보도록 하자.(필터)

```python
class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass

```



many to many로 추가

```python
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
    room_type = models.ManyToManyField(RoomType, blank=True)
```



migrate



어드민을 바꿔보자

```python

@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass

```

이러면 room type을 admin에서 볼 수 있어진다. 그리고 admin 페이지에서 새롭게 room type을 생성할 수 있게 된다





abstract item을 만들어준 것은 구체적인 내용만 다를 뿐 item이 필요하기 때문





## 4.4 on_delete, Amenity, Facility, HouseRule Models

### on_delete

User가 삭제되었을 때, User를 foreign key로 가지고 있는 room까지 삭제된다. 폭포수와 같은 것.

PROTECT 옵션은 남아있는 room이 있을 때 user를 삭제할 수 없음. room을 삭제해야 user를 삭제 가능하다.

SET_NULL : user가 없어지면 room의 foreign key는 null이 됨



many to many에는 on_delete 옵션이 없다. 어차피 많은 개체랑 연결될 수 있기 때문



### Amenity

```python
class RoomType(AbstractItem):
    
    """ RoomType Object Definition """

    pass

class Amenity(AbstractItem):

    """ Amenity Object Definition """

    pass


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
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField(Amenity)
```

룸타입은 foreign key로 수정



### Facility, HouseRule

```python
class Facility(AbstractItem):

    """ Facilitiy Model Definition """

    pass

class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    pass

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
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)
```



migrate



### admin에 등록

```python
from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
```

register를 동시에 여러개 가능하다.





## 4.5 Meta Class and Photos Model

### verbose name

Amenitys라고 잘못 복수형을 붙이는걸 고쳐보다.

class Meta를 사용한다



#### models.py

```python
class RoomType(AbstractItem):
    
    """ RoomType Model Definition """

    class Meta:
        verbose_name_plural = "Room Types"

class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facilitiy Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name_plural = "House Rules"
```



### ordering

created, -created, alphabet 등 가능

```python
class RoomType(AbstractItem):
    
    """ RoomType Model Definition """

    class Meta:
        verbose_name_plural = "Room Types"
        ordering = ['created'] # order one is first
```



### blank=True

직접 추가해줄 때 문제가 발생하므로 비우는 것도 가능하도록 설정

```python
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)
```



### photo

photo는 room에 링크된다. room은 user에 링크된다.

```python
class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """
    
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    model = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
```

Room을 String화 하여 넣을 수 있다. 이렇게 하면 굳이 Room 뒤에 Photo를 정의할 필요도 없음

이렇게 되면 import 할 필요도 없다.



```python
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)
```

유저는 유저 앱에서 가져와야 한다.



포토는 다른 어드민이 있다.

```python
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
```



migrate





































