import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
# Read data form file big_mac_file and define a DataFrame
    df = pd.read_csv(big_mac_file) 
    country_code_in = country_code.upper()
    query = (f"iso_a3 == '{country_code_in}'and date >='{year}-01-01'and date < '{year}-12-31'")
    year_country_df = df.query(query)
    result = round(year_country_df['dollar_price'].mean(),2)
    return result    

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    country_code = country_code.upper()
    query = (f"iso_a3 == '{country_code}' and name")
    country_df = df.query(query)
    result = round(country_df['dollar_price'].mean(),2)
    return result 

def get_the_cheapest_big_mac_price_by_year(year): 
    df = pd.read_csv(big_mac_file)
    query = (f"date > '{year}-01-01' and date < '{year}-12-31'")
    message_df = df.query(query)
    message = round(message_df['dollar_price'].min(),2)
    min_num = message_df['dollar_price'].idxmin()
    min_row = message_df.loc[min_num]
    temp_row = f"{min_row['name']}({min_row['iso_a3']}):${round(min_row['dollar_price'],2)}"
    return temp_row
       
def get_the_most_expensive_big_mac_price_by_year(year):
  df = pd.read_csv(big_mac_file)
  query = (f"date > '{year}-01-01' and date < '{year}-12-31'")
  message_df = df.query(query)
  message = round(message_df['dollar_price'].max(),2)
  max_num = message_df['dollar_price'].idxmax()
  max_row = message_df.loc[max_num]
  temp_row = f"{max_row['name']}({max_row['iso_a3']}):${round(max_row['dollar_price'],2)}"
  return temp_row

# call the main function
if __name__ == "__main__":
    print(get_big_mac_price_by_year("2015","SAU"))
    print(get_big_mac_price_by_country("SAU"))
    print(get_the_cheapest_big_mac_price_by_year("2015"))
    print(get_the_most_expensive_big_mac_price_by_year ("2015"))