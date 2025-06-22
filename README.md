# AI4SE: Intelligent Solutions Project

This repository contains solutions for various tasks in the AI4SE specialization, focusing on building intelligent solutions for software engineering problems. The project is organized into three main parts, each demonstrating the use of AI and automation in different domains.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Task 1: Python List Sorting](#task-1-python-list-sorting)
- [Task 2: Automated Login Testing with Selenium IDE](#task-2-automated-login-testing-with-selenium-ide)
- [Task 3: Predictive Analytics for Resource Allocation](#task-3-predictive-analytics-for-resource-allocation)
- [Dependencies](#dependencies)
- [Contributors](#contributors)

---

## Project Structure

```
.
├── Part 1/
│   └── Part1_Theoretical_Analysis.docx
├── Part 2 Task 1/
│   ├── manual_python_list.py
│   ├── ai_suggested_list.py
│   └── Comparison.docx
├── Part 2 Task 2/
│   ├── summary.md
│   ├── Auto-Testing-with-AI.side
│   └── Screenshots/
├── Part 2 Task 3/
│   ├── Breast_Cancer_Model.ipynb
│   └── data.csv
├── requirements.txt
├── Assignment.docx
└── README.md
```

- **Part 1/**: Theoretical analysis and case study answers (`Part1_Theoretical_Analysis.docx`)
- **Part 2 Task 1/**: Python list sorting (manual vs. AI-suggested)
- **Part 2 Task 2/**: Automated login testing with Selenium IDE
- **Part 2 Task 3/**: Predictive analytics for resource allocation

---

## Setup & Installation

1. **Clone the repository** and navigate to the project root.
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Task 1: Python List Sorting

- **Files:** `manual_python_list.py`, `ai_suggested_list.py`
- **Description:**  
  Implements and compares manual and AI-suggested methods for sorting a list of dictionaries by a specific key in Python.  
  See `Comparison.docx` for analysis.

---

## Task 2: Automated Login Testing with Selenium IDE

- **Files:** `Auto-Testing-with-AI.side`, `summary.md`, `Screenshots/`
- **Description:**  
  Automated login tests (valid/invalid credentials) using Selenium IDE on a public demo site.  
  AI-powered locator strategies improve test stability and coverage.
- **How to run:**  
  Open the `.side` file in Selenium IDE (browser extension) and run the test.  
  See `summary.md` for analysis and `Screenshots/` for results.

---

## Task 3: Predictive Analytics for Resource Allocation

- **Files:** `Breast_Cancer_Model.ipynb`, `data.csv`
- **Description:**  
  Jupyter Notebook for preprocessing, training, and evaluating a Random Forest model on the Kaggle Breast Cancer dataset.  
  Includes data cleaning, feature engineering, model training, and performance evaluation (accuracy, F1-score).
- **How to run:**  
  Open the notebook in Jupyter, ensure `data.csv` is present, and run all cells.


## Ethical Reflection on Task 3: Predictive Analytics for Resource Allocation

In Task 3, we developed a predictive analytics model for resource allocation using the Kaggle Breast Cancer dataset. When deploying such a model in a company, it is crucial to consider potential biases in the dataset and the impact these biases may have on decision-making regarding resource distribution and prioritization.

**Potential Biases in Task 3:**  
The dataset may contain biases if certain teams, departments, or demographic groups are underrepresented or overrepresented in the historical data. For example, if most records come from a specific team or region, the model may learn patterns that favor those groups, leading to unfair resource allocation or issue prioritization for others. Additionally, if the data reflects past human biases (such as prioritizing issues from certain teams over others), the model may perpetuate or even amplify these biases in its predictions.

**Addressing Bias with Fairness Tools:**  
Fairness toolkits like IBM AI Fairness 360 (AIF360) can help identify and mitigate these biases in the context of resource allocation. AIF360 provides metrics to detect disparate impact and bias in model predictions, and offers algorithms to reduce unfairness. By integrating such tools into the Task 3 model development pipeline, practitioners can evaluate the fairness of their resource allocation predictions, apply bias mitigation techniques, and ensure more equitable outcomes across all groups. This proactive approach helps build trust and accountability in AI-driven decision-making within the company.

---

## Dependencies

All required Python packages are listed in `requirements.txt`.  
Key packages include:
- pandas
- numpy
- scikit-learn
- matplotlib

Install them with:
```sh
pip install -r requirements.txt
```

---

## Contributors

- [Your Name]
- [Collaborators' Names]

---

## License

This project is for educational purposes as part of the AI4SE specialization.

## Part 1: Theoretical Analysis (30%)

This section contains theoretical questions and a case study analysis. Answers are provided in the attached `Part1_Theoretical_Analysis.docx` file.

### 1. Short Answer Questions
- **Q1:** Explain how AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?
- **Q2:** Compare supervised and unsupervised learning in the context of automated bug detection.
- **Q3:** Why is bias mitigation critical when using AI for user experience personalization?

### 2. Case Study Analysis
- **Article:** AI in DevOps: Automating Deployment Pipelines
- **Question:** How does AIOps improve software deployment efficiency? Provide two examples.

---


