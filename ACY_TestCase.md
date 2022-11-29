# ACY Register for a Live Account ([Website](https://acy.com/en/open-live-account))



## Content

### A.  [Website Forum List](#A-Website-Forum-List)

### B.  [Test Case for ACY](#B-Test-Case-List)



## A. Website Forum List

## 1. Personal Detail

- Account Type **(list)**
- Country **(list)**
- Title **(list)**
- First Name
- Middle Name(optional)
- Last Name
- Email
- Phone
- Mobile Authentication (Get Code)

## 2. About You

- Gender **(list)**
- Date of Birth (date, month, year) **(list)**
- Photo ID Number
- Residential Address
- City State
- Zip Code

## 3. Investment

- Employment **(list)**
- Occupation **(list)**
- Industry **(list)**
- Annual Income (USD) **(list)**
- Total amount of investment (USD) **(list)**
- Trading Platform (MetaTrader4/5) **(list)**
- Funding Currency **(list)**
- Account Types **(list)**
- Leverage **(list)**

## 4. Experience

10 Questions about investment experience

## 5. Terms & Conditions

- I have read the Key Information Statement
- I have read the Client Terms and Conditions
- I have read the Privacy Policy Statement

## 6. Confirm ID

Upload files:

1. ID Document Front

   Please upload the front of your drivers licence/ID or the front page of your passport. (Note: the size of the document should be less than 5MB)

2. ID Document Back

   Please upload the back of your drivers licence/ID or the front page of your passport. (Note: the size of the document should be less than 5MB)

3. Proof of Address

   Please upload the back of your drivers licence/ID or the bank statements or utility bills. (Note: the size of the document should be less than 5MB)

4. Other Document（銀行賬單、戶口本、駕駛證等）

   Please upload your drivers licence/ID or bank statements or utility bills. (Note: the size of the document should be less than 5MB)

[TOP](#Content)



## B. Test Case List

| ID   | Test Feature    | Description                                           | Test Step                                                    | Test Data                          | Expected result                |
| ---- | --------------- | ----------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------- | ------------------------------ |
| 1    | required fields | filling all required fields                           | 1. Enter valid values into all fields<br />2. Click on Next bottom |                                    | pass                           |
| 2    | required fields | not filling any required fields                       | 1. Not enter any value in the field<br />2. Click on Next bottom |                                    | notify missing fields          |
| 3    | optional fields | filling data                                          | 1. Enter valid values into optional fields (with all required fields)<br />2. Click on Next bottom |                                    | pass                           |
| 4    | optional fields | not filling data                                      | 1. Not enter any value into optional fields (with all required fields)<br />2. Click on Next bottom |                                    | pass                           |
| 5    | validation      | valid email                                           | 1. Enter a valid email<br />2. Click on Next bottom          | test@gmail.com                     | pass                           |
| 6    | validation      | check email format (without @ symbol)                 | 1. Enter an invalid email<br />2. Click on Next bottom       | testgmail.com                      | notify incorrect  email        |
| 7    | validation      | check email format (random string)                    | 1. Enter an invalid email<br />2. Click on Next bottom       | test@woerjaod                      | notify incorrect email         |
| 8    | validation      | valid phone number                                    | 1. Enter a valid phone number<br />2. Click on Next bottom   | 0412345678                         | pass                           |
| 9    | validation      | check phone number format(incorrect digits)           | 1. Enter an invalid phone number<br />2. Click on Next bottom | 04123                              | notify incorrect phone number  |
| 10   | validation      | check phone number format(string)                     | 1. Enter an invalid phone number<br />2. Click on Next bottom | 04abcd                             | notify incorrect phone number  |
| 11   | validation      | First Name string length (random string)              | 1. Enter an invalid First Name<br />2. Click on Next bottom  | (random 255-long string)           | notify invalid name            |
| 12   | validation      | Last Name string length (random string)               | 1. Enter an invalid Last Name<br />2. Click on Next bottom   | (random 255-long string)           | notify invalid name            |
| 13   | validation      | valid photo ID number                                 | 1. Enter a valid ID number<br />2. Click on Next bottom      | A123456789                         | pass                           |
| 14   | validation      | check photo ID number format(incorrect digits)        | 1. Enter an invalid ID number<br />2. Click on Next bottom   | A123456(none regular ID number)    | notify invalid ID number       |
| 15   | validation      | check photo ID number format(string)                  | 1. Enter an invalid ID number<br />2. Click on Next bottom   | AAAABBBCCC(none regular ID number) | notify invalid ID number       |
| 16   | validation      | valid residential address                             | 1. Enter a valid address<br />2. Click on Next bottom        | (Some normal address)              | pass                           |
| 17   | validation      | check residential address format (random string)      | 1. Enter an invalid address<br />2. Click on Next bottom     |                                    | notify invalid address         |
| 18   | validation      | check residential address format (symbol)             | 1. Enter an invalid address<br />2. Click on Next bottom     |                                    | notify invalid address         |
| 19   | validation      | valid city state                                      | 1. Enter a valid city state name<br />2. Click on Next bottom | Taichung City                      | pass                           |
| 20   | validation      | check city state format (random string)               | 1. Enter an invalid city state name<br />2. Click on Next bottom | (Some none-exist city name)        | notify invalid city state name |
| 21   | validation      | check city state format (symbol)                      | 1. Enter an invalid city state name<br />2. Click on Next bottom | Taichung@City                      | notify invalid city state name |
| 22   | validation      | valid zip code                                        | 1. Enter a valid zip code<br />2. Click on Next bottom       | 54068                              | pass                           |
| 23   | validation      | check zip code format(incorrect digits)               | 1. Enter an invalid zip code<br />2. Click on Next bottom    | 540                                | notify incorrect zip code      |
| 24   | validation      | check zip code format(string)                         | 1. Enter an invalid zip code<br />2. Click on Next bottom    | 540AA                              | notify incorrect zip code      |
| 25   | validation      | valid upload file size                                | 1. Select images<br />2. Click on Upload                     | (some file within 5MB)             | pass                           |
| 26   | validation      | check upload file size (over 5MB)                     | 1. Select images<br />2. Click on Upload                     | (some file over 5MB)               | notify oversized-file          |
| 27   | performance     | response time (< n seconds) after next-bottom         | 1. Monitoring web actions<br />2. Check actions time-consume |                                    | pass                           |
| 28   | performance     | large amount of registration at a time (>N) not crash | 1. Simulate N registration at same time                      |                                    |                                |
| 29   | security        | encrypting data to back-end server                    |                                                              |                                    |                                |
| 30   | security        | check upload file extension                           |                                                              |                                    |                                |
| 31   | security        | varify data at back-end server                        |                                                              |                                    |                                |
| 32   | security        | cookie                                                |                                                              |                                    |                                |
| 33   | security        | Mobile Authentication error times (< n times)         |                                                              |                                    |                                |
| 34   | security        | SQL injection                                         |                                                              |                                    |                                |
| 35   | security        | command injection                                     |                                                              |                                    |                                |
| 36   | compatibility   | different browser                                     |                                                              |                                    |                                |
| 37   | compatibility   | different OS                                          |                                                              |                                    |                                |

[TOP](#Content)

