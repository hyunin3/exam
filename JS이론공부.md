######
JavaScript는 클라이언트 측 웹(브라우저)에서 실행
이벤트 발생 시 웹페이지가 작동하는 디자인/프로그래밍. 동작제어에 사용
HTML문서의 컨텐츠를 동적으로 변경

######
웹 브라우저는 URL을 통해 웹을 탐색. HTML/CSS/JavaScript를 해석해서 사용자에게
화면으로 보여줌
javascript engine 대체적으로 웹브라우저에서 사용. 웹브라우저의 console에서 자바스크립트 입력해도 실행됨. Vanilla JavaScript 웹 브라우저에서 바로 실핼할 수 있는 문법들
ECMAscript는 자바스크립트를 표준화하며 기본적인 문법, 데이터 타입, 연산자 등을 정의

######
식별자는 변수를 구분할 수 있는 변수명. 문자, $, _ 로 시작. for, if, function 등 예약어 사용불가

1. 카멜 케이스 - 변수, 객체, 함수에 사용. camelCase
2. 파스칼 케이스 - 클래스, 생성자에 사용. PascalCase
3. 대문자 스네이크 케이스 - 상수에 사용. SNAKE_CASE

######
변수 선언 키워드
셋 다 변수 선언하며 동시에 값을 초기화

1. let 블록 스코프 지역 변수를 선언. 재할당 가능. 재선언 불가능
2. const 블록 스코프 읽기 전용 상수를 선언. 재할당 및 재선언 불가능
3. var 변수를 선언. 재할당 및 재선언 가능

호이스팅: 변수를 선언 이전에 참조할 수 있는 현상. 원래는 undefined 반환해야하지만 변수를 코드 최상단으로 끌어올려 사용함

######
데이터 타입

1. 원시 타입(primitive type)
  Number- 정수 또는 실수형 숫자를 표현. NaN을 반환하는 몇 가지 경우가 있음 
  
  String- 문자열을 표현. 덧셈만 가능. 따옴표 사용하면 선언 시 줄 바꿈 \n만 가능. Template Literal사용(``과 ${}사용)
  
  null- 값이 없음
  
  undefined- 값이 할당되지 않은 변수. 값이 필요한데 할당 안해놨을 경우에 나옴
  
  Boolean - 참, 거짓

2. 참조 타입(reference type)
   Object- 이름과 값을 가진 속성들의 집합으로 이루어진 자료구조
   Array- 여러개의 값을 순서대로 저장하는 자료구조
   function- function키워드를 통해 생성하며 호출 시 실행될 코드를 정의

######
객체(object)
객체는 속성의 집합이며 {}내부에 키와 밸류 쌍으로 표현
key는 문자열 타입만 가능. value는 모든 타입 가능. 객체 요소는 .이나 []로 가능
키 이름에 띄어쓰기 같은 구분자 있을 시 대괄호만 접근 가능.

배열(Array)
키와 속성들을 담고 있는 참조 타입의 객체. 순서를 보장하는 특징이 있음. []로 생성. 파이썬과 유사한 방식으로 특정 값과 길이에 접근 가능

######
배열 메서드
array.reverse() 원본 배열 요소들의 순서를 반대로 정렬

array.push() 배열의 가장 뒤에 요소 추가

array.pop() 배열의 마지막 요소 제거

array.includes(value) 배열에 특정 값이 존재하는지 판별 후 true 또는 false반환

array.indexOf(value) 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환. 해당값이 없을 경우엔 -1 반환

Array Helper Methods
배열을 순회하며 특정 로직을 수행하는 메서드. 메서드 호출시 인자로 콜백함수 받음
콜백함수: 다른 함수의 인자로 전달되는 함수

forEach 배열의 각 요소에 대해 한번씩 실행. 반환값 없음

map 배열의 각 요소에 대해 콜백 함수를 한번씩 실행하고 새로운 배열 반환. 기존 배열을 바꿈
(forEach + return) 같은 느낌


함수(Function)

함수 선언식 
function add(num1, num2) {
  return num1 + num2
}

함수 표현식 
const sub = function (num1, num2) {
  return num1 - num2
}
######
객체 관련 문법

1. 속성명 축약: 객체를 정의할 때 key와 할당하는 변수 이름이 같으면 축약 가능
const bookShop = {
  books: books, 
  magazines: magazines,
}  

const bookShop = {
  books, 
  magazines,
}  

2. 메서드명 축약: 메서드 선언 시 function 키워드 생략가능
var obj = {
  greeting: function () {
    console.log('Hi!')
  }
}
obj.greeting()

var obj = {
  greeting() {
    console.log('Hi!')
  }
}
obj.greeting()

3. 계산된 속성: 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성가능
4. 구조 분해 할당: 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있음
const name = userInformation
const {name} = userInformation

5. Spread syntax: 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 전개 가능
얕은 복사에 활용 가능
const obj = {b:2, c:3, d:4}
const newObj = {a:1, ...obj, e: 5}

######
JSON
키-밸류 형태로 이루어진 자료 표기법. 오브젝트는 그 자체로 타입이고 제이슨은 형식이 있는 문자열. 제이슨을 오브젝트로 활용하기 위해서는 변환 작업이 필요

const objToJson = JSON.stringify(jsObject)  // Object -> JSON

const jsonToObj = JSON.parse(objToJson)  // JSON -> Object

######
DOM
Browser APIs는 웹 브라우저에 내장된 API로 웹 브라우저가 여러 유용한 일을 수행할 수 있게 함. 그 중 하나가 DOM. 자바스크립트는 DOM API를 통해 HTML과 CSS를 동적으로 수정. 사용자 인터페이스에 많이 쓰임.

문서객체모델. 문서의 구조화된 표현을 제공하며 HTML문서를 구조화하여 각 요소를 객체로 취급. 돔 메서드를 사용하면 문서의 구조, 스타일, 컨텐츠를 변경 가능.문서를 조작하는 방법 제공. 돔에서 모든 것은 Node

Node 돔의 구성 요소 중 하나. HTML문서의 모든 요소를 나타냄.

DOM의 주요 객체: window, document
윈도우는 돔을 표현하는 창이자 가장 최상위 객체이고 작성시 생략가능
도큐멘트는 브라우저가 불러온 웹 페이지. 수많은 다른 요소들 포함하고 있음


######
연산자
할당연산자- 단축연산자 지원
비교연산자- 비교하고 결과값을 t/f로 반환. 뒷쪽 문자가 크고 알파벳은 소문자가 대문자보다 큼.
일치연산자- === 사용. 암묵적 타입 변환 발생하지 않고 엄격한 비교함
논리연산자- and는 &&, or은 ||, not은 ! 이고 단축 평가 지원함
삼항연산자- 3개의 피연산자 사용
스프레드연산자- 배열이나 객체를 분리하여 전달

######
조건문
if, else if, else
조건은 소괄호 안에 작성. 실핼할 코드는 중괄호 안에 작성

######
반복문
while, for, for in(속성 이름을 통해 반복. 객체의 속성을 순회), for of(속성 값을 통해 반복. 반복 가능한 객체를 순회. array, set, string 등)

######
Event
HTML요소에서 발생하는 모든 상황을 의미. 클릭하면 무언가 결과를 받는 것 등

addEventListener()메서드를 통해 이벤트 처리기를 다양한 html요소에 부착하여 처리
Event handler(이벤트 처리기) 이벤트가 발생했을 때 호출되는 함수. 이벤트 객체를 매개로 전달받음
EventTarget.addEventListener(type,handler function)
  대상                    특정 이벤트     할 일

addEventListener 지정한 이벤트가 대상에 전달될 때마다 호출할 함수 설정
type 반응할 이벤트 유형을 나타냄. input, click, submit...  
handler function 지정된 타입의 이벤트 수신할 객체. 콜백함수여야 하고 이벤트 객체를 매개변수로 받음

addEventListener ~하면 ~한다. 특정 이벤트가 발생하면 할 일을 등록한다.

######
이벤트 전파: DOM요소에서 발생한 이벤트가 상위노드에서 하위노드 혹은 그 반대로 전파되는 현상
addEventListener 메서드를 사용해서 전파방식 제어 가능 
event.preventDefault() 현재 이벤트의 기본 동작을 중단. a태그(클릭시 이동)나 form태그(폼 데이터 전송) 등 기본 동작 작동 안하도록
h1.addEventListener('copy', function(event) {
  event.preventDefault()
})

btn.addEventListener('click', function (event) {
    event.preventDefault()
})

######
동기와 비동기

주문 후 커피 나올 때까지 기다림(동기식)
주문 순서 상관없이 나오는 대로 가져감(비동기식)

1. 동기
모든 일을 순서대로 하나씩 처리. 이전 작업이 끝나면 다음 작업을 시작. 파이썬 코드 등

2. 비동기 
결과를 기다리지 않고 다음 작업 처리(병렬적 수행). 시간이 오래 걸리는 작업은 요청 보내고 응답 빨리 오는 작업부터 처리

사용자 경험에 긍정적 효과를 보기 위해 비동기 사용. 동기식 처리로 하면 이미지 등 오래 걸리는 작업하면 로딩 오래 걸려서 멈춘것처럼 느낌.

######
JS는 single thread언어라서 동시에 여러 작업 처리 못함. 비동기 처리 도와주는 환경 필요. 
비동기와 관련된 작업은 브라우저나 노드 환경에서 처리.
1. Call Stack
2. Web API
3. Task Queue
4. Event Loop

비동기 처리의 동작방식
1. 모든 작업은 Call Stack으로 들어간 후 처리
2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue에 순서대로 들어간다
4. Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 작업을 Call Stack으로 보낸다

Call Stack: 요청이 들어올때마다 순차적으로 처리. 기본적인 JS의 작업 처리
Web API: JS엔진이 아닌 브라우저에서 제공하는 runtime 환경. 시간이 소요되는 작업을 처리
Task Queue: 비동기 처리된 콜백함수가 대기하는 큐. 웹에이피아이에서 받음
Event Loop: 콜스택과 태스크 큐 지속적으로 모니터링하다가 콜스택 비면 태스크큐에서 오래 대기 중인 작업을 콜스택으로 push

######
Axios 
자바스크립트의 HTTP 웹 통신을 위한 라이브러리. 비동기 데이터로 통신을 가능하게 함
axios.get('URL')
  .then(성공하면 수행할 콜백함수)
  .catch(실패하면 수행할 콜백함수)

######
비동기 처리는 Web API로 들어오는 순서대로가 아니라 작업이 완료되는 순서에 따라
처리. 그래서 코드 실행순서 명확하게 하기 위해 콜백함수를 사용함. 코드의 가독성과 유지보수 위해 프로미스라는 객체를 사용. 비동기 작업의 완료 또는 실패를 나타내는 객체

.then(callback)
.catch(callback)

둘 다 항상 promise 객체를 반환. 액시오스로 처리한 비동기 로직이 항상 프로미스 객체를 반환. chaining

동기식 코드는 위에서부터 순서대로 처리가 되기 때문에 순서대로 print되는 반면 비동기식 코드는 바로 처리가 가능한 작업인 console.log는 바로 처리하고 이미지 요청하고 가져오는 일은 기다리지 않고 다음 코드 진행하고 결과 출력 진행함

######
비동기 처리는 web api 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리함
개발자 입장에서 코드의 실행순서가 불명확하기 때문에 콜백함수 사용. 그러나 유지보수와 가독성을 위해 promise사용. 작업이 끝나면 실행시켜준다는 약속. 비동기 작업의 완료 또는 실패를 나타내는 객체. 프로미스 기반의 클라이언트가 Axios 라이브러리

######
axios로 처리한 비동기 로직이 항상 promise객체를 반환
콜백은 이전 작업의 성공/실패를 인자로 받음. then, catch 둘 다 promise객체를 반환하기 때문에 계속 chaining 가능. then으로 계속 연결 가능

######
promise vs 비동기 콜백

1. promise의 콜백함수는 이벤트 큐에 배치되는 순서대로 호출됨. 일반 콜백함수는 이벤트 루프가 현재 실행 중인 콜 스택을 완료하기 전엔 호출되지 않음

2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1과 같이 동작

3. then을 여러번 사용하여 여러개의 콜백함수 추가 가능. chaining된 순서대로 하나씩 실행 