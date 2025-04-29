n = 4  # iş sayısı
m = 3  # makine sayısı

# Her işin her makinedeki işlenme süresi
processing_time = [
    [4, 6, 8],
    [2, 5, 3],
    [7, 4, 5],
    [6, 3, 4]
]

# Makineden makineye geçiş maliyetleri
transition_cost = [
    [0, 1, 2],
    [1, 0, 1],
    [2, 1, 0]
]

# dp[i][j]: i. işin j. makinada yapılmasının minimum toplam süresi
dp = [[float('inf')] * m for _ in range(n)]

# İlk iş için sadece işlem süreleri yazılır
for j in range(m):
    dp[0][j] = processing_time[0][j]

# Diğer işler için dp hesaplaması
for i in range(1, n):
    for j in range(m):  # şu anki işin yapıldığı makine
        for k in range(m):  # önceki işin yapıldığı makine
            dp[i][j] = min(dp[i][j], dp[i-1][k] + transition_cost[k][j] + processing_time[i][j])

# Sonuç: Son işin herhangi bir makinada bitişiyle elde edilen minimum toplam süre
min_total_time = min(dp[n-1])

print("Minimum toplam süre:", min_total_time)
