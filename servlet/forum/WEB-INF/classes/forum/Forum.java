package forum;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/login")

public class Forum extends HttpServlet
{
   public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
      response.setContentType("text/html");

      request.getRequestDispatcher("/login.jsp").forward(request, response);
   }

   public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
   }
}

