import requests
import streamlit as st
import pint
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def main():
    
    st.set_page_config(page_title="SSE-UnitConvertPro", page_icon="💲", layout="wide")
    st.subheader("Welcome to :wave:-")
    st.title("📐SSE-UnitConvertPro - Currency Version")

    unit_format = {
        "Default": "D",
        "Short default": "~D",
        "Pretty": "P",
        "Short pretty": "~P",
        "Compact": "C",
        "Short compact": "~C" 
    }
    
    with st.sidebar:
        temp = st.sidebar.title("Navigation")
        
        page_selection = st.sidebar.radio("Go to: ", ("Home", "About", "Contact"))
        
        if page_selection == "Home":
            st.subheader("[Main SSE-UnitconvertPro site](app.py)")
        
        elif page_selection == "About":
            st.markdown("[About Us](#about)")
            
        elif page_selection == "Contact":
            st.markdown("[About Us](#Contact)") 
        
        st.write("##")
        st.write("##")
        st.write("##")
        
        st.header("Settings")
        fmt = st.radio("Output style", unit_format.keys(), index=2)
    
    class Currency_converter:
        rates = {}
        
        def __init__(self, url):
            data = requests.get(url).json()
            self.rates = data["rates"]

        def convert(self, from_currency, to_currency, amount):
            if from_currency != 'EUR':
                amount = amount / self.rates[from_currency]
                
            amount = round(amount * self.rates[to_currency], 2)
            return '{} {} = {} {}'.format(amount, from_currency, round(amount,2), to_currency)
    
    url = ('http://data.fixer.io/api/latest?access_key=590b7ed2e9ed359a5d9583502810da8e')
    c = Currency_converter(url)
    
    #from_country = input("From Country: ")
    #to_country = input("To Country: ")
    #amount = init(input("Amount: "))
    #result = c.convert(from_country, to_country, amount)
       
    st.write("---")
    
    
    
    with st.container():
        st.markdown("""
        ## CURRENCY Conversion

        ### Instructions
        Enter the amount and the source currency on the left, and the target currency on the right.
        Example: "50 USD to EUR"
        """)

        left_column, right_column = st.columns((1, 2))

        with left_column:
            st.subheader("Input")
            user_input = st.text_input("Enter amount and source currency (e.g., '50 USD')", value="50 USD")

        with right_column:
            st.subheader("Output")
            
            
            try:
                amount, source_currency = user_input.split(" ")
                target_currency = st.text_input("Enter target currency", value="EUR")
                
                
                conversion_rate = 0.85  # 1 USD to EUR
                
                converted_amount = float(amount) * conversion_rate
                st.markdown(f"{converted_amount:0.2f}{unit_format[fmt]} {target_currency}")
            except ValueError:
                st.warning("Invalid input. Please use the format 'amount source_currency to target_currency'.")
    
    
    st.write("---")
    
    
    st.write("##")
     
    
    st.write("##")
    st.write("##")
    st.markdown("This is some random text ")

    
    st.write("---")
    left_Tcolumn, right_Tcolumn = st.columns([1,3])
    with left_Tcolumn:
        st.subheader("Liked our work?🏋️" )
        st.markdown("<a name='contact'></a>", unsafe_allow_html=True)
        st.write("[Check out our Team 👈 ](https:youtube.com)")
    
    with right_Tcolumn:
        
        st.subheader("About Us" )
        st.write("##")
        st.markdown("""We are a TEAM👌 of typical witty minded misfit developers, 
                          coming up with ways to make doing complex tasks simpler.""")
        

if __name__ == "__main__":
    main()
    
    
    
    
