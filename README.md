# **Key-Value Manager API**

<br/>

#### About
This is a pet-project, it should not be used for commercial purposes!
<br/>Key-Value Manager API. An application developed using Flask and MongoDB,
<br/>that provides the ability to create, update and get key-value pairs from a MongoDB.

##### Technology stack:
* Python 3.8, Flask 3.2;
* MongoDB;
* Docker
* Docker Compose

##### Getting Started
* Clone the repository
* Go to the project directory
* `docker-compose up`

##### API Endpoints
* `POST /api/create`
  * `{ "key": "test_key", "value": "test_value" }`
* `PUT /api/update/<key>`
  * `{ "value": "new_test_value" }`
* `GET /api/get/<key>`
  * `{ "key": "test_key", "value": "new_test_value"} `

<br/>

Made by `Self`.