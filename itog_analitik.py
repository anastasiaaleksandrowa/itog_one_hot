# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# получаем one-hot encoding
one_hot = pd.get_dummies(data['whoAmI'])
# объеденяем исходный dataFrame с  one-hot
data = pd.concat([data, one_hot], axis=1)
data.head()

