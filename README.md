Contents:
  - data dictionary
  - problem statement
  - method
  - analysis
  - conclusions

--- Data Dictionary ---

The data description has been provided with the dataset here:
http://jse.amstat.org/v19n3/decock/DataDocumentation.txt

--- Problem Statement ---

We are a Data Scientist working for a (fictional) company that buys housing with the intent of making cost-effective improvements and flipping them back onto the market. Our goal is to find the most effective features for this process in the context of the Ames, Iowa housing market.

--- Method ---

Data cleaning was accomplished by turning null values into either 0s or categoricals, or a function of other data where appropriate. Outliers were checked for clerical accuracy and one was converted to a more correct value.

Data engineering consisted of converting all nominals into linear integer values, removing all outliers that affected the linear shape of the data, and dummying all remaining categorical variables.

Model testing and selection involved testing basic Linear Regression models, Ridge models, and LASSO models with or without both outliers and binning (called bucketing frequently). Each model was submitted to Kaggle to determine testing RMSE. The final selection was the columns of the LASSO model performed by an MLR with neither outliers nor binning.

Analysis included using a calculated importance factor for each LASSO weight divided by the largest LASSO weight to make an 'importance percentage', followed by multiplication with the expected USD gain predicted by the coefficients of the MLR. The top 25 columns in this importance metric were evaluated based on if they were within the control of the company and what their MLR expected value was after subtracting average costs pulled from outside data.

--- Conclusions ---

Several features have been identified as having potential for cost-effective remodeling:
 - Adding cement board paneling
 - Converting garages and kitchens to living space
 - Painting the exterior
 - Replacing roof with wooden shingles
 - Purchasing better equipment for kitchens
 - Adding a gas heating system
 - Converting Townhouses to Condominiums

Early modeling suggests that these will turn profit for the company, but additional research is required. The accuracy of the model is bounded by its RMSE of 28405.96638, meaning that every feature which showed calculated gain could be entirely nullified by the error, with the exception of adding a gas heater.

Additionally, the model violates line assumptions, having some multicolinearity between variables (though less than expected), and multiple values do not show a strictly linear trend. The model is also built on the principle of all-else-equal, meaning improving more than one housing feature at a time restricts the model's usefulness.

With this in mind, we recommend taking the features identified as suggestions for future research and experimentation for the company as a whole.
