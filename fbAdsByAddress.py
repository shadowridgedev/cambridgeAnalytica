from facebookads.adobjects.adset import AdSet

adset = AdSet(parent_id='act_<AD_ACCOUNT_ID>')
adset.update({
    AdSet.Field.name: 'My AdSet',
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 150,
    AdSet.Field.daily_budget: 2000,
    AdSet.Field.campaign_id: <CAMPAIGN_ID>,
    AdSet.Field.targeting: {
        'geo_locations': {
            'custom_locations': [
                {
                    'custom_type': 'multi_city',
                    'min_population': 500000,
                    'max_population': 1000000,
                    'country': 'BR',
                },
                {
                    'custom_type': 'multi_city',
                    'country_group': 'Europe',
                },
            ],
            'location_types': ['recent', 'home'],
        },
    },
})
adset.remote_create(params={
    'status': AdSet.Status.active,
})