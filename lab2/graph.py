import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_longtail_edges(m, n, alpha):
    nodes = range(m)
    edges = []
    for i in range(n):
        source = random.choice(nodes)
        while True:
            target = random.choice(nodes)
            if target != source and random.random() < alpha * (m-1) / (m**(1-alpha)):
                break
        edges.append((source, target))
    return edges

m_values = [10, 10, 20, 20] # 节点数
n_values = [20, 10, 40, 20] # 边数
alpha = 0.8 # 长尾分布参数
m = 20 # 节点数
n = 40 # 边数
alpha = 0.8 # 长尾分布参数

def darw_Garph(m, n, alpha):
    G = nx.DiGraph()
    G.add_nodes_from(range(m))
    edges = generate_longtail_edges(m, n, alpha)
    G.add_edges_from(edges)
    pr = nx.pagerank(G)
    nx.draw(G)
    plt.show()
    pr = dict(sorted(pr.items(), key=lambda x:x[1]))
    # 打印pagerank值
    for node, score in pr.items():
        print(f'Node {node}: PageRank score {round(score, 3)}')
    # 绘制柱状图
    plt.bar(range(len(pr)), list(pr.values()), align='center')
    plt.xticks(range(len(pr)), list(pr.keys()))
    plt.show()
for i in range(len(m_values)):
    darw_Garph(m_values[i], n_values[i], alpha)
