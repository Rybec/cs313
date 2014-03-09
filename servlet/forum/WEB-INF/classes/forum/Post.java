package forum;

public class Post
{
   private String owner = "";
   private String timestamp = "";
   private String post = "";

//   This will make reading in simpler
//   public Post(String poststring)

   public Post(String owner, String timestamp, String post)
   {
      this.owner = owner;
      this.timestamp = timestamp;
      this.post = post;
   }

   public String getOwner()
   {
      return owner;
   }

   public String getTimestamp()
   {
      return timestamp;
   }

   public String getPost()
   {
      return post;
   }

   // Generates the poststring format string for writing to a file
   public String toString()
   {
      // Those are Unicode 0xfff0, not spaces; at the end is Unicode 0xffff
      return owner + "￰" + timestamp + "￰" + post + "￿";
   }
}
