# Sorting Algorithm

## Selection Sort

『找到數列中最小值，丟到最左邊』，重複此動作在『未排序的部分』。

```python
def SelectionSort(list_of_elements):
  list_len = len(list_of_elements)
  
  for i in range(list_len-1):
    min_index = i
    #find minimum element
    for j in range(i+1, list_len):
      if list_of_elements[min_index] > list_of_elements[j]:
        min_index = j
    #sort
    list_of_elements[min_index], list_of_elements[i] = list_of_elements[i], list_of_elements[min_index]
  
  return list_of_elements
```

延伸討論：時間複雜度 (Big O)

有 $n$ 個元素，第 $1$ 次需要從 $n$ 個元素找 (步驟)，第 $2$ 次需要從 $n-1$ 個元素找，第 $n$ 次需要從最後 $1$ 個元素找。因此總共要進行 $n+(n-1)+...+1=\frac{n(n+1)}{2}$ 個步驟；而每次找到最小元素時都要進行一次位置交換的動作，因此有 $n$ 個步驟。

因此一共有 $\frac{n(n+1)}{2}+n=\frac{n^2+3n+1}{2} \sim n^2$ ，故稱此排序法的時間複雜度為 $O(n^2)$。





## Insertion Sort



## Merge Sort



