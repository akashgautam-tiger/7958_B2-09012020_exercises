library(readr)
library(dplyr)
df=read_delim('C:/Users/akash.gautam/imdb.csv',delim = ',',escape_backslash = T,escape_double = F)
nrow(df)

# drop the rows with na value in column on which we are using grouby
df <- df[!(is.na(df$year) | is.na(df$type)),]

get_subframe <- function(df,name){
  m=grep(name,colnames(df))
  df <- df[,m:ncol(df)]
  return(df)
  
} 

get_report <- function(df)
{
  df1 <- df %>% group_by(year,type) %>% summarise(avg_rating=mean(imdbRating),min_rating=min(imdbRating),
                                                  max_rating=max(imdbRating),total_run_time_mins=sum(duration,na.rm=T)/60)
  df2 <- df %>% group_by(year,type) %>% summarise_if(is.numeric, funs(sum))
  df2=get_subframe(df2,"Action")
  
  df2$genre_combo <- simplify2array(
    apply(
      df2[1:ncol(df2)], 1, 
      function(x) paste(names(df2[1:ncol(df2)])[x != 0], collapse = " ")
    )
  )
  col <- df2$genre_combo
  df1$genre_combo=df2$genre_combo
  df1
  colnames(df1)
  df1 <- df1[,c(1:2,7,3:6)]
  returnValue(df1)
  
}

get_report(df)


 

