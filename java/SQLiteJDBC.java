import java.sql.*;
import java.util.*;

public class SQLiteJDBC
{
  public static void main( String args[] )
  {
    Connection c = null;
    Statement stmt = null;
    try {
      Class.forName("org.sqlite.JDBC");
      c = DriverManager.getConnection("jdbc:sqlite:db.sqlite3");
      c.setAutoCommit(false);
      System.out.println("Opened database successfully");

      stmt = c.createStatement();
      ResultSet rs = stmt.executeQuery("SELECT name FROM sqlite_master WHERE type='table';");

      while ( rs.next() ) {
         String  name = rs.getString("name");
         System.out.println( "NAME = " + name );
         System.out.println();
      }    

      stmt = c.createStatement();
      ResultSet rs1 = stmt.executeQuery("SELECT * FROM auth_user;");
      while ( rs1.next() ) {
        int id = rs1.getInt("id");
         String  name = rs1.getString("username");
         System.out.println( "ID = " + id );
         System.out.println( "NAME = " + name );
         System.out.println();
      }    c.close();

    } catch ( Exception e ) {
      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
      System.exit(0);
    }
    System.out.println("Operation done successfully");
  }
}