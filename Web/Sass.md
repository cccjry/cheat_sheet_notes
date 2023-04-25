# Sass

> Syntactically Awesome Style Sheets，是將CSS視為程式語言的開發技術。

在文字編輯器當中的scss無法被瀏覽器讀取，所以需要透過編譯器將scss轉換成css，才能被瀏覽器讀取。

## 常見功能

-  Nested CSS：巢狀編輯
    ```scss
    header {
        nav {
            li {
                list-style-type: none;
                a{
                    color: $themeColor;
                    text-decoration: none;
                }
            }
        }
    }
    ```
    The complied css will be like this:
    ```css
    header nav li {
        list-style-type: none;
    }
    header nav li a {
        color: green;
        text-decoration: none;
    }/*# sourceMappingURL=style.css.map */
    ```

-  Variables：變數
    ```scss
    $themeColor: green;
    header {
        nav {
            li {
                list-style-type: none;
                a {
                    color: $themeColor;
                    text-decoration: none;
                }
            }
        }
    }
    ```
    The complied css will be like this:
    ```css
    header nav li {
        list-style-type: none;
    }
    header nav li a {
        color: green; /* $themeColor */
        text-decoration: none;
    }/*# sourceMappingURL=style.css.map */
    ```

-  self ampersand `&`：自己的父層、引用自己
    ```scss
    header {
        nav {
            li {
                list-style-type: none;
                a {
                    color: $themeColor;
                    text-decoration: none;
                    &:hover {
                        color: red;
                    }
                }
            }
        }
    }
    ```
    The complied css will be like this:
    ```css
    header nav li {
        list-style-type: none;
    }
    header nav li a {
        color: green;
        text-decoration: none;
    }
    header nav li a:hover {
        color: red;
    }/*# sourceMappingURL=style.css.map */
    ```

-  Import：分類分類
    Import file name: `_<your file name>.scss`
    ``` scss
    @import "./<your file name>";
    ```

-  Mixins：重複使用的程式碼
    ```scss
    @mixin flex($direction, $justify, $align) {
        display: flex;
        flex-direction: $direction;
        justify-content: $justify;
        align-items: $align;
    }
    ```
    ```scss
    header {
        @include flex(row, space-between, center);
    }
    ```


