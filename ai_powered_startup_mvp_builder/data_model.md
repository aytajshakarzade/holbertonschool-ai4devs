# Data Model – FocusFlow

## 1. User

Stores user account information.

| Field | Type |
|---|---|
| id | Integer (Primary Key) |
| name | String |
| email | String (Unique) |
| password | String |
| created_at | DateTime |

## 2. Task

Stores tasks created by users.

| Field | Type |
|---|---|
| id | Integer (Primary Key) |
| user_id | Integer (Foreign Key) |
| category_id | Integer (Foreign Key) |
| title | String |
| description | Text |
| priority | String |
| status | String |
| due_date | DateTime |
| created_at | DateTime |

## 3. Category

Stores task categories.

| Field | Type |
|---|---|
| id | Integer (Primary Key) |
| user_id | Integer (Foreign Key) |
| name | String |
| created_at | DateTime |

## Relationships

- One user can have many tasks.
- One user can create many categories.
- One category can contain many tasks.
- Each task belongs to one user and one category.
