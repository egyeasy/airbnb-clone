```bash
brew install pipenv
mkdir airbnb-clone
cd airbnb-clone

pipenv --three
```



VS code에서 폴더를 연다



```bash
pipenv shell
```



가상환경 안으로 들어갈 수 있다.



```bash
pipenv install Django==2.2.5
```

이렇게 하면 가상환경 안에서만 Django가 설치되는 것이다.



`which django-admin` 을 통해 어디에 설치돼있는지를 볼 수 있다.

버블 바깥 환경에서는 볼 수 없음.

