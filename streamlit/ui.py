import streamlit as st
import json
import requests

backend = "http://0.0.0.0:8000/query"
def process(url:str, query:str, doc1:str, doc2:str, doc3:str):
  data = {
    'query': query,
    'doc1' : doc1,
    'doc2': doc2,
    'doc3': doc3
  }
  res = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
  return res
st.set_page_config(page_title="KLUE Semantic Search")
st.title("KLUE Semantic Search")
st.markdown("### 🍓 입력된 문장과 가장 유사한 문장 찾기")
st.write("")
query = st.text_input("가장 유사한 문장을 찾고자 하는 문장을 입력해주세요.")
st.markdown("### 🍓 3개의 문장 후보군")
doc1 = st.text_input("첫 번째 문장 후보군을 입력해주세요.")
doc2 = st.text_input("두 번째 문장 후보군을 입력해주세요.")
doc3 = st.text_input("세 번째 문장 후보군을 입력해주세요.")

if st.button("어떤 문장이 가장 유사할까요?"):
  sts = process(backend, query, doc1, doc2, doc3)
  res = sts.json()
  st.write("")
  st.write(res)
  # idx, score, sentence = res["idx"], res["score"], res["sentence"]
