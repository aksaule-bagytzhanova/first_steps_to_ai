from scipy.stats import stats

A = """X Y
4 2
5 1
2 4
3 3
1 5"""

x, y = [], []

[(x.append(int(a[0])), y.append(int(a[2]))) for a in A.split('\n') if a[0].isdigit()]

print(stats.pearsonr(x,y)[0])