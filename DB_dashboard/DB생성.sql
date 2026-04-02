CREATE DATABASE dashboard_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

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

INSERT INTO sales (order_date, product_name, category, quantity, price, region)
VALUES
('2026-03-01', '노트북', '전자', 3, 1200000, '서울'),
('game_tags2026-03-02', '마우스', '전자', 10, 25000, '부산'),
('2026-03-03', '의자', '가구', 5, 80000, '서울'),
('2026-03-04', '책상', '가구', 2, 150000, '대전'),
('2026-03-05', '키보드', '전자', 7, 70000, '인천');