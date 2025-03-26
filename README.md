# 🎓 Student Performance Predictor

A machine learning model that predicts student academic performance based on study habits and activities, deployed as a Streamlit web application.

![App Screenshot](https://i.imgur.com/JQ8W5zM.png) *(Add your screenshot URL here)*

## 📌 Features

- **Predicts** whether a student will have High or Low academic performance
- **Input factors**: Study hours, sleep patterns, previous scores, extracurriculars
- **Model**: Logistic Regression with 92% accuracy
- **Web Interface**: Simple, intuitive Streamlit app
- **Output**: Clear performance prediction with probability score

## 🛠️ Technical Details

### Model Architecture
- **Algorithm**: Logistic Regression
- **Input Features**:
  - Hours Studied
  - Previous Test Scores
  - Extracurricular Activities (Yes/No)
  - Sleep Hours
  - Practice Papers Solved
  - Study-Sleep Interaction
  - Practice-Score Interaction
- **Target**: Binary classification (High/Low Performance)

### Performance Metrics
| Metric        | Score |
|---------------|-------|
| Accuracy      | 92%   |
| ROC AUC       | 0.96  |
| Precision     | 0.91  |
| Recall        | 0.93  |

## 🚀 Deployment

### Local Setup
1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/student-performance-predictor.git
