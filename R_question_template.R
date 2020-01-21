require(readxl)
df = read_excel("C:/Users/akash.gautam/SaleData.xlsx")

library(dplyr)
df

#1
least_sale <- function(df){
  df %>% group_by(Item) %>% summarise(least_sale=min(Sale_amt))
}


#2
total_sales <- function(df){
  df %>% group_by(format(as.Date(df$OrderDate),'%Y'),Region) %>% summarise(tottal_sales=sum(Sale_amt))
}


#3
days_diff <- function(df){
  df['days_diff'] <- Sys.Date() - as.Date(df$OrderDate)
}


#4
sales_man <- function(df){
  ls <-  df %>% group_by(Manager) %>% summarise(list_of_salesman=paste(unique(SalesMan),collapse = ","))
}
ls


#5
region_sales_count <- function(df){
  df %>% group_by(Region) %>% summarise(sales_man_count=n_distinct(SalesMan),total_sales=sum(Sale_amt))
}


#6
percentage_sales <- function(df){
  ln <- df %>% group_by(Manager) %>% summarise(percent_sale=100*sum(Sale_amt)/sum(df$Sale_amt))
}
ln


library(readr)
df=read_delim('C:/Users/akash.gautam/imdb.csv',delim = ',',escape_backslash = T,escape_double = F)
nrow(df)

#7
fifth_row <- function(df){
  df[5,'imdbRating']
}

fifth_row(df)


#8
movie_time <- function(df){
  sorted <- na.omit(df[order(df$duration,decreasing = T),])
  shortest <- tail(sorted,1)['title']
  longest <- head(sorted,1)['title']
  lst <- list(shortest,longest)
  return(lst)
}

movie_time(df)


#9
sort_release <- function(df){
  df[order(df$year,-df$imdbRating),]
}


df=read_delim('C:/Users/akash.gautam/movie_metadata.csv',delim = ',',escape_backslash = T,escape_double = F)

#10
subset_df <- function(df){
  df[which(df$gross>2000000 & df$budget<1000000 & df$duration>30 & df$duration<180),]
}



df=read_delim('C:/Users/akash.gautam/diamonds.csv',delim = ',',escape_backslash = T,escape_double = F)


#11
count_dup <- function(df){
  sum(duplicated(df)==T)
}
df

library(tidyr)
#12
drop_rows <- function(df){
  df %>% drop_na(carat,cut)
}


#13
numeric_columns <- function(df){
  nums <- unlist(lapply(df,is.numeric))
  df[,nums]
}


#14
compute_vol <- function(df){
  df$volume <- df$x*df$y*as.integer(df$z)
  df <- within(df,volume[depth < 60] <- 8)
  
}

#15
df$price[is.na(df$price)] <- mean(df$price,na.rm = T)
df
