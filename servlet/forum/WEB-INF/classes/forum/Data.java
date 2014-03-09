package forum;

import java.io.*;

public class Data
{
   String filename = "/home/pi/public_html/forum/forum.posts";

   public Post[] getPosts()
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

      if (contents.equals(""))
      {
         return null;
      }

      String[] poststrings = contents.trim().split("￿");  // Unicode 0xffff

      Post[] posts = new Post[poststrings.length];

      String[] post;
      for (i = 0; i < poststrings.length; i++)
      {
         post = poststrings[i].split("￰"); // Unicode 0xFFF0
         if (post.length == 3)
         {
            posts[poststrings.length - i - 1] = new Post(post[0], post[1], post[2]);
         }
      }

      return posts;
   }

   public void writePost(Post post)
      throws IOException
   {
      String poststring = post.toString();

      FileWriter writer = new FileWriter(filename, true);
      writer.write(poststring);
      writer.close();
   }
}
