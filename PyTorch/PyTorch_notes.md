# PyTorch Notes

## Built-in Datasets

More information on [PyTorch Datasets](https://pytorch.org/vision/stable/datasets.html) .

### Images

- `torchvision.datasets.MNIST()`
- `torchvision.datasets.CIFAR10()`

### Text

- `torchtext.datasets.IMDB()`



## Ways of Loading Data

### Images in Class Folders

```
 root
├── orange
│   ├── orange_image1.png
│   └── orange_image1.png
├── apple
│   └── apple_image1.png
│   └── apple_image2.png
│   └── apple_image3.png
```

```python
torchvision.datasets.ImageFolder(root, transform)
```

