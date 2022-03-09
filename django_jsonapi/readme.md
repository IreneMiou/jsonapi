# JSON API
---
Hello!This is a JSON DJANGO REST API that returns quotes for cities.

## HOW TO USE
---
Every quote is modelled like following:

|name   |type   |mandatory   |max size   |
|-------|-------|------------|-----------|
|quote|textfiled|yes||
|category|charfield|no|200|

quote:this is the content of the quote

category:this is the category of the quote

API ENDPOINTS

/city_quotes/:returns all the quotes under the category 'city'
/city_quotes/idnumber:returns specific quote

In order to use the api you need an API key that only the admin can provide
