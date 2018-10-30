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
            'countries': ['US'],
        },
        'interests': [
            {
                'id': 6003139266461,
                'name': 'Movies',
            },
            {
                'id': 6003397425735,
                'name': 'Tennis',
            },
            {
                'id': 6003659420716,
                'name': 'Cooking',
            },
        ],
    },
})
adset.remote_create(params={
    'status': AdSet.Status.active,
})