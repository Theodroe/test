import streamlit as st
from sqlalchemy import create_engine, text

# DB 연결

# local
# @st.cache_resource
# def get_engine():
#     db = st.secrets["mysql"]
#     url = (
#         f"mysql+pymysql://{db['user']}:{db['password']}"
#         f"@{db['host']}:{db['port']}/{db['database']}"
#         f"?charset={db['charset']}"
#     )
#     engine = create_engine(url, pool_pre_ping=True)
#     return engine


@st.cache_resource
def get_engine():
    url = st.secrets["connections"]["dashboard_db"]["url"]
    
    engine = create_engine(url, pool_pre_ping=True)
    return engine


# DB 연결 테스트

def test_connection():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return result.scalar()