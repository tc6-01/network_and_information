import networkx as nx
import pandas as pd
import re
# 读取爬取数据中的作者，以及一篇文章中的作者信息

data = pd.read_csv(r'../vldb/VLDB2020.csv')
author = data['author']
papers = []
authors = []
for i in range(len(author)):
    tmp = author[i].replace('*', '').replace('; ', ',').replace(', ', ',')
    tmp = re.sub(r'( )?[(](.*?)[)]( )?', '', tmp)
    tmp = tmp.split(',')
    # 将每个作者存放入作者节点中，确保不重复
    authors.extend(tmp)
    # 将每篇文章的作者放入一个列表，实现边的添加
    papers.append(tmp)

# 构建作者合作网络
G = nx.Graph()
# 添加节点
for author in authors:
    G.add_node(author)

# 添加边
for paper in papers:
    for i in range(len(paper)):
        for j in range(i+1, len(paper)):
            G.add_edge(paper[i], paper[j])

# 计算PageRank值
pr = nx.pagerank(G)

# 输出PageRank值排名前10的作者
top10 = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:10]
for author, score in top10:
    print(author, score)
