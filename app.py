# # Author: Oluwafemi Olasegiri
# # Organization: CareerOnDemand
# # this class handle the Wasted Spend Calculator
# # It model the data according to the give data
# # It allows to process data after the order of the style of the WatedSpendCalculator excel sheet

import streamlit as st

data = {
    'monthly_traffic':10000.0,
    'cpa':150.0,
    'sales_conversion_rate':2.0,
    'aovp':300.0,
    'pixel_match_rate':45.0,
    'data_cleaning':70.0,
    'platform_match_rate':90.0
}
sd = st.sidebar
sd.header("Fundamental Dataset")
sd.divider()
# x = my_cal()

monthly_traffic = sd.number_input("Enter Monthly Traffic", min_value=1.0, step=1.0, key="monthly_traffic", value=data['monthly_traffic'])
data['monthly_traffic'] = monthly_traffic

cpa = sd.number_input("CPA:", min_value=1.0, key="cpa", value=data['cpa'])
data['cpa'] = cpa

sales_conversion_rate = sd.number_input("Sales Conversion Rate:", min_value=1.0, key="sales_conversion_rate", value=data['sales_conversion_rate'])
data['sales_conversion_rate'] = sales_conversion_rate

aovp = sd.number_input("AOV/Price:", min_value=1.0, key="aovp", value=data["aovp"]) 
data['aovp'] = aovp

pixel_match_rate = sd.slider("Pixel Match Rate %", min_value=0.0, max_value=100.0, step=1.0, key="pixel_match_rate", value=data['pixel_match_rate'])
data['pixel_match_rate'] = pixel_match_rate

data_cleaning = sd.slider("Data Cleaning %", min_value=0.0, max_value=100.0, step=1.0, key="data_cleaning", value=data['data_cleaning'])
data['data_cleaning'] = data_cleaning

platform_match_rate = sd.slider("Platform Match Rate %", min_value=0.0, max_value=100.0, step=1.0, key="platform_match_rate", value=data['platform_match_rate'])
data['platform_match_rate'] = platform_match_rate

def my_cal(data):
    solve_data1 = {
        'sales_per_units':data['sales_conversion_rate'] * data['monthly_traffic'],
        'lost_traffic_total':data['monthly_traffic'] - (data['monthly_traffic'] * data['sales_conversion_rate']),
        'profiles_fb_per_google_pixel_captured':data['monthly_traffic'] * 15/100,
    }

    solve_data2 = {
        'estimated_spend':data['cpa'] * solve_data1['sales_per_units'],
        'revenue':data['aovp'] * solve_data1['sales_per_units'],
        'matched_visitors': data['pixel_match_rate']/100 * solve_data1['lost_traffic_total']
    }

    solve_data3 = {
        'profit':solve_data2['estimated_spend'] * solve_data2['revenue'],
        'wasted_spend':solve_data2['estimated_spend'] * 75 / 100,
        'contactable_leads':data['data_cleaning'] * solve_data2['matched_visitors'],
        'targetable_per_pixeled_audience':data['platform_match_rate'] * solve_data2['matched_visitors']
    }
    return {
        'sales_per_units':solve_data1['sales_per_units'],
        'lost_traffic_total':solve_data1['lost_traffic_total'],
        'profiles_fb_per_google_pixel_captured':solve_data1['profiles_fb_per_google_pixel_captured'],
        'estimated_spend':solve_data2['estimated_spend'],
        'revenue':solve_data2['revenue'],
        'matched_visitors':solve_data2['matched_visitors'],
        'profit':solve_data3['profit'],
        'wasted_spend':solve_data3['wasted_spend'],
        'contactable_leads':solve_data3['contactable_leads'],
        'targetable_per_pixeled_audience':solve_data3['targetable_per_pixeled_audience']
    }

def view(data=my_cal(data)):
    col1, col2, col3 = st.columns(3)  # Create three columns

    with col1:
        # monthly_traffic = sd.number_input("Monthly Traffic", min_value=1, step=1, key="monthly_traffic")
        st.write('lost traffic total: ')
        st.write(data['lost_traffic_total'])

    with col2:
        st.write('Profiles FB Per Google Pixel Captured: ')
        st.write(data['profiles_fb_per_google_pixel_captured'])

    with col3:
        st.write('Sales Per Units: ')
        st.write(data['sales_per_units'])

    with col1:
        st.write('Estimated Spend: ')
        st.write(data['estimated_spend'])

    with col2:
        st.write('Revenue')
        st.write(data['revenue'])

    with col3:
        st.write('Matched Visitors')
        st.write(data['matched_visitors'])

    with col1:
        st.write('Profit: ')
        st.write(data['profit'])

    with col2:
        st.write('Wasted Spend: ')
        st.write(data['wasted_spend'])

    with col3:
        st.write('Contactable Leads: ')
        st.write(data['contactable_leads'])

    with col1:
        st.write('Targetable Per Pixeled Audience: ')
        st.write(data['targetable_per_pixeled_audience'])

    return

def calculate_lost_traffic_total():
    pass
    

# start interface
st.header("Sales Pipeline Forecast")
st.write("Wasted Spend Calculator")
input1 = st.text_input("Lost Traffic Total", disabled=True)

btn2 = st.button("Lost Traffic Total", key="lost_traffic_total", type="primary")
if btn2:
    view()

st.write(my_cal(data))
col1, col2, col3 = st.columns(3)  # Create three columns

# with col1:
#     # monthly_traffic = sd.number_input("Monthly Traffic", min_value=1, step=1, key="monthly_traffic")
#     st.write('lost traffic total: '+data[])

# with col2:
#     # cpa = sd.number_input("CPA", min_value=1, key="cpa")
#     st.write('profiles_fb_per_google_pixel_captured: '+solve_data1['profiles_fb_per_google_pixel_captured'])

# with col3:
#     # sales_conversion_rate = sd.number_input("Sales Conversion Rate", min_value=1, key="sales_conversion_rate")
#     # data['sales_conversion_rate'] = sales_conversion_rate
#     st.write('lost traffic total: '+solve_data1['profiles_fb_per_google_pixel_captured'])

# with col1:
#     # aovp = sd.number_input("AOV/Price", min_value=1, key="aovp")
#     # data['aovp'] = aovp
#     st.write('lost traffic total: '+solve_data1['profiles_fb_per_google_pixel_captured'])

# with col2:
#     # pixel_match_rate = sd.slider("Pixel Match Rate %", min_value=0, max_value=100, step=1, key="pixel_match_rate", value=45)
#     # data['pixel_match_rate'] = pixel_match_rate
#     st.write('lost traffic total: '+solve_data1['profiles_fb_per_google_pixel_captured'])

# with col3:
#     # data_cleaning = sd.slider("Data Cleaning %", min_value=0, max_value=100, step=1, key="data_cleaning", value=70)
#     # data['data_cleaning'] = data_cleaning
#     st.write('lost traffic total: '+solve_data1['profiles_fb_per_google_pixel_captured'])

# with col1:
#     # platform_match_rate = sd.slider("Platform Match Rate %", min_value=0, max_value=100, step=1, key="platform_match_rate", value=90)
#     # data['platform_match_rate'] = platform_match_rate
#     st.write('lost traffic total: '+solve_data1['profiles_fb_per_google_pixel_captured'])