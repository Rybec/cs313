package forum;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.text.SimpleDateFormat;
import java.util.Date;

@WebServlet("/view")

public class List extends HttpServlet
{
   public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
      response.setContentType("text/html");

      Cookie[] cookies = request.getCookies();
      String name = Auth.auth(cookies);

      if (name == null)
      {
         request.getRequestDispatcher("/").forward(request, response);
      }
      else
      {
         Data data = new Data();

         request.setAttribute("posts", data.getPosts());
         request.setAttribute("username", name);
         request.getRequestDispatcher("/list.jsp").forward(request, response);
      }
   }

   public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
      response.setContentType("text/html");

      Cookie[] cookies = request.getCookies();
      String name = Auth.auth(cookies);

      if (name == null)
      {
         request.getRequestDispatcher("/login").forward(request, response);
      }
      else
      {
         Data data = new Data();

         String post = request.getParameter("post");

         SimpleDateFormat sdf = new SimpleDateFormat("d MMMMM yyyy, h:mm a");
         Date now = new Date();
         String timestamp = sdf.format(now);

         if (post.length() > 0)
         {
            data.writePost(new Post(name, timestamp, post));
         }

         request.setAttribute("posts", data.getPosts());
         request.setAttribute("username", name);
         request.getRequestDispatcher("/list.jsp").forward(request, response);
      }
   }
}
