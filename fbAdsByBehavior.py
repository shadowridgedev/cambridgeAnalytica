
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My AdSet',
  'optimization_goal': 'REACH',
  'billing_event': 'IMPRESSIONS',
  'bid_amount': '2',
  'daily_budget': '1000',
  'campaign_id': '<adCampaignConversionsID>',
  'targeting': {
  	'geo_locations':{'countries':['US']},
  	'behaviors':[
  		{'id':6007101597783,'name':'Business Travelers'},
  		{'id':6004386044572,'name':'Android Owners (All)'}
  	]},
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)

