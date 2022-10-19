# Streamlit book

Here saves some useful manual.

[TOC]





## 0.Hello World

```bash
pip install streamlit
streamlit hello
```

some other galleries: https://streamlit.io/gallery

### 0.1.Example Code

```python
# example.py
import streamlit as st
import pandas as pd

st.title('Hello World')
uploaded_csv = st.file_uploader('選擇您要上傳的CSV檔')

if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)
    st.header('您所上傳的CSV檔內容：')
    st.dataframe(df)
```

### 0.2.Example Execute (Locally)

```bash
streamlit run example.py
```





## 1.Some Functions

### 1.1.常用

- `st.text_input()`: 輸入文字

- `st.selectbox()`: 下拉選單

- `st.checkbox()`: 勾選項目

- `st.radio()`: 呈現數個勾選項目（單選）

- `st.select_slider(label, options, value)`

- `st.number_input`: 數字選單

- `st.date_input()`: 日期選擇器

- `st.button()`: 按鈕（action）

- [`st.download_button(label, data, file_name, mime='text/csv')`](https://docs.streamlit.io/library/api-reference/widgets/st.download_button): 下載按鈕

- `st.image(image_url_here, caption="caption here")`

  - `st.code("code here", language="python")`: 放置程式碼區塊

- 標題類：

  1. `st.title()`
  2. `st.header()`
  3. `st.subheader()`

- 說明文字(可markdown)

  1. `st.write()`: 呈現純文字
  2. `st.markdown()`: 純markdown語法

- Running Status

  1. `st.progress(int_or_float)`: 進度條

     ```python
     my_bar = st.progress(0)
     
     for percent_complete in range(100):
         my_bar.progress(percent_complete + 1)
     ```

  2. `st.spinner()`: 載入訊息

     ```python
     with st.spinner("infomation text here"):
       """action inside here"""
     ```

  3. `st.info()`: 呈現文字(可加入markdown)(藍底)

  4. `st.success()`: 呈現文字(可加入markdown)(綠底)

  5. `st.warning()`: 呈現文字(可加入markdown)(黃底)

  6. `st.exception`: 把 `exception` 訊息放到前端（必須配合 `Error`)

  7. 特效：

     - `st.balloons()` 氣球
     - `st.snow()` 雪花片

- `st.expander()`: 隱藏／展開一個區塊

  ```python
  with st.expander("顯示文字"):
    """在裡面放入想先隱藏的區塊的內容"""
    """E.g.
    st.header("HI")
    st.image(image_url_here, caption="caption here")
    """
  ```

- `st.set_page_config(page_title, page_icon, layout="wide")`: 設定頁面預設內容

  其他更詳細資訊可以到 [cheet sheet](https://docs.streamlit.io/library/cheatsheet) 和 [API](https://docs.streamlit.io/library/api-reference) 查詢其他功能；同時也有[第三方擴充元件](https://streamlit.io/components)可選擇

- `st.sidebar.*`: 側邊選單，繼承所有 `st.*`的功能

- `st.stop()`: 停止執行該頁面接下來的內容



### 1.2.Decoratored Function

- `@st.cache()`: 快取功用，避免每次都重新載入，加在函式上方（以後好像會被下面兩個取代？）
- `@st.experimetal_memo()`: 暫存計算結果、資料 [連結](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- `@st.experimetal_singleton()`: 暫存非資料類資訊，如session、資料庫連線 [連結](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
- `st.experimetal_memo.clear()`: 清除暫存



### 1.3.多頁

[LINK](https://docs.streamlit.io/library/get-started/multipage-apps) （1.13.0才有）

Structure: 

```
Home.py # This is the file you run with "streamlit run"
└─── pages/
  └─── About.py # This is a page
  └─── 2_Page_two.py # This is another page
  └─── 3_Page_three.py # So is this
```

`Home.py`為這個結構的進入節點(entrypoint file/page)，**<u>頁面</u>**名稱即為**<u>檔案</u>**名稱，副檔名皆是 `.py` ，並且這些頁面都存放在 `pages` 目錄底下，`streamlit`會自動忽視其他副檔名的檔案。

分頁可以直接使用URL連結，透過分頁的 `label` 名稱（若名稱重複取第一個）



#### 1.3.1.Need to know

Valid filenames for pages：

- A `number` — 編號
- A separator — 可以是 `_`、 `-`、空格、或是其他任何的組合
- A `label` — 其他標記、名稱，不包含 `.py`
- The extension — 只能是 `.py`

預設顯示：

- 沒有 `label` 就用 `number` 
- `Streamlit` 會自動把 `_` 取代成空格

預設排序：

- 有數字的會排在沒有數字的前面

- 基於數字排序

- When files are sorted, Streamlit treats the `number` as an actual number rather than a string. So `03` is the same as `3`

  範例：

  | **Filename**              | **Rendered label** |
  | :------------------------ | ------------------ |
  | `1 - first page.py`       | first page         |
  | `12 monkeys.py`           | monkeys            |
  | `123.py`                  | 123                |
  | `123_hello_dear_world.py` | hello dear world   |
  | `_12 monkeys.py`          | 12 monkeys         |



## 2.第三方元件

### 2.1.Streamlit-aggrid

> 整合 JavaScript 的元件 AG Grid

[DOC](https://streamlit-aggrid.readthedocs.io/en/docs/)

[JS Data Grid](https://www.ag-grid.com/javascript-data-grid/column-properties/)

E.g.建立一個 `GridOptionBuilder` 物件（把 `dataframe` 丟進去）

```python
#builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_column("first_column", header_name="First", editable=True)
go = builder.build()

#uses the gridOptions dictionary to configure AgGrid behavior.
AgGrid(df, gridOptions=go)
```





## 3.畫圖

已知支援的：Matplotlib、Bokeh、Plotly、Vega-Altair、(有用到再增加)



### 設定欄位版面

[LINK](https://docs.streamlit.io/library/api-reference/layout/st.columns)

`st.column(數量, gap="small")`

入量可以是數值(平均分配欄寬)；數值`list`(依照給予的數字比例分配)

E.g.

```python
"""各自指定內容"""
col1, col2, col3 = st.column(3) # 設定對應欄位數量
with col1:
  """column1 content"""
with col2:
  """column2 content"""
with col3:
  """column3 content"""

  
"""直接從欄位叫方法"""
col1, col2 = st.columns([3, 1]) # 產生寬度比為3:1的兩個欄位
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)
```



### `Plotly`

`st.plotly_chart(fig_or_data, use_container_width=False, sharing="streamlit", **kwargs)`

E.g.

```python
import streamlit as st
import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
```

