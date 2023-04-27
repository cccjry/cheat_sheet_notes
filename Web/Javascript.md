# Javascript

## Basics

JavaScript是一種**腳本**，擁有自己的規範，稱為 ECMAScript(European Computer Manufacturers Association)；原本叫做 LiveScript，跟 Java 完全沒有關係。

Vanilla JavaScript 是指沒有使用任何額外的 library或框架的 JavaScript。常見的 library 有 jQuery(普遍度逐漸下降)、React、Vue.js、Angular 等等，越來越多網站使用純 JavaScript 來開發，因為這樣可以減少網頁的載入時間，並且可以避免使用到不必要的功能。

每個瀏覽器有自己的 JavaScript 引擎，例如 Chrome 的 V8、Firefox 的 SpiderMonkey、Safari 的 JavaScriptCore、Edge 的 Chakra 等等。若要確認瀏覽器的JavaScript引擎是否支援某種功能，可以參考 [Can I use](https://caniuse.com/)。

## 基本語法

### `<script>`通常放在哪？

通常會放在`<body>`的最後面，因為如果放在`<head>`裡面，瀏覽器會先讀取`<script>`，而`<script>`裡面的程式碼可能會需要讀取`<body>`裡面的元素，所以會造成錯誤。先讓瀏覽器加載HTML、CSS，再加載JavaScript，可以讓網頁更快顯示出來(提升使用者體驗)。

### 常見 JS 函數

- `console.log()`：在瀏覽器的開發者工具中，將 message 輸出到 Web 控制台，可以在 console 裡面看到輸出的結果。Message可以是任何資料型態，例如字串、數字、物件、陣列等 JavaScript Object。
    ```javascript
    console.log("Hello World!");
    ```

- `window.alert()`：在瀏覽器的畫面中，跳出一個對話框，顯示 message，並等待使用者按下確認按鈕後，才會繼續執行下面的程式碼。
    ```javascript
    window.alert("Hello World!");
    ```

- `window.prompt()`：在瀏覽器的畫面中，跳出一個對話框，顯示 message，並等待使用者輸入資料後，才會繼續執行下面的程式碼。
    ```javascript
    window.prompt("Please enter your name:");
    ```
## Lexical Structure

好比自然語言有自己的語法規則，例如英文的句子要以大寫字母開頭，以句號結尾，中間要有主詞、動詞、受詞等等，JavaScript 也有自己的，稱為 Lexical Structure。幾個基本的規則如下：

- Case Sensitive：大小寫有別，`a`跟`A`是不同的變數。

- Whitespace：JavaScript 會忽略(minification)空白字元，例如空格、換行、縮排等等。

- 註解：單行註解以`//`開頭，多行註解以`/*`開頭，`*/`結尾。
    ```javascript
    // This is a single-line comment.
    /* This is a
    multi-line comment. */
    ```
- 變數名稱必須以字母、底線、美元符號開頭(數字不可)，後面可以接字母、數字、底線、美元符號。
    ```javascript
    var _name = "John";
    var $name = "John";
    var name = "John";
    ```

- Reserved Words：JavaScript 有一些保留字，不能用來當作變數名稱，例如 `var`、`let`、`const`、`function`、`return`、`if`、`else`、`for`、`while`、`switch`、`case`、`break`、`continue`、`true`、`false`、`null`、`undefined` 等等。

- Unicode：JavaScript 支援任何 Unicode 字元，例如中文字、日文字、韓文字等等。

- Semicolons：一行可以有多個敘述，以分號 `;` 分隔；也可以不用分號，但是不建議這樣做，因為會造成錯誤。
    ```javascript
    var x = 5; var y = 6; var z = x + y;
    ```




