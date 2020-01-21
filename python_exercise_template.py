# import pandas, numpy
# Create the required data frames by reading in the files

#df=pd.read_excel("SaleData.xlsx")
# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
    ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls

# Q2 compute total sales at each year X region
def sales_year_region(df):
    # write code to return pandas dataframe
    ls=df.groupby(['Region',df.OrderDate.dt.year])['Sale_amt'].sum().reset_index().rename(columns={'OrderDate':'OrderYear'})
    return ls
	

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    # write code to return pandas dataframe
    import datetime as dt
    df['days_diff']= [x.days for x in dt.datetime.now()-df['OrderDate']]
    return df

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    # write code to return pandas dataframe
    ls=df.groupby(['Manager'])['SalesMan'].apply(np.unique).to_frame().reset_index().rename(columns={"SalesMan":'list_of_salesmen','Manager':'manager'})
    return ls

# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe
    ls=df.groupby(['Region']).agg({'SalesMan':[('salesmen_count',pd.Series.nunique)],'Units':[('Units_count',sum)]})
    ls.columns=ls.columns.droplevel(0)
    return ls


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    # write code to return pandas dataframe
    ls=df.groupby(['Manager'])['Sale_amt'].sum().to_frame().reset_index()
    ls['percent_sales']=(ls['Sale_amt']/ls['Sale_amt'].sum())*100
    ls.drop('Sale_amt',axis=1,inplace=True)   
    return ls.round({'percent_sales':2})

#___________________________________________________________

#df=pd.read_csv("imdb.csv",escapechar='\\')

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	# write code here
	ra=df.iloc[4]['imdbRating']
	return ra

# Q8 return titles of movies with shortest and longest run time
def movies(df):
	# write code here
    	shortest=df.loc[df['duration']==df['duration'].min()]['title']
    	longest=df.loc[df['duration']==df['duration'].max()]['title']
    	return shortest,longest

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	# write code here
	ls=df.sort_values(['year','imdbRating'],ascending=[True,False])
	return ls

#df=pd.read_csv("movie_metadata.csv",escapechar='\\')
# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	# write code here
	db=df[(df['budget']<1000000) & (df['gross']>2000000) & (df['duration']<180) & (df.duration>30)]
	#df.query('budget<1000000 & gross > 2000000 & duration < 180 & duration >30')
	return db
	

#____________________________________

#df=pd.read_csv('diamonds.csv',error_bad_lines=False)

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	# write code here
	m=len(df)-len(df.drop_duplicates())
	return m

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here
	m=df.dropna(subset=['cut','carat'])
	return m

# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here
	m=df.select_dtypes(include=[np.number])
	return m

# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	# write code here
    	m=df[df['z']!='None']
    	m['volume']=np.where(m['depth']>60,m['x']*m['y']*pd.to_numeric(m['z']),8)
    	m.fillna({'volume':8},inplace=True)
    	return m
	

# Q15 impute missing price values with mean
def impute(df):
	# write code here
	m=df.copy()
	m.fillna({'price':df['price'].mean()},inplace=True)
	return m


# Optional 1

import pandas as pd
import numpy as np
#df=pd.read_csv("imdb.csv", escapechar = '\\')
#df.shape

# def subset_data(df,col1,col2):
#     '''df:dataframe
#     col1,col2: columns on which grouby is applied must be not Null'''
#     df.dropna(subset=[col1,col2],inplace=True)
#     return df

# df=subset_data(df,'year','type')

def get_genredb(df,name='Action'):
    '''
    df: dataframe
    name : column name from which genre columns starts
    '''
    Colnames=df.columns.to_list()
    m=Colnames.index(name)
    newdb=df.groupby(['year','type'])[Colnames[m:]].sum()
    return newdb

def genre_combo(newdb):
    genre_list=[]
    for row,index in newdb.T.iteritems():
        s=index.to_dict()
        keys=[k for (k,v) in s.items() if v>0]
        items="|".join(keys)
        genre_list.append(items)
    newdb['genre_combination']=genre_list
    return newdb

def get_report(df):
    '''
    df: original dataframe
    newdb: new dataframe with only genre columns as obtained above
    '''
    resultdb=df.groupby(['year','type']).agg({'imdbRating':['mean','min','max'],'duration':'sum'})
    resultdb.columns=resultdb.columns.droplevel() # drop multilable index
    resultdb['sum']=resultdb['sum']/60            # convert seconds to minutes
    
    newdb=get_genredb(df,'Action')
    newdb=genre_combo(newdb)
    
    cols=['avg_rating','min_rating','max_rating','total_run_times_mins']
    resultdb.rename(columns=dict(zip(resultdb.columns,cols)),inplace=True)
    resultdb=pd.concat([newdb['genre_combination'],resultdb],axis=1,sort=False)
    resultdb.to_csv('report1.csv',sep=',')
    return resultdb



# Optional 2
#df=pd.read_csv("imdb.csv",escapechar='\\')
#df.shape
    
# 2
def gen_relation(df):
    df['len_movie_title']=[len(i.split(' (')[0]) for i in df['title']]
    print(df.iloc[9019]['title'].split(' (')[0])# subtract 7 for space followed by year of release in title
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.plot(df['len_movie_title'],df['imdbRating'])
    plt.xlabel('length')
    plt.ylabel('rating')
    plt.show()
    print('From plot we can find that there is No relation between length of movie  title and rating')
    print('Also the correlation is :',df['len_movie_title'].corr(df['imdbRating']))
    
def quartile(series,quartile):
    '''input1: takes the length of movie title as series
       input2: takes the series generated by quartile.
       return: list containing the quartile to which the len_movie_title belong 
    '''
    l=[]
    keys=quartile.keys()
    for i in series:
        if i < quartile[0.25]:
            l.append('1st')
        elif quartile[0.25]<=i<quartile[0.5]:
            l.append('2nd')
        elif quartile[0.5]<=i<quartile[0.75]:
            l.append('3rd')
        elif i>=quartile[0.75]:
            l.append('4th')
    return l
def gen_report2(df):
    df['len_movie_title']=[len(i.split(' (')[0]) for i in df['title']]
    gh=df['len_movie_title'].quantile([.25,0.5,.75])
    m=quartile(df['len_movie_title'],gh)
    df['quantile']=m
    cols=['num_videos_<25Percentile','num_videos_25_50Percentile',
          'num_videos_50_75Percentile','num_videos_>75Precentile']
    n=pd.crosstab(df['year'],df['quantile'])
    n.rename(columns=dict(zip(n.columns,cols)),inplace=True)
    mx=df.groupby(['year'])['len_movie_title'].agg({'min_len':'min','max_len':'max','avg_len':'mean'})
    result=pd.concat([mx,n],axis=1,sort=False)
    result.to_csv('report2.csv',sep=',')
    return result



# Optional 3

#df=pd.read_csv("diamonds.csv",escapechar='\\')
#df.info()

def volume(df):
    m=df[df['z']!='None']
    m['volume']=np.where(m['depth']>60,m['x']*m['y']*pd.to_numeric(m['z']),8)
    m.fillna({'volume':8},inplace=True)
    return m

def gen_report(df,no_of_quartile):
    m=volume(df)
    m['binned']=pd.qcut(m['volume'],q=no_of_quartile)
    # n=pd.crosstab(m['binned'],m['cut'])
    # n=n.apply(lambda x: 100*x/(n.sum().sum()))

    n=pd.crosstab(m['binned'],m['cut'],normalize=True)*100
    n.to_csv('report3.csv',sep=',')
    return n

#Optional 4
#df=pd.read_csv('movie_metadata.csv',escapechar='\\')

def last_10year(df):
    df1=df[df['title_year']>max(df['title_year'])-10]
    a=0.1 # top 10% of the record
    df1 = (df1.groupby('title_year',group_keys=False)
            .apply(lambda x: x.nlargest(int(len(x) * a), 'gross'))) #select the top 10% for each year
    
    ls=df1.groupby('title_year').agg({'imdb_score':'mean','genres':'count'})
    ls.rename(columns={'imdb_score':'avg_imdbscore',"genres":'nrOfmovie_for_each_genre'},inplace=True)
    ls.to_csv('report4.csv',sep=",")
    return ls

# Optional 5
#df=pd.read_csv('imdb.csv',escapechar='\\')
#df.info()

def get_index(df,name):
        '''
    df: dataframe
    name : column name from which genre columns starts
    '''
        Colnames=df.columns.to_list()
        m=Colnames.index(name)
        return m
def gen_decile(df,name='Action'):
    '''
    df: dataframe
    m = index of column from which genre columns starts in dataframe
    '''
    df['duration_decile_mins']=pd.cut(df['duration']/60,bins=10)
    ls=df.groupby('duration_decile_mins').agg({'nrOfNominations':'sum','nrOfWins':'sum','title':'count'})
    colsn=['total_nomination','wins','title_count']
    ls.rename(columns=dict(zip(ls.columns,colsn)),inplace=True)
    m=get_index(df,name)
    genredb=df.groupby('duration_decile_mins')[df.columns[m:-1]].sum()
    genredb = pd.DataFrame(genredb.columns[np.argsort(-genredb.values, axis=1)[:,:3]], 
                               index=genredb.index)
    genredb = genredb.rename(columns = lambda x: 'Top_{}_genre'.format(x + 1))
    ls=pd.concat([ls,genredb],axis=1)
    ls.to_csv('report5.csv',sep=',')
    return ls
    

