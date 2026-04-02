import streamlit as st
import pandas as pd
from db.crud import get_all_sales, search_sales

# _____ 함수 정의 _____



# _____ 코드 _____


st.title("🔎 판매데이터 조회")

with st.sidebar:
    st.header("조회 조건")
    category = st.text_input("카테고리")
    region = st.text_input("지역")
    keyword = st.text_input("상품명 키워드")


if st.button("조회"):
    df = search_sales(
        category=category if category else None,
        region=region if region else None,
        keyword=keyword if keyword else None
    )
else:
    df = get_all_sales()

st.dataframe(df, use_container_width= True)

csv = df.to_csv(index=False).encode("utf-8-sig") # 한글 깨짐 방지 위해 utf-8-sig로 인코딩
st.download_button(
    label="CSV 다운로드",
    data=csv,
    file_name="data/sales_data.csv",
    mime="text/csv"
)

# 드롭다운으로 선택하게