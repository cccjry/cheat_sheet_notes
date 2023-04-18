# CSS

> Cascading Style Sheets，用來控制HTML的外觀與佈局。包含字體、顏色、尺寸、間距、邊框、背景、浮動、定位等等。

## DOM Tree

**Document Object Model**，加載到瀏覽器當中的樹狀表示。

![DOM tree](img/DOM_Tree.png)

Inside nesting structure:
- Parent Node (Parent element)
- Child Node (Child element)

這兩者可以互相嵌套，形成一個樹狀的結構。

## 可放置的位置

- **Inline** only apply to current element
  ``` html
  <h1 style="color: green"></h1>
  ```
  設定對象較為侷限，不易維護。

- **Internal** only apply to current page
  ``` html
  ``` html
  <head>
    <style>
      h1 {
        color: green;
      }
    </style>
  </head>
  ```
  若頁面較多，則需要在每個頁面都加入，不易維護，且會造成頁面載入時間過長。

- **external** apply to all pages linked to this file
  ``` html
  <link rel="stylesheet" href="style.css">
  ```
  一個獨立的檔案，可在所有頁面中使用，且只需載入一次，容易維護且可大幅減少頁面載入時間。

Priority: *inline* > *internal* > *external*

## 顏色設定

- Color name
  ``` css
  h1 {
    color: red;
  }
  ```
  有限的顏色名稱，不易維護。

- RGB
  ``` css
  h1 {
    color: rgb(255, 0, 0);
  }
  ```
    紅、綠、藍，0為最暗，255為最亮，每個值都介於0~255之間，每個值都用1byte（8bit）來表示。

- rgba
  ``` css
  h1 {
    color: rgba(255, 0, 0, 0.5);
  }
  ```
    第四個為透明度，0為完全透明，1為完全不透明。

- HEX
  ``` css
  h1 {
    color: #ff0000;
  }
  ```
    16進位，每個值都用2byte（16bit）來表示。

- HSL
  ``` css
  h1 {
    color: hsl(0, 100%, 50%);
  }
  ```
    Hue（色相）、Saturation（飽和度）、Lightness（亮度），色相為0~360，飽和度為0~100%，亮度為0~100%。

For more information, please refer to [CSS Color](https://www.w3schools.com/css/css_colors.asp).

## CSS Selectors

- Universal Selector
  ``` css
  * {
    color: red;
  }
  ```
  選取所有元素。

- Element Selector
  ``` css
  h1 {
    color: red;
  }
  ```
  選取所有`h1`元素。

- ID Selector
  ``` css
  #my_id {
    color: red;
  }
  ```
  開頭`#`選取所有`id`為`my_id`的元素。`id`為唯一值，不可重複。

- Class Selector
    ``` css
    .my_class {
        color: red;
    }
    ```
    開頭`.`選取所有`class`為`my_class`的元素。`class`可重複，多個`class`用空格分開。
    ``` html
    <h1 class="my_class1 my_class2">Hello World</h1>
    ```
    
    ``` css
    .my_class1.my_class2 {
        color: red;
    }
    ```

ID, Class, Element Selector 以及其他tag可以互相組合使用，例如：
``` css
/*eg1*/
#my_id.my_class {
    color: red;
}

/*eg2*/
a.my_class {
    color: red;
}

/*eg3*/
a#my_id {
    color: red;
}
```

Selector Priority:
ID Selector > Class Selector > Element Selector

- Group Selector
    ``` css
    h1, h2, h3 {
        color: red;
    }
    ```
    選取所有`h1`、`h2`、`h3`元素。

- Descendant Selector
    ``` html
    <h2>
        <span>Hello World</span>
    </h2>
    ```

    ``` css
    h2 span {
        color: red;
    }
    ```
    選取所有`h2`元素中的`span`元素。依據DOM Tree，的結構，範例中`span`為`h2`的子元素，非透過`id`或`class`來選取。

- Attribute Selector
    ``` css
    input[type="password"] {
        color: red;
    }
    ```



