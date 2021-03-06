
import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['sample_data.csv'].decode('utf-8')))
print(df)

import matplotlib.pyplot as plt
plt.plot(df['column_a'],df['column_b'],'o',label = 'column a vs b',linestyle = '--',linewidth = 3,markersize = 5)
plt.legend()
plt.show()

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['countries.csv'].decode('utf-8')))
print(df)

pd.set_option('display.max_rows',None)
df.h

new_df1 = df[df['country']=='United States']
print(new_df1)

new_df2 = df[df['country']=='China']
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10),dpi = 50)
plt.plot(new_df2['year'],new_df2['population'],'bo-',linewidth = 2,markersize=10,label='chine poplulation')
plt.plot(new_df1['year'],new_df1['population'],'g^-',linewidth = 2,markersize = 10,label = 'US population')
plt.xticks(new_df1['year'],color='white',fontsize=12)
#fig = plt.gcf()
plt.yscale('log')
plt.savefig('test2.png')
plt.legend(loc='upper left')
plt.show



"""import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['countries.csv'].decode('utf-8')))
print(df)
"""

import matplotlib.pyplot as plt
df.hist()

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-np.pi,np.pi,0.1)
plt.plot(x,np.sin(x),'g*',label='Curve of sine')
plt.xlabel('angles',fontsize=20,color='white')
plt.legend(loc='upper left')
plt.show()

import pandas as pd
import matplolib.pyplot as plt
import numpy as np
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
plt.bar(bars,height)
plt.show()

import pandas as pd
import matplolib.pyplot as plt
import numpy as np
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
plt.bar(bars,height)
plt.show()

d = np.ones(10,dtype = float) - 1
print(d)

import numpy as np
np.random.seed(4)
a = np.random.rand(5,1,2)
b = np.transpose(a,(2,0,1))
print(b.shape)

print(np.full((3,3),0.0))

import pandas as pd
df = pd.read_csv('tita')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

height = (3, 12, 5, 18, 45)
bars = ['A', 'B', 'C', 'D', 'E']

plt.bar(bars,height,edgecolor='black',alpha =0.5)
plt.xticks(bars)
plt.title('$Height_{bars}$', fontsize=24,color='white')
plt.xlabel('categories are',fontsize=20,color='white')
plt.show()



plt.bar(bars,height)
plt.show()

import pandas as pd
df = pd.DataFrame({'year': [2015, 2016, 2017, 2018, 2019], 'T20': [24, 36, 12, 18, 25], 'ODI': [89, 24, 37, 63, 98]})
df.hist()
plt.show()

from google.colab import drive
drive.mount('/content/drive')



import pandas as pd
import matplotlib.pyplot as plt
plt.scatterplot(kind='bar')

import pandas as pd
url = "https://raw.githubusercontent.com/shala2020/shala2020.github.io/master/Lecture_Materials/Google_Colab_Notebooks/DataScience/L2/moviesData.csv"
movies = pd.read_csv(url)
movies.head()

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['moviesData.csv']))
#pd.set_option('display.max_rows',None)
print(df)

import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show

"""from google.colab import files

> Indented block


uploaded = files.upload()
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['moviesData.csv']))
print(df.columns)

import matplotlib.pyplot as plt

print(plt.pie(df['genre'].value_counts(),labels=df['genre'].value_counts().index.tolist()))

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',pctdistance=2.5,rotatelabels=True,wedgeprops={'linewidth':6},textprops={'color':'white'},
        shadow=True, startangle=90)
ax1.axis('equal')  
# Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts,size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.show()

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['moviesData.csv'].decode('utf-8')))
print(df.head())

moviesub = df[0:10]
moviesub.shape

plt.bar(moviesub.title, moviesub.imdb_rating)
plt.xlabel('Movies title')
plt.title('imdb_rating')
plt.xticks(rotation='vertical')
plt.ylim(0,10)
plt.show()

import seaborn as sns
import numpy as np

plt.figure(figsize=(10,10))
matrix = np.triu(df.corr())
sns.heatmap(df.corr(),mask = matrix)

plt.figure(figsize=(10,10))
mask = np.zeros_like(df.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(df.corr(),mask = mask)
# vmin = -1, cmap='coolwarm', annot=True, mask = mask

plt.scatter(df['imdb_rating'],df['audience_score'],marker='^')
plt.show()

plt.figure(figsize=(10,10))
df['diff']=df['audience_score']-df['critics_score']
sns.boxplot(df['genre'],df['diff'])
plt.xticks(rotation=90,fontsize='x-large')
plt.yticks(fontsize='x-large')
plt.show()

probs = np.array([0.70, 0.3,0.5])
side = [0, 1,2]
plt.bar(side, probs)
plt.title('Bernoulli Distribution of a Biased Coin', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.xlabel('Outcome', fontsize=12)
#axes = plt.gca()
#axes.set_ylim([0,1])
plt.xlim(0,2)
plt.ylim(0,0.5)

import numpy as np
import matplotlib.pyplot as plt
lambda1 = 0.5
x = np.arange(0,15,0.1)
y = lambda1*np.exp(-lambda1*x)
plt.plot(x,y,label='')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

probs = [1/6]*6
side = [1,2,3,4,5,6]
s = pd.Series(probs,side)

#Set descriptions:
plt.title("Uniform Distribution",fontsize=16)
plt.ylabel('side', fontsize=16)
plt.xlabel('probability',fontsize=16)

#Set tick colors:
#ax = plt.gca()
plt.tick_params(axis='x', colors='blue',length=5,labelbottom = False,labelleft=False,)
plt.tick_params(axis='y', colors='red')
plt.ylim([0,1])

#Plot the data:


s.plot(kind = 'bar')

plt.show()

import scipy.stats as  stats
x = np.arange(0, 25)
prob = 0.2
p = 100   
binom = stats.binom.pmf(x,p, prob)
mark1 = [15,17]
plt.plot(x, binom, '-o',markevery=mark1)
plt.xlabel('Random Variable', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title("Binomial Distribution")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
n = np.arange(-100, 100)
mean = 0
normal = stats.norm.pdf(n, mean, 20)
mark1=[-20,20]
plt.plot(n, normal,markevery=mark1,marker='o')
plt.xlabel('Random Variable', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title("Normal Distribution")

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

bars=[10,20,30,40,50,60,70]
height=[2,5,3,4,6,3,7]
plt.bar(bars,height)
plt.tick_params(axis='x',length = 15,width = 5, color='white',labelcolor='white')
plt.show()

plt.barh(bars,height)
plt.tick_params(axis='y',colors='white',length=15,width=4,labelleft=False,left=False)
plt.show()

df = pd.DataFrame({'year': [2015, 2016, 2017, 2018, 2019], 'T20': [24, 36, 12, 18, 25], 'ODI': [89, 24, 37, 63, 98]})
mark1=[2016.0]
plt.plot(df['year'],df['ODI'],marker='o')
plt.tight_layout()
plt.show()

plt.plot( 'year', 'T20', data = df,linewidth = 1,marker='o',markersize=15)
plt.plot('year', 'ODI', data = df, c='red', linewidth = 1,marker='^',markersize=15)
plt.xticks(np.arange(min(df.year), max(df.year)+1, 1.0), fontsize = 15)
plt.yticks(np.arange(0,125,25), fontsize = 15)
plt.title('Points scored by India', fontsize = 15)
plt.xlabel('Year', fontsize = 15)
plt.ylabel('Points', fontsize = 15)
plt.legend(loc='upper center')
plt.grid(b=True,color='green',axis='y',linewidth=2,linestyle='-.',markeredgecolor='black')
plt.tick_params(axis='x',length=15,width=2,colors='white') #which argument to choose the axis 
plt.show()

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['moviesData.csv'].decode('utf-8')))
df.columns

import seaborn as sns
sns.regplot(x=df['critics_score'],y=df['audience_score'],ci=95,marker='^',scatter_kws={'color':'black'},line_kws={'color':"green",'linestyle':"-.",'linewidth':4})
plt.grid(b=True,color='red',lw=4,alpha=0.5)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,VotingClassifier,VotingRegressor
from sklearn.model_selection import StratifiedKFold,train_test_split,GridSearchCV,StratifiedKFold
from sklearn.metrics import accuracy_score,mean_squared_error,mean_absolute_error,f1_score
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn import svm

from sklearn.datasets import california_housing
df = california_housing.fetch_california_housing()
df

df1 = pd.DataFrame(df.data,columns=df.feature_names)
target = pd.DataFrame(df.target,columns=['Target'])
final_df = df1.join(target)
final_df.head()

final_df.isnull().sum()

final_df.info()
plt.figure(figsize=(10,10))
sns.heatmap(final_df.corr(),annot=True,cmap='coolwarm')

#plt.boxplot(x=final_df['MedInc'])
q1 = final_df.quantile(0.25)
q3 = final_df.quantile(0.75)
IQR = q3-q1
print(IQR)

final_df = final_df[~((final_df<(q1-1.5*IQR))|(final_df>(q3+1.5*IQR))).any(axis=1)]

sns.boxplot(x=final_df['MedInc'])

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier,RandomForestClassifier,VotingClassifier,VotingRegressor
from sklearn.metrics import accuracy_score,mean_squared_error,mean_absolute_error,classification_report,confusion_matrix
from sklearn.model_selection import train_test_split,StratifiedKFold,cross_val_score
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor

from sklearn.datasets import california_housing

house = california_housing.fetch_california_housing()

features = pd.DataFrame(house.data,columns=house.feature_names)
target = pd.DataFrame(house.target,columns=['Target'])
df = features.join(target)
df.head()

df.isnull().sum()

df.describe()

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),annot=True)

df[['MedInc','Target']].describe()

from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.impute import SimpleImputer

ss = StandardScaler()
df1 = ss.fit_transform(df)

df

df.isnull().sum()
.intercept_
.coef_
.coeffs)
plt.legend(frameon=True,borderpad=)

df

from google.colab import files
uploaded = files.upload()

import io
new = pd.read_csv(io.StringIO(uploaded['diabetes.csv'].decode('utf-8')))
new.head()

plt.figure(figsize=(10,10))
sns.heatmap(new.corr(),annot=True)

new.info()

import tensorflow as tf
from tensorflow import keras

multidimensional array called as tensor

google i/o

import tensorflow as tf
from tensorflow import keras
tf._version_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mnist = keras.datasets.fashion_mnist

(X_train,y_train),(x_test,y_test) = mnist.load_data()

np.max(x_train)

x_train = x_train/255

class_names = ['top','trouser','dress','bed','ankleboat']

plt.figure()
plt.imshow(x_train[1])
plt.colorbar()

x_test = x_test/255.0

plt.figure()
plt.imshow(x_train[0])
plt.colorbar()

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense

model = Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()

model.compile(optimizers='adam',loss='sparse_categorial_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10)

test_loss,test_acc = model.evaluate(x_test,y_test)

from sklearn.metric import accuracy_score

y_pred = model.predict_classes(x_test)

accuracy_score(y_pred,y_test)

pred = model.predict(x_test)

np.argmax(pred[0])

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras import Sequential

model = Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))

model.compile(optimisers='adam',loss = 'sparse_categorical_crossentropy')

# Importing some packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing some packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm



























