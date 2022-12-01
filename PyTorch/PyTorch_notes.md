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

### `DataLoader` class in PyTorch that helps us to load and iterate over elements in a dataset.

```python
from torch.utils.data import DataLoader

DataLoader(
    dataset,
    batch_size=1,
    shuffle=False,
    num_workers=0,
    collate_fn=None,
    pin_memory=False,
 )
```

- `dataset`
- `batch_size=1`
- `shuffle=False` 是否將資料集打散到 batch 當中，非按照資料原本順序。
- `num_workers=0`
- `collate_fn=None` 合併資料 (還沒用過)
- `pin_memory=False` 有 CUDA 可以直接將 Tensors 放到記憶體上面運算直到結束。



## Load the Data onto Device

- Having CUDA:

    ```python
    "cuda" if torch.cuda.is_available() else "cpu"
    ```

    ```python
    device = "cuda" if torch.cuda.is_available() else "cpu"
    kwargs = {'num_workers': 1, 'pin_memory': True} if device=='cuda' else {}
    
    train_loader = torch.utils.data.DataLoader(
                        torchvision.datasets.MNIST('/files/', 
                                                   train=True, 
                                                   download=True),
        				batch_size=batch_size_train, **kwargs)
    ```

    

- Having Mac with Apple Silicon Chip:

    ```python
    "mps" if torch.backends.mps.is_available() else "cpu"
    ```

- Others (only CPU):

    ```python
    "cpu"
    ```



