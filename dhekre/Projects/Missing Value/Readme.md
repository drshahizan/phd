# Effect of Missing Values on Feature Selection and Classification Prediction for Thyroid Dataset
This project explores the effect of missing values on feature selection and classification prediction for the Thyroid Disease dataset. The project uses three techniques for missing value imputation: mean imputation, k-nearest neighbor (KNN) imputation, and cold-deck imputation. Then, feature selection is performed using random forest (RF), and classification prediction is done using support vector machine (SVM), logistic regression (LR), naive Bayes, light gradient boosting machine (LGBM), and recurrent neural network (RNN) deep learning. The dataset is obtained from the [UCI](https://archive.ics.uci.edu/ml/index.php) Machine Learning Repository and consists of 9172 instances and 31 features.

## Files
The following files are included in the project:

* `cold_deck.py`: This file contains the implementation of cold-deck imputation technique.
* `mean.py`: This file contains the implementation of mean imputation technique.
* `knn.py`: This file contains the implementation of k-nearest neighbor (KNN) imputation technique.
* `knn_imputer.py`: This file contains the implementation of KNN imputer class.
* `step1.py`: This file performs data preprocessing, including loading the dataset, handling missing values, and encoding categorical features.
* `step2.py`: This file performs feature selection using random forest (RF) algorithm.
* `step3.py`: This file performs classification prediction using support vector machine (SVM), logistic regression (LR), naive Bayes, light gradient boosting machine (LGBM), and recurrent neural network (RNN) deep learning algorithms.
* `Step 4`: Evaluation and Comparison: This file evaluates the performance of the classification algorithms and compares their results.

## Usage
To run the project, follow these steps:

Run `step1.py` to preprocess the data and handle missing values.
Run `step2.py` to perform feature selection using RF algorithm.
Run `step3.py` to perform classification prediction using SVM, LR, naive Bayes, LGBM, and RNN deep learning algorithms.
Run `Step 4`: Evaluation and Comparison to evaluate the performance of the classification algorithms and compare their results.
Note: Before running `step3.py`, you need to impute the missing values using one of the three techniques (mean, KNN, or cold-deck). To do this, you can run `mean.py`, `knn.py`, or `cold_deck.py` to generate the imputed dataset, then use the output dataset in `step3.py`.

## Conclusion
This project shows that missing values can significantly affect feature selection and classification prediction results. The best missing value imputation technique depends on the nature of the data and the classification algorithm used. The results of this project can help researchers and practitioners in choosing the appropriate missing value imputation technique and classification algorithm for their datasets.

