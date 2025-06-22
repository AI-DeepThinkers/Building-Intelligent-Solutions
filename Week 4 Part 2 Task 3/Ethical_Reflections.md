# Ethical Reflection

When deploying a predictive model like the one from Task 3 in a company, it is crucial to consider potential biases in the dataset and the impact these biases may have on decision-making.

**Potential Biases:**  
The dataset may contain biases if certain teams, departments, or demographic groups are underrepresented or overrepresented. For example, if the majority of historical data comes from one team or region, the model may learn patterns that favor those groups, leading to unfair predictions for others. Additionally, if the data reflects past human biases (such as prioritizing issues from certain teams over others), the model may perpetuate or even amplify these biases in its predictions.

**Addressing Bias with Fairness Tools:**  
Fairness toolkits like IBM AI Fairness 360 (AIF360) can help identify and mitigate these biases. AIF360 provides metrics to detect disparate impact and bias in model predictions, and offers algorithms to reduce unfairness. By integrating such tools into the model development pipeline, practitioners can evaluate the fairness of their models, apply bias mitigation techniques, and ensure more equitable outcomes across all groups. This proactive approach helps build trust and accountability in AI-driven decision-making within the company. 