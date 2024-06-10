import random

from website_scrapers.DataRelevanceInterface import DataRelevanceInterface


class GrantDotGovRelevanceEvaluator(DataRelevanceInterface):

    def rankData(self, data, contextData):

        #TODO need to ask shayla for how she sees if a form is good or bad
        return random.random()