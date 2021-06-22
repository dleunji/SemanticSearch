from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from starlette.responses import JSONResponse
from sentence_transformers import SentenceTransformer, util
import torch
model = SentenceTransformer("model")
class Input(BaseModel):
  query: str
  doc1: str
  doc2: str
  doc3: str
  doc4: str
  doc5: str

app = FastAPI(
  title = "KLUE STS",
  description = "입력된 문장과 가장 유사한 문장 찾기",
  version = "1.0.0"
)

@app.post("/query")
def query(input: Input):
  query = input.query
  docs = []
  docs.append(input.doc1)
  docs.append(input.doc2)
  docs.append(input.doc3)
  docs.append(input.doc4)
  docs.append(input.doc5)
  query_embeddings = model.encode(query)
  document_embeddings = model.encode(docs)
  cos_scores = util.pytorch_cos_sim(query_embeddings, document_embeddings)
  top_results = torch.topk(cos_scores, 1)
  print({'idx': top_results[1].item() + 1, 'score': top_results[0].item(), 'sentence': docs[top_results[1]]})
  return JSONResponse({'idx': top_results[1].item() + 1, 'score': top_results[0].item(), 'sentence': docs[top_results[1]]})


