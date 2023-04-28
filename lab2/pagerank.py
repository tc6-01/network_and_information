# 定义一个表示网页的图形，每个节点表示一个网页，每个边表示一个链接。
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A']
}
# 初始化每个节点的PageRank值
pagerank = {
    'A': 1,
    'B': 1,
    'C': 1
}
# 定义迭代次数和阻尼因子
iterations = 10
damping_factor = 0.85
# 每次迭代中，根据网页之间的链接关系更新每个节点的PageRank值
for i in range(iterations):
    for node in graph:
        # 将其PageRank值初始化为阻尼因子，然后将其所有入边的贡献值相加
        rank = (1 - damping_factor)/3 + damping_factor * sum(pagerank[link] / len(graph[link]) for link in graph if node in graph[link])
        pagerank[node] = rank

sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
for page, rank in sorted_pagerank:
    print(f"{page}: {rank}")
