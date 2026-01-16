import pandas as pd 
import plotly.graph_objects as go

def generate_chart():
    df = pd.read_csv("system_monitor.csv")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["CPU Usage"], name="CPU Usage"))
    fig.add_trace(go.Scatter(x=df["Timestamp"], y=df["Memory Usage"], name="Memory Usage"))
    fig.update_layout(title="System Monitor", xaxis_title="Timestamp", yaxis_title="Usage")
    fig.write_html('dashboard.html')
    print("Dashboard updated")

if __name__ == "__main__":
    generate_chart()