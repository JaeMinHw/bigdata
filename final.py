# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sb


# train_df = pd.read_csv('./data/total.csv',header=0,engine = 'python')

# print(train_df.head())
# print(train_df.corr(method='pearson'))

# plt.rcParams["figure.figsize"] = (5,5)
# sb.heatmap(train_df.corr(),
#            annot= True,
#            cmap = 'Greys',
#            vmin = -1, vmax=1
#            )

# plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# 데이터 불러오기
df = pd.read_csv('./data/total.csv', header=0, engine='python')


# 독립 변수와 종속 변수 선택
X = df.iloc[:, 1:-1]  # 첫 번째 열(num)과 마지막 열(result) 제외
y = df[' result']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 로지스틱 회귀 모델 구축 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 테스트 데이터로 예측
y_pred = model.predict(X_test)

# 성능 평가
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
