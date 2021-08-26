# Test Bimedoc

## Documentation API

## POST
### /api/webpage/data

#### Body:

{
    "url": "https://www.example.com"
}

#### Return Code:

400: Bad URL
200: OK

## GET
### /api/eurovalue

### Return Code:

200: OK

## Library Used

djangorestframework
django-cors-headers
requests
beautifulsoup4
