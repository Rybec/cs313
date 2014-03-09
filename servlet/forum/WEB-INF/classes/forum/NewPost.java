package forum;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/newpost")

public class NewPost extends HttpServlet
{
   public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
      Cookie[] cookies = request.getCookies();

      response.setContentType("text/html");

      String name = Auth.auth(cookies);

      if (name == null)
      {
         request.getRequestDispatcher("/login.jsp").forward(request, response);
      }
      else
      {
         request.setAttribute("username", name);
         request.getRequestDispatcher("/newpost.jsp").forward(request, response);
      }
   }

   public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
      response.setContentType("text/html");

      String name;

      if (request.getParameter("username") == null &&
          request.getParameter("password") == null)
      {
         request.getRequestDispatcher("/login.jsp").forward(request, response);
      }
      else if ((name = Auth.auth(request.getParameter("username"),
                         request.getParameter("password"))) != null)
      {
         response.addCookie(new Cookie("username",
                                      request.getParameter("username")));
         request.setAttribute("username", request.getParameter("username"));
         request.getRequestDispatcher("/newpost.jsp").forward(request, response);
      }
      else
      {
         request.getRequestDispatcher("/fail.jsp").forward(request, response);
      }
   }
}

