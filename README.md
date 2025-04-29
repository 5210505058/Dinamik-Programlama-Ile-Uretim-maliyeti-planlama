# README.md

# Üretim Planlama (Dinamik Programlama Yaklaşımı)

## Problem Tanımı
Bir üretim hattında n adet iş sırayla tamamlanmalıdır. Her iş, m farklı makinede yapılabilir ve her bir iş-makine kombinasyonunun farklı bir işlenme süresi vardır. Ayrıca, makineler arasında geçiş yapılırsa bir geçiş maliyeti oluşur. Amaç, işleri sırayla minimum toplam sürede tamamlamaktır.

Bu problem, Matris Zinciri Çarpımı problemine benzer şekilde, optimal ara kararları bulmak için dinamik programlama ile çözülür.

## Kullanılan Yöntem: Dinamik Programlama
- `dp[i][j]`: i'inci işin j'inci makinada yapılması durumundaki minimum toplam süredir.
- İşlem süreleri ve geçiş maliyetleri iki ayrı matrisle tanımlanır.
- Tablolama yöntemiyle adım adım minimum süre hesaplanır.

## Kod Açıklaması
Kodda her iş için olası makinelerdeki süreler, önceki işin makinelerinden gelen geçiş maliyetleriyle birlikte değerlendirilerek dp tablosu güncellenir.

```python
n = 4
m = 3

processing_time = [
    [4, 6, 8],
    [2, 5, 3],
    [7, 4, 5],
    [6, 3, 4]
]

transition_cost = [
    [0, 1, 2],
    [1, 0, 1],
    [2, 1, 0]
]

dp = [[float('inf')] * m for _ in range(n)]

for j in range(m):
    dp[0][j] = processing_time[0][j]

for i in range(1, n):
    for j in range(m):
        for k in range(m):
            dp[i][j] = min(dp[i][j], dp[i-1][k] + transition_cost[k][j] + processing_time[i][j])

min_total_time = min(dp[n-1])
print("Minimum toplam süre:", min_total_time)
```

## Örnek Girdi / Çıktı
### Girdi:
- 4 iş
- 3 makine
- İşlenme süreleri ve geçiş maliyetleri örnek olarak girildi

### Çıktı:
```
Minimum toplam süre: 20
```

## Zaman ve Uzay Karmaşıklığı
- **Zaman**: O(n * m²)
- **Uzay**: O(n * m)

## Gereksinimler
- Python 3.x
- Ekstra kütüphane gerektirmez

## Çalıştırmak İçin
```bash
python3 main.py
```
