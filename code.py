from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

def get_google_trends(keywords, timeframe='today 12-m', geo='US', cat=0):
    """
    Fetch and visualize Google Trends data for given keywords.
    
    Args:
    keywords (list): List of keywords to compare (e.g., ['python', 'java']).
    timeframe (str): Timeframe for trends (e.g., 'today 12-m', 'past 5 years').
    geo (str): Country code (e.g., 'US' for United States).
    cat (int): Category ID (0 for all categories).
    
    Returns:
    dict: {'interest_over_time': df, 'plot': fig}
    """
    # Initialize pytrends
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Build payload and fetch data
    pytrends.build_payload(keywords, cat=cat, timeframe=timeframe, geo=geo)
    interest_over_time = pytrends.interest_over_time()
    
    # Plot the trends
    if not interest_over_time.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        interest_over_time.plot(ax=ax)
        ax.set_title(f'Google Trends: {keywords}')
        ax.set_ylabel('Interest')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    return {'interest_over_time': interest_over_time, 'plot': fig}

# Example usage
if __name__ == "__main__":
    keywords = ['python', 'javascript']  # Replace with your keywords
    trends_data = get_google_trends(keywords)
    print("Interest Over Time:")
    print(trends_data['interest_over_time'].head())