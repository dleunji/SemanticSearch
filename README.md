## Semantic Search
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://master-semantic-search-dleunji.endpoint.ainize.ai/)<br>

<img width="709" alt="스크린샷 2021-06-26 오후 11 31 34" src="https://user-images.githubusercontent.com/46207836/123516363-aa185980-d6d6-11eb-8200-ddc2069f26d9.png">

`klue/roberta-base` 모델을 **Sentence Transformers**를 활용해 **KLUE** 내 **STS** 데이터셋을 활용하여 모델을 훈련하고, 모델을 활용하여 세 가지 문장 중에서 가장 유사한 문장을 찾는 서비스입니다.

모델은 **Ainize Workspace**에서 학습하였습니다.<br>
학습된 모델은 [도커 허브](https://hub.docker.com/repository/docker/dleunji/klue-sts-model)에 업로드해두었습니다.

API에 대한 안내는 [ainize](https://ainize.ai/dleunji/SemanticSearch?branch=master)에 자세히 안내되어있습니다.


## Reference
Huffon님의 [github](https://github.com/Huffon/klue-transformers-tutorial)과 [colab](https://colab.research.google.com/github/Huffon/klue-transformers-tutorial/blob/master/sentence_transformers.ipynb)을 참고하였습니다.