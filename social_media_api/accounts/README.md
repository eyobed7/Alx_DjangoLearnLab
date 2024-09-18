1. Project Overview
The API has two main resources:

Posts: Represents blog or social media posts created by users.
Comments: Represents comments made by users on specific posts.
Features:
CRUD operations for both posts and comments.
Token-based authentication for secure access.
Permission checks to ensure users can only modify or delete their own posts or comments.
Pagination and filtering support for better data handling.
2. API Endpoints
Authentication
Register a new user: POST /register/
Login to get token: POST /login/
Both registration and login will return an authentication token that should be used for subsequent requests.

Posts
List All Posts

Endpoint: GET /poscom/posts/
Description: Returns a list of all posts.
Example Request:
bash
Copy code
curl -X GET http://127.0.0.1:8000/poscom/posts/ -H 'Authorization: Token <your_token>'
Create a New Post

Endpoint: POST /poscom/posts/
Description: Creates a new post. Requires authentication.
Example Request:
bash
Copy code
curl -X POST http://127.0.0.1:8000/poscom/posts/ -H 'Authorization: Token <your_token>' -d '{"title": "New Post", "content": "Post content here"}'
Example Response:
json
Copy code
{
  "id": 1,
  "author": "user1",
  "title": "New Post",
  "content": "Post content here",
  "created_at": "2024-09-18T06:00:00Z",
  "updated_at": "2024-09-18T06:00:00Z"
}
Retrieve a Single Post

Endpoint: GET /poscom/posts/{id}/
Description: Fetches details of a specific post by ID.
Update a Post

Endpoint: PUT /poscom/posts/{id}/
Description: Updates a post. Only the author can update the post.
Permissions: Must be the post author.
Delete a Post

Endpoint: DELETE /poscom/posts/{id}/
Description: Deletes a post. Only the author can delete the post.
Permissions: Must be the post author.
Comments
List Comments on a Post

Endpoint: GET /poscom/posts/{id}/comments/
Description: Lists all comments associated with a specific post.
Create a New Comment

Endpoint: POST /poscom/comments/
Description: Creates a comment on a post.
Example Request:
bash
Copy code
curl -X POST http://127.0.0.1:8000/poscom/comments/ -H 'Authorization: Token <your_token>' -d '{"post": 1, "content": "This is a comment."}'
Update a Comment

Endpoint: PUT /poscom/comments/{id}/
Description: Updates a comment. Only the comment's author can update it.
Delete a Comment

Endpoint: DELETE /poscom/comments/{id}/
Description: Deletes a comment. Only the comment's author can delete it.
3. Pagination and Filtering
Pagination:
Posts and comments can return large datasets, so pagination is used to limit the number of items returned in one response.
You can navigate through pages using ?page= query parameter.
Example:

bash
Copy code
GET /poscom/posts/?page=2
Filtering:
Posts can be filtered by title and content. You can use query parameters like:

?title=<keyword> to filter posts by title.
?content=<keyword> to filter posts by content.
4. Permissions
Posts: Users can create, view, update, and delete their own posts. They cannot modify or delete posts created by others.
Comments: Users can add comments to any post but can only modify or delete their own comments.
All endpoints, except registration and login, require token-based authentication.
5. Usage with Postman or Curl
Register a New User:
bash
Copy code
curl -X POST http://127.0.0.1:8000/register/ -d '{"email": "user@example.com", "username": "user1", "password": "password123"}'
Login to Get Token:
bash
Copy code
curl -X POST http://127.0.0.1:8000/login/ -d '{"username": "user1", "password": "password123"}'
Response:
json
Copy code
{
  "token": "your_token_here"
}
Authenticated Requests:
Include the token in the header of every authenticated request:

bash
Copy code
curl -X GET http://127.0.0.1:8000/poscom/posts/ -H 'Authorization: Token your_token_here'
6. Testing
To ensure the API is functioning as expected, tests have been implemented for:

Registration and login.
CRUD operations for posts and comments.
Permission handling for unauthorized updates/deletes.
Postman Collection:
A Postman collection is available for testing the API. It contains:

Example requests for each endpoint (POST, GET, PUT, DELETE).
Sample tokens for authenticated requests.
7. Conclusion
This API is designed to manage posts and comments in a social media-like application with proper permissions and security through token-based authentication. It also provides pagination and filtering for efficient data management.






