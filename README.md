# fast-api-example-from-sun
fast api example

안녕하세요 최선입니다.
요즘 fastapi의 관심이 많아지고 있더라구요. 쉽게 사용하시길 바랍니다.

일단. Fast API를 사용하기 위해서 패키지를 설치해주세요.

1. pip install fastapi

![image](https://user-images.githubusercontent.com/86217603/181398123-ba9b9ac3-2b06-4880-9c9f-f3f481970a1d.png)

파이썬 실행시 서버 구동을 위해 uvicorn을 설치 해줍니다.

2. pip install uvicorn

![image](https://user-images.githubusercontent.com/86217603/181398346-f65e0a66-b781-4c1b-b8b1-8e16c088eaac.png)

FastAPI Class를 testServer라는 이름으로 생성 해줍니다.

3. testServer = FastAPI()

![image](https://user-images.githubusercontent.com/86217603/181398741-afd69c46-a96a-4770-8a1f-ad3021fc703e.png)

@testServer.get("/url") 방식으로 get을 쉽게 구현 가능

![image](https://user-images.githubusercontent.com/86217603/181398974-6079b3f7-3cf0-48d1-83b7-ee75bbfe7323.png)

4. 실행문을 작성해줍니다.

![image](https://user-images.githubusercontent.com/86217603/181399034-082b0e16-2b95-4833-80f5-dedd5be34c4f.png)

정말 간단하게 완성된 코드

![image](https://user-images.githubusercontent.com/86217603/181399100-b50a7e74-86ea-4803-bbc0-813b431f6e13.png)


Fast API의 장점은 /docs에 사용법이 자동으로 만들어집니다

![image](https://user-images.githubusercontent.com/86217603/181400019-811c9d85-e171-4041-a83a-c49da97d73a6.png)

