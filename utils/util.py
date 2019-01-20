import torch


def save_checkpoint(state, filename):
    """
    Save state to filename
    :param state:
    :param filename:
    :return:
    """
    print("=> Saving checkpoint...")
    torch.save(state, filename)
