# Video Game Sales Analysis

This project aims to analyze video game sales data to gain insights into the gaming industry. We use the "Video Game Sales" dataset, which contains information about the sales of video games across various platforms, genres, and regions.

## Dataset

The dataset used in this project is the "Video Game Sales" dataset, available on Kaggle: https://www.kaggle.com/gregorut/videogamesales

The dataset includes the following columns:
- Rank: Ranking of overall sales
- Name: The name of the game
- Platform: Platform of the game (e.g. PC, PS4, etc.)
- Year: Year of the game's release
- Genre: Genre of the game
- Publisher: Publisher of the game
- NA_Sales: Sales in North America (in millions)
- EU_Sales: Sales in Europe (in millions)
- JP_Sales: Sales in Japan (in millions)
- Other_Sales: Sales in other regions (in millions)
- Global_Sales: Total worldwide sales (in millions)

## Analysis

The analysis includes the following steps:

1. Data exploration and cleaning: We load the dataset using pandas and check for missing values. We drop rows with missing values to ensure the quality of our analysis.

2. Analyzing top platforms and publishers: We visualize the top platforms and publishers with the highest number of games sold.

3. Analyzing game sales by year: We calculate the total sales by year and visualize the yearly sales trends.

4. Analyzing top-selling game genres: We visualize the top-selling game genres in the dataset.

## Libraries Used

- pandas
- numpy
- matplotlib
- seaborn
