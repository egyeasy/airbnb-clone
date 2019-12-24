## 3.0 Replacing Default User

### 모델

유저에 관한 기능을 더 확장해야 한다. 생년월일, super 호스트, 성별 등

django에는 sqlite라는 db가 이미 있다.



### substituting a custom User model

#### settings.py

```python
AUTH_USER_MODEL = 'myapp.MyUser'
```



#### users/models.py

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass
```



### 앱 등록

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

PROJECT_APPS = [
    "users.apps.UsersConfig",
]

# Application definition

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS


...


AUTH_USER_MODEL = 'users.User' // 앱이름/모델이름
```





`python manage.py makemigrations`

`python manage.py migrate`

migration 파일을 보면 이미 다 설정돼있는 것을 볼 수 있다.



`python manage.py createsuperuser`



어드민에 모델을 연결해보자.



### admin.py

```python
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUser(admin.ModelAdmin):
    pass
```

user에 대한 admin이 추가된 것을 볼 수 있다.



django가 내가 model에 쓴 것을 form으로 만들어준다.



### models.py

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    
    bio = models.TextField()
```

이러고 admin 페이지 가서 refresh하면 에러가 발생

database에 column 정보를 알려줘야 한다.



`python manage.py makemigrations`

디폴트 추가 해야한다고 뜸

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    
    bio = models.TextField(default="")
```

`python manage.py migrate`



이제 어드민에서 bio가 추가된 것을 볼 수 있따.



## 3.2 First Model Fields

### 유저 만들기

User에 bio default를 설정하는 이유는 이미 유저가 한 명 만들어져있기 때문. 그 유저의 bio를 무엇으로 할지를 정해줘야 한다. 방법은 두 가지다

1. 디폴트 값 설정해줘서 나머지를 디폴트로 채우기
2. null값 허용



### docstring

#### models.py

```python
class User(AbstractUser):
    """ Custom User Model """
    bio = models.TextField(default="")
```

클래스에 대한 설명을 볼 수 있다. 무슨 클래스인지 알려줌

마우스를 갖다대면 알려준다.



### 유저 avatar

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """ Custom User Model """
    avatar = models.ImageField()
    gender = models.CharField(max_length=10, null=True) # empty여도 괜찮다.
    bio = models.TextField(default="")

```

migrations 만들면 안된다.

image를 쓰려면 pillow를 써야 한다고 나온다.



`pipenv install Pillow`



```python
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """ Custom User Model """
    avatar = models.ImageField(null=True)
    gender = models.CharField(max_length=10, null=True) # empty여도 괜찮다.
    bio = models.TextField(default="")

```





`python manage.py makemigrations`

`python manage.py migrate`



characterfield는 한 줄 form, textfield는 여러 줄 form



### 젠더에 선택 옵션 주기 - choices

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male")
        (GENDER_FEMALE, "Female")
        (GENDER_OTHER, "Other")
    )
    avatar = models.ImageField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True) # empty여도 괜찮다.
    bio = models.TextField(default="")

```

이 변화는 데이터베이스에 직접 영향을 주지 않는다. form에 영향을 준 것이기 때문. migrate할 필요가 없다.

 

admin에서 직접 데이터를 생성하려고 하면 required가 뜨는 것을 볼 수 있다. null=True인데도 왜 그러냐면, null은 데이터베이스에서 사용되는 것. form에 대해서는 blank=True 설정을 해줘야 한다.



```python
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True) # empty여도 괜찮다.
    bio = models.TextField(default="", blank=True)

```





## 3.3 Finishing User Model

몇몇 필드를 더 추가해보자

```python
class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True) # empty여도 괜찮다.
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    superhost = models.BooleanField(default=False)
```



migrate



## 3.4 Falling in Love with Admin Panel

### django admin site

admin에게 model이 나타나게 하려면 두 가지 방법이 있다.

1. `admin.site.register(User, CustomUserAdmin)`

2. ```python
   # Register your models here.
   @admin.register(models.User)
   class CustomUserAdmin(admin.ModelAdmin):
       pass
   ```

CustomUserAdmin이 User를 컨트롤하게 됨

아래는 데코레이터를 사용한 방법



### list display

```python
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """
    
    list_display = ('username', 'gender', 'language', 'currency', 'superhost')
```

admin에서 user 리스트를 보면 column들이 추가된 것을 볼 수 있다.



### 필터

```python
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
    list_filter = ('language', 'currency', 'superhost')
```





## 3.5 UserAdmin + CustomAdmin

어드민 패널의 구성을 바꿔보자.



```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    pass
```

admin 리스트와 개별 페이지가 달라진 것을 볼 수 있다.

UserAdmin은 User의 필드를 모른다.

fieldset을 사용해볼 것. 파란 타이틀로 구분되는 것이 fieldset이다.



```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # 기존의 fieldset과 합쳐준다.
    fieldsets = UserAdmin.fieldsets + \
                (
                    (
                        "Custom Profile",
                        {
                            "fields": (
                                "avatar",
                                "gender",
                                "bio",
                                "birthdate",
                                "language",
                                "currency",
                                "superhost",
                            )
                        },
                    ),
                )

```

튜플 처리를 위해 콤마를 찍어줄 것



## 3.6 RECAP OMG!

### models.py

```python

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True) # empty여도 괜찮다.
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
```

null=True를 지워주자.

단, datefield는 null=True를 잡아주자. text는 빈 값이 있지만 date는 없기 때문

migration, pycache 삭제



migrate











































