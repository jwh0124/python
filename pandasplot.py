import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

age = [random.randint(20,100) for x in range(0, 50)]

weight = [random.randint(40,150) for i in range(0,50)]

df = pd.DataFrame({
    'age': age,
    'weight': weight
})

df.plot(kind='bar', subplots=True) # pandas 라이브러리 써서 그래프 그림.
plt.title('Bar Chart') # 차트에 제목 붙이기
plt.savefig('bar_chart_random.png') # 차트 이미지로 저장하기
plt.show()