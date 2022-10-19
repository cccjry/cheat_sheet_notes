import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

from Utility import (
    get_exoplanet_table_by_astroquery,
    get_distance_unit_dict,
    convert_exoplanet_table_distance_unit)


page_title = '系外行星資料表篩選器'
st.set_page_config(page_title=page_title, page_icon=':star', layout='wide')
st.title(page_title)
st.info('藉由[Astroquery](https://astroquery.readthedocs.io/en/latest/ipac/nexsci/nasa_exoplanet_archive.html)套件取得[NASA系外行星資料庫](https://exoplanetarchive.ipac.caltech.edu/)提供的資料表，篩選出所需資料後匯出CSV檔。')

with st.spinner('正在載入系外行星資料表，請稍候...'):
    exoplanet_table = get_exoplanet_table_by_astroquery()

distance_unit_dict = get_distance_unit_dict()
distance_unit = st.radio(
    '切換表格中的距離單位', list(distance_unit_dict.keys()), horizontal=True
)
exoplanet_table = convert_exoplanet_table_distance_unit(
    exoplanet_table, distance_unit_dict, distance_unit
)

with st.expander('各距離單位的換算'):
    st.markdown('[秒差距](https://zh.wikipedia.org/zh-tw/%E7%A7%92%E5%B7%AE%E8%B7%9D)、[光年](https://zh.wikipedia.org/zh-tw/%E5%85%89%E5%B9%B4)和[天文單位](https://zh.wikipedia.org/zh-tw/%E5%A4%A9%E6%96%87%E5%96%AE%E4%BD%8D)都是常用來描述星體距離的長度單位')
    st.markdown('1秒差距約為 $3.09*10^{13}$ 公里')
    st.markdown('1光年約為 $9.46*10^{12}$ 公里')
    st.markdown('1天文單位是地球和太陽的平均距離，約為 $1.5*10^{8}$ 公里')


## Sidebar functions below ##
# sidebar年份篩選器
year_min = int(exoplanet_table['發現年份'].min())
year_max = int(exoplanet_table['發現年份'].max())
year_lst = list(range(year_min, year_max + 1))
year_range = st.sidebar.select_slider(
    '篩選某年份區間內被發現的行星',
    options=year_lst,
    value=(year_min, year_max),
)
exoplanet_table = exoplanet_table[
    (exoplanet_table['發現年份'] >= year_range[0]) &
    (exoplanet_table['發現年份'] <= year_range[1])
]

# sidebar某欄位篩選器
method_lst = sorted(list(exoplanet_table['發現方法'].unique()))
selected_method = st.sidebar.selectbox(
    '篩選被某個方法發現的行星', ['不限'] + method_lst
)
if selected_method != '不限':
    exoplanet_table = exoplanet_table[exoplanet_table['發現方法']
                                      == selected_method]

# sidebar function
column_name_lst = list(exoplanet_table.columns)
selected_columns = st.sidebar.multiselect(
    '去除某幾個欄位值為空值的行星', column_name_lst
)
exoplanet_table = exoplanet_table.dropna(subset=selected_columns)

# sidebar function
exoplanet_table = exoplanet_table.reset_index(drop=True)
st.dataframe(exoplanet_table)
st.sidebar.download_button(
    label='將篩選資料表匯出成CSV檔',
    data=exoplanet_table.to_csv(index=False),
    file_name='exoplanet_table.csv',
    mime='text/csv'
)

# sidebar function
if st.sidebar.button('清除資料表快取'):
    st.experimental_memo.clear()
    st.balloons()
    st.sidebar.success('已清除快取，請重新載入頁面')

## Sidebar functions end ##


# 透過Aggrid調整表格顯示方式
gb = GridOptionsBuilder.from_dataframe(exoplanet_table)
gb.configure_column('行星名稱', pinned='left')
gb.configure_column(
    '行星名稱',
    cellRenderer=JsCode('''
    function(params) {
        return '<a href="https://exoplanets.nasa.gov/eyes-on-exoplanets/#/planet/' + params.value.replaceAll(" ", "_") + '" target="_blank">' + params.value + '</a>'
    };
    ''')
)  # rendering url into names
for col in exoplanet_table.columns.values.tolist():
    gb.configure_column(col, suppressMovable=True, suppressMenu=True)

gridOptions = gb.build()
AgGrid(
    exoplanet_table,
    gridOptions=gridOptions,
    allow_unsafe_jscode=True,
    height=400,
    theme='balham'
)

