<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<!DOCTYPE html>
<html>
<head>
<title>The Posts</title>
<link href="forum.css" rel="stylesheet" type="text/css" />
</head>
<body>
  <h1>The Posts</h1>
  <h4>The single thread forum</h4>
  <div class="posts">
    <a href="./newpost">Add new post</a>
    <c:forEach items="${posts}" var="post">
      <div class="post">
         <div class="header">
           <span class="name">${post.owner}</span>
           <span class="date">${post.timestamp}</span>
         </div>
         <div class="text">
           <pre>${post.post}</pre>
         </div>
      </div>
    </c:forEach>
  </div>
</body>
</html>
