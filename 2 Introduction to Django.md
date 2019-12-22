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