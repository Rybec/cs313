package forum;

import java.io.*;
import javax.servlet.http.*;

public class Auth
{
   static String filename = "/home/rybec/www/forum.auth";

   public static String auth(String username, String password)
      throws IOException
   {
      FileReader reader = new FileReader(filename);
      String contents = "";

      // The whole file will be read into the string
      int i;
      while ((i = reader.read()) != -1)
      {
         char ch = (char)i;
         contents = contents + ch;
      }
      reader.close();

      String[] authstrings = contents.split("\n");

      String[] auth;
      for (i = 0; i < authstrings.length; i++)
      {
         auth = authstrings[i].split("￰"); // Unicode 0xFFF0
         if (username.equals(auth[0]) && password.equals(auth[1]))
         {
            return username;
         }
      }

      return null;
   }

   public static String auth(Cookie[] cookies)
   {

      String name = null;
      if (cookies == null)
      {
         return null;
      }

      for (int i = 0; i < cookies.length; i++)
      {
         if (cookies[i].getName().equals("username"))
            name = cookies[i].getValue();
      }

      return name;
   }
}
