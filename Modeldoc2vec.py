from androguard.misc import AnalyzeAPK
import os
from pathlib import Path
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

# Đường dẫn đến file APK
apk_path = os.path.join(os.getcwd(), 'apk_test.apk')
# phân tích APK
a, d, dx = AnalyzeAPK(apk_path)

# tạo đồ thị FCG
cg = dx.get_call_graph()

# tạo data để train model doc2vec
class_method_strings = []

# lấy ra tên lớp và các phương thức có trong đỉnh
for node in cg.nodes():
    class_name = node.class_name
    method_name = node.name
    class_method_string = f"{class_name} {method_name}"
    class_method_strings.append(class_method_string)

# tạo data frame từ danh sách chuỗi
df = pd.DataFrame(class_method_strings, columns=["class_and_methods"])
    
 # Tạo danh sách các văn bản từ DataFrame
documents = [TaggedDocument(words=(doc.lower()).split(), tags=[str(i)]) for i, doc in enumerate(df['class_and_methods'])]

# Huấn luyện mô hình Doc2Vec
model = Doc2Vec(vector_size=20, window=2, min_count=1, workers=4, epochs=20)
model.build_vocab(documents)
model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)

# Chuyển đổi dữ liệu thành vector
vectors_of_node = [model.infer_vector(word_tokenize(doc.lower())) for doc in df['class_and_methods']]

# In ra vector của một số văn bản
for i, vec in enumerate(vectors_of_node):
    print(f"Vector của văn bản {i+1}: {vec}")
   