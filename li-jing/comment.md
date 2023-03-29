## Title: 
- original text: A novel attack classification framework based on feature manipulation of IoT data for IoT security
- modified text:

- comment: IoT attack classification framework... Can replace framework with algorithm. Does this research will include attack detection?

## Executive Summary:
- original text: In recent years, the number of Internet of Things (IoT) smart devices connected to one another and systems to form various applications that make daily life more convenient and smarter has increased. However, the associated security risks, such as large-scale attacks from a large number of infected IoT devices and various variations of known IoT threats, such as zero-day attacks, are increasing in tandem with the large volume of malicious traffic worldwide. As a result, academics and industry are proposing extensive machine learning and deep learning-based data-driven security frameworks. Comprehensive datasets such as UNSW-NB15, Bot-IoT, and TON-IoT were also created as benchmark validation data to train machine learning classifiers to detect attack traffic in IoT networks. In this research, a predictive framework with multiple datasets will be developed to detect attacks represented by instances from the large-scale attack category, specifically botnet subcategories such as Distributed Denial-of-Service (DDoS). The research focuses on large-scale attack class detection (more efficient classification frameworks) that can be used at the edge of resource-constrained IoT systems, and appropriate performance metrics to deal with class imbalances and reduce overfitting. Appropriate data preparation with large datasets, ensemble feature selection methods combining Chi-square, Correlation Feature Selection (CFS), Gain Ratio (GR), and Minimum-Redundancy-Maximum-Relevance (MRMR) with majority voting mechanisms, SMOTE boost with traditional machine learning, and deep learning classifiers are used to classify specific large-scale attacks for the proposed framework. A variety of classifiers will be used, including Deep Neural Network (DNN) and machine learning techniques such as Decision Tree (DT), Support Vector Machine (SVM), and Random Forest (RF). For validation, cross-validation, time complexity analysis, and appropriate performance measures such as accuracy, precision, F1-score, sensitivity, and the AUC value of the ROC will be employed. Wilcoxon-signed testing, paired sample t-tests, and research comparisons will be used to verify statistical testing.

- modified text:

- comment: Highlight the actual IoT attack classification problem and its uniqueness. Does the normal attack classification cannot solve the problem. State in brief the current state of other research findings and what to improve.

## Research Background: 

- comment: Elaborate in details on IoT attack detection and classification. Focus on the main concern of research, highlight the recent related research and what to improves.

## Objective: 
- original text: 
(a)	To identify techniques to handle unclean data in networking and IoT data sets in the pre-processing stage.
(b)	To construct feature manipulation algorithms in order to select the significant features and reduce overall data size with informative knowledge from networking and IoT data sets in the processing stage.
(c)	To enhance an integrated synthetic minority oversampling technique with the boost technique and to use classic machine learning and deep neural network classifiers (SMOTE Boost + DT, SVM, RF/DNN) in the post-processing stage to handle class imbalance, alleviate overfitting, and improve model performances with appropriate evaluation measures 

- modified text:

- comment: Objectives need to tally with the main research issue of IoT attack detection/classification algorithm

## Methodology:
- original text:

The research framework, as shown in Figure 1, is divided into five main phases and involves a three-stage framework. Each phase contributes to the outcome of the objectives, respectively. This proposal involves problem identification and formulation in Phase 1. Phase 2 involves data collection and data understanding. While the construction of the classification methods and their algorithms is in Phase 3 and the evaluation measurement is in Phase 4, Finally, Phase 5 is the verification of the obtained results. 

Phase 1: Problem Identification and Formulation. The main purpose of this phase is to have a clearer understanding of the problems faced by researchers in the IoT security field, especially in various attacks on IoT networks. The reviewed articles based on this domain area, involving data collection, data pre-processing, and feature manipulation approaches such as feature ranking, dimensionality reduction, and feature selection, were gathered to understand the problem background in the present and also to make improvements. A literature review is a phase that collects important information from the past, present, and future regarding the conducted research. In this proposal, conceptualization is used to complete a rigorous process on IoT data that consists of handling missing values, non-numerical values, redundant instances, feature manipulation approaches, class imbalance problems, and the classification of attacks in IoT datasets.
Phase 2: Data Collection and Understanding. Phase 2 is the phase of collecting and understanding the data. This research uses publicly published IoT data sets utilised by academics that fall into two main categories. One type is networking data from the traditional real-world scenario or simulated network without IoT devices. The other type is the traffic data generated from a real-world IoT network scenario where IoT devices are connected and data is constantly transmitted, or from a simulated IoT network involving IoT data traffic with an IoT-enabled protocol, such as the MQTT protocol. These datasets that are collected can be regarded as big data; for example, the BoT-IoT data set has more than 50 million instances in maximum. Furthermore, some of the data sets collected fall into high-dimension. For instance, AWID has more than 156 features to present its characteristics, some of which have more than 50 features, which can be considered high dimensional data. Thus, the data used in this research was considered to have high-dimensional features, involving both traditional networking and increasing IoT data sets.
Phase 3: Construction of the Classification Framework and its Algorithms. The construction of classification methods and their algorithms is the one of the important phases of this proposal, as it processes the data and produces informative information regarding the networking and IoT data sets.
(a)	In stage 1, the framework in the pre-processing stage will handle missing values, non-numeric value transformation and discretization, handling redundant instances, and data normalization.
(b)	In stage 2, feature manipulation will be conducted in the processing stage, where invalid feature elimination is implemented by domain expertise, then ensemble feature ranking and selection using Chi-square, Correlation Feature Selection (CFS), Gain Ratio (GR), and Minimum-Redundancy-Maximum-Relevance (MRMR) with a majority voting mechanism, is conducted in order to make good use of individual feature selection techniques to select the best informative feature subsets.
(c)	In stage 3, post-processing stage Synthetic Minority Oversampling Technique with Boost technique (SMOTE Boost) is specifically designed for learning from imbalanced data sets, which creates synthetic examples from the rare or minority class, thus indirectly changing the updating weights and compensating for skewed distributions. Machine learning and deep learning algorithms involving classic machine learning classifiers, such as Decision Tree (DT), Support Vector Machine (SVM), and Random Forest (RF), and deep learning classifier Deep Neural Network (DNN), will be utilised to improve the performance of the proposed model while handling the class imbalance issue.
Phase 4: For validation, this research uses cross validation, time complexity analysis, and appropriate performance measures such as accuracy, precision, F1-score, sensitivity values, FAR, and the AUC value of the ROC. Evaluation of the model will be conducted with and without the factors or algorithms designed for each stage. A comparison of the performance measures with and without data transformation in the pre-processing stage, will be implemented to verify if the transformation of the original data takes effect. Then, based on the output of the first stage, a comparison of the performance metrics with and without feature manipulation in the processing stage, will be conducted to verify if feature selection of the original data has an effect. Finally, based on the result of the second stage, a comparison of the performance results with and without SMOTE Boost in the post-processing stage, will be conducted to verify if the proposed techniques can alleviate skewed results caused by class imbalance and overfitting caused by irrelevant features.
Phase 5: After the validation of the techniques and algorithms of the 3-stage classification framework, further verification will be conducted using pair-sampled test and the Wilcoxon signed rank-sum test. The rule for the t-test is that if the p-value is less than 0.05, then the result produced is significant. A Wilcoxon signed-rank sum test is used to compare sample output and validate its significance and validity, and if p-values of 0.05 indicate that the results are significant (95% confidence in the results), Finally, further comparison with recent studies using the same datasets UNSW-NB15, Bot-IoT, and TON-IoT, and the prediction of the same target classes in terms of performance measures will be conducted to verify the proposed framework really takes effect.

The use of appropriate hardware and software is very important in conducting research. The required hardware for this research is intel i5 2.3G with 8G RAM, while the required software is Weka 3.8.3 and Jupyter notebook with pandas, scikit-learn, and tensor flow libraries. Weka 3.8.3 were used for initial findings and Python3.11 in Jupyter notebook are used for the development of algorithms. Besides that, SPSS was used for statistical tests to verify the obtained results.

- modified text:

- comment: Methodology is not clear in order to achieve the objectives. Make it precise and focus on the improvement of the algorithm

## Expected Result: 
1. Novel theories/New findings/Knowledge
- original text: (a)	A hybrid of enhanced approach for feature ranking and feature selection
(b)	An enhanced Synthetic Minority Oversampling Technique with Boost technique (SMOTE Boost) 

- modified text:

- comment: In this proposal several terminologies used. Framework, algorithm, technique, approach. Be consistent, the appropriate term is algorithm, not framework.

## Track Record and Composition of Team: Related field

## Quality of Proposal: Not clear

## Elements of FRGS Criteria: No clear contribution
