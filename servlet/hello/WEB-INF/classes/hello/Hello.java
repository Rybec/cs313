package hello;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/")

public class Hello extends HttpServlet
{
   public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
      response.setContentType("text/html");
      PrintWriter out = response.getWriter();
      out.println("<!DOCTYPE><html><head><title>Hello</title></head>");
      out.println("<body><h1>Hello stinking world!</h1></body></html>");
   }

   public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws IOException, ServletException
   {
      doGet(request, response);
   }
}
