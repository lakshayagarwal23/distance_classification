# Face Clustering with Hue & Saturation

This project performs face detection and clustering using OpenCV and K-Means based on hue and saturation features.  

## Weights & Biases Dashboard  
![W&B Dashboard](wandb_dashboard.png)  

## Features  
- Face detection using OpenCV  
- Clustering based on color features  
- Automated logging to W&B  
- GitHub Actions workflow to auto-run notebook on code updates  

Report
#### 1. What are the common distance metrics used in distance-based classification algorithms? 
A.1 Distance-based classification algorithms like KNN and clustering methods rely on different distance metrics to measure similarity between data points:

Euclidean Distance: Measures the straight-line distance between two points.

Manhattan Distance: Computes distance along axes, useful in grid-like structures.

Minkowski Distance: A generalized form of Euclidean and Manhattan distances.

Cosine Similarity: Measures the angle between vectors, commonly used in text classification.

Mahalanobis Distance: Accounts for correlations in data, useful in anomaly detection.

Hamming Distance: Measures the difference in categorical or binary data, applied in text and error detection.


#### 2. What are some real-world applications of distance-based classification algorithms? 
A.2 Distance-based classification is widely used across various domains:

Medical Diagnosis: Predicting diseases using patient data.

Recommendation Systems: Movie and product recommendations using user preferences.

Fraud Detection: Identifying anomalies in financial transactions.

Text Analysis: Spam filtering and document similarity detection.

Image Recognition: Face detection and image retrieval.

Customer Segmentation: Grouping customers based on purchasing behavior.
#### 3. Explain various distance metrics. 
A.3 Each distance metric has its strengths:

Euclidean: Effective for continuous numerical data but sensitive to scale variations.

Manhattan: Suitable for high-dimensional data with independent features.

Minkowski: Adaptable using different values of p.

Cosine Similarity: Ideal for high-dimensional sparse data, such as text.

Mahalanobis: Useful when features are correlated.

Hamming: Best for categorical or binary attributes.

#### 4. What is the role of cross validation in model performance? 
A.4 Cross-validation helps improve model generalization by splitting data into multiple training and validation sets. It prevents overfitting, aids model selection, and balances the bias-variance tradeoff. Common techniques include k-fold cross-validation, stratified k-fold, and leave-one-out (LOO) validation

#### 5. Explain variance and bias in terms of KNN? 
A.5 The value of k in KNN directly affects bias and variance:

Low k (e.g., 1-3) → Low bias, high variance → Overfitting.

Moderate k (e.g., 5-10) → Balanced tradeoff → Good generalization.

High k (e.g., 50+) → High bias, low variance → Underfitting.
