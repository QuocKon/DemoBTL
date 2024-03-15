from androguard.misc import AnalyzeAPK
import os
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt

# Đường dẫn đến file APK
apk_path = os.path.join(os.getcwd(), 'apk_test.apk')
# phân tích APK
a, d, dx = AnalyzeAPK(apk_path)

# tạo đồ thị FCG
cg = dx.get_call_graph()

# in ra các đỉnh và các cạnh ra một file out_put.txt
with open("out_put.txt", "w") as f:
    for node in cg.nodes:
        f.write(node+"\n")
    for edge in cg.edges:
        f.write(edge[0]+" "+edge[1]+"\n")

# vẽ đồ thị
nx.draw_networkx(cg, with_labels=False, node_size=10)
plt.show()