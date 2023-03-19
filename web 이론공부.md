<시험대비 web공부>

html의 요소는 태그와 내용(contents)으로 구성. 모든 내용은 태그로 
감싸져 있어야함. 요소는 시작태그와 종료태그, 그 사이의 내용으로 구성.
속성은 각 태그별로 사용 가능한 것이 다름. href같은 것이 속성명.
https...같은 것이 속성값. 태그와 상관없이 사용가능한 속성도 있음. id, class, style 등.

label을 클릭하여 input자체의 초점을 맞추거나 활성화 가능.
label에는 for속성, input에는 id속성을 활용.

css의 정의방법에는 인라인, 내부참조, 외부참조가 있음.
선택자, 선언, 속성, 값으로 구성.
css적용 우선 순위는 중요도>인라인>id>class,속성>요소. 
그리고 클래스에선 늦게 선언된 것으로.

css상속은 text관련 요소는 상속되고 box model 관련 요소는 상속되지 않음.

normal flow 모든 요소는 박스모델이고 왼쪽에서 오른쪽으로, 위에서 아래로 향함.

margin, border, padding, content로 구성

마진 주는거 숏핸드 한개: 4방향, 두개: (상하) (좌우), 세개: (상) (좌우) (하)
네개: 시계방향으로 하나씩

보더 숏핸드: 2px dashed black 형식

일반적으론 boder-box이기 때문에 우리가 생각하는 크기로 하려면
box-sizing으로 content-box해줘야됨.

display;block 줄바꿈이 일어남. 가로전체. 안에 인라인 들어갈 수 있음
div, ul, p, form 등. 너비하고 남으면 나머지 자동으로 마진 부여되서 꽉채움.
margin-right

display:inline 줄바꿈 안일어나고 content만큼 차지 
span, a, img, input, label 등
text-align:center;

display:inline-block 인라인 블록 모두의 특징 가짐.
display:none해당요소를 화면에 표시하지 않고 공간도 부여하지 않음.
visibility:hidden은 화면에 표시는 안하지만 공간은 차지함.

static: 기본값. 기준위치. 노말플로우 따름
relative: 상대위치. 노말 플로우 따르면서 자신의 스태틱위치를 기준으로 이동.
absolute: 요소를 노말플로우에서 벗어나게 하고 공간차지하지않게 제거 후 
스태틱이 아닌 가장 가까이 있는 부모/조상요소 기준으로 이동.
fixed: 노말플로우에서 벗어나고 뷰포트 기준으로 이동함. 스크롤해도 같은 위치.

float 노말플로우 벗어나도록 신문형태 레이아웃 잡을 때 쓰는데 요즘은 잘 안씀

flex박스 부모요소인 container와 자식요소인 item으로 구성. 축은 메인축과 교차축.
컨테이너에 적용하는 속성과 아이템에 적용하는 속성이 다름.

배치속성
flex-direction row는 가로방향 column은 세로방향. 메인축의 방향 설정
flex-wrap 아이템이 컨테이너를 벗어나지 않게 배치. 강제로 한줄에 배치되게 할지 설정
wrap(넘치면 그 다음줄 배치)과 nowrap(기본값. 한줄배치)
공간 나누기
flex-flow는 디렉션과 랩의 숏핸드

justify-content(main axis) 메인축 기준으로 공간배분. 
align-content(cross axis) 교차축 기준으로 공간배분.
정렬
align-items(모든 아이템을 교차축 기준으로)
align-self(개별 아이템) 컨테이너에 적용되는 것이 아니라 개별 아이템에 적용됨.

Bootstrap 반응형 웹을 구현하기 좋음.
Grid system 안쪽요소들 오와 열 맞추는 것에서 기인. 
12개의 column 6개의 breakpoints
column 실제 컨텐츠를 포함하는 부분 
gutter 칼럼 사이 간격
container 칼럼들을 담고 있는 공간

컨테이너 로우 콜

col-sm-8 col-md-4 col-lg-5 스몰 이상에선 8 미디엄 이상에선 4 라지 이상에선 5
