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
            'regions': [{'key': '3847'}],
            'cities': [
                {
                    'key': '2430536',
                    'radius': '12',
                    'distance_unit': 'mile',
                },
            ],
        },
        'genders': [1],
        'relationship_statuses': [2, 3, 4],
        'age_min': 18,
        'age_max': 43,
        'interests': [
            {
                'id': 6003139266461,
                'name': 'Movies',
            },
        ],
    },
})
adset.remote_create(params={
    'status': AdSet.Status.active,
})