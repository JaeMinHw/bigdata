### bigdata

# project : The relationship between Korea's low birth rate and various factors

- using data
인구수(population) – 
https://jumin.mois.go.kr/ageStatMonth.do

출산율(birth rate)  - 
https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1428#

경제 성장률(economic growth rate) – 
https://www.index.go.kr/unify/idx-info.do?idxCd=4201

혼인율(number of marriages) – 
https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1580#

물가 지수(consumer price) - 
https://kosis.kr/search/search.do?query=%EC%86%8C%EB%B9%84%EC%9E%90%EB%AC%BC%EA%B0%80%EC%A7%80%EC%88%98




- result 
![image](https://github.com/JaeMinHw/bigdata/assets/95284552/38ffa6df-f700-48ff-9a6e-5ce90764b8a1)


그 결과, 출산율(birth rate)와 소비자 물가(consumer price)와는 약 86%의 음의 상관 관계가 있다고 간주할 수 있다. 또한 경제 성장률(economic growth rate)와 혼인율(number of marriages)과는 양의 상관 관계가 49%, 94%로 관계가 있다고 간주할 수 있다. 즉 혼인율이 가장 큰 상관 관계가 있다고 생각할 수 있다. 하지만 상관 계수가 크다고 인과관계가 있다는 뜻은 아니다. 또한 소비자 물가가 오를수록 출산율이 낮아지는 그러한 관계로 볼 수 있다.

As a result, it can be considered that there is a negative correlation of about 86% between birth rate and consumer price. In addition, it can be considered that there is a positive correlation between the economic growth rate and the number of marriages at 49% and 94%. In other words, it can be considered that the marriage rate has the greatest correlation. However, a high correlation coefficient does not mean that there is a causal relationship. It can also be seen as such a relationship in which the fertility rate decreases as consumer prices rise.


- logistic regression
![image](https://github.com/JaeMinHw/bigdata/assets/95284552/45bff4b1-4384-4c69-bfdb-512b8b2ce0bc)

 정확도(Accuracy)는 전체 예측 중 올바르게 예측한 비율을 나타낸다. 주어진 데이터에서 정확도는 약 0.778로 나타난다. 이는 모델이 전체 테스트 데이터에서 약 77.8%의 예측을 정확하게 맞췄음을 의미한다. 
 
 정밀도(Precision)은 예측한 양성 샘플 중 실제로 양성인 비율을 나타낸다. 주어진 데이터에서 정밀도는 1.0으로 나타난다. 이는 모델이 예측한 모든 양성 샘플이 실제로 양성인 경우를 의미한다.
재현율(Recall)은 실제로 양성인 샘플 중에 모델이 정확하게 양성으로 예측한 비율을 나타낸다. 주어진 데이터에서 재현율은 0.5로 나타난다. 이는 모델이 실제 양성 중 절반에 해당하는 샘플을 정확하게 양성으로 예측한 것을 의미한다.

 정확도, 정밀도, 재현율은 모델의 성능을 다양한 측면에서 평가하기 위한 지표이다. 정확도가 높으면 모델이 전체적으로 예측을 정확하게 수행한 것이고, 정밀도가 높으면 양성으로 예측된 샘플 중 실제로 양성인 비율이 높은 것이며, 재현율이 높으면 실제 양성인 샘플 중에서 모델이 양성으로 정확하게 예측한 비율이 높은 것이다. 

 분석한 결과를 보면 정확도는 상대적으로 높은 편이지만, 정밀도와 재현율의 차이가 크다. 이는 모델이 양성 예측을 많이 하지만 실제로 양성인 샘플을 제대로 예측하지 못하는 경향이 있다. 모델의 성능을 평가할 때는 정확도, 정밀도, 재현율을 종합적으로 고려해야 한다.
 
 
 Accuracy represents the proportion of correctly predicted out of total predictions. For the given data, the accuracy appears to be about 0.778. This means that the model got around 77.8% of the predictions correct across the entire test data.

 Precision represents the proportion of predicted positive samples that are actually positive. For the given data, the precision is shown as 1.0. This means that all positive samples predicted by the model are actually positive.
Recall represents the proportion of samples that are actually positive that the model correctly predicts to be positive. For the given data, the recall is 0.5. This means that the model accurately predicted half of the actual positive samples as positive.

 Accuracy, precision, and recall are indicators for evaluating model performance in various aspects. If the accuracy is high, the model performed the predictions correctly as a whole, if the precision is high, the proportion of actually positive samples out of the predicted positive samples is high, and if the recall rate is high, the proportion of the actual positive samples correctly predicted by the model is high.

As a result of the analysis, the accuracy is relatively high, but the difference between precision and recall is large. This means that the model tends to predict a lot of positives, but poorly predicts samples that are actually positive. Accuracy, precision, and recall should be comprehensively considered when evaluating the performance of a model.
