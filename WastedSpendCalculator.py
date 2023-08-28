# # Author: Oluwafemi Olasegiri
# # Organization: CareerOnDemand
# # this class handle the Wasted Spend Calculator
# # It model the data according to the give data
# # It allows to process data after the order of the style of the WatedSpendCalculator excel sheet

# depreciated class
class WastedSpendCalculator:
    def __init__(self, monthly_traffic=10000.0, cpa=150.0, sales_conversion_rate=2.0, sales_per_units=None, estimated_spend=None, aov_price=300.0, 
                 revenue=None, profit=None, wasted_spend=None, lost_traffic_total=None, profiles_fb_google_pixel_captured=None, 
                 pixel_match_rate=45.0, matched_visitors=None, data_cleaning=70.0, contactable_leads=None, platform_match_rate=90.0, 
                 targetable_pixel_audience=None
                 ):
    
        self.monthly_traffic = monthly_traffic
        self.cpa = cpa
        self.sales_conversion_rate = sales_conversion_rate/100
        self.sales_per_units = sales_per_units if sales_per_units is not None else self.get_sales_per_units()
        self.estimated_spend = estimated_spend if estimated_spend is not None else self.get_estimated_spend()
        self.aov_price = aov_price
        self.revenue = revenue if revenue is not None else self.get_revenue()
        self.profit = profit if profit is not None else self.get_profit()
        self.wasted_spend = wasted_spend if wasted_spend is not None else self.get_wasted_spend() 
        self.lost_traffic_total = lost_traffic_total if lost_traffic_total is not None else self.get_lost_traffic_total()
        self.profiles_fb_google_pixel_captured = profiles_fb_google_pixel_captured if profiles_fb_google_pixel_captured is not None else self.get_profiles_fb_google_pixel_captured()
        self.pixel_match_rate = pixel_match_rate / 100
        self.matched_visitors = matched_visitors if matched_visitors is not None else self.get_matched_visitors()
        self.data_cleaning = data_cleaning/100
        self.contactable_leads = contactable_leads if contactable_leads is not None else self.get_contactable_leads()
        self.platform_match_rate = platform_match_rate/100
        self.targetable_pixel_audience = targetable_pixel_audience if targetable_pixel_audience is not None else self.get_targetable_pixel_audience()

        
    def get_sales_per_units(self):
        return self.monthly_traffic * self.sales_conversion_rate

    def get_estimated_spend(self):
        return self.cpa * self.sales_per_units

    def get_revenue(self):
        return self.aov_price * self.sales_per_units

    def get_profit(self):
        return self.revenue - self.estimated_spend

    def get_wasted_spend(self):
        return self.estimated_spend * 75 / 100

    def get_lost_traffic_total(self):
        return self.monthly_traffic - (self.monthly_traffic * self.sales_conversion_rate)

    def get_profiles_fb_google_pixel_captured(self):
        return self.monthly_traffic * 15 / 100

    def get_matched_visitors(self):
        return self.pixel_match_rate * self.lost_traffic_total

    def get_contactable_leads(self):
        return self.matched_visitors * self.data_cleaning

    def get_targetable_pixel_audience(self):
        return self.matched_visitors * self.platform_match_rate


# Example usage:
# wsc = WastedSpendCalculator()
# print(wsc.lost_traffic_total)
