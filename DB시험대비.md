######
1. 관계형DB (RDB): 표로 정리된 DB. 일반적으로 메인으로 많이 사용되고 있음. 
형식이 정해져 있고 관계에 대해 표현을 해야함. 수정이 어렵고 테이블 형식이라
유연성이 없고 확장도 힘듦. 대부분의 관계형에서 SQL을 이용해 조작 가능.
자료를 테이블로 나누어 관리, 테이블 간 간계 설정. 데이터 무결성 유지에 장점.
외래키를 사용하여 각 행에서 서로 다른 테이블 간 관계 만드는데 사용 가능.

2. 비관계형 DB: 관계형의 한계를 극복하기 위해 조금 더 유연하게 만든 DB. 빠른 처리나 확장이
필요할 때 서브로 사용함. NoSQL

스키마: 청사진. 테이블의 구조, 데이터 베이스에서 자료구조, 관계, 표현 방법 등 명세 기술한 것

테이블: 필드와 레코드를 사용해 조직된 데이터 요소들 집합. 관계(Relation)
필드(속성, 칼럼, 세로), 레코드(튜플, 행, 가로)

PK: 고유한 단일값
FK: 외래키. 다른 테이블의 레코드 식별할 수 있는 키. 테이블 간 관계 만드는데 사용

DBMS: DB를 조작하는 프로그램

SQL: 관계형 데이터베이스 관리 + CRUD하는 언어

######
SQL commands

1. DDL: 데이터 정의 언어. 구조를 정의하기 위한 명령어. 테이블, 스키마를 생성, 수정, 삭제
CREATE, DROP, ALTER

CREATE TABLE 새 테이블 생성

ALTER TABLE: Rename a table(RENAME TO), Rename a column(RENAME COLUMN), Add a new column to a table(ADD COLUMN), Delete a column(DROP COLUMN)

ALTER TABLE ADD COLUMN에서 만약 테이블에 기존 데이터 있는데 새로 추가할 경우 NULL이
기존 데이터에 추가되어야 하는데 NOT NULL조건 있으면 에러나기 때문에 DEFAULT제약조건
줘야함.

컬럼삭제 못하는 경우: 컬럼이 다른 부분에서 참조되는 경우, PK인 경우, 유니크 제약조건인 경우

DROP TABLE: DB에서 테이블 제거. 존재하지 않는 테이블 제거시 오류발생. 복구불가. 한번에 한 테이블만 삭제 가능

######

2. DML: 데이터 조작 언어. 데이터를 조작하기 위한 명령어. 추가, 조회, 변경, 삭제
INSERT, SELECT, UPDATE, DELETE

SELECT 특정 테이블에서 데이터를 조회하기 위해 사용. FROM으로 데이터 가져올 테이블 지정
SELECT * FROM users;(테이블명) users에 있는 모든 컬럼 조회
SELECT first_name, age FROM users;

ORDER BY절은 FROM 절 뒤에 위치. ASC, DESC를 통해 정렬가능.
SELECT first_name, age FROM users ORDER BY age;

SELECT DISTINCT 중복제거

WHERE 절은 FROM 절 뒤에 위치.
SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;

LIKE 절은  WHERE 뒤에
SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');

BETWEEN, OR, NOT IN

LIMIT 10 OFFSET 10


3. SQL syntax 
SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고 ;으로 끝남. 대소문자 구분하지
않지만 대문자 권장. 

######
Data types: NULL, INTEGER, REAL, TEXT, BLOB
타입 선호도가 있어서 호환성 상승. 다른 데이터 타입 선언하면 5가지 선호도로 인식됨.
NULL 정보가 없거나 알 수 없음
INTEGER 정수. 크기에 따라 가변 크기를 가짐
REAL 실수. 부동 소수점 사용하는 10진수 값이 있는 실수
TEXT 문자 데이터
BLOB 입력된 그대로 저장된 데이터 덩어리. 이미지 데이터 등

######
Constraints 제약조건

데이터 무결성: DB내 정확성, 일관성 보장 위해 변경 시 제한을 두는 것
NOT NULL: 컬럼이 NULL값 허용하지 않도록. 명시적으로 지정하지 않는한은 NULL값 허용
UNIQUE: 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록
PRIMARY KEY: 테이블에서 행의 고유성 식별에 사용. 각 테이블엔 하나의 기본 키만 있음.
암시적으로 NOT NULL 제약조건 포함.
AUTOINCREMENT: id컬럼에 기본적으로 사용하는 제약조건. 사용되지 않은 값이나 이전에
삭제된 행의 값 재사용 방지. 해당 rowid재사용 못하게 함.

rowid: 암시적 자동증가 컬럼, 테이블의 행 고유하게 식별. 1부터 시작.
데이터 삽입시 명시적 지정 없으면 다음 순서 할당. 별칭 rowid가능


#####
집계함수: COUNT()외에는 컬럼이 int일 때 사용가능. AVG(), COUNT(), MAX(), MIN(), SUM()
SELECT avg(balance) FROM users;

GROUP BY: FROM, WHERE 뒤에 작성. 
SELECT country, avg(balance) FROM users
GROUP BY country ORDER BY avg(balance) DESC;

#####
Changing data

INSERT INTO 새 행을 테이블에 삽입

INSERT INTO classmates(name, age, address)
VALUES('홍길동', 23, '서울')

INSERT INTO classmates
VALUES
 ('김철수', 20, '경기')
 ('이영미', 23, '경기')

UPDATE 업데이트할 테이블 지정하고 SET절에서 테이블 각 컬럼에 대해 새 값을 설정하고
WHERE 절 조건 사용해서 업데이트할 행 지정(선택사항). 

UPDATE classmates
SET name='이태형'
  address='제주도'
WHERE rowid=2;

DELETE 테이블에서 행을 제거. WHERE 생략하면 모든 행 삭제. ORDER BY나 LIMIT절로 삭제할 
행 수 지정 가능.

DELETE FROM classmates WHERE name LIKE '%영%';


#####
정규형
테이블은 유지 보수를 용이하게 하고 데이터의 무결성을 지키기 위해 나눔. 중복을 최소화하고
일관성과 무결성 보장하기 위해 구조화.

1. 제1 정규형
하나의 속성값이 복수형을 가지면 안된다. 하나의 속성값엔 값이 하나만 들어가야함.
(ex) 등록완료 박민서 수영, 필라테스 -->이런거 안된다.

2. 제2 정규형
테이블의 기본키에 종속되지 않는 컬럼은 테이블 분리해야함. 관련없는 애들 따로 분리.
FK를 사용. 
(ex) 기존 테이블에서 운동은 FK로 하고 다른 테이블에 운동 명과 금액 분리시킴.

3. 제3 정규형
다른 속성에 의존하는 속성은 따로 분리할 것.
(ex) 운동 명과 나이 분리 

#####
JOIN 테이블 합치기. 

CROSS JOIN 그냥 다 합치는거. 모든 조합 출력

INNER JOIN 두 테이블에서 일치하는 데이터만 결과 출력

SELECT * FROM articles, users
WHERE articles.userid=user.rowid;

SELECT * FROM articles INNER JOIN users
ON userid=users.rowid;


LEFT JOIN 왼쪽 테이블의 데이터를 기준으로 오른쪽 데이터 결합. 없으면 NULL
RIGHT JOIN
FULL OUTER JOIN

######

RDB에서의 관계

1:1 한 테이블의 레코드 하나가 다른 테이블의 레코드 한 개와 관련된 경우

N:1 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우

M:N 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 0개 이상의 레코드와 관련된 경우
양쪽 모두에서 N:1 관계를 가짐



N:1 고객(1)은 여러 주문(N) 진행 가능. 고객 테이블의 PK를 주문 테이블에 FK로 집어넣어
관계를 표현. 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음.

FK 외래키. 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키.
참조되는 테이블의 PK. 참조하는 테이블의 행에는 참조되는 테이블에 없는 값 포함할 수 없고
참조하는 테이블 행 여러 개가 참조되는 테이블의 동일한 행 참조 가능.
키를 사용해 부모 테이블의 유일한 값 참조(참조 무결성) 외래키가 반드시 부모 테이블의
기본키는 아니어도 되지만 유일한 값이어야함.

######

Django Relationship fields

Foreignkey
N:1담당하는 장고의 모델 필드 클래스. 외래키 속성을 담당.
2개의 필수 인자 필요. 참조하는 model class와 on_delete 옵션

on_delete 데이터 무결성을 위해 필요. 외래키가 참조하는 객체가 사라졌을 때 어떻게 할지.
CASCADE: 부모객체(참조된 객체)가 삭제되면 이를 참조하는 객체도 삭제.


Related manager
N:1이나 M:N관계에서 사용 가능한 문맥. 역참조 시 사용할 수 있는 manager생성.
objects써서 queryset api 사용했던 것처럼 related manager를 통해 queryset api 
사용할 수 있게 함.

역참조: 나를 참조하는 테이블(나를 외래키로 지정한)을 참조하는 것.
N:1에서는 1이 N을 참조하는 상황이므로 외래키를 가지지 않은 1이 외래키를 가진 
N을 참조. 


#####
article.comment_set.method() 
Article모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저.
article.comment 형식으로는 댓글 객체 참조 못함. Article 클래스엔 Comment와의
관계 작성되어 있지 않음. 대신 역참조 할 수 있는 comment_set 매니저를 자동으로
생성하여 article.comment_set 형태로 댓글 객체 참조 가능.

참조 상황인 Comment -> Article에서는 comment.article형태 작성 가능.

related_name은 Foreignkey 클래스의 선택 옵션으로 역참조 시 사용하는 매니저 이름을
변경 가능. article.comment_set 대신 article.comments 사용.

save(commit=False) 아직 데이터베이스에 저장되지 않은 인스턴스를 반환. 
저장 전 객체에 대한 사용자 지정 처리 수행에 유용.

댓글 개수 출력
{{ comments | length }} {{ comments.count }}
댓글이 없는 경우 
for empty 활용

#####
Django에서 User모델을 참조하는 방법

1. settings.AUTH_USER_MODEL
  반환값: 'accounts.User'
  User모델에 대한 외래키 또는 M:N관계 정의할 때 사용. 
  models.py의 모델 필드에서 User모델 참조할 때 사용

2. get_user_model()
  반환값: User Object(객체)
  models.py가 아닌 다른 모든 곳에서 유저 모델 참조할 때 사용

######
CREATE 

외래키 데이터 누락(NOT NULL...에러)
artile = form.save(commit=False) 작성해줘야 함  --> articles/views.py

DELETE 

게시글 삭제 시 본인 확인(본인만 삭제 가능하도록)
if request.user == article.user: 추가  --> articles/views.py

UPDATE

게시글 수정 시 본인 확인(본인만 수정 가능하도록)
if request.user == article.user: 추가  --> articles/views.py
{ % if request.user == article.user % } --> articles/detail.html

READ

<p>작성자: {{ article.user }}</p> --> index, detail템플릿

######
Comment와 User 간 모델 관계 설정
Comment모델에 User모델 참조하는 외래 키 작성
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

인증된 사용자인 경우 외 접근 제한
@require_POST
if request.user.is_authenticated:
{ % if request.user.is_authenticated % }

######

M:N관계
병원에서 의사와 환자의 관계
target model 관계 필드를 가지지 않은 모델
target model 관계 필드를 가진 모델

이를 표현하는데엔 1:N으론 한계가 있음. 그래서 관계테이블을 만들어주거나
ManyToMany필드를 만들어줘야함.
장고는 ManyToMany필드를 통해 자동으로 중계 테이블을 생성함.


2. ManyToManyField
  patient1.doctors.add(doctor1) ==> 환자1이 의사1에게 예약
  doctor1.patient_set.all() ==> 의사1이 자신에게 예약한 환자들 확인
  patient1.doctors.all() ==> 환자1이 자신이 예약한 의사목록 확인
  doctor1.patient_set.add(patient2) ==> 의사1이 환자2를 예약

  doctor1.patient_set.remove(patient1) ==> 의사1이 환자1 예약 취소
  patient2.doctors.remove(doctor1) ==> 환자2가 예약 취소

related_name: target model이 target model 참조할 때 사용할 manager name
설정시 _set 매니저는 사용불가  

through: 중계 테이블 직접 작성하는 경우. 다대다 관계와 연결할 때.

symmetrical: 기본값은 True이고 대칭을 이룸. 팔로우하면 자동으로 맞팔되는 그런거.
대칭을 원하지 않으면 False설정.

#####
Related Manager 
N:1이나 M:N관계에서 사용가능한 문맥.
모델 생성 시 objects 썼던 것 처럼 Related Manager 통해 쿼리셋 api사용가능.
같은 이름의 메서드여도 관계에 따라 다르게 동작.
add, remove... 등

#####
LIKE
모델 관계 설정
article.user 게시글을 작성한 유저 N:1

user.article_set 유저가 작성한 게시글(역참조) N:1

article.like_users 게시글을 좋아요한 유저 M:N

user.like_articles 유저가 좋아요한 게시글(역참조) M:N

.exists() 쿼리셋에 결과가 포함되어 있으면 True반환하고 그렇지 않으면 False반환

@require_POST
if request.user.is_authenticated:
추가

######
get_object_or_404 가져오던가 없으면 404줘
article = get_object_or_404(Article, pk=pk)
article = Article.object.get(pk=pk)
정상적인 상황에선 같은 기능
######
ORM: SQL사용하지 않고 데이터베이스 조작할 수 있게 만들어주는 매개체
shell이나 shell_plus 사용

쿼리셋 API의 CRUD

CREATE

1. 첫번째 방법 다음의 단계를 거친다 
   article = Article() 클래스를 통한 인스턴스 생성
   Article(class)로 부터 article(instance)

   article.title 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
  article.title = 'first' 인스턴스 변수(title)에 값을 할당
  article.content = 'django!' 인스턴스 변수(content)에 값을 할당

  article.save() 인스턴스로 save 메서드 호출
  save 메서드 호출해야 DB에 값이 저장됨. 그래야 Article.objects.all()로 호출 가능
  article.title 하면 'first' 나옴

2. 두번째 방법 인스턴스 생성 시 초기 값을 함께 작성하여 생성
  article = Article(title='second', content='django!')
  이것도 article.save()해줘야 저장됨.

3. 세번째 방법 
   Article.objects.create(title='third', content='django!') 
   생성된 데이터 바로 반환됨

READ

all() 전체 데이터 조회 Article.objects.all()

get() 단일 데이터 조회, 고유성 보장하는 조회에서 사용하지 않으면 에러
Article.objects.get(pk=1)
Article.objects.get(content='django!')

filter() 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 쿼리셋을 반환 
조회된 객체가 없거나 1개여도 쿼리셋 반환
Article.objects.filter(content='django!)

Field lookups 특정 레코드에 대한 조건을 설정하는 방법. 필터를 더 구체적으로  
메서드 filter(), exclude(), get()에 대한 키워드 인자로 지정됨.
Article.objects.filter(content__contains='dj')  (필드명__gte=20) 필드명 언더바 2개 이퀄
content 컬럼에 'dj'가 포함된 모든 데이터 조회       20보다 크거나 같다

UPDATE

수정하고자 하는 인스턴스 객체 조회하고 새로운 값 할당한 뒤 저장
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()

DELETE

조회 후 삭제
article = Article.objects.get(pk=1)
article.delete()

######
Improve Query 에서 Lazy Loading / Eager Loading 

장고는 기본적으로 Lazy Loading 전략 사용. ORM을 작성하면 DB에 쿼리하는 것이 아니라
미루다가 실제로 데이터를 사용할 때 쿼리를 날림.
ORM 함수를 호출할 때가 아니라 print등 쿼리셋이 실제로 평가될 때 DB에 콜을 날려 데이터를 조회
모든 경우에 호출을 하면 효율이 낮아서 성능개선을 위해 이렇게 함.

Eager Loading은 지금 사용하지 않더라도 가져오는 것으로 보통 여러 테이블의 데이터를 한번에
가져올 때 사용 

 ######
