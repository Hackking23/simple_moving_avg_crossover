import pandas as pd 
from sqlalchemy import create_engine
import pymysql
import numpy as np
import matplotlib.pyplot as plt

# Stores given data into sql
def cnvt_to_sql(data,t_name):
    engine= create_engine("mysql+mysqldb://user:password@host/database")
    data.to_sql(t_name,engine,if_exists='append')
    return

# Valadate the given data input.
def validate_input(d_frame):
    
    datafraame_schema = pd.Series(data=['datetime64[ns]','float64','float64','float64','float64','int64','object'] , index=['datetime', 'close', 'high', 'low', 'open', 'volume', 'instrument'])
    error_list=[]
    for i in range(0,7):
        if (datafraame_schema[i]!=d_frame.dtypes[i]):
            error_list.append(d_frame.dtypes.index[i])
        pass
    if error_list ==[]:
        return (True) 
    else :
        raise TypeError("following column/columns are not in specified format: %s" %",".join(error_list))
     
    
# Performs Simple moving average startegy on given data and plots graph for it.
def moving_avg_crossover(data,fma_period=5,sma_period=30,column='close'):
    def SMPL_MA(data,period=30, column_ma='close'):
        return data[column_ma].rolling(window=period).mean()
    data['FMA']=SMPL_MA(data,fma_period,column)
    data['SMA']=SMPL_MA(data,sma_period,column)
    data['signal']=np.where(data['FMA']>data['SMA'],1,0)
    data['position']=data['signal'].diff()
    data["buy"]=np.where(data['position']==1,data[column],np.NAN)
    data["sell"]=np.where(data['position']==-1,data[column],np.NAN)

    plt.style.use('fivethirtyeight')
    plt.figure(figsize=(16,8))
    plt.plot(data.datetime,data[column],alpha=0.5,label=column)
    plt.plot(data.datetime,data['FMA'],alpha=0.5,label='fast moving average')
    plt.plot(data.datetime,data['SMA'],alpha=0.5,label='Slow moving average')
    plt.scatter(data.datetime,data['buy'],alpha=1,label='BUY_SIGNAL',marker='|',color='green',s=500)
    plt.scatter(data.datetime,data['sell'],alpha=1,label='SELL_SIGNAL',marker='|',color='red',s=500)
    plt.title("Moving Average Crossover")
    plt.xlabel('Year')
    y_name = column + " price"
    plt.ylabel (y_name) 
    plt.show()

def process_file(file_path):
    try:
        df = pd.read_excel(file_path)
        cnvt_to_sql(df, 'invst')
        validate_input(df)
        moving_avg_crossover(df,column='high')
    except TypeError as e:
        raise TypeError(e.message)
    except Exception as E:
        print('ERROR OCCURED')
        print(E)

if __name__ == "__main__" :
    process_file(file_path="HINDALCO_1D.xlsx")



