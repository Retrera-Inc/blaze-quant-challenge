"""
Copy this file and add your business logic for the predictions. Add your file in
the format: predictions_<team_lead_name>.py
"""

from instructions import ETHPriceRanges


def predictions():
    """
    All of the business logic should go here. The output should be a list
    of size 7 with values from ETHPriceRanges
    """
    return [
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
        ETHPriceRanges.pr_2300_2325,
    ]


"""
DO NOT REMOVE
"""
preds = predictions()
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
