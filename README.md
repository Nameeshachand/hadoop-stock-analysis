# hadoop-stock-analysis
Hadoop MapReduce project using Python to analyze stock data and compute maximum closing prices using HDFS and Hadoop Streaming.
# Stock Price Analysis using Hadoop MapReduce

##  Description
This project uses Hadoop MapReduce with Python (Hadoop Streaming) to analyze stock market data and find the maximum closing price for each stock.

##  Technologies Used
- Hadoop
- HDFS
- MapReduce
- Python

##  Files
- mapper.py → Extracts stock and closing price
- reducer.py → Computes maximum closing price
- stocks1.csv → Sample dataset

##  How It Works
1. Data is stored in HDFS
2. Mapper extracts (stock, closing price)
3. Reducer finds maximum price per stock

##  Output
AAPL → 189.0  
GOOG → 2775.0
