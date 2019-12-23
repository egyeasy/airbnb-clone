# 2 Introduction to Django

django-admin을 써서 프로젝트를 개시하는 법을 살펴보자.

django-admin startproject 같은 방식은 좋지 않다.



airbnb-clone/ 에서

```bash
django-admin startproject config
```



Config 폴더를 Aconfig로 이름 바꾸고,

안에 있는 것들을 밖으로 꺼낸다.



vscode에서는 사용할 python version을 선택할 수 있다.

내 vscode에서는 예전에 설정을 했던건지 무시를 했던건지 메시지 창이 뜨지 않아서 수동으로 설정해준다.

proejct에 한정해서 setting.json을 설정할 수 있다.

https://www.benjaminpack.com/blog/vs-code-python-pipenv/

이를 따라 pipenv python의 path를 찾아서 configure해줄 수 있다.



## 2.1 setting up vscode and python like a PRO

python은 컴파일 언어가 아니다. 대신 linter가 있는데 에러를 미리 탐지한다. 잘못되었다고 알려줌. linter는 코드가 실행되기 전에 잘못되었다고 알려준다.

python pep은 python coding에 관한 스타일 가이드. space before function 등

linter가 에러를 알려줌

formatter는 코드를 특정한 형식에 맞게 보여준다

linter는 flake8, formatter는 black을 쓰고 setting에서 format on save ON 설정



### settings.py

linter에 의해 line to long 에러가 뜨게 됨(E501) 지금의 모니터는 충분히 크므로 이 설정을 바꿔주자.

formmatter를 체크해보려면 저장해보면 된다. -> 알아서 바꿔서 저장해줌.





## 2.2 Falling in love with Django

단어 위에 command를 누르면 정의로 갈 수 있다



`pipenv shell`

`python manage.py runserver`

가상환경 내에서 server를 돌릴 수 있다. django가 준 주소로 가면 볼 수 있다.

ctrl+z를 누르면 서버를 끌 수 있다



### admin

`python manage.py migrate`

이러고 admin 페이지를 갈 수 있다

`python manage.py createsuperuser`

dz / 123으로 만든다

/admin으로 들어가면 관리자 페이지가 이미 만들어져있는 것을 볼 수 있다.





## 2.4 Django Migrations

sqlite3를 제거하고 다시 run server 해보자.

unmigrated changes 메시지가 뜬다.

이 상태에서 admin을 들어가면 database가 없으므로 에러가 뜬다.



### SQL

우리는 데이터베이스와 소통할 때 sql을 사용하기도 한다. django에서는 알아서 다 해주기도 한다.



### migration

데이터 형식 변경사항이 발생할 때 migration이 생성된다.

이것들을 migrate 시켜야 데이터베이스에 반영됨.



`python manage.py migrate`



## 2.5 Django Applications

django 프로젝트는 application의 집합이다.

application은 function의 집합이다.

function의 집합에는 **room**의 검색, 생성, 수정, 삭제, 보여주기, 업로드 등이 포함된다 -> 이게 하나의 어플리케이션

but 숙소에는 **리뷰**도 있다. 룸에 대한 리뷰는 같은 어플리케이션에 넣을 것인가? review의 CRUD까지 들어간다면 10가지의 function이 들어감.

**예약**도 있다. 예약과 관련된 기능들도 넣을 것인가?

user는 다른 어플리케이션으로 분류할 것. - 로그인, 로그아웃, 구글, 페이스북, 등등



이 강좌에서는 divide and conquer할 것이다. list는 list의 CRUD만. 

하나의 팁은 **하나의 문장으로 어플리케이션을 표현할 수 있어야 한다.**



## 2.6 Creating the Apps

application 이름은 복수형이어야 한다.

`django-admin startapp rooms`

`django-admin startapp users`

`django-admin startapp reviews`

`django-admin startapp conversations`

`django-admin startapp lists`

`django-admin startapp reservations`



###user application은 왜 만든 것일까?

일단 super user를 다시 만들자

admin을 들어가게 되면 이미 admin 페이지가 일종의 user 관리 페이지가 될 수 있다.

하지만 유저가 여기에 접근하는 것은 안된다.

따라서 admin과 분리된 별도의 user 관련 어플리케이션을 만드는 것.



## 2.7 Explaining the Apps

파일 이름을 변경해서는 안된다. framework를 쓰고 있는 것이다.

framework는 그 룰을 따라 사용해야 한다.

library는 build stuff하기 위해 쓰는 것

파일 이름은 django의 룰을 따라 만들어져야 함.

그래야 django 프레임워크가 파일을 찾아서 소통할 수 있다.