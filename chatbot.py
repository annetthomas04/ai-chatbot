import pandas as pd
df = pd.read_csv('genai.csv')

def simple_chatbot(user_query, company_name):
    # Normalize the user query (lowercase and strip extra spaces and punctuation)
    user_query = user_query.lower().strip().replace("?", "")
    company_name = company_name.lower().strip()

    # Filter data for the specified company
    company_data = df[df['Company'].str.lower().str.strip() == company_name]

    if company_data.empty:
        return f"Sorry, I don't have data for {company_name.title()}."

    latest_data = company_data.iloc[-1]  # Get the most recent row of data for the company
    prev_data = company_data.iloc[-2]    # Get the second last row (previous year's data)

    # "What is the total revenue?" query
    if user_query == "what is the total revenue":
        total_revenue = latest_data['Total Revenue']
        return f"The total revenue for {company_name.title()} is {total_revenue}."

    # "How has net income changed over the last year?" query
    elif user_query == "how has net income changed over the last year":
        net_income_change = latest_data['Net Income'] - prev_data['Net Income']
        change_type = "increased" if net_income_change > 0 else "decreased"
        return f"The net income for {company_name.title()} has {change_type} by {abs(net_income_change)} over the last year."
    
    # "What is the asset to liability ratio for [Company]?" query
    elif user_query == "what is the asset to liability ratio":
        assets = latest_data['Total Assets']
        liabilities = latest_data['Total Liabilities']
        if liabilities != 0:
            asset_to_liability_ratio = assets / liabilities
            return f"The asset to liability ratio for {company_name.title()} is {asset_to_liability_ratio:.2f}."
        else:
            return f"The liabilities for {company_name.title()} are zero, so the asset to liability ratio is undefined."

    # Add more conditions for other predefined queries
    else:
        return "Sorry, I can only provide information on predefined queries."

while True:
    user_query = input("Ask me a financial question (or type 'exit' to quit): ")
    
    if user_query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    company_name = input("For which company (e.g., Microsoft, Tesla, Apple)?: ")
    
    response = simple_chatbot(user_query, company_name)
    print(response)