import numpy as np


def precision_scorer(gold, probs, preds, pos_label=1):
    """Precision.

    :param gold: Ground truth (correct) target values.
    :type gold: 1-d np.array
    :param probs: Predicted target probabilities.
    :type probs: 1-d np.array
    :param preds: Predicted target values.
    :type preds: 1-d np.array
    :return: Precision.
    :rtype: dict
    """

    pred_pos = np.where(preds == pos_label, True, False)
    gt_pos = np.where(gold == pos_label, True, False)
    TP = np.sum(pred_pos * gt_pos)
    FP = np.sum(pred_pos * np.logical_not(gt_pos))

    precision = TP / (TP + FP) if TP + FP > 0 else 0.0

    return {"precision": precision}
