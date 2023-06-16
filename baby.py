import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.ticker as ticker
import seaborn as sns

rc('font', family='AppleGothic')

marry_data_df = pd.read_csv('./data/혼인.csv',header=0,engine = 'python')
baby_data_df = pd.read_csv('./data/출산.csv',header=0,engine = 'python')
market_data_df = pd.read_csv('./data/소비자물가.csv',header=0,engine = 'python')
social_data_df = pd.read_csv('./data/경제성장.csv',header=0,engine = 'python')
peo_data_df = pd.read_csv('./data/peo.csv',header=0,engine='python')
age_data_df = pd.read_csv('./data/08_22_total.csv',header=0,engine='python')
dead_data_df = pd.read_csv('./data/사망자.csv',header = 0,engine='python')

year = market_data_df.iloc[:,0]
marke = market_data_df.iloc[:,1]
marry_year = marry_data_df.iloc[:,0]
marry_total= marry_data_df.iloc[:,1]
baby_year = baby_data_df.iloc[:,0]
baby_count = baby_data_df.iloc[:,1]
baby_ratio = baby_data_df.iloc[:,2]
social_year = social_data_df.iloc[:,0]
social_ratio = social_data_df.iloc[:,1]
peo_year = peo_data_df.iloc[:,0]
peo_count = peo_data_df.iloc[:,1]
age_year = age_data_df.iloc[:,0]
age_total = age_data_df.iloc[:,1]
age_20 = age_data_df.iloc[:,2]
age_30 = age_data_df.iloc[:,3]

# result = pd.merge(marry_data_df,baby_data_df,on="년도",how = "right")
# result = pd.merge(result,market_data_df,on="년도",how = "right")
# result = pd.merge(result,social_data_df,on="년도",how = "right")
# result = pd.merge(result,peo_data_df,on="년도",how = "right")
# result.to_csv("total.csv")



# result = pd.merge(result,age_data_df,on="년도",how = "right")
# result = pd.merge(result,dead_data_df,on="년도",how = "right")


def market_size() :
    plt.figure(num = 1, dpi = 100,facecolor='white')
    plt.plot(year, marke,color = "blue",linewidth = 0.5)

    plt.title("소비자 물가")
    plt.xlabel('년도')
    plt.ylabel('소비자 물가 (기준 2020년도)')
    plt.xlim(1994,2022)
    plt.ylim(30,120)
    plt.rcParams['axes.unicode_minus'] = False

    plt.show()
    
    
    
def marry_size() :
    plt.figure(num=1,dpi = 100,facecolor='white')
    
    plt.plot(marry_year, marry_total,color = "blue",linewidth = 0.5)

    plt.title("혼인 건수")
    plt.xlabel('년도')
    plt.ylabel('혼인 건수')
    plt.xlim(1994,2022)
    plt.ylim(150,450)
    plt.rcParams['axes.unicode_minus'] = False

    plt.show()
    
    


def baby_size() :
    fig,ax1 = plt.subplots()
    ax1.plot(baby_year,baby_count,color= "blue",linewidth = 0.5,marker='o',label='신생아수(천명)')
    ax1.tick_params(axis = 'y',labelcolor = "blue")
    
    ax2 = ax1.twinx()
    ax2.plot(baby_year,baby_ratio,color = "red",marker='o',label='출생율')
    ax2.tick_params(axis = 'y',labelcolor = "red")
    plt.title("출생율 및 신생아 수",fontsize = 20)
    ax1.legend(loc = 'upper center')
    ax2.legend(loc = 'upper right')
    plt.show()
    
    
    
def social_size() :
    plt.figure(num=1,dpi = 100,facecolor='white')
    
    plt.plot(social_year, social_ratio,color = "blue",linewidth = 0.5)

    plt.title("경제 성장")
    plt.xlabel('년도')
    plt.ylabel('경제 성장룰')
    plt.xlim(1994,2022)
    plt.ylim(-10,15)
    plt.rcParams['axes.unicode_minus'] = False

    plt.show()
    
    


def peo_size() :
    plt.figure(num=1,dpi = 100,facecolor='white')
    
    plt.plot(peo_year, peo_count,color = "blue",linewidth = 0.5,marker='o',label='인구수')

    plt.title("인구수")
    plt.xlabel('년도')
    plt.ylabel('인구수(천명))')
    plt.xlim(1994,2022)
    plt.ylim(43000,52000)
    plt.rcParams['axes.unicode_minus'] = False
    plt.legend()
    plt.show()
    


    
def age_size() :
    fig,ax1 = plt.subplots()
    ax1.plot(age_year,age_total,color= "blue",linewidth = 0.5,marker='o',label='총 인구')
    ax1.tick_params(axis = 'y',labelcolor = "blue")
    
    ax2 = ax1.twinx()
    ax2.plot(age_year,age_20,color = "red",marker='o',label='20대')
    ax2.tick_params(axis = 'y',labelcolor = "red")
    
    ax3 = ax1.twinx()
    ax3.plot(age_year,age_30,color = "green",marker='o',label='30대')
    ax3.tick_params(axis = 'y',labelcolor = "green")
    
    ax1.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax2.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax3.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.title("20대 30대 인구수",fontsize = 20)
    ax1.legend(loc = 'lower left')
    ax2.legend(loc = 'upper right')
    ax3.legend(loc = 'upper left')
    plt.show()



# fig, axes = plt.subplots(3,3)

# axes[0][0].plot(year,marke)
# axes[0][1].plot(marry_year,marry_total)
# axes[0][2].plot(social_year,social_ratio)
# axes[1][0].plot(baby_year,baby_count)
# axes[1][1].plot(baby_year,baby_ratio)
# axes[1][2].plot(peo_year,peo_count)
# axes[2][0].plot(age_year,age_total)
# axes[2][1].plot(age_year,age_20)
# axes[2][2].plot(age_year,age_30)

# plt.rcParams['axes.unicode_minus'] = False
# plt.tight_layout()
# plt.show()



