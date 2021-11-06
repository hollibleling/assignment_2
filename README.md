# Asignment2
원티드x위코드 백엔드 프리온보딩 과제2
- 과제 출제 기업 정보
  - 기업명 : 프레시코드
  - [프레시코드 사이트](https://www.freshcode.me/)
  - [wanted 채용공고 링크](https://www.wanted.co.kr/wd/34118)

## Members
|이름   |Github                   |Blog|
|-------|-------------------------|--------------------|
|이태성 |[yotae07](https://github.com/yotae07)     | 추가   |
|임유선 |[YusunL](https://github.com/YusunL)   | 추가   |
|윤현묵 |[fall031-muk](https://github.com/fall031-muk) | https://velog.io/@fall031   |
|김정수 |[hollibleling](https://github.com/hollibleling) | https://velog.io/@hollibleling  |
|최현수 |[filola](https://github.com/filola) | https://velog.io/@chs_0303 |

## 과제 내용
> 아래 요구사항에 맞춰 게시판 Restfull API를 개발합니다.

### [필수 포함 사항]
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅

### [개발 요구사항]
- Database 는 RDBMS를 이용합니다
- 로그인 기능(JWT 인증 방식)

## 기술스택
- python, django-rest-framework
- sqlite3
- AWS EC2
- Slack, Git

## 구현 기능
### 로그인 기능
- 내용추가

### 상품 관리 기능
- 상품 전체목록 조회 가능 및 페이징 기능(한 페이지당 5개 상품)
- 사용자는 상품 조회만 가능하며 관리자는 상품 추가/수정/삭제 가능

## API

## 실행 방법(endpoint 호출방법)

### ENDPOINT

| Method | endpoint | Request Header | Request Body | Remark |
|:------:|-------------|-----|------|--------|
|GET|/product||    |전체 상품 조회|
|GET|/product/product_id||    |개별 상품 조회|
|PATCH|/product/product_id||name|상품 수정|
|DELETE|/product/product_id||| 상품 삭제 |

## API 명세(request/response)

### 1. 전체 상품 조회
- Method : GET
- EndpointURL : /product
- Remark : 페이징 포함(상품 5개 조회)
- Request
```
GET "http://127.0.0.1:8000/product HTTP/1.1"

```
- Response
```
{
    "count": 11,
    "next": 2,
    "previous": null,
    "results": [
        {
            "id": 1,
            "category": "salad",
            "name": "깔깔마리 달래 샐러드",
            "description": "해산물 샐러드",
            "isSold": false,
            "badge": "new",
            "items": [
                {
                    "id": 1,
                    "name": "스몰",
                    "size": "S",
                    "price": 7000,
                    "isSold": false,
                    "menuid": 1
                },
                {
                    "id": 2,
                    "name": "미디움",
                    "size": "M",
                    "price": 7500,
                    "isSold": false,
                    "menuid": 1
                },
                {
                    "id": 3,
                    "name": "라지",
                    "size": "L",
                    "price": 8000,
                    "isSold": false,
                    "menuid": 1
                }
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "샐러드",
                    "type": "샐러드",
                    "menuid": 1
                }
            ]
        },
        {
            "id": 2,
            "category": "salad",
            "name": "연어 샐러드",
            "description": "샐러드",
            "isSold": false,
            "badge": "new",
            "items": [
                {
                    "id": 4,
                    "name": "스몰",
                    "size": "S",
                    "price": 10000,
                    "isSold": false,
                    "menuid": 2
                },
                {
                    "id": 5,
                    "name": "미디움",
                    "size": "M",
                    "price": 11000,
                    "isSold": false,
                    "menuid": 2
                }
            ],
            "tags": [
                {
                    "id": 2,
                    "name": "샐러드",
                    "type": "샐러드",
                    "menuid": 2
                }
            ]
        },
        {
            "id": 3,
            "category": "salad",
            "name": "차돌박이 샐러드",
            "description": "샐러드",
            "isSold": false,
            "badge": "old",
            "items": [
                {
                    "id": 6,
                    "name": "미디움",
                    "size": "M",
                    "price": 12000,
                    "isSold": false,
                    "menuid": 3
                },
                {
                    "id": 7,
                    "name": "라지",
                    "size": "L",
                    "price": 13000,
                    "isSold": false,
                    "menuid": 3
                }
            ],
            "tags": [
                {
                    "id": 3,
                    "name": "샐러드",
                    "type": "샐러드",
                    "menuid": 3
                }
            ]
        },
        {
            "id": 4,
            "category": "salad",
            "name": "닭가슴살 샐러드",
            "description": "샐러드",
            "isSold": false,
            "badge": "old",
            "items": [
                {
                    "id": 8,
                    "name": "미디움",
                    "size": "M",
                    "price": 8000,
                    "isSold": true,
                    "menuid": 4
                }
            ],
            "tags": [
                {
                    "id": 4,
                    "name": "샐러드",
                    "type": "샐러드",
                    "menuid": 4
                }
            ]
        },
        {
            "id": 5,
            "category": "milk",
            "name": "우유",
            "description": "우유",
            "isSold": false,
            "badge": "new",
            "items": [
                {
                    "id": 9,
                    "name": "라지",
                    "size": "L",
                    "price": 7000,
                    "isSold": true,
                    "menuid": 5
                }
            ],
            "tags": [
                {
                    "id": 5,
                    "name": "우유",
                    "type": "우유",
                    "menuid": 5
                }
            ]
        }
    ]
}
```

### 2. 개별 상품 조회
- Method : GET
- EndpointURL : /product / product_id
- Remark : product_id로 개별 상품 선택
- Request
```
GET "http://127.0.0.1:8000/product/1 HTTP/1.1"

```
- Response
```
{
    "id": 1,
    "category": "salad",
    "name": "깔깔마리 달래 샐러드",
    "description": "해산물 샐러드",
    "isSold": false,
    "badge": "new",
    "items": [
        {
            "id": 1,
            "name": "스몰",
            "size": "S",
            "price": 7000,
            "isSold": false,
            "menuid": 1
        },
        {
            "id": 2,
            "name": "미디움",
            "size": "M",
            "price": 7500,
            "isSold": false,
            "menuid": 1
        },
        {
            "id": 3,
            "name": "라지",
            "size": "L",
            "price": 8000,
            "isSold": false,
            "menuid": 1
        }
    ],
    "tags": [
        {
            "id": 1,
            "name": "샐러드",
            "type": "샐러드",
            "menuid": 1
        }
    ]
}
```

### 3. 개별 상품 수정
- Method : PATCH
- EndpointURL : /product / product_id
- Remark : product_id로 개별 상품 선택
- Request
```
PATCH "http://127.0.0.1:8000/product/1 HTTP/1.1"
{
    "name" : "깔깔마리 달래 샐러드(수정)"
}

```
- Response
```
{
    "id": 1,
    "category": "salad",
    "name": "깔깔마리 달래 샐러드(수정)",
    "description": "해산물 샐러드",
    "isSold": false,
    "badge": "new",
    "items": [
        {
            "id": 1,
            "name": "스몰",
            "size": "S",
            "price": 7000,
            "isSold": false,
            "menuid": 1
        },
        {
            "id": 2,
            "name": "미디움",
            "size": "M",
            "price": 7500,
            "isSold": false,
            "menuid": 1
        },
        {
            "id": 3,
            "name": "라지",
            "size": "L",
            "price": 8000,
            "isSold": false,
            "menuid": 1
        }
    ],
    "tags": [
        {
            "id": 1,
            "name": "샐러드",
            "type": "샐러드",
            "menuid": 1
        }
    ]
}
```



## 폴더 구조
```
.
├── README.md
├── requirements.txt
├── manage.py
├── freshcode
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   ├── urls.py
│   └── wsgi.py
├── products
│   ├── migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── pagination.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
└── users
    ├── migrations
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── permissions.py
    ├── serializers.py
    ├── tests.py
    └── views.py

```

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 프레시코드에서 출제한 과제를 기반으로 만들었습니다.
