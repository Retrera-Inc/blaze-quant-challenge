"""
Copy this file and add your business logic for the predictions. Add your file in
the format: predictions_<team_lead_name>.py
"""

from instructions import ETHPriceRanges, ARBPriceRanges, LINKPriceRanges


def predictions_ETH():
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


def predictions_ARB():
    """
    All of the business logic should go here. The output should be a list
    of size 7 with values from ARBPriceRanges
    """
    return [
        ARBPriceRanges.pr_180_185,
        ARBPriceRanges.pr_180_185,
        ARBPriceRanges.pr_180_185,
        ARBPriceRanges.pr_180_185,
        ARBPriceRanges.pr_180_185,
        ARBPriceRanges.pr_180_185,
        ARBPriceRanges.pr_180_185,
    ]


def predictions_LINK():
    """
    All of the business logic should go here. The output should be a list
    of size 7 with values from LINKPriceRanges
    """
    return [
        LINKPriceRanges.pr_1875_1900,
        LINKPriceRanges.pr_1875_1900,
        LINKPriceRanges.pr_1875_1900,
        LINKPriceRanges.pr_1875_1900,
        LINKPriceRanges.pr_1875_1900,
        LINKPriceRanges.pr_1875_1900,
        LINKPriceRanges.pr_1875_1900,
    ]


"""
DO NOT REMOVE
"""
preds_ETH = predictions_ETH()
assert len(preds_ETH) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds_ETH])

preds_ARB = predictions_ARB()
assert len(preds_ARB) == 7
assert all([isinstance(val, ARBPriceRanges) for val in preds_ARB])

preds_LINK = predictions_LINK()
assert len(preds_LINK) == 7
assert all([isinstance(val, LINKPriceRanges) for val in preds_LINK])
