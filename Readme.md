# ERM 管理

> 是一個練習專案 配套的前端是 https://github.com/virgil724/something_happend_frontend

## 功能
 - [x] 登入/註冊
 - [x] 填寫週報表
 - [x] 回覆報表
 - [x] 成員分組/組長指派
 - [ ] 修改報表
 - [ ] API權限
    - 反正就沒封 現在全部只有`isAuthenticated`是必須的


## 模組
- Group
  - MemberAssign
  - LeaderAssign
- Report
  - Report
  - Comment


# API EndPoint
## Version: 0.0.0

### /v1/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/comment/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/comment/{id}/

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this comment. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this comment. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this comment. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/comment/report/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/comment/report/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/depart_manager/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/depart_manager/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department manager. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department manager. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department manager. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department manager. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/department/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/department/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this department. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/login/

#### POST
##### Description:

Check the credentials and return the REST Token
if the credentials are valid and authenticated.
Calls Django Auth login method to register User ID
in Django session framework

Accept the following POST parameters: username, password
Return the REST Framework Token Object's key.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/logout/

#### POST
##### Description:

Calls Django logout method and delete the Token object
assigned to the current User object.

Accepts/Returns nothing.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/password/change/

#### POST
##### Description:

Calls Django Auth SetPasswordForm save method.

Accepts the following POST parameters: new_password1, new_password2
Returns the success/fail message.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/password/reset/

#### POST
##### Description:

Calls Django Auth PasswordResetForm save method.

Accepts the following POST parameters: email
Returns the success/fail message.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/password/reset/confirm/

#### POST
##### Description:

Password reset e-mail link is confirmed, therefore
this resets the user's password.

Accepts the following POST parameters: token, uid,
    new_password1, new_password2
Returns the success/fail message.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/registration/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/registration/resend-email/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/registration/verify-email/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/dj-rest-auth/user/

#### GET
##### Description:

Reads and updates UserModel fields
Accepts GET, PUT, PATCH methods.

Default accepted fields: username, first_name, last_name
Default display fields: pk, username, email, first_name, last_name
Read-only fields: pk, email

Returns UserModel fields.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PUT
##### Description:

Reads and updates UserModel fields
Accepts GET, PUT, PATCH methods.

Default accepted fields: username, first_name, last_name
Default display fields: pk, username, email, first_name, last_name
Read-only fields: pk, email

Returns UserModel fields.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Description:

Reads and updates UserModel fields
Accepts GET, PUT, PATCH methods.

Default accepted fields: username, first_name, last_name
Default display fields: pk, username, email, first_name, last_name
Read-only fields: pk, email

Returns UserModel fields.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/group/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/group/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this group. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this group. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this group. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this group. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/group_leader/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/group_leader/group/{id}

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/managedepartment/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/managegroup/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/report/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/report/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this report. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this report. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this report. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this report. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/report/group/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/report/manage/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/report/user/{id}

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /v1/token/

#### POST
##### Description:

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /v1/token/refresh/

#### POST
##### Description:

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /v1/token/validate/

#### POST
##### Description:

Takes a token and indicates if it is valid.  This view provides no
information about a token's fitness for a particular use.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /v1/users/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |
