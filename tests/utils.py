import numpy as np
import matplotlib.pyplot as plt


def np_feq(a: np.ndarray, b: np.ndarray, epsilon: float = 1e-15) -> bool:
    return (np.abs(a - b) < epsilon).all()


def teq(a, b, eps=1e-15) -> bool:
    return np_feq(a.detach().numpy(), b.detach().numpy(), eps)


def show_example(img, label) -> None:
    print(f"Label: {label}, Shape: {img.shape}")
    plt.imshow(img.permute((1, 2, 0)))
