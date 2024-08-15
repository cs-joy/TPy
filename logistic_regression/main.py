import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Example data
data = {
    'x1': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'x2': [4, 9, 25, 49, 121, 169, 289, 361, 529, 841],
    'y':  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]  # Binary dependent variable
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Check correlation matrix
print("Correlation Matrix:\n", df.corr())

# Independent variables
X = sm.add_constant(df[['x1', 'x2']])

# Calculate VIF for each variable
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print("\nVariance Inflation Factors:\n", vif_data)

# Removing one of the variables (e.g., x2)
X = sm.add_constant(df[['x1']])

# Logistic Regression Model
logit_model = sm.Logit(df['y'], X)

# Fitting the model
result = logit_model.fit()

# Print the summary of the model
print(result.summary())
