## 필요한 라이브러리 설치
```
pip install streamlit pandas sqlalchemy pymysql plotly
```

## 패키지 기록
```
pip freeze > requirements.txt
```
예시 `requirements.txt`
```
streamlit
pandas
sqlalchemy
pymysql
plotly
```

## MySQL DB 준비
1) DB 생성
```
# SQL

CREATE DATABASE dashboard_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

2) 테이블 생성
```
# SQL

USE dashboard_db;

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    region VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

3) 데이터 삽입
```
# SQL

INSERT INTO sales (order_date, product_name, category, quantity, price, region)
VALUES
('2026-03-01', '노트북', '전자', 3, 1200000, '서울'),
('2026-03-02', '마우스', '전자', 10, 25000, '부산'),
('2026-03-03', '의자', '가구', 5, 80000, '서울'),
('2026-03-04', '책상', '가구', 2, 150000, '대전'),
('2026-03-05', '키보드', '전자', 7, 70000, '인천');

```

## 프로젝트 폴더 구조
```
streamlit_mysql_dashboard/
│
├─ app.py
├─ requirements.txt
├─ README.md
│
├─ db/
│  ├─ connection.py
│  ├─ crud.py
│  └─ init_db.py
│
├─ utils/
│  ├─ charts.py
│  ├─ pagination.py
│  └─ state.py
│
├─ pages/
│  ├─ 1_데이터조회.py
│  ├─ 2_판매관리.py
│  ├─ 3_고객관리.py
│  ├─ 4_시각화.py
│  └─ 5_대시보드.py
│
└─ .streamlit/
   └─ secrets.toml

```

## 환경설정
```
conda create -n streamlit_dashdb python=3.13 -y
conda activate streamlit_dashdb
pip install -r requirements.txt
```