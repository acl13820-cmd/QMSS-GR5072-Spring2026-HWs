# homework 3 - Functions I

## Instructions

1.  Use the `flights` dataset in the data folder to answer the questions below.

2.  Your final document should be an `.ipynb` file. You will submit this file, along with any other scripts you used to create the report, on Canvas.

3.  In answering each of the questions for the assignment please include:

    -   the question as a header in your Jupyter Notebook
    -   the raw code that you used to generate any tables
    -   the first and last five rows of the resulting data tables you're submitting as your answer

### Assignment items `[100 pts]`

1.  `[20 pts]` Write a function that takes a single numerical variable and returns three values, the minimum number, the median, and the maximum number of the vector. Test your function using the month column of the flights data set.

2.  `[5 pts]` Explain your reasoning for choosing your function's name in the previous question.

3.  `[20 pts]` Write a function that categorizes a numerical variable in the flights data into four categories.

The function should have two arguments. The first should represent the data object and the second should represent a column name in the data object.

The function should return one new column which categorizes the *dep_time* column into four categories in the following manner. For any particular variable in the flights data that represents military time (i.e., 0 to 2400 where 1200 represents 12 in the afternoon and 2400 represents midnight), the function should classify values into four categories:

-   "Morning" for values from 5 am to 11:59 am

-   "Afternoon" for values from 12 pm to 4:59 pm

-   "Evening" for values from 5 pm to 8:59 pm

-   "Night" for values from 9 pm to 4:59 am

Test your function using the *dep_time* column of the flights dataset. Print a frequency table of the output.

4.  `[5 pts]` Explain your reasoning for choosing your function's name in the previous question.

5.  `[20 pts]` Write a function that calculates the median of all numeric variables in the flights dataset.

*Hint: There are several ways to subset a DF to numeric values only, you will need to search online (using google, stackexchange or some generative AI like chat GPT) to find a suitable way to do so. Alternatively, you could try to do this manually with a for loop, which was reviewed in datacamp, although as a class we are not learning for loops together until next week.*

6.  `[5 pts]` Explain your reasoning for choosing your function's name in the previous question.

7.  `[20 pts]` Modify the function `t_test()` we wrote in class together this week so that this function can handle violations to the homogeneity of variance (HOV) assumption. This assumption is described below in case you are not familiar with it. Please read the class activity carefully - as all of those details are relevant.

    The t-test makes three key assumptions, requiring one continuous variable and one binary variable before we can use it:

    -   The continuous variable is normally distributed

    -   Homogeneity of variance (HOV): For the two groups based on the binary predictor, the variance of the continuous variable is similar

    -   Each observation is independent of all others

We will ignore the first and third assumptions for now. If the homogeneity of variance assumption is broken, then the solution is to use an alternative called Welch's t-test. To assess this second assumption, we will compare the variance statistic from the two groups -- and if they are different by a factor greater than 4:1 (or less than 1:4) then we will consider this assumption violated. Note that there are statistical procedures available to test the HOV assumption as well (e.g., Levene's test), but the results of any statistical test are strongly tied to the sample size/statistical power and therefore cannot be considered reliable in every context.

To assess whether the HOV assumption is violated, this function has to compare the sample variances of the two groups. If the ratio of the variances is between 0.25 - 4.00, then we will consider the HOV assumption to **not** be broken. We then would use the standard two-samples independent t-test which was programmed in the class activity. If the HOV assumption is broken however, then we will instead conduct Welch's t-test. To compute Welch's t-test you will need the formulas below to compute the t-statistic and df. Like the independent samples t-test, you will need both sample means, both sample variances, and both group sample sizes.

$\LARGE t = \frac{\overline{x}_1 - \overline{x}_2 }{\sqrt{ \frac{s_1^{2}}{n_1} + \frac{s_2^{2}}{n_2} }}$

$\LARGE df = \frac{\left(\frac{s_1^{2}}{n_1} + \frac{s_2^{2}}{n_2}\right)^{2}}{\frac{1}{n_1 - 1}\left(\frac{s_1^{2}}{n_1}\right)^{2} + \frac{1}{n_2 - 1}\left(\frac{s_2^{2}}{n_2}\right)^{2}}$

To recap, your task is to modify `t_test()` which we worked on as a class activity in the following ways:

-   Create temporary objects within your function to hold the sample means, variances, and sample sizes, objects which will be used in the computation for both versions of the t-test (i.e., you should create these objects once, before you jump into an if-else statement about whether the HOV assumption is broken)

-   Compare the sample variances. Use an `if-else` statement that depends on the ratio of the sample variances. If this ratio is in between 0.25 - 4 (inclusive of the 0.25 and 4.0), then:

    -   Conduct the standard t test, using the code from the class activity. The last column of the return output, "test", should now read "Independent samples t-test" since we need to be more specific here to distinguish this type of t test from Welch's t-test

    -   Also, print the following message: "The homogeneity of variance assumption was not violated, so an independent samples t-test was conducted"

-   If the HOV assumption is violated, then:

    -   Conduct Welch's t-test, using the formulas above

    -   Return an object with the same 9 columns from the class activity, but the "test" column should read "Welch's t-test"

    -   Also, print the following message: "The homogeneity of variance assumption was violated, so Welch's t-test was conducted"

`8. [5 pts]` Import the GED data set we used for the class activity. Call the `t_test()` function and test it out on the GED data set we used in class. Let the numeric variable be 'income_log' and let the binary variable be 'ged'.
