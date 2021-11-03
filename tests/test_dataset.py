import os
import sys
import random
import unittest
from pathlib import Path

import torch
import torchvision

import cranet
from src import cravision

import torch
import torchvision

from .utils import show_example, teq


class TestVision(unittest.TestCase):
    def test_svhn(self):
        print()
        HOME = Path.home()
        DATA_DIR = HOME / "Downloads" / "dataset"
        cradataset = cravision.datasets.SVHN(root=DATA_DIR, transform=cravision.transforms.ToTensor())
        torchdataset = torchvision.datasets.SVHN(root=DATA_DIR, transform=torchvision.transforms.ToTensor())

        test_nums = 1000
        i = 0
        for tdata, cdata in zip(torchdataset, cradataset):
            if i >= test_nums:
                break

            i += 1
            torimg, _ = tdata
            cimg, clabel = cdata
            self.assertTrue(teq(torimg, cimg, 1e-7), f"torch:{torimg.detach().numpy()}\n\ncranet:{cimg.detach().numpy()}")

        # print(cimg.shape, clabel)
        # show_example(*cradataset[0])
        # print(len(cradataset))


if __name__ == '__main__':
    sys.path.append(os.getcwd())
    unittest.main()
