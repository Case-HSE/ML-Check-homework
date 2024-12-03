# Documentation

### Start guides
- [Start backend locally](#start-backend-locally)
- [Start backend via Docker](#start-backend-via-docker)

### Auth service
- [Add account](#add-account)
- [Basic auth](#basic-auth)
- [Onboarding set data](#onboarding-set-data)

### ML service
- [GPT prompt](#gpt-prompt)
- [OCR prompt](#ocr-prompt)
- [Work checking from texts](#work-checking-from-texts)
- [Work checking from images](#work-checking-from-images)


## Start backend locally

```bash
pip install -r backend/requirements.txt
python backend/main.py
```

## Start backend via Docker
```bash
docker build . -f backend/Dockerfile -t kch-backend
docker run <your params> kch-backend
```


# Auth service

### Add account
Create account with username and password
```html request
POST /auth/add-account
```
Input:
```html request
{
  "username": "string",
  "password": "string"
}
```
Output:
```html request
{
  "status": "success"
}
```

### Basic auth
Auth with credentials
``` html request
GET /auth/basic-auth
```
Input:
```User credentials```

Output:
```html request
{
  "status": "success"
}
```

### Onboarding set data
Set user's data from onboarding (with checking auth)
```html request
POST /onboarding/set_data
```
Input:
```html request
{
  "name": "string",
  "school": "string",
  "class_num": "string",
  "subjects_wishes": [
    "string"
  ],
  "favourite_areas": [
    "string"
  ],
  "hate_areas": [
    "string"
  ],
  "extra_activities": [
    "string"
  ],
  "achievements": [
    "string"
  ],
  "year_purposes": [
    "string"
  ],
  "final_class": 0
}
```
Output:
```html request
{
  "status": "success"
}
```

# ML Service

### GPT prompt.
Prompt to a GPT model.
```html request
POST /ai/gpt/prompt
```
Input:
```html request
{
  "text": "string"
}
```
Output:
```html request
{
  "text": "string",
  "status": "success"
}
```

### OCR prompt
Prompt to an OCR model
```html request
POST /ai/ocr/prompt
```
Input:
```Image File```
Output:
```html request
{
  "text": "string",
  "status": "success"
}
```

### Work checking from texts
Check work from text tasks and text works.
```html request 
POST /workchecking/from_text
```
Input:
```html request
{
  "texts": [
    "string"
  ],
  "tasks": [
    "string"
  ]
}
```
Output (mistakes and marks):
```html request
{
  "texts": [
    "string"
  ]
}
```

### Work checking from images
Check works from image tasks and image solutions
```html request
POST /workchecking/from_images
```
Input:

tasks: ```Image files```

solutions: ```Image files```

Output (mistakes and marks):
```html request
{
  "texts": [
    "string"
  ]
}
```
