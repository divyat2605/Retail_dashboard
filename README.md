# 📊 Interactive Retail Dashboard

> A live, interactive business intelligence dashboard for retail analytics, featuring real-time sales trends, store performance, category breakdowns, and KPI metrics

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Deployed](https://img.shields.io/badge/Deployed-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://retail-dashboard-thg4wqvkio8vvqykgesj9t.streamlit.app/)

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [Key Features](#-key-features)
- [Dashboard Preview](#-dashboard-preview)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Installation & Usage](#-installation--usage)
- [Business Impact](#-business-impact)
- [Future Improvements](#-future-improvements)
- [Connect With Me](#-connect-with-me)

---

## 📊 Overview

**Interactive Retail Dashboard** is a self-service business intelligence tool that helps retail executives, managers, and analysts monitor key performance indicators, identify trends, and make data-driven decisions in real-time.

### Why This Matters

| Challenge | Impact on Business |
|-----------|-------------------|
| Data scattered across spreadsheets | Slow, manual reporting processes |
| No real-time visibility | Missed opportunities and delayed responses |
| Complex data tools | Non-technical stakeholders can't access insights |
| Time-consuming reporting | 10+ hours/week wasted on manual reports |

**This dashboard solves that by:**
- Providing instant visibility into sales, revenue, and customer metrics
- Enabling self-service analytics for non-technical users
- Saving hours of manual reporting time
- Empowering faster, data-driven decisions

---

## 🌐 Live Demo

**View the live dashboard here:**
👉 [https://retaildashboard-divyat2605.streamlit.app/](https://retaildashboard-divyat2605.streamlit.app/)

---

## 🎯 The Problem

Retail teams face several challenges when trying to monitor performance:

| Problem | Consequence |
|---------|-------------|
| Data in multiple spreadsheets | No single source of truth |
| Manual weekly reports | Outdated information |
| No interactive filters | Can't drill down into specific stores or categories |
| Static charts | Can't explore data dynamically |

**Example Scenario:**
A retail executive needs to understand why sales dropped last week. Currently, they wait 3-5 days for a manual report. By then, the opportunity to act has passed.

**This dashboard solves that** by providing instant, interactive insights.

---

## 💡 The Solution

The Interactive Retail Dashboard provides:

| Feature | Benefit |
|---------|---------|
| Real-time KPI monitoring | Sales, revenue, customer metrics at a glance |
| Interactive filtering | Filter by date, store, and category |
| Dynamic visualizations | Charts update instantly based on filters |
| Actionable insights | Automatic business recommendations |

---

## 🔑 Key Features

| Feature | Description | Business Impact |
|---------|-------------|-----------------|
| **KPI Cards** | Total revenue, sales, daily average, customers | Instant performance overview |
| **Sales Trend** | Daily sales volume over time | Identify trends and patterns |
| **Category Breakdown** | Sales by product category | Optimize inventory allocation |
| **Store Performance** | Revenue comparison across stores | Identify best and worst performers |
| **Revenue vs Sales** | Dual-axis chart showing relationship | Understand pricing impact |
| **Interactive Filters** | Date range, store, category filters | Self-service analytics |
| **Business Insights** | Automatic recommendations | Faster decision-making |
| **Live Dashboard** | Web-based, accessible anywhere | No software installation needed |

---

## 🖥️ Dashboard Preview

### KPI Cards Display
- **Total Revenue**: $1,245,000
- **Total Sales**: 45,230 units
- **Avg Daily Sales**: 1,508 units
- **Total Customers**: 28,450

### Interactive Filters (Sidebar)
- **Date Range**: Select any date period
- **Store Filter**: Choose specific store or view all
- **Category Filter**: Filter by product category

### Charts Displayed
- **Sales Trend**: Line chart showing daily sales over time
- **Sales by Category**: Horizontal bar chart
- **Store Performance**: Revenue by store
- **Revenue vs Sales**: Dual-axis chart

### Business Insights Cards
- **Top Category**: Identifies highest revenue category
- **Best Store**: Identifies top performing store
- **Opportunity Alert**: Suggests growth opportunities

---

## 🛠️ Tech Stack

### Languages & Libraries

| Tool | Proficiency |
|------|-------------|
| Python | ████████████████████ 90% |
| Streamlit | ██████████████████░░ 85% |
| Plotly | ██████████████████░░ 85% |
| pandas | ████████████████████ 90% |
| NumPy | ██████████████████░░ 85% |

### Deployment
- **Streamlit Cloud** - Free hosting for Python apps
- **GitHub** - Version control and collaboration

---

## ⚙️ How It Works

### Step-by-Step Process

**Step 1: Data Generation**
- Creates 2 years of realistic retail data
- Includes: date, store, category, sales, inventory, customers, revenue
- Simulates seasonal patterns and weekend effects

**Step 2: Data Processing**
- Filters data based on user selections
- Aggregates metrics for KPI cards
- Prepares data for visualizations

**Step 3: Visualization**
- Sales trend line chart
- Category breakdown bar chart
- Store performance bar chart
- Revenue vs Sales dual-axis chart

**Step 4: Insights Generation**
- Identifies top category
- Identifies best store
- Calculates opportunity for growth

**Step 5: User Interface**
- Sidebar for filters
- KPI cards for overview
- Interactive charts
- Insight cards

---

## 🚀 Installation & Usage

### Option 1: View Live Demo (Recommended)
👉 [https://retail-dashboard-thg4wqvkio8vvqykgesj9t.streamlit.app/](https://retail-dashboard-thg4wqvkio8vvqykgesj9t.streamlit.app/)

### Option 2: Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Michaeldw012/Retail-Dashboard.git
   cd Retail-Dashboard
2. Install Requirements:
   pip install -r requirements.txt
3. Run the app:
   streamlit run Streamlit-retail_dashboard.py
4. Open your browser to http://localhost:85016

💼 Business Impact
By implementing this dashboard, retail teams can achieve:

Metric	Improvement
Reporting Time	↓ 10+ hours per week saved
Decision Speed	↑ From days to minutes
Data Accessibility	↑ Self-service for non-technical users
Revenue Opportunities	↑ Identify trends faster
Team Alignment	↑ Single source of truth
Real-World Example
Before:

10+ hours per week on manual reporting

3-5 day delay for insights

Only analysts could access data

Static, outdated reports

After using Interactive Retail Dashboard:

Instant access to live data

Self-service for any team member

Real-time insights and alerts

10+ hours per week saved

🔮 Future Improvements
□ Real data integration - Connect to actual retail databases
□ Automated alerts - Email notifications for anomalies
□ Sales forecasting - Predictive analytics integration
□ User authentication - Personalized views per user
□ Export functionality - Download reports as PDF or Excel
□ Mobile responsive - Optimized for phone viewing
□ Dark mode - User preference option
□ Multi-language - Internationalization support
📊 How This Helps Different Teams
Team	Benefit
Executive	Instant performance overview
Store Managers	Compare performance across stores
Marketing	Track campaign impact on sales
Operations	Monitor inventory and sales trends
Finance	Revenue tracking and forecasting
📝 Sample User Journey
Executive opens dashboard → Sees total revenue, sales, customers

Filters by last quarter → Revenue trend appears

Filters by store → Compare Store A vs Store B

Notices category performance → Home category is underperforming

Takes action → Increases marketing spend on Home category

Measures impact → Checks dashboard next week to see improvement

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.



📜 License
This project is open source and available under the MIT License.

⭐ Show Your Support
If you found this project helpful, please star this repository and share it with others!

"Data is the new oil - refine it, visualize it, and use it wisely."


 