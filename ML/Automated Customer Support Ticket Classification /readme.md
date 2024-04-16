# Overview

  Customer complaints are invaluable for financial firms, offering insights into product and service deficiencies. Swift resolution of complaints is pivotal for preserving customer satisfaction and loyalty. However, as companies expand, managing the increasing volume of support tickets becomes cumbersome. Natural language processing (NLP) and machine learning (ML) offer a remedy. NLP algorithms can automate ticket categorization and prioritization based on content and sentiment analysis. ML models predict optimal resolution paths, expediting support processes. This not only enhances customer experience by accelerating resolutions but also extracts valuable insights for continuous improvement.

# Objective
  The objective of this project is to revolutionize the customer support ticket system of a financial company by harnessing the power of natural language processing (NLP) and machine learning (ML) techniques. The primary aim is to automate the identification and categorization of support tickets with precision, leveraging the content within each ticket. By employing advanced NLP algorithms, the project seeks to analyze the text data, extract key information, and classify tickets into appropriate categories.

# Problem Statement

Build a model that is able to classify customer complaints based on the products/services. By doing so, you can segregate these tickets into their relevant categories and, therefore, help in the quick resolution of the issue.

You will be doing topic modelling on the .json data provided by the company. Since this data is not labelled, you need to apply NMF to analyse patterns and classify tickets into the following five clusters based on their products/services:

- Credit card / Prepaid card

- Bank account services

- Theft/Dispute reporting

- Mortgages/loans

- Others 

With the help of topic modelling, you will be able to map each ticket onto its respective department/category. You can then use this data to train any supervised model such as logistic regression, decision tree or random forest. Using this trained model, you can classify any new customer complaint support ticket into its relevant department.

# Relsuts

<img width="538" alt="image" src="https://github.com/PriyankWebpage/Projects/assets/65448205/256a5f9a-fabf-405a-b1a6-f9001a1b3089">

# Conclusion

  As from the results we can see that Logistic Regression and XGBoost Classifier are performing the best with an F1 score of 0.91. So we will be using these models to predict the topics for the new complaints.
