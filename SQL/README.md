## 프로그래머스 SQL 고득점 KIT 풀이

### 1. SELECT

- 평균 일일 대여 요금 구하기
```sql
SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';
```

- 흉부외과 또는 일반의사 외과 목록 출력하기
```sql
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC;
```

- 조건에 맞는 회원 수 구하기
```sql
SELECT COUNT(USER_ID) as USERS FROM USER_INFO
WHERE JOINED LIKE '2021%' AND AGE BETWEEN 20 AND 29;
```

- 상위 n개 레코드
```sql
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
```

- 여러 기준으로 정렬하기
```sql
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```

- 동물의 아이디와 이름
```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

- 어린 동물 찾기
```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;
```

- 아픈 동물 찾기
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID;
```

- 역순 정렬하기
```sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```

- 모든 레코드 조회하기
```sql
SELECT *
FROM ANIMAL_INS
ORDER BY ANIAML_ID;
```

- 오프라인/온라인 데이터 통합하기
```sql
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'

UNION

SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'

ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC;
```

- 재구매가 일어난 상품과 회원 리스트 구하기
```sql
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(ONLINE_SALE_ID) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;
```

- 과일로 만든 아이스크림 고르기
```sql
SELECT f.FLAVOR
FROM FIRST_HALF f, ICECREAM_INFO i
WHERE f.FLAVOR = i.FLAVOR AND 
    f.TOTAL_ORDER > 3000 AND
    i.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;
```

- 3월에 태어난 여성 회원 목록 출력하기
```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_FORMAT
FROM MEMBER_PROFILE
WHERE TLNO IS NOT NULL AND GENDER = 'W' AND DATE_OF_BIRTH LIKE '%03%'
ORDER BY MEMBER_ID ASC;
```

- 12세 이하인 여자 환자 목록 출력하기
```sql
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME ASC;
```

- 강원도에 위치한 생산공장 목록 출력하기
```sql
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID ASC;
```

- 서울에 위치한 식당 목록 출력하기
```sql
SELECT i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, ROUND(AVG(r.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS i, REST_REVIEW AS r
WHERE i.REST_ID = r.REST_ID AND i.ADDRESS LIKE '서울%'
GROUP BY i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS
ORDER BY SCORE DESC, FAVORITES DESC;
```

- 조건에 맞는 도서 리스트 출력하기
```sql
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND PUBLISHED_DATE LIKE '2021%'
ORDER BY PUBLISHED_DATE ASC;
```

- 인기있는 아이스크림
```sql
SELECT FLAVOR FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;
```

### 2. SUM, MAX, MIN

- 가장 비싼 상품 구하기
```sql
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT;
```

- 가격이 제일 비싼 식품의 정보 출력하기
```sql
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) AS PRICE FROM FOOD_PRODUCT); /* 서브 쿼리 */
```

- 최댓값 구하기
```sql
SELECT MAX(DATETIME)
FROM ANIMAL_INS;
```

- 최솟값 구하기
```sql
SELECT MIN(DATETIME)
FROM ANIMAL_INS;
```

- 동물 수 구하기
```sql
SELECT COUNT(*)
FROM ANIMAL_INS;
```

- 중복 제거하기
```sql
SELECT COUNT(DISTINCT NAME) /* NULL 제외, 중복 고려 */
FROM ANIMAL_INS;
```

### 3. GROUP BY

- 카테고리 별 도서 판매량 집계하기
```sql
SELECT b.CATEGORY AS CATEGORY, SUM(s.SALES) AS TOTAL_SALES
FROM BOOK_SALES AS s, BOOK as b
WHERE b.BOOK_ID = s.BOOK_ID AND s.SALES_DATE LIKE '2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;
```

- 진료과별 총 예약 횟수 출력하기
```sql
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05-%' /* 2022년 5월 건만 조회 조건*/
GROUP BY MCDP_CD
ORDER BY 5월예약건수 ASC, 진료과코드 ASC;
```

- 성분으로 구분한 아이스크림 총 주문량
```sql
SELECT i.INGREDIENT_TYPE, SUM(f.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF AS f, ICECREAM_INFO AS i
WHERE f.FLAVOR = i.FLAVOR
GROUP BY i.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC;
```

- 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
```sql
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS REGEXP '통풍시트|열선시트|가죽시트' /* 정규표현식 */
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC;
```

- 고양이와 개는 몇 마리 있을까
```sql
SELECT ANIMAL_TYPE, COUNT(*)
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN('Cat', 'Dog')
GROUP BY ANIMAL_TYPE
ORDER BY FIELD (ANIMAL_TYPE, 'Cat', 'Dog'); /* 고양이, 개 순 조회 */
```

- 동명 동물 수 찾기
```sql
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
GROUP BY NAME HAVING COUNT(NAME) >= 2
ORDER BY NAME;
```

- 입양 시각 구하기(1)
```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19 /* 조건이 9시부터 19:59까지 출력하라고 되어있음 */
GROUP BY HOUR
ORDER BY HOUR ASC;
```

- 가격대 별 상품 개수 구하기
```sql
SELECT PRICE - PRICE % 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE ASC;
```

### 4. IS NULL

- 경기도에 위치한 식품창고 목록 출력하기
```sql
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기%'
ORDER BY WAREHOUSE_ID ASC;
```

- 이름이 없는 동물의 아이디
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL;
```

- 이름이 있는 동물의 아이디
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;
```

- NULL 처리하기
```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS;
```

- 나이 정보가 없는 회원 수 구하기
```sql
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;
```

### 5. JOIN

- 오랜 기간 보호한 동물(1)
```sql
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I
LEFT JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NOT NULL AND O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3;
```

- 조건에 맞는 도서와 저자 리스트 출력하기
```sql
SELECT b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d')
FROM BOOK AS b
LEFT JOIN AUTHOR AS a ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE b.CATEGORY = '경제'
ORDER BY b.PUBLISHED_DATE ASC;
```

- 없어진 기록 찾기
```sql
SELECT o.ANIMAL_ID, o.NAME
FROM ANIMAL_OUTS AS o
LEFT JOIN ANIMAL_INS AS i ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE o.ANIMAL_ID IS NOT NULL AND i.ANIMAL_ID IS NULL;
```

- 있었는데요 없었습니다
```sql
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS AS O 
JOIN ANIMAL_INS AS I 
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE O.DATETIME < I.DATETIME
ORDER BY I.DATETIME ASC; /* 보호 시작일 : I.DATETIME */
```

- 보호소에서 중성화한 동물
```sql
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS AS I
JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME
ORDER BY I.ANIMAL_ID;
```

- 상품 별 오프라인 매출 구하기
```sql
SELECT p.PRODUCT_CODE, SUM(p.PRICE * f.SALES_AMOUNT) AS SALES
FROM PRODUCT AS p
LEFT JOIN OFFLINE_SALE AS f ON p.PRODUCT_ID = f.PRODUCT_ID
GROUP BY p.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE ASC;
```

### 6. String, Date

- 자동차 대여 기록에서 장기/단기 대여 구분하기
 
```sql
SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE,'%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE,'%Y-%m-%d') AS END_DATE,
    (
        CASE WHEN DATEDIFF(DD, END_DATE, START_DATE) + 1 >= 30
        THEN '장기 대여'
        ELSE '단기 대여'
        END
    ) AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09-%'
ORDER BY HISTORY_ID DESC;
```

- 조건별로 분류하여 주문상태 출력하기

```sql
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d'), (
    CASE WHEN DATEDIFF('2022-05-01', OUT_DATE) >= 0 THEN '출고완료'
    WHEN DATEDIFF('2022-05-01', OUT_DATE) < 0 THEN '출고대기'
    ELSE '출고미정'
    END
)AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC;
```

- 대여 기록이 존재하는 자동차 리스트 구하기

```sql
SELECT DISTINCT R.CAR_ID /* DISTINCT 사용 */
FROM CAR_RENTAL_COMPANY_CAR AS R
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
ON R.CAR_ID = H.CAR_ID
WHERE R.CAR_TYPE = '세단' AND MONTH(H.START_DATE) = 10
ORDER BY R.CAR_ID DESC;
```

- 자동차 평균 대여 기간 구하기

```sql
SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE)),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;
```

- 특정 옵션이 포함된 자동차 리스트 구하기

```sql
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE('%네비게이션%')
ORDER BY CAR_ID DESC;
```

- 루시와 엘라 찾기

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;
```

- 이름에 el이 들어가는 동물 찾기

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%eL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME;
```

- 중성화 여부 파악하기

```sql
SELECT ANIMAL_ID, NAME, (
    CASE WHEN (SEX_UPON_INTAKE LIKE '%Neutered%') OR (SEX_UPON_INTAKE LIKE '%Spayed%')
    THEN 'O'
    ELSE 'X'
    END
)AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

- 오랜 기간 보호한 동물(2)

```sql
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS AS I
JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2;
```

- 카테고리 별 상품 개수 구하기

```sql
SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY PRODUCT_CODE ASC;
```

- DATETIME에서 DATE로 형 변환

```sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```