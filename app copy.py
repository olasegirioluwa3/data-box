# Author: Oluwafemi Olasegiri
# Organization: CareerOnDemand
# this class handle the Wasted Spend Calculator
# It model the data according to the give data
# It allows to process data after the order of the style of the WatedSpendCalculator excel sheet

import streamlit as st
import math
import pandas as pd

data = {
    'monthly_traffic':10000.0,
    'cpa':150.0,
    'sales_conversion_rate':2.0,
    'aovp':300.0,
    'pixel_match_rate':45.0,
    'data_cleaning':70.0,
    'platform_match_rate':90.0
}

alp_data = {
    'alp_your_plan':2500.0,
    'alp_avg_plan_ref':2500.0,
    'alp_ref_payout':10.0,
    'alp_sales_conversion_rate':40.0,
    'alp_response_rate':60.0
}


excel_file = pd.ExcelFile("data/Sales_PipeLine_Forecast_Model_2023.xlsx")

# Get the list of sheet names
sheet_names = excel_file.sheet_names
for sheet_name in sheet_names:
    print(sheet_name)
    sheet_name = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx", sheet_name="Affiliate Program")


sp_df = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx", sheet_name="SuperPixel")
wsc_df = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx", sheet_name="Wasted Spend Calculator")
ab_df = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx", sheet_name="Audience Builder")
ap_df = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx", sheet_name="Affiliate Program")

sp_df.head()
wsc_df.head()
ab_df.head()
ap_df.head()

ap_df.set_index("AudienceLab Partners", inplace=True)


ap_df.columns = ap_df.columns.str.replace(' ', '_')

# Rename cell values to remove spaces
for column in ap_df.columns:
    ap_df[column] = ap_df[column].apply(lambda x: str(x).replace(' ', '_'))
    print(ap_df)



for label, index in sheet_name['AudienceLab Partners'].count:
    sheet_name['AudienceLab Partners'][index] = sheet_name['AudienceLab Partners'][index].replace(' ', '_')


sd = st.sidebar
sd.header("Fundamental Dataset")
sd.divider()


collapse1 = sd.expander("Wasted Spend Calculator", expanded=False)
collapse_alp = sd.expander("AudienceLab Partner", expanded=False)

# collapse1 Wasted Spend Calculator
monthly_traffic = collapse1.number_input("Enter Monthly Traffic", min_value=1.0, step=1.0, key="monthly_traffic", value=data['monthly_traffic'])
data['monthly_traffic'] = monthly_traffic

cpa = collapse1.number_input("CPA:", min_value=1.0, key="cpa", value=data['cpa'])
data['cpa'] = cpa

sales_conversion_rate = collapse1.number_input("Sales Conversion Rate:", min_value=1.0, key="sales_conversion_rate", value=data['sales_conversion_rate'])
data['sales_conversion_rate'] = sales_conversion_rate

aovp = collapse1.number_input("AOV/Price:", min_value=1.0, key="aovp", value=data["aovp"]) 
data['aovp'] = aovp

pixel_match_rate = collapse1.slider("Pixel Match Rate %", min_value=0.0, max_value=100.0, step=1.0, key="pixel_match_rate", value=data['pixel_match_rate'])
data['pixel_match_rate'] = pixel_match_rate

data_cleaning = collapse1.slider("Data Cleaning %", min_value=0.0, max_value=100.0, step=1.0, key="data_cleaning", value=data['data_cleaning'])
data['data_cleaning'] = data_cleaning

platform_match_rate = collapse1.slider("Platform Match Rate %", min_value=0.0, max_value=100.0, step=1.0, key="platform_match_rate", value=data['platform_match_rate'])
data['platform_match_rate'] = platform_match_rate

btn2 = collapse1.button("Calculate Wasted Spend", key="lost_traffic_total", type="primary")

# collapse_alp AudienceLab Partner
alp_your_plan = collapse_alp.number_input("Your Plan $:", min_value=1.0, key="alp_your_plan", value=alp_data["alp_your_plan"]) 
alp_data['alp_your_plan'] = alp_your_plan

alp_avg_plan_ref = collapse_alp.number_input("Avg Plan Ref $:", min_value=1.0, key="alp_avg_plan_ref", value=alp_data["alp_avg_plan_ref"]) 
alp_data['alp_avg_plan_ref'] = alp_avg_plan_ref

alp_ref_payout = collapse_alp.slider("Ref Payout %", min_value=0.0, max_value=100.0, step=1.0, key="alp_ref_payout", value=alp_data['alp_ref_payout'])
alp_data['alp_ref_payout'] = alp_ref_payout

alp_sales_conversion_rate = collapse_alp.slider("Sales Conversion Rate:", min_value=0.0, max_value=100.0, step=1.0, key="alp_sales_conversion_rate", value=alp_data['alp_sales_conversion_rate'])
alp_data['alp_sales_conversion_rate'] = alp_sales_conversion_rate

alp_response_rate = collapse_alp.slider("Response Rate:", min_value=0.0, max_value=100.0, step=1.0, key="alp_response_rate", value=alp_data['alp_response_rate'])
alp_data['alp_response_rate'] = alp_response_rate

alp_btn = collapse_alp.button("Calculate AudienceLab Partner", key="alp_button", type="primary")

def my_cal(data):
    solve_data1 = {
        'sales_per_units':data['sales_conversion_rate'] /100 * data['monthly_traffic'],
        'lost_traffic_total':data['monthly_traffic'] - (data['monthly_traffic'] * data['sales_conversion_rate'] / 100),
        'profiles_fb_per_google_pixel_captured':data['monthly_traffic'] * 15 / 100,
    }

    solve_data2 = {
        'estimated_spend':data['cpa'] * solve_data1['sales_per_units'],
        'revenue':data['aovp'] * solve_data1['sales_per_units'],
        'matched_visitors': data['pixel_match_rate']/100 * solve_data1['lost_traffic_total']
    }

    solve_data3 = {
        'profit':solve_data2['revenue'] - solve_data2['estimated_spend'],
        'wasted_spend':solve_data2['estimated_spend'] * 75 / 100,
        'contactable_leads':data['data_cleaning'] / 100 * solve_data2['matched_visitors'],
        'targetable_per_pixeled_audience':data['platform_match_rate'] /100 * solve_data2['matched_visitors']
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

def alp_my_cal(alp_data):
    solve_data1 = {
        'payout':(alp_data['alp_ref_payout'] / 100) * alp_data['alp_avg_plan_ref']
    }

    solve_data2 = {
        'referrals_needed_to_be':alp_data['alp_your_plan'] / solve_data1['payout']
    }

    solve_data3 = {
        'conversations_needed':solve_data2['referrals_needed_to_be'] / (alp_data['alp_sales_conversion_rate']  / 100)
    }

    solve_data4 = {
        'touch_points_needed':solve_data3['conversations_needed'] / (alp_data['alp_response_rate'] / 100)
    }

    return {
        'payout':solve_data1['payout'],
        'referrals_needed_to_be':solve_data2['referrals_needed_to_be'],
        'conversations_needed':solve_data3['conversations_needed'],
        'touch_points_needed':solve_data4['touch_points_needed']
    }

def View(data=my_cal(data)):
    st.write("Wasted Spend Calculator")
    col1, col2, col3 = st.columns(3)  # Create three columns

    with col1:
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

def alpView(data=alp_my_cal(alp_data)):
    st.write("AudienceLab Partners")
    col1, col2, col3 = st.columns(3)  # Create three columns
    
    with col1:
        st.write('Payout: ')
        st.write(math.ceil(data['payout']))

    with col2:
        st.write('Referrals Needed To Be: ')
        st.write(math.ceil(data['referrals_needed_to_be']))

    with col3:
        st.write('Conversations Needed: ')
        st.write(math.ceil(data['conversations_needed']))

    with col1:
        st.write('Touch Points Needed: ')
        st.write(math.ceil(data['touch_points_needed']))

    return

    

# start interface
st.header("SALES PIPELINE FORECAST MODEL") 



if btn2:
    View()

if alp_btn:
    alpView()

col1, col2, col3 = st.columns(3)  # Create three columns