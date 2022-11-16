# Sorting Algorithm

## Selection Sort

> 『找到數列中最小值，丟到最左邊』，重複此動作在『未排序的部分』直到所有元素都被檢查過。
>

```python
def SelectionSort(list_of_elements):
  
	for i in range(len(list_of_elements)-1):
        min_index = i
    
        #find minimum element
        for j in range(i+1, len(list_of_elements)):
            if list_of_elements[min_index] > list_of_elements[j]:
                min_index = j
    
        #sort
        if i != min_index:
            list_of_elements[min_index], list_of_elements[i] = list_of_elements[i], list_of_elements[min_index]
  
	return list_of_elements
```

延伸討論：時間複雜度 (Big O = $O(n^2)$ )

有 $n$ 個元素，第 $1$ 次需要從 $n$ 個元素找 (步驟)，第 $2$ 次需要從 $n-1$ 個元素找，第 $n$ 次需要從最後 $1$ 個元素找。因此總共要進行 $n+(n-1)+...+1=\frac{n(n+1)}{2}$ 個步驟；而每次找到最小元素時都要進行一次位置交換的動作，因此有 $n$ 個步驟。

因此一共有 $\frac{n(n+1)}{2}+n=\frac{n^2+3n}{2}$ 個步驟，而當 $n$ 夠大時， $\frac{n^2+3n}{2} \sim n^2$ ，故稱此排序法的時間複雜度為 $O(n^2)$。





## Insertion Sort

> 從數列中的第一個元素開始，往前 (左邊) 依序比較，找到其符合大小排序的位置，重複此動作直到所有元素都被檢查過。
>

```python
def InsertionSort(list_of_elements):
    
    #start from second element
    for i in range(len(list_of_elements)):
        #storage current element
        element_index = i
        current_value = list_of_elements[i]
        
        #comparing with previous element
        while element_index >= 0 and list_of_elements[element_index-1] > current_value:
            list_of_elements[element_index] = list_of_elements[element_index-1]
            element_index -= 1
        #put back current element at stop index
        list_of_elements[element_index] = current_value
	
    return list_of_elements
```

延伸討論：時間複雜度 (Big O = $O(n^2)$ )

因為有非常順利的情況，也有最糟糕的情況，通常討論 ***時間複雜度會透過最糟糕的情況進行討論***。

> 最糟糕的狀況：整個數列呈現由大到小排序
>

因此從第 $2$ 個元素開始，第 $2$ 個元素需要往前比較並移動 $1$ 次，第 $3$ 個元素需要往前比較並移動 $2$ 次，第 $n$ 個元素需要往前比較並移動 $n-1$ 次。因此總共要進行 $1+2+...+(n-1)=\frac{n(n+1)}{2}-n$ 個步驟，而當 $n$ 夠大時， $\frac{n(n+1)}{2}-n=\frac{n^2-n}{2} \sim n^2$ ，故此排序法時間複雜度同樣為 $O(n^2)$。



## Merge Sort

> #### 拆分
>
> 1. 把大陣列切一半成為兩個小陣列
> 2. 把切好的兩個小陣列再各自切一半
> 3. 重複步驟二直到每個小陣列都只剩一個元素
>
> #### 合併
>
> 1. 排序兩個只剩一個元素的小陣列並合併
> 2. 把兩邊排序好的小陣列合併並排序成一個陣列
> 3. 重複步驟二直到所有小陣列都合併成一個大陣列

```python
def MergeSort(list_of_elements):
    if len(list_of_elements) <= 1:
        return list_of_elements
    else: #len(list_of_elements) > 1:
        middle = len(list_of_elements) // 2
        left_list, right_list = list_of_elements[:middle], list_of_elements[middle:]
        
        MergeSort(left_list)
        MergeSort(right_list)
        
        result_index = 0
        while left_list and right_list:
            #put element which has been pop out from the list back
            if left_list[0] < right_list[0]:
                list_of_elements[result_index] = left_list.pop(0)
            else:
                list_of_elements[result_index] = right_list.pop(0)
            result_index += 1

        #if any element left in the list
        while left_list:
            list_of_elements[result_index] = left_list.pop(0)
            result_index += 1
        while right_list:
            list_of_elements[result_index] = right_list.pop(0)
            result_index += 1
            
        return list_of_elements
```

延伸討論：時間複雜度 (Big O = $n\log_2(n)$ )

拆分： $n$ 個元素被拆分到每個數列只有 $1$ 個元素需要 $n-1$ 個步驟。

合併：每一階段合併，陣列都會少一半，所以合併的步驟總計會有 $\log_2(n)$ ，而每一次合併時，總計都會有 $n$ 個元素需要被決定位置 (合併進到新數列時) 。因此合併總共包含 $n\log_2(n)$。

總計： $(n-1)+n\log_2(n)$ 次步驟，而當 $n$ 夠大時， $(n-1)+n\log_2(n) \sim n\log_2(n)$ ，故稱此排序法的時間複雜度為 $O(n\log_2(n))$。



## Continuous Reading

- [十大經典演算法](https://github.com/hustcc/JS-Sorting-Algorithm)
