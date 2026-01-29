# homework 2 - data wrangling with pandas

## Instructions

1.  Use data logging NBA player season statistics from the
    `\homework-2-main\Data` folder in this repo. Variable descriptions
    can be found
    [here](https://www.kaggle.com/drgilermo/nba-players-stats/data).

2.  Your final document should be a **Jupyter Notebook** (an `.ipynb`
    file), along with any other scripts you used to create the report.

3.  Submit your work on Canvas.

In answering each of the questions for the assignment:

-   Please include the question as a header in your Jupyter Notebook
    report 
-   Near the very top of your Jupyter Notebook, you should import all
    libraries used throughout your report
-   Include the raw code that you used to generate any tables
-   Include the first five and last five rows of the data tables you're
    submitting as your answer\

### Assignment items `[100 pts]`

Use Python functions (from the pandas library where possible) to answer
the following questions:

1.  `[5 pts]` Which NBA player scored the most points in a single
    season? What seasons/year was this?

2.  `[5 pts]` Which NBA player scored the most points in 1991?

3.  `[10 pts]` Which player had the best free throw percentage ("FT%")
    from the year 2000 to the most recent year in the data? If there are
    multiple players who have tied for the best percentage, then sort on
    the column with player names and submit your answer as a
    `pd.DataFrame object`.

4.  `[10 pts]` Among those with at least 50 attempts ('FTA'), which
    player had the best free throw percentage ("FT%") from the year 2000
    to the most recent year in the data?

5.  `[5 pts]` Rename the variable "Pos" to "Position".

6.  `[10 pts]` Use this variable to create two variables that are called
    "first_position" and "second_position". **Hint:** If a player plays
    two positions, then the "-" is used as a delimiter between their
    first and second positions. In these cases, you will have to split
    the position variable into two.

    If you are not familiar with the different positions in basketball,
    I have put a list of them below:

    -   PF = Power Forward

    -   SF = Strong Forward

    -   SG = Shooting Guard

    -   PG = Point Guard

    -   G = Guard

    -   C = Center

7.  `[5 pts]` Combine these two variables back into a single variable
    called "position_united". Make sure to separate the two positions by
    "-", as the original data field did. If there is no second position,
    then there will only be a single position. Again, this is similar to
    how the original variable was coded. Present a frequency table of
    "position_united".

8.  `[10 pts]` Create two new datasets.

-   a new dataset from the original dataset that includes all data
    except the age variable (be sure to give this dataset a new name).
-   a new dataset from the original dataset that includes the year, the
    player name, and age.
-   add a new column to both datasets called `mergeid` that includes a
    sequence of numbers beginning with a 1 in the first row of the data
    and ending with the total number of rows in the last row of the data

9.  `[10 pts]` Join the two datasets from question (8) together to
    recreate the original dataset plus the new merge id.

10. `[10 pts]` Subset the original dataset to the years 1995-1997. Group
    the data by team name and year and then summarize the average number
    of points per team. Arrange from most to least points. (**Hint:**
    Your answer should have a shape of 88 x 3, since we are looking at
    the average points scored over the 1995-1997 seasons. Note that 2 of
    these columns could be indexes, in which case Pandas will tell you
    your data is 88 rows x 1 columns. Finally, also note that the data
    for VAN and TOR are missing in 1995 as these teams did not exist in
    that year. So your answer could also be 90 x 3, if you include
    missing/empty data in these rows).

12. `[10 pts]` Similar to Q10, start by subsetting the original dataset
    to the years 1995-1997. Then create a wide dataset that keeps each
    year in its own row, but spreads team names to multiple columns with
    each column delineating points per team in each of the 1995-1997
    seasons (**Hint:** Your final answer should have a shape of 3 x 30).

13. `[10 pts]` Now return the data from #11 back into a long (tidy)
    format by moving Team (TM), Points and Year into their own columns
    (**Hint:** Your data shape should be 90 x 3).
