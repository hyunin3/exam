######
관계형DB (RDB): 표로 정리된 DB. 일반적으로 메인으로 많이 사용되고 있음. 
형식이 정해져 있고 관계에 대해 표현을 해야함. 수정이 어렵고 테이블 형식이라
유연성이 없고 확장도 힘듦. 대부분의 관계형에서 SQL을 이용해 조작 가능.
자료를 테이블로 나누어 관리, 테이블 간 간계 설정. 데이터 무결성 유지에 장점.
외래키를 사용하여 각 행에서 서로 다른 테이블 간 관계 만드는데 사용 가능.

비관계형 DB: 관계형의 한계를 극복하기 위해 조금 더 유연하게 만든 DB. 빠른 처리나 확장이
필요할 때 서브로 사용함. NoSQL

스키마: 청사진. 테이블의 구조, 데이터 베이스에서 자료구조, 관계, 표현 방법 등 명세 기술한 것

테이블: 필드와 레코드를 사용해 조직된 데이터 요소들 집합. 관계(Relation)
필드(속성, 칼럼, 세로), 레코드(튜플, 행, 가로)

PK: 고유한 단일값
FK: 외래키. 다른 테이블의 레코드 식별할 수 있는 키. 테이블 간 관계 만드는데 사용

DBMS: DB를 조작하는 프로그램

SQL: 관계형 데이터베이스 관리 + CRUD하는 언어

######
DDL: 데이터 정의 언어. 구조를 정의하기 위한 명령어. 테이블, 스키마를 생성, 수정, 삭제
CREATE, DROP, ALTER

data types: NULL, INTEGER, REAL, TEXT, BLOB
타입 선호도가 있어서 호환성 상승

데이터 무결성: DB내 정확성, 일관성 보장 위해 변경시 제한을 두는 것
NOT NULL, UNIQUE, PRIMARY KEY, AUTOINCREMENT

rowid: 암시적 자동증가 컬럼, 테이블의 행 고유하게 식별. 1부터 시작.
데이터 삽입시 명시적 지정 없으면 다음 순서 할당. 별칭 rowid가능

CREATE TABLE 새 테이블 생성

ALTER TABLE: Rename a table(RENAME TO), Rename a column(RENAME COLUMN), Add a new column to a table(ADD COLUMN), Delete a column(DROP COLUMN)

컬럼삭제 못하는 경우: 컬럼이 다른 부분에서 참조되는 경우, PK인 경우, 유니크 제약조건인 경우

DROP TABLE: DB에서 테이블 제거. 존재하지 않는 테이블 제거시 오류발생. 복구불가. 한번에 한 테이블만 삭제 가능

######

DML: 데이터 조작 언어. 데이터를 조작하기 위한 명령어. 추가, 조회, 변경, 삭제
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

제1 정규형
하나의 속성값이 복수형을 가지면 안된다. 하나의 속성값엔 값이 하나만 들어가야함.
(ex) 등록완료 박민서 수영, 필라테스 -->이런거 안된다.

제2 정규형
테이블의 기본키에 종속되지 않는 컬럼은 테이블 분리해야함. 관련없는 애들 따로 분리.
FK를 사용. 
(ex) 기존 테이블에서 운동은 FK로 하고 다른 테이블에 운동 명과 금액 분리시킴.


제3 정규형
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
RTGHT JOIN
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
