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

















































