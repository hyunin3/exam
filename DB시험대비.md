관계형DB(RDB): 표로 정리된 DB. 일반적으로 메인으로 많이 사용되고 있음. 
형식이 정해져 있고 관계에 대해 표현을 해야함. 수정이 어렵고 테이블 형식이라
유연성이 없고 확장도 힘듦. 대부분의 관계형에서 SQL을 이용해 조작 가능.
자료를 테이블로 나누어 관리, 테이블 간 간계 설정. 데이터 무결성 유지에 장점.

비관계형 DB: 관계형의 한계를 극복하기 위해 조금 더 유연하게 만든 DB. 빠른 처리나 확장이
필요할 때 서브로 사용함. NoSQL

스키마: 청사진. 테이블의 구조, 데이터 베이스에서 자료구조, 관계, 표현 방법 등 명세 기술한 것

테이블: 필드와 레코드를 사용해 조직된 데이터 요소들 집합. 관계(Relation)
필드(속성, 칼럼, 세로), 레코드(튜플, 행, 가로)

PK: 고유한 단일값
FK: 외래키. 다른 테이블의 레코드 식별할 수 있는 키. 테이블 간 관계 만드는데 사용

DBMS: DB를 조작하는 프로그램

SQL: 관계형 데이터베이스 관리 + CRUD하는 언어

DDL: 데이터 정의 언어. 구조를 정의하기 위한 명령어. 테이블, 스키마를 생성, 수정, 삭제
CREATE, DROP, ALTER

DML: 데이터 조작 언어. 데이터를 조작하기 위한 명령어. 추가, 조회, 변경, 삭제
INSERT, SELECT, UPDATE, DELETE

data types: NULL, INTEGER, REAL, TEXT, BLOB
타입 선호도가 있어서 호환성 상승

데이터 무결성: DB내 정확성, 일관성 보장 위해 변경시 제한을 두는 것
NOT NULL, UNIQUE, PRIMARY KEY, AUTOINCREMENT

rowid: 암시적 자동증가 컬럼, 테이블의 행 고유하게 식별. 1부터 시작.
데이터 삽입시 명시적 지정 없으면 다음 순서 할당. 별칭 rowid가능

CREATE TABLE 새 테이블 생성

ALTER TABLE: Rename a table, Rename a column, Add a new column to a table, Delete a column