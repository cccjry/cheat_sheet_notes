# Sorting Algorithm

## Selection Sort

『找到數列中最小值，丟到最左邊』，重複此動作在『未排序的部分』直到所有元素都被檢查過。

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

因此一共有 $\frac{n(n+1)}{2}+n=\frac{n^2+3n}{2}$ 個步驟，而當 $n$ 夠大時， $\frac{n^2+3n}{2} \sim n^2$ ，故稱此排序法的時間複雜度為 $O(n^2)$。





## Insertion Sort

從數列中的第二個元素開始，往前 (左邊) 依序比較，找到其符合大小排序的位置，重複此動作直到所有元素都被檢查過。

```python
def InsertionSort(list_of_elements):
    list_len = len(list_of_elements)
    
    #start from second element
    for i in range(1, list_len):
        element_index = i
        
        while element_index > 0 and list_of_elements[element_index-1] > list_of_elements[element_index]:
            list_of_elements[element_index], list_of_elements[element_index-1] = list_of_elements[element_index-1], list_of_elements[element_index]
            element_index -= 1
	
    return list_of_elements
```

延伸討論：時間複雜度 (Big O)

因為有非常順利的情況，也有最糟糕的情況，通常討論 ***時間複雜度會透過最糟糕的情況進行討論***。

> 最糟糕的狀況：整個數列呈現由大到小排序
>

因此從第 $2$ 個元素開始，第 $2$ 個元素需要往前比較並移動 $1$ 次，第 $3$ 個元素需要往前比較並移動 $2$ 次，第 $n$ 個元素需要往前比較並移動 $n-1$ 次。因此總共要進行 $1+2+...+(n-1)=\frac{n(n+1)}{2}-n$ 個步驟，而當 $n$ 夠大時， $\frac{n(n+1)}{2}-n=\frac{n^2-n}{2} \sim n^2$ ，故此排序法時間複雜度同樣為 $O(n^2)$。



## Merge Sort



## Continuous Reading

- [十大經典演算法](https://github.com/hustcc/JS-Sorting-Algorithm)
