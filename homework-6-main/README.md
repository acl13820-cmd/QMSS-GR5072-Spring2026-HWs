## Instructions

1.  Answer the questions below.

2.  Your final document should be an .ipynb file. You will submit this file, along with any other scripts you used to create the report, on Canvas. In answering each question below, please include:

-   the question as a header in your jupyter Notebook
-   the raw code that you used to generate your results

### Assignment items `[100 pts]`

1.  [`10 pts`] Web-scrape all table data from the following [webpage](http://vincentarelbundock.github.io/Rdatasets/datasets.html) and build a pd.DataFrame object. Limit your final table to include columns for "Package", "Item", "Title", "Rows", and "Cols". Print the dimensions and first five rows of the table.

2.  [`10 pts`] Web-scrape the full links to every CSV file listed in the CSV column of the web-page. Add a new column to your data frame that includes these links. Name the column "`csv_links`". Print the first five rows of the table.

3.  [`5 pts`] Search the "Title" column to return the row of data with the title "Violent Crime Rates by US State".

4.  [`10 pts`] Import the csv file for the dataset identified in #3 using the full link listed in the "`csv_links`" column for this dataset. Create a new variable called "`violent_crime`" that adds together data for all columns in the dataset that contain violent crime data (i.e.-add data from assault, murder, and rape columns together in new column called "`violent_crime`").

5.  [`10 pts`] Merge all the data from the `states.csv` data set (found in the data folder of this HW6 directory) with your dataset to your Violent Crime Rates data frame. Print the first five lines of your new dataset.

6.  [`5 pts`] Calculate the average for each numeric column in the dataset.

7.  [`10 pts`] Group the data by region and then calculate the average for each numeric column in the dataset per region. Which region had the highest population (data is from the late 1970s)? Which region had the most violent crime?

8.  [`5 pts`] What SQL statement would you write to return two columns denoting income and Illiteracy in your state data?

9.  [`10 pts`] What SQL statement would you write to return two columns denoting income and Illiteracy in your state data and sort the data from the highest to lowest income values and limit the data to incomes at or higher than 5000?

10. [`10 pts`] Create a new data frame that includes two columns from your state data denoting state names and violent crimes. Spread the state names to 50 unique columns with a single row that includes the violent crime data per state. Print the first five columns of the new dataset.

11. [`10 pts`] Take the dataset from question 10 and use a function to return a dictionary with each key denoting a state and each value indicating the square root of the value for violent crimes.

12. [`5 pts`] Subset the list you created in question 12 to extract values for Texas and New York.
