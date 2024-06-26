# 🤖IE-FI Project

### 📑 프로젝트 개요
- 서비스명 : **아이파이(IE-FI)**
- 주제 : 유저 정보를 기반으로 한 금융상품 조회 및 추천 서비스
- 기간 : 2024.05.08(수) ~ 2023.05.23(목)

<br>


### 🐂 서비스 소개
- 당신의 금융 생활, 만족스러우신가요? 저희는 <b>'아이파이(IE-FI)'</b>라는 플랫폼을 통해 개인 맞춤형 금융 서비스와 다양한 금융 정보를 한 눈에 제공해드립니다. **아이파이**는 <b>'나만의 금융, 한 눈에 금융'</b>이라는 의미를 담고 있으며, 사용자가 자신의 금융 상황을 쉽게 파악하고 최적의 금융 상품을 찾을 수 있도록 도와줍니다.
- <b>아이파이(IE-FI)</b>와 함께라면, 복잡한 금융 정보를 한 눈에 확인하고, 나에게 딱 맞는 금융 상품을 쉽게 찾아 가입할 수 있습니다. 지금 <b>아이파이(IE-FI)</b>와 함께 스마트한 금융 생활을 시작하세요!<br><br>
[🌟PPT 발표자료 바로가기🌟](https://www.canva.com/design/DAGGAdcSfL8/XMwzKyHoKB6agQzcJtEzvg/view?utm_content=DAGGAdcSfL8&utm_campaign=designshare&utm_medium=link&utm_source=editor)

<br>



### 📺 서비스 메인페이지
![MainPage_1](https://github.com/Kangsooyeon/final-pjt/assets/64363148/96f93c47-c33e-41f5-bd3e-48eca2d595d4)
![MainPage_2](https://github.com/Kangsooyeon/final-pjt/assets/64363148/5a2abe60-f5ba-42c1-87d7-46fdc056c20e)
<br>
<br>



### ✨ 주요 기능

- 메인페이지
    - Nav바, Carousel, 빠른메뉴, footer 에서 주요 기능 페이지 전환
    - Carousel 및 환율 Auto Slide
    - 실시간 환율 그래프 출력 (미국, 일본, 유럽, 중국)
    - 실시간 News 키워드별 10개 출력 (금융, 경제, 주식, 코인) 
    - 반응형 디자인 : 햄버거 바 나타남, 빠른 메뉴 사라짐

- 회원 관리
    - 회원 가입을 통해 개인 정보 등록 
        - 필수 : ID, 비밀번호, 비밀번호 확인, 이름, 이메일
        - 선택 : 생년월일, 성별, 주거래계좌, 연봉, 자산, 희망자산
    - 로그인 후 사용할 수 있는 기능  
        - 프로필(가입상품, 추천상품)
        - 상품가입
        - 게시글 작성/수정/삭제
        - 댓글 작성/수정/삭제
        - 내가 작성한 게시글

- 프로필
    - [회원정보] 회원 정보 출력 및 수정 가능
    - [가입상품] 사용자가 가입한 예금 및 적금 리스트 출력
    - [가입상품] 금융 상품 상세 페이지로 이동
    - [가입상품] 특정 상품 클릭 시, 동적으로 그래프 출력 (예상 수입금 및 금리), 최대 5개
    - [추천상품] 금융 상품 추천 알고리즘을 통해 사용자 개인 정보에 따른 상품 추천, 최대 5개
    - [추천상품] 금융 상품 상세 페이지로 이동

- 상품 조회
    - 다양한 은행들의 예적금 상품의 가입기간 별 금리 정보를 제공
    - 각 상품의 금리, 기간, 조건 등에 대한 정보를 제공
    - 특정 상품에서 다양한 금리 옵션 중, 하나 선택하여 가입 가능
    - 가입 시, 가입할 금액을 입력하면 최고한도, 최저한도, 만기 후 예상 금액 출력
    - 이미 가입한 상품이면 **'이미 가입한 상품입니다.'** 표시

- 환율 계산
    - 송금 보낼 때 및 송금 받을 때의 환율 계산 가능
    - 국가 선택 시, 해당 국가의 국기 및 단위 동적으로 출력
    - 실시간 환율 그래프 출력
    - 5일 후 환율 예측 그래프 출력

- 은행 지도
    - 은행 지도 페이지 진입 시, 현재 실시간 위치 반영하여 지도 렌더링
    - 시/도, 시/군/구, 읍/면/동, 특정 은행, 검색 시, 조건에 만족하는 은행 리스트 및 해당 은행 위치의 지도 마커 출력
    - 초기 위치로 이동 클릭 시, 현재 위치의 지도 렌더링

- 커뮤니티
    - 로그인하지 않은 사용자는 게시글 목록 및 상세 게시글 조회만 가능
    - 로그인한 사용자는 게시글 생성/수정/삭제 및 댓글 생성/수정/삭제 가능
    - 로그인한 사용자는 내가 쓴 글 목록 확인 가능
    - 닉네임, 제목으로 게시글 검색 가능

<br>


### 🗓️ 프로젝트 진행 일정(ERD)
![project schedule](https://github.com/Kangsooyeon/final-pjt/assets/64363148/fd6190a7-5110-4486-8098-bfa226eb1baa)

<br>
<br>



### 📚 데이터베이스 모델링(ERD)
![ssafy_ERD](https://github.com/Kangsooyeon/final-pjt/assets/64363148/71517db1-361f-478b-b1ee-6521087bb61b)

[ERD 자세히보기](https://drive.google.com/file/d/1N95VM-OvSkWVJ4va5LuDluMedzobXN0n/view?usp=sharing 
)
<br>
<br>


### 💡 컴포넌트 다이어그램(CD)
![Component_Diagram)](https://github.com/Kangsooyeon/final-pjt/assets/64363148/5e6b808a-eba2-4854-937d-1bf4216f64ea)
<br>
<br>

### 🎨 Figma
[피그마(Figma) 바로가기](https://www.figma.com/design/Uy31BZyMWYI5IgdI6UUQeb/Finla_PJT_FirstSemester?node-id=0:1&t=wQzCsVWLCIowAyXC-1)
<br>
<br>


### 🔍 금융 상품 추천 알고리즘에 대한 기술적 설명

##### 사용자 나이
>- 40세 미만 : 12개월 이하 상품 필터링
>- 40세 이상 : 12개월 이상 상품 필터링


##### 1차 필터링
>- 예금 : 자산>0 & 최대한도 < 자산
>- 적금 : 연봉>0 & 최대한도 < 연봉/12*0.6
>- 적금 : 자산>0 & 최대한도 < 자산/12*0.6

(최대한도금액으로 가입 유도)

생년월일을 입력했을 때, 위의 조건으로 예금 및 적금 각각 필터링


##### 사용자 자산+연봉
>- 5천만원 미만 : 예금 2개, 적금 3개 추천<br>
    만약 예금상품 추천 개수가 2개 미만이면 <br> 
    ⇒ (적금상품 추천 개수) = 5 - (예금상품 추천 개수) 로 지정
    
>- 5천만원 이상 : 예금 3개, 적금 2개 추천<br>
    만약 예금상품 추천 개수가 3개 미만이면 <br>
    ⇒ (적금상품 추천 개수) = 5 - (예금상품 추천 개수) 로 지정
    
⇒ 사용자마다 총 5개의 상품 추천

만약 자산 0원, 연봉 0원이면 **“추가 정보를 입력해주세요!”** 텍스트 출력 및 회원정보 수정 페이지로 이동


##### 사용자의 주거래은행
>- 추천상품 5개 중에 주거래은행이 존재하면 가장 먼저 추천!

<br>
<br>



### 👽 AI 구현 내용
- 📈 환율 예측 (시계열 분석)
    - 각 나라별 시계열 데이터프레임 생성
    - 차분 및 정상성 확인(ADF 테스트)
    - ACF 및 PACF 분석
    - 최적의 (p, d, q) 선택
    - ARIMA 모델을 통한 예측 수행
    - 예측 결과 시각화

- 📰 뉴스 키워드 추출 (NLP 자연어 처리)
    - Okt 형태소 분석기를 통한 명사 추출
    - 불용어 직접 지정
    - TF-IDF를 활용하여 키워드별 중요한 정도 수치화
    - 수치가 가장 높은 키워드 출력
<br>
<br>


### 😊 팀원 소개 및 역할 분담

- **🦸‍♀️강수연(팀장 - BackEnd)**

설계
>- ERD 작성
>- 피그마 작성
    
User
>- 커스텀 유저 모델 생성
>- 회원가입, 로그인, 로그아웃, 회원정보수정 URL 생성
    
Article & Comment
>- 게시글 및 댓글 모델 생성
>- 게시글 CRUD, 댓글 CRUD URL 생성

Products
>- 예금 및 적금의 상품&옵션 모델 생성
>- 금융감독원 API를 활용하여 예금 및 적금의 상품&옵션 DB 저장
>- 예금 및 적금 리스트 URL 생성
>- 예금 및 적금의 상품&옵션 Detail URL 생성
>- 예금 및 적금 최고 이율 Top5 상품 URL 생성

SubcribedProducts
>- 사용자가 가입한 예금 및 적금 모델 생성
>- 예금 및 적금 가입 URL 생성
>- 사용자가 가입한 예금 및 적금 리스트 URL 생성

RecommentProduct
>- 사용자 정보에 따른 금융 상품 추천 알고리즘 설계
>- 상품 추천 URL 생성

ExchangeRate
>- 환율 모델 생성
>- 한국수출입은행 API를 활용하여 환율 DB저장
>- 국기 모델 생성
>- 외교부 API를 활용하여 국기 DB 저장

ExchangeRate-Graph & Predict
>- 한국은행 API를 활용하여 환율 그래프 생성
>- ARIMA 모델을 통해 5일 후 환율 예측하여 그래프 생성

Location
>- 읍면동별 위도 및 경도 데이터 DB 저장

News & Keyword Extraction
>- 네이버 뉴스 API를 활용하여 특정 키워드별 실시간 검색한 뉴스 리스트 URL 생성
>- OKT 형태소 분석기 및 TF-IDF를 활용하여 실시간 수집한 뉴스 본문의 주요 키워드 추출

Create Dummy Data
>- 사용자 dummy_data 생성
>- 사용자별 가입한 상품 dummy_data 생성
>- 사용자별 작성한 게시글 및 댓글 dummy_data 생성

Create Image & Presentation
>- IE-FI 로고 제작
>- Carousel 이미지 제작
>- PPT 제작

<br>



- **🦸‍♂️김동건(팀원 - FrontEnd)**
  
설계
>- Vue3 Diagram작성
>- 피그마 작성
    
Nav
>- 로그인 여부에 따라 다른 버튼 
>- 화면 크기에 따라 햄버거바 적용
>- 각각의 메뉴로 링크

Footer
>- 각각의 메뉴로 링크

Login, Update, Logout
>- 유효성 검사
>- Userinfo 각각 초기화, 토큰 초기화, 로그인 여부(computed)

Signup
>- 유효성 검사

ProductList
>- 정렬 및 검색 구현
>- Pagination 구현

ProductDetail
>- 상품정보 처리
>- Option에 따른 상품 가입버튼
>- 가입 알고리즘(가입금액-예상금액-가입여부)
>- 가입여부 표시

ExchangeRate
>- 국가 전환 버튼
>- 환율 전환 버튼
>- 그래프 전환버튼(현재 - 예측)

Map
>- 카카오 맵 API(현재 위치 시작)
>- 검색 기능
>- 마커생성 및 리스트 생성
>- 마커 혹은 리스트 클릭시 해당 위치로 이동 및 현재 위치 이동

Community
>- 게시글 CRUD
>- 게시글 검색
>- 댓글 CRUD

Profile
>- 유저정보 조회
>- 가입한 상품 리스트 & 그래프 
>- 상품추천 서비스 유효성 검사
>- 상품 카드 및 리스트 


<br>



### 💙 느낀 점

- 🧚‍♀️강수연
    - ERD 설계 및 테스트 케이스 설계의 중요성  
    - 실시간 진행 상황 보고 필요성
    - 긍정적인 마인드 함양 필요

- 🧚‍♂️김동건
    - 알고리즘과 자료구조의 중요성을 체감했다. 하지만 API명세서와 DB를 팀원과의 협업으로 잘 설계 한다면 알고리즘을 짤 필요가 없겠다고 생각했다.
    - 자세한 구조를 알지 못하는 프레임 워크는 내가 마음대로 쓰기 힘들었다.
    - 협업에서는 뭐든지 상의를 해야 할 것 같다. 
<br>
<br>


### ⏳ 기능 테스트
![function test_1](https://github.com/Kangsooyeon/final-pjt/assets/64363148/75eaea6b-40e5-4d85-a12e-bbd5446e3212)
![function test_2](https://github.com/Kangsooyeon/final-pjt/assets/64363148/10c303a4-f3e2-4faf-9f31-f9e32aea0139)


<br>
<br>


### 📂API 명세서
[Postman Documentation 바로가기](https://documenter.getpostman.com/view/34202855/2sA3JRYecY)
<br>
<br>

### 🎀 Notion
[Notion 바로가기](https://www.notion.so/1-19ab026c923543e2bdebb73e841cfe8b?p=a05e3ab960bc49fca014638c53f166dc&pm=s)
<br>
<br>

