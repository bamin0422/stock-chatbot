# Bamin-Stock

| ![](/home/bamin/Projects/stock-chatbot/image/Bamin-Stock02.png) |
| :----------------------------------------------------------: |

> To. **주린이들에게...**
>
> 
>
> 안녕하세요! 주린이 여러분 :)
>
> 주식 한지 한 달밖에 안 된 주린이 **"Bamin"** 입니다.
>
> 저와 여러분과 같이 주식에 입문한지 얼마 안 된 주린이들을 위한, 'Bamin-Stock'  chatbot을 만드려고 합니다. 
>
> Bamin-stock은 종목시황, 공시, 현재주가, 관심종목 등의 정보를 실시간으로 주린이들과 소통하기 위해 기획되었습니다.
>
> 아직 부족하지만 차근차근 공부하면서, chatbot을 구현해보자구요.
> 																			
>
> ​																											      		From.  **Bamin**



[![thumbnail](/image/plusfriend.png)](http://pf.kakao.com/_xircaxb)






## Bamin-Stock 구현 명세
<br/>

고객은 Bamin-stock을 인증번호를 입력하면 메뉴가 뜨면서 주식 정보를 얻을 수 있다.



Bamin-Stock은 현재 관심 가지고 있는 종목, 주요 공시와 특징주 정보를 Bamin-Stock-Site에서 불러온다.

불러온 정보를 Bamin-Stock이라는 챗봇을 통해 클라이언트에게 제공해준다.



프로그램 구동시 발생하는 시나리오는 다음과 같다.
=======
Bamin-Stock은 현재 관심 가지고 있는 종목, 장 공시와 특징주 정보를 불러오는 기능을 가졌습니다.

고객은 Bamin-stock을 인증번호를 입력하면 메뉴가 뜨면서 주식 정보를 얻을 수 있습니다.



프로그램 구동시 발생하는 시나리오는 다음과 같습니다.


> 1. 인증번호를 입력하면 챗봇이 활성화 된다.
> 2. 챗봇 안내 메시지와, 하단의 메뉴가 출력된다.
> 3. 입력, 메뉴가 클릭된다.
> 4. 입력에 맞는 정보를 Bamin-Stock-Site에서 찾는다.
> 5. 찾은 정보를 챗봇을 통해 보내준다.

### 프로필 화면 구현 명세

프로필 화면은 하단의 사진과 같다.  더 알아보기를 클릭하면, 깃허브로 이동한다.

| ![](/image/Bamin-Stock02.png) |
| ------------------------------------------------------------ |





### 하단 메뉴 구현 명세

 하단 메뉴의 구성 요소는 **주식검색, 주요공시, 특징주, 관심종목1, 관심종목2, 관심종목3** 으로 구성되어 있다.

| ![](/image/Bamin-Stock03.png) |
| ------------------------------------------------------------ |

