import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Retail Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Generate realistic retail data
@st.cache_data
def generate_data():
    """Generate 2 years of retail data with more metrics"""
    np.random.seed(42)
    
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
    categories = ['Electronics', 'Clothing', 'Home', 'Beauty', 'Toys', 'Food', 'Books']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    
    data = []
    for date in dates:
        for store in stores:
            for category in categories:
                # Base patterns
                weekday = date.weekday()
                is_weekend = weekday >= 5
                month = date.month
                
                # Seasonal factors
                if month in [6, 7, 8]:
                    season_factor = 1.3
                elif month == 12:
                    season_factor = 1.5
                else:
                    season_factor = 1.0
                
                weekend_factor = 1.4 if is_weekend else 1.0
                
                # Generate metrics
                base_sales = random.randint(50, 200)
                sales = int(base_sales * season_factor * weekend_factor * random.uniform(0.8, 1.2))
                
                # Inventory (2-4x sales)
                inventory = random.randint(sales * 2, sales * 4)
                
                # Customers (30-70% of sales)
                customers = int(sales * random.uniform(0.3, 0.7))
                
                # Revenue ($20-100 per unit)
                unit_price = random.uniform(20, 100)
                revenue = sales * unit_price
                
                # Cost (50-70% of revenue)
                cost = revenue * random.uniform(0.5, 0.7)
                profit = revenue - cost
                
                # Returns (1-8% of sales)
                returns = int(sales * random.uniform(0.01, 0.08))
                
                data.append({
                    'date': date,
                    'store': store,
                    'category': category,
                    'sales': sales,
                    'inventory': inventory,
                    'customers': customers,
                    'revenue': revenue,
                    'cost': cost,
                    'profit': profit,
                    'returns': returns,
                    'unit_price': unit_price
                })
    
    return pd.DataFrame(data)

# Load data
df = generate_data()

# ============================================
# SIDEBAR FILTERS
# ============================================

st.sidebar.title("🎛️ Filters")

# Date range
min_date = df['date'].min().date()
max_date = df['date'].max().date()
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Store filter
stores = ['All'] + sorted(df['store'].unique().tolist())
selected_store = st.sidebar.selectbox("🏪 Select Store", stores)

# Category filter
categories = ['All'] + sorted(df['category'].unique().tolist())
selected_category = st.sidebar.selectbox("📂 Select Category", categories)

# Apply filters
filtered_df = df.copy()
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df['date'].dt.date >= start_date) &
        (filtered_df['date'].dt.date <= end_date)
    ]
if selected_store != 'All':
    filtered_df = filtered_df[filtered_df['store'] == selected_store]
if selected_category != 'All':
    filtered_df = filtered_df[filtered_df['category'] == selected_category]

# ============================================
# MAIN DASHBOARD
# ============================================

st.title("📊 Retail Analytics Dashboard")
st.markdown(f"*Showing data from {filtered_df['date'].min().strftime('%B %d, %Y')} to {filtered_df['date'].max().strftime('%B %d, %Y')}*")
st.markdown("---")

# ============================================
# KPI CARDS - 4 ROWS
# ============================================

# Row 1: Revenue & Profit
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_revenue = filtered_df['revenue'].sum()
    st.metric(
        label="💰 Total Revenue",
        value=f"${total_revenue:,.0f}",
        delta=f"{((total_revenue / df['revenue'].sum()) * 100):.1f}% of total"
    )

with col2:
    total_profit = filtered_df['profit'].sum()
    profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
    st.metric(
        label="📈 Total Profit",
        value=f"${total_profit:,.0f}",
        delta=f"{profit_margin:.1f}% margin"
    )

with col3:
    avg_order_value = filtered_df['revenue'].sum() / filtered_df['sales'].sum() if filtered_df['sales'].sum() > 0 else 0
    st.metric(
        label="🛒 Avg Order Value",
        value=f"${avg_order_value:.2f}",
        delta=f"{filtered_df['store'].nunique()} stores"
    )

with col4:
    total_customers = filtered_df['customers'].sum()
    st.metric(
        label="👥 Total Customers",
        value=f"{total_customers:,.0f}",
        delta=f"{(total_customers / df['customers'].sum() * 100):.1f}%"
    )

# Row 2: Sales & Inventory
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = filtered_df['sales'].sum()
    st.metric(
        label="📦 Total Sales",
        value=f"{total_sales:,.0f} units",
        delta=f"{filtered_df['date'].nunique()} days"
    )

with col2:
    avg_daily_sales = filtered_df.groupby('date')['sales'].sum().mean()
    st.metric(
        label="📈 Avg Daily Sales",
        value=f"{avg_daily_sales:,.0f} units"
    )

with col3:
    total_returns = filtered_df['returns'].sum()
    return_rate = (total_returns / total_sales * 100) if total_sales > 0 else 0
    st.metric(
        label="🔄 Return Rate",
        value=f"{return_rate:.1f}%",
        delta=f"{total_returns:,.0f} returns"
    )

with col4:
    total_inventory = filtered_df['inventory'].sum()
    st.metric(
        label="📦 Total Inventory",
        value=f"{total_inventory:,.0f} units",
        delta=f"{(total_inventory / df['inventory'].sum() * 100):.1f}%"
    )

st.markdown("---")

# ============================================
# ROW 1: Sales Trend + Category Breakdown
# ============================================

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Sales Trend")
    
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    
    fig_trend = px.line(
        daily_sales,
        x='date',
        y='sales',
        title='Daily Sales Volume',
        labels={'date': 'Date', 'sales': 'Sales (Units)'},
        line_shape='spline'
    )
    fig_trend.update_layout(height=400)
    st.plotly_chart(fig_trend, use_container_width=True)

with col2:
    st.subheader("🏷️ Sales by Category")
    
    category_sales = filtered_df.groupby('category')['sales'].sum().reset_index()
    category_sales = category_sales.sort_values('sales', ascending=True)
    
    fig_category = px.bar(
        category_sales,
        x='sales',
        y='category',
        title='Sales by Category',
        labels={'sales': 'Sales (Units)', 'category': ''},
        color='sales',
        color_continuous_scale='Blues',
        orientation='h'
    )
    fig_category.update_layout(height=400)
    st.plotly_chart(fig_category, use_container_width=True)

# ============================================
# ROW 2: Store Performance + Revenue vs Profit
# ============================================

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏪 Store Performance")
    
    store_performance = filtered_df.groupby('store').agg({
        'revenue': 'sum',
        'profit': 'sum',
        'sales': 'sum'
    }).reset_index()
    
    fig_store = px.bar(
        store_performance,
        x='store',
        y='revenue',
        title='Revenue by Store',
        labels={'store': 'Store', 'revenue': 'Revenue ($)'},
        color='revenue',
        color_continuous_scale='Greens',
        text_auto='.2s'
    )
    fig_store.update_layout(height=350)
    st.plotly_chart(fig_store, use_container_width=True)

with col2:
    st.subheader("📊 Revenue vs Profit")
    
    daily_metrics = filtered_df.groupby('date').agg({
        'revenue': 'sum',
        'profit': 'sum'
    }).reset_index()
    
    fig_dual = go.Figure()
    fig_dual.add_trace(go.Bar(
        x=daily_metrics['date'],
        y=daily_metrics['revenue'],
        name='Revenue',
        marker_color='lightblue',
        yaxis='y'
    ))
    fig_dual.add_trace(go.Scatter(
        x=daily_metrics['date'],
        y=daily_metrics['profit'],
        name='Profit',
        marker_color='darkgreen',
        yaxis='y2',
        line=dict(width=3)
    ))
    fig_dual.update_layout(
        title='Revenue vs Profit',
        height=350,
        yaxis=dict(title='Revenue ($)'),
        yaxis2=dict(title='Profit ($)', overlaying='y', side='right')
    )
    st.plotly_chart(fig_dual, use_container_width=True)

# ============================================
# ROW 3: Inventory Status + Returns
# ============================================

col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Inventory Status")
    
    inventory_status = filtered_df.groupby('category').agg({
        'inventory': 'sum',
        'sales': 'sum'
    }).reset_index()
    inventory_status['inventory_cover_days'] = inventory_status['inventory'] / (inventory_status['sales'] / 30)
    
    fig_inventory = px.bar(
        inventory_status,
        x='category',
        y='inventory_cover_days',
        title='Inventory Coverage (Days)',
        labels={'category': 'Category', 'inventory_cover_days': 'Days of Inventory'},
        color='inventory_cover_days',
        color_continuous_scale='RdBu'
    )
    fig_inventory.update_layout(height=350)
    st.plotly_chart(fig_inventory, use_container_width=True)

with col2:
    st.subheader("🔄 Returns by Category")
    
    returns_by_category = filtered_df.groupby('category').agg({
        'returns': 'sum',
        'sales': 'sum'
    }).reset_index()
    returns_by_category['return_rate'] = (returns_by_category['returns'] / returns_by_category['sales'] * 100)
    
    fig_returns = px.bar(
        returns_by_category,
        x='category',
        y='return_rate',
        title='Return Rate by Category (%)',
        labels={'category': 'Category', 'return_rate': 'Return Rate (%)'},
        color='return_rate',
        color_continuous_scale='Reds'
    )
    fig_returns.update_layout(height=350)
    st.plotly_chart(fig_returns, use_container_width=True)

# ============================================
# ROW 4: Business Insights
# ============================================

st.markdown("---")
st.subheader("💡 Business Insights")

col1, col2, col3 = st.columns(3)

with col1:
    # Top category
    top_category = filtered_df.groupby('category')['revenue'].sum().idxmax()
    top_revenue = filtered_df.groupby('category')['revenue'].sum().max()
    top_profit = filtered_df.groupby('category')['profit'].sum().max()
    
    st.info(
        f"**🏆 Top Category**\n\n"
        f"**{top_category}** leads with **${top_revenue:,.0f}** in revenue.\n\n"
        f"Profit: **${top_profit:,.0f}**\n\n"
        f"Consider increasing inventory and marketing for this category."
    )

with col2:
    # Best store
    best_store = filtered_df.groupby('store')['revenue'].sum().idxmax()
    best_revenue = filtered_df.groupby('store')['revenue'].sum().max()
    best_profit = filtered_df.groupby('store')['profit'].sum().max()
    
    st.success(
        f"**🏪 Best Store**\n\n"
        f"**{best_store}** generates **${best_revenue:,.0f}** in revenue.\n\n"
        f"Profit: **${best_profit:,.0f}**\n\n"
        f"Analyze what makes this store successful and replicate."
    )

with col3:
    # Opportunity
    total_sales_all = filtered_df['sales'].sum()
    avg_daily = filtered_df.groupby('date')['sales'].sum().mean()
    top_category_sales = filtered_df[filtered_df['category'] == top_category]['sales'].sum()
    
    st.warning(
        f"**📈 Growth Opportunity**\n\n"
        f"Current average daily sales: **{avg_daily:.0f}** units.\n\n"
        f"Increasing sales by 10% could generate:\n"
        f"💰 **${total_sales_all * 0.1 * 50:,.0f}** in additional revenue\n\n"
        f"Focus on **{top_category}** for best results."
    )

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown(
    f"""
    <div style='text-align: center; color: gray;'>
        <p>📊 Retail Analytics Dashboard | Built with Streamlit</p>
        <p>Data refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    """,
    unsafe_allow_html=True
)
