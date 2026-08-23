# 🏘️ Airbnb Stock Price Prediction

A machine learning project focused on predicting Airbnb (ABNB) stock prices using regression models, technical indicators, and historical market data.

---

## 📌 Project Overview
This project builds a complete workflow for stock price forecasting, including data preprocessing, exploratory analysis, feature engineering, model training, and evaluation. The goal is to understand market behavior and generate accurate price predictions.

---

## 🧰 Tech Stack
- **Language:** Python  
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn  
- **Environment:** Jupyter Notebook / Google Colab  

---

## 🔄 Workflow Summary

### **1. Data Collection**
Historical Airbnb stock data imported from Yahoo Finance containing:
- Date, Open, High, Low, Close, Adj Close, Volume  

---

### **2. Exploratory Data Analysis (EDA)**
- Price trends over time  
- Volatility and daily returns  
- Volume patterns  
- Correlation analysis  

---

### **3. Feature Engineering**
- Moving Averages (MA7, MA14, MA30)  
- Lag features  
- Volatility metrics (rolling std)  
- Date-based features (day, month, quarter)  
- Normalization for ML compatibility  

---

### **4. Modeling**
Models used:
- **Linear Regression** (baseline)  
- **Random Forest Regressor** (best performance)  

---

### **5. Evaluation**
Metrics:
- RMSE  
- MAE  
- R²  

**Result:** Random Forest achieved the highest accuracy and stable predictions.

---

### **6. Prediction**
- Generated short-term forecasts  
- Analyzed feature importance influencing stock price behavior  

---

## 📁 Project Structure

AirBnB Stock Price Prediction/
```│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```


---

## 📈 Key Findings
- Airbnb stock shows seasonal patterns and volatility cycles  
- Engineered features significantly boost prediction accuracy  
- Random Forest outperforms linear models due to non-linear behavior  

---

## 🚀 Future Improvements
- Add LSTM/GRU deep learning models  
- Deploy model using Flask or Streamlit  
- Integrate real-time stock market API  

---

## 🧑‍💻 Author
**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**  

## Let's Connect <img src="https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif" height="30px" style="max-width:100%;">

<div align="center">

<a href="https://www.linkedin.com/in/tajamulkhann/">
  <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://www.instagram.com/tajamul.datascientist/" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white">
</a>
<a href="https://topmate.io/tajamulkhan" target="_blank">
  <img src="https://img.shields.io/badge/Topmate-FF0000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0MCIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white">
</a>
<a href="https://www.whatsapp.com/channel/0029VaYs05jJkK7JKCesw42f">
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white">
</a>
<a href="https://t.me/tajamul_khan">
  <img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
</a>
<a href="https://substack.com/@tajamulkhan">
  <img src="https://img.shields.io/badge/Substack-%23006f5c.svg?style=for-the-badge&logo=substack&logoColor=FF6719">
</a>
<a href="https://www.kaggle.com/tajamulkhan">
  <img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white">
</a>
<a href="https://github.com/tajamulkhann">
  <img src="https://img.shields.io/badge/Github-12100E?style=for-the-badge&logo=github&logoColor=white">
</a>
<a href="https://medium.com/@tajamulkhan">
  <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white">
</a>
<a href="https://www.youtube.com">
  <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">
</a>
</div>




