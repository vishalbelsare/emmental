import numpy as np
from scipy.stats import spearmanr


def spearman_correlation_scorer(gold, probs, preds):
    """Spearman rank-order correlation coefficient and the p-value.

    :param gold: Ground truth (correct) target values.
    :type gold: 1-d np.array
    :param probs: Predicted target probabilities.
    :type probs: 1-d np.array
    :param preds: Predicted target values.
    :type preds: 1-d np.array
    :return: Spearman rank-order correlation coefficient and the p-value
    :rtype: dict
    """

    correlation, pvalue = spearmanr(gold, preds)
    if np.isnan(correlation):
        correlation = 0.0
    return {"spearman_correlation": correlation, "spearman_pvalue": pvalue}
