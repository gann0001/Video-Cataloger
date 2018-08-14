/**
 * @author Sumith Kumar Gannarapu
 *
 */
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.sql.*;

public class Individual_Project {
 public static void main(String[] args) throws ClassNotFoundException, SQLException {
  //Loading a database driver 
  try {
   Class.forName("oracle.jdbc.driver.OracleDriver");
  } catch (Exception e) {
   System.out.println("Unable to load the driver class");
  }
  Connection conn = null;
  //Creating an Oracle JDBC Connection.
  try {

   System.out.println("Connecting to database...");
   conn = DriverManager.getConnection("jdbc:oracle:thin:@//oracle.cs.ou.edu:1521/pdborcl.cs.ou.edu", "gann0001", "DSlt3Dt5");
   System.out.println("connection established");
   //Creating a JDBC Statement object 
   Statement st = conn.createStatement();
   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
   String query;
   String query1;
   System.out.println("WELCOME TO PAN CLIENT AND DONOR DATABASE SYSTEM");
   while (true) {
    System.out.println("-------------------------------------- OPTIONS -----------------------------------");
    System.out.println("1.	Enter a new team into the database");
    System.out.println("2.	Enter a new client into the database and associate him or her with one or more teams");
    System.out.println("3.	Enter a new volunteer into the database and associate him or her with one or more teams");
    System.out.println("4.	Enter the number of hours a volunteer worked this month for a particular team");
    System.out.println("5.	Enter a new employee into the database and associate him or her with one or more teams");
    System.out.println("6.	Enter an expense charged by an employee");
    System.out.println("7.	Enter a new organization and associate it to one or more PAN teams");
    System.out.println("8.	Enter a new donor and associate him or her with several donations");
    System.out.println("9.	Enter a new organization and associate it with several donations");
    System.out.println("10.	Retrieve the name and phone number of the doctor of a particular client");
    System.out.println("11.	Retrieve the total amount of expenses charged by each employee for a particular period of time. The list should be sorted by the total amount of expenses");
    System.out.println("12.	Retrieve the list of volunteers that are members of teams that support a particular client");
    System.out.println("13.	Retrieve the names and contact information of the clients that are supported by teams sponsored by an organization whose name starts with a letter between B and K. The client list should be sorted by name");
    System.out.println("14.	Retrieve the name and total amount donated by donors that are also employees. The list should be sorted by the total amount of the donations, and indicate if each donor wishes to remain anonymous");
    System.out.println("15.	For each team, retrieve the name and associated contact information of the volunteer that has worked the most total hours between March and June");
    System.out.println("16.	Increase the salary by 10% of all employees to whom more than one team must report");
    System.out.println("17.	Delete all clients who do not have health insurance and whose value of importance for transportation is less than 5");
    System.out.println("18.	Import: Enter new teams from a data file until the file is empty");
    System.out.println("19.	Export: Retrieve names and mailing addresses of all people on the mailing list and output them to a data file");
    System.out.println("20.	Quit");
    System.out.println("Enter Your Choice");
    int choice = Integer.parseInt(br.readLine());
    switch (choice) {
     case 1:
      //Enter a new team into the database
      // Storing Values in variables
      System.out.println("Enter Team Name:");
      String team_name = br.readLine();
      System.out.println("Enter Team Type:");
      String team_type = br.readLine();
      System.out.println("Enter Team Form Date - Please enter date in the form of 01-JAN-2017:");
      String team_form_date = br.readLine();
      query = "Insert into Team values('" + team_name + "','" + team_type + "','" + team_form_date + "')";
      st.executeUpdate(query);
      System.out.println("Database records for team table has been inserted");
      break;

     case 2:
      //Enter a new client into the database and associate him or her with one or more teams
      // Storing Values in variables
      System.out.println("Executing Query 2 ...");
      System.out.println("Enter Client SSN:");
      int client_ssn = Integer.parseInt(br.readLine());
      System.out.println("Enter Doctor Name:");
      String client_doc_name = br.readLine();
      System.out.println("Enter Doctor Phone Number:");
      long client_doc_phn = Long.parseLong(br.readLine());
      System.out.println("Enter Attorney Name:");
      String client_attorney_name = br.readLine();
      System.out.println("Enter Attorney Phone Number:");
      long client_attorney_phn = Long.parseLong(br.readLine());
      System.out.println("Enter Client Assign Date - Please enter date in the form of 01-JAN-2017:");
      String client_assign_date = br.readLine();
      query = "Insert into clients values(" + client_ssn + ",'" + client_doc_name + "','" + client_doc_phn + "','" + client_attorney_name + "','" + client_attorney_phn + "','" + client_assign_date + "')";
      st.executeUpdate(query);
      System.out.println("How many teams you want to associate\t" + client_ssn + "\tclient ?");
      int num = Integer.parseInt(br.readLine());
      for (int i = 1; i <= num; i++) {
       System.out.println("Enter Team Name:");
       team_name = br.readLine();
       System.out.println("Enter Team Care Status:");
       String team_care_status = br.readLine();
       query1 = "insert into team_cares values(" + client_ssn + ",'" + team_name + "','" + team_care_status + "')";
       st.executeUpdate(query1);
      }
      System.out.println("Database records for clients table has been inserted and" + client_ssn + "associated with one or more teams");
      break;

     case 3:
      //Enter a new volunteer into the database and associate him or her with one or more teams
      // Storing Values in variables
      System.out.println("Enter Volunteer SSN:");
      int vol_ssn = Integer.parseInt(br.readLine());
      System.out.println("Enter Vol Join Date - Please enter date in the form of 01-JAN-2017:");
      String vol_join_date = br.readLine();
      System.out.println("Enter Vol Train Date - Please enter date in the form of 01-JAN-2017:");
      String vol_train_date = br.readLine();
      System.out.println("Enter Vol Train Location:");
      String vol_train_loc = br.readLine();
      query = "Insert into volunteer values('" + vol_ssn + "','" + vol_join_date + "','" + vol_train_date + "','" + vol_train_loc + "')";
      st.executeUpdate(query);
      System.out.println("How many teams you want to associate\t" + vol_ssn + "\tVolunteer?");
      num = Integer.parseInt(br.readLine());
      for (int i = 1; i <= num; i++) {
       System.out.println("Enter Team Name:");
       team_name = br.readLine();
       System.out.println("Enter No Of Hours worked:");
       int no_of_hours = Integer.parseInt(br.readLine());
       System.out.println("Enter Serve Months:");
       int serve_months = Integer.parseInt(br.readLine());
       System.out.println("Enter Team Care Status:");
       String team_care_status = br.readLine();
       query1 = "insert into vol_serve values('" + vol_ssn + "','" + team_name + "','" + no_of_hours + "','" + serve_months + "','" + team_care_status + "')";
       st.executeUpdate(query1);
      }
      System.out.println("Database records for Volunteer table has been inserted and\t" + vol_ssn + "\tassociated with one or more teams");
      break;

     case 4:
      //Enter the number of hours a volunteer worked this month for a particular team
      // Storing Values in variables
      System.out.println("Enter Volunteer SSN:");
      vol_ssn = Integer.parseInt(br.readLine());
      System.out.println("Enter Team Name:");
      team_name = br.readLine();
      System.out.println("Enter No Of Hours:");
      int no_of_hours = Integer.parseInt(br.readLine());
      System.out.println("Enter Serve Month:");
      int serve_months = Integer.parseInt(br.readLine());
      System.out.println("Enter Team Care Status:");
      String team_care_status = br.readLine();
      query = "insert into vol_serve values('" + vol_ssn + "','" + team_name + "','" + no_of_hours + "','" + serve_months + "','" + team_care_status + "')";
      st.executeUpdate(query);
      System.out.println("Database records for Volunteer with number of hours worked for particular months has been inserted");
      break;

     case 5:
      //Enter a new employee into the database and associate him or her with one or more teams
      // Storing Values in variables
      System.out.println("Enter Employee SSN:");
      int emp_ssn = Integer.parseInt(br.readLine());
      System.out.println("Enter Employee Salary:");
      int emp_sal = Integer.parseInt(br.readLine());
      System.out.println("Enter Marrital Status:");
      String emp_marrital_status = br.readLine();
      System.out.println("Enter Hire Date - Please enter date in the form of 01-JAN-2017:");
      String emp_hire_date = br.readLine();
      query = "Insert into employee values('" + emp_ssn + "','" + emp_sal + "','" + emp_marrital_status + "','" + emp_hire_date + "')";
      st.executeUpdate(query);
      System.out.println("How many teams you want to associate\t" + emp_ssn + "\tEmployee?");
      num = Integer.parseInt(br.readLine());
      for (int i = 1; i <= num; i++) {
       System.out.println("Enter Team Name:");
       team_name = br.readLine();
       System.out.println("Enter Report Date - Please enter date in the form of 01-JAN-2017:");
       String report_date = br.readLine();
       System.out.println("Enter Report Description:");
       String report_desc = br.readLine();
       query1 = "insert into report_emp values('" + emp_ssn + "','" + team_name + "','" + report_date + "','" + report_desc + "')";
       st.executeUpdate(query1);
      }
      System.out.println("Database records for employee table has been inserted and\t" + emp_ssn + "\tassociated with one or more teams");
      break;

     case 6:
      //Enter an expense charged by an employee
      // Storing Values in variables
      System.out.println("Enter Employee SSN:");
      emp_ssn = Integer.parseInt(br.readLine());
      System.out.println("Enter Expense Date - Please enter date in the form of 01-JAN-2017:");
      String expense_date = br.readLine();
      System.out.println("Enter Expense Amount:");
      int expense_amnt = Integer.parseInt(br.readLine());
      System.out.println("Enter Expense Description:");
      String expense_descr = br.readLine();
      query = "Insert into emp_expense values('" + emp_ssn + "','" + expense_date + "','" + expense_amnt + "','" + expense_descr + "')";
      st.executeUpdate(query);
      System.out.println("Database records for Expense charged by an employee emp_expense table has been inserted");
      break;

     case 7:
      //Enter a new organization and associate it to one or more PAN teams
      // Storing Values in variables
      System.out.println("Enter Organization Name:");
      String org_name = br.readLine();
      System.out.println("Enter Mail Address:");
      String mail_addr = br.readLine();
      System.out.println("Enter Phone Number:");
      Long org_phn_num = Long.parseLong(br.readLine());
      System.out.println("Enter Contact Person:");
      String contact_person = br.readLine();
      System.out.println("Enter Organization Anonymus Status:");
      String org_anon_status = br.readLine();
      query = "Insert into organizations values('" + org_name + "','" + mail_addr + "','" + org_phn_num + "','" + contact_person + "','" + org_anon_status + "')";
      st.executeUpdate(query);
      System.out.println("How many teams you want to associate\t" + org_name + "\tOrganization?");
      num = Integer.parseInt(br.readLine());
      for (int i = 1; i <= num; i++) {
       System.out.println("Enter Team Name:");
       team_name = br.readLine();
       query1 = "insert into sponsors values('" + team_name + "','" + org_name + "')";
       st.executeUpdate(query1);
      }
      System.out.println("Database records for Organizations table has been inserted and\t" + org_name + "\tassociated with one or more teams");
      break;

     case 8:
      //Enter a new donor and associate him or her with several donations
      // Storing Values in variables
      System.out.println("Enter Donor SSN:");
      int donor_ssn = Integer.parseInt(br.readLine());
      System.out.println("Enter Donor Anonymus Status:");
      String donor_anon_status = br.readLine();
      query = "Insert into donor values('" + donor_ssn + "','" + donor_anon_status + "')";
      st.executeUpdate(query);
      System.out.println("How many donations you want to associate\t" + donor_ssn + "\tdonor?");
      num = Integer.parseInt(br.readLine());
      for (int i = 1; i <= num; i++) {
       System.out.println("Enter Donate Date - Please enter date in the form of 01-JAN-2017:");
       String donate_date = br.readLine();
       System.out.println("Enter Donate Amount:");
       int donate_amount = Integer.parseInt(br.readLine());
       System.out.println("Enter Campaign Name:");
       String campain_name = br.readLine();
       query1 = "insert into donor_donations values('" + donor_ssn + "','" + donate_date + "','" + donate_amount + "','" + campain_name + "')";
       st.executeUpdate(query1);
      }
      System.out.println("Database records for donor table has been inserted and\t" + donor_ssn + "\tassociated with several donations");
      break;

     case 9:
      //Enter a new organization and associate it with several donations
      // Storing Values in variables
      System.out.println("Enter Organization Name:");
      org_name = br.readLine();
      System.out.println("Enter Mail Address:");
      mail_addr = br.readLine();
      System.out.println("Enter Organization Phone Number:");
      org_phn_num = Long.parseLong(br.readLine());
      System.out.println("Enter Contact Person:");
      contact_person = br.readLine();
      System.out.println("Enter Organization Anonymus Status:");
      org_anon_status = br.readLine();
      query = "Insert into organizations values('" + org_name + "','" + mail_addr + "','" + org_phn_num + "','" + contact_person + "','" + org_anon_status + "')";
      st.executeUpdate(query);
      System.out.println("How many donations you want to associate\t" + org_name + "\torganization?");
      num = Integer.parseInt(br.readLine());
      for (int i = 1; i <= num; i++) {
       System.out.println("Enter Donate Date - Please enter date in the form of 01-JAN-2017:");
       String donate_date = br.readLine();
       System.out.println("Enter Donate Amount:");
       int donate_amount = Integer.parseInt(br.readLine());
       System.out.println("Enter Campaign Name:");
       String campain_name = br.readLine();
       query1 = "insert into org_donations values('" + org_name + "','" + donate_date + "','" + donate_amount + "','" + campain_name + "')";
       st.executeUpdate(query1);
      }
      System.out.println("Database records for organizations table has been inserted and" + org_name + "associated with several donations");
      break;

     case 10:
      //Retrieve the name and phone number of the doctor of a particular client
      System.out.println("Enter Client SSN");
      client_ssn = Integer.parseInt(br.readLine());
      query = "Select CLIENT_DOC_NAME, CLIENT_DOC_PHN from clients Where CLIENT_SSN = " + client_ssn + "";
      ResultSet rs = st.executeQuery(query);
      System.out.println("CLIENT_DOC_NAME\tCLIENT_DOC_PHONE");
      System.out.println("----------------------------------");
      while (rs.next()) {
       System.out.println(rs.getString(1) + "\t|\t " + rs.getString(2));
      }
      break;

     case 11:
      //Retrieve the total amount of expenses charged by each employee for a particular period of time. The list should be sorted by the total amount of expenses
      System.out.println("Employee Expense Charged Start Date - Please enter date in the form of 01-JAN-2017:");
      String start_date = br.readLine();
      System.out.println("Employee Expense Charged End Date - Please enter date in the form of 01-JAN-2017:");
      String end_date = br.readLine();
      query = "SELECT EMP_SSN,SUM(EXPENSE_AMNT) AS TOTAL_AMOUNT_EXPENSES FROM EMP_EXPENSE WHERE EXPENSE_DATE BETWEEN  '" + start_date + "'  AND '" + end_date + "' GROUP BY EMP_SSN ORDER BY TOTAL_AMOUNT_EXPENSES DESC";
      rs = st.executeQuery(query);
      System.out.println("EMP_SSN\tTOTAL_AMOUNT_EXPENSES");
      System.out.println("----------------------------------");
      while (rs.next()) {
       System.out.println(rs.getString(1) + "\t|\t " + rs.getString(2));
      }
      break;

     case 12:
      //Retrieve the list of volunteers that are members of teams that support a particular client
      System.out.println("Enter Client SSN:");
      client_ssn = Integer.parseInt(br.readLine());
      query = "Select v.VOL_SSN from VOLUNTEER v\n" +
       "JOIN VOL_SERVE vs ON v.VOL_SSN = vs.VOL_SSN\n" +
       "JOIN TEAM t ON vs.TEAM_NAME = t.TEAM_NAME\n" +
       "JOIN TEAM_CARES tc ON t.TEAM_NAME = tc.TEAM_NAME\n" +
       "JOIN CLIENTS c  ON tc.CLIENT_SSN = c.CLIENT_SSN\n" +
       "WHERE c.CLIENT_SSN = " + client_ssn + "";
      rs = st.executeQuery(query);
      System.out.println("Volunteer SSN");
      System.out.println("----------------");
      while (rs.next()) {
       System.out.println(rs.getString(1));
      }
      break;

     case 13:
      //Retrieve the names and contact information of the clients that are supported by teams sponsored by an organization whose name starts with a letter between B and K. The client list should be sorted by name
      query = "SELECT NAME,MAIL_ADDR,EMAIL_ID,HOME_PHN,WORK_PHN,CELL_PHN FROM PERSON P\n" +
       "JOIN CLIENTS C ON P.SSN = C.CLIENT_SSN\n" +
       "JOIN TEAM_CARES TC ON C.CLIENT_SSN = TC.CLIENT_SSN\n" +
       "JOIN TEAM T ON TC.TEAM_NAME = T.TEAM_NAME\n" +
       "WHERE TC.TEAM_NAME IN \n" +
       "(SELECT TEAM_NAME FROM SPONSORS WHERE ORG_NAME BETWEEN 'B%' AND 'K%')";
      rs = st.executeQuery(query);
      System.out.println("Name \t Mail Address \t Email Id \t Home Phone \t Work Phone \t Cell Phone");
      System.out.println("--------------------------------------------------------------------------");
      while (rs.next()) {
       System.out.println(rs.getString(1) + "|\t " + rs.getString(2) + "|\t " + rs.getString(3) + "|\t " + rs.getString(4) + "|\t " + rs.getString(5) + "|\t " + rs.getString(6));
      }
      break;

     case 14:
      //Retrieve the name and total amount donated by donors that are also employees. The list should be sorted by the total amount of the donations, and indicate if each donor wishes to remain anonymous
      query = "SELECT P.NAME, SUM(DD.DONATE_AMOUNT), D.DONOR_ANON_STATUS AS SUM_OF_DONATE_AMOUNT FROM DONOR D \n" +
       "JOIN EMPLOYEE E ON D.DONOR_SSN = E.EMP_SSN\n" +
       "JOIN PERSON P ON P.SSN = E.EMP_SSN\n" +
       "JOIN DONOR_DONATIONS DD ON D.DONOR_SSN = DD.DONOR_SSN\n" +
       "GROUP BY P.NAME, D.DONOR_ANON_STATUS";
      rs = st.executeQuery(query);
      System.out.println("Name \t Sum of Donation \t Anonymus Status ");
      System.out.println("--------------------------------------------");
      while (rs.next()) {
       System.out.println(rs.getString(1) + " |\t " + rs.getString(2) + " |\t " + rs.getString(3));
      }
      break;

     case 15:
      //For each team, retrieve the name and associated contact information of the volunteer that has worked the most total hours between March and June
      query = " WITH DATA AS ( SELECT P.NAME,P.MAIL_ADDR,P.EMAIL_ID," + "P.HOME_PHN,P.WORK_PHN,P.CELL_PHN,VS.TEAM_NAME, VS.NO_OF_HOURS,V.VOL_SSN FROM person p " + "INNER JOIN volunteer v ON v.vol_ssn = p.ssn INNER JOIN VOL_SERVE VS ON VS.VOL_SSN = v.VOL_SSN " + "INNER JOIN TEAM T ON T.TEAM_NAME = VS.TEAM_NAME WHERE VS.SERVE_MONTHS >=3 AND VS.SERVE_MONTHS  <=6  )," + "MAXHOURSTEAM AS (SELECT DISTINCT MAX(NO_OF_HOURS) AS HOURSMAX, TEAM_NAME FROM DATA GROUP BY TEAM_NAME ) " + "SELECT DT.NAME,DT.MAIL_ADDR,DT.EMAIL_ID,DT.HOME_PHN,DT.WORK_PHN,DT.CELL_PHN,DT.TEAM_NAME FROM DATA DT " + "INNER JOIN MAXHOURSTEAM MT ON MT.TEAM_NAME = DT.TEAM_NAME AND MT.HOURSMAX = DT.NO_OF_HOURS  ";
      rs = st.executeQuery(query);
      System.out.println("Name \t Mail Address \t Email Id \t Home Phone \t Work Phone \t Cell Phone\t Team Name");
      System.out.println("--------------------------------------------------------------------------");
      while (rs.next()) {
       System.out.println(rs.getString(1) + " |\t " + rs.getString(2) + " |\t " + rs.getString(3) + " |\t " + rs.getString(4) + " | " + rs.getString(5) + " | " + rs.getString(6) + " | " + rs.getString(7));
      }
      break;

     case 16:
      //Increase the salary by 10% of all employees to whom more than one team must report
      System.out.println("Executing Query 16.... ");
      query = "UPDATE EMPLOYEE SET EMP_SAL = EMP_SAL*1.1 WHERE EMP_SSN IN\n" +
       "(SELECT RE.EMP_SSN FROM EMPLOYEE E \n" +
       "JOIN REPORT_EMP RE ON E.EMP_SSN = RE.EMP_SSN\n" +
       "GROUP BY RE.EMP_SSN HAVING COUNT(RE.EMP_SSN)>= 2)";
      rs = st.executeQuery(query);
      System.out.println("Eligible Employees salary has been increased");
      query1 = "select * from EMPLOYEE";
      rs = st.executeQuery(query1);
      System.out.println("Emp SSN \t Emp Salary \t Marrital Status \t Hire Date ");
      System.out.println("------------------------------------------------------");
      while (rs.next()) {
       System.out.println(rs.getString(1) + " |\t " + rs.getString(2) + " |\t " + rs.getString(3) + " |\t " + rs.getString(4));
      }
      break;

     case 17:
      //Delete all clients who do not have health insurance and whose value of importance for transportation is less than 5 
      System.out.println("Executing query 17.... ");
      query = "DELETE FROM CLIENTS WHERE CLIENT_SSN IN\n" +
       "(SELECT C.CLIENT_SSN FROM CLIENTS C\n" +
       "JOIN COVERED_BY CB ON CB.CLIENT_SSN = C.CLIENT_SSN\n" +
       "JOIN INSURANCE_POLICY IP ON IP.POLICY_ID =CB.POLICY_ID AND IP.POLICY_TYPE != 'HEALTH' \n" +
       "INTERSECT \n" +
       "SELECT C.CLIENT_SSN FROM CLIENTS C\n" +
       "JOIN CLIENT_NEED CN ON CN.CLIENT_SSN = C.CLIENT_SSN AND  CN.NEED_TYPE ='TRANSPORTATION'\n" +
       "WHERE CN.IMPORTANCE < 5)";
      rs = st.executeQuery(query);
      System.out.println("Clients who do not have health insurance and whose transport importance less than 5 records deleted");
      break;

     case 18:
      /* Import: Enter new team from a data file */
      System.out.println("Enter import file name: ");
      String file_name = br.readLine();
      FileInputStream fstream = new
      FileInputStream("/Users/sumithkumargannarapu/Desktop/" + file_name);
      DataInputStream in = new DataInputStream(fstream);
      BufferedReader br1 = new BufferedReader(new InputStreamReader( in ));
      String strLine;
      while ((strLine = br1.readLine()) != null) {
       String a[] = strLine.split("\\t+");
       team_name = a[0];
       team_type = a[1];
       String team_date = a[2];
       st.executeUpdate("insert into team values('" + team_name + "','" + team_type + "','" + team_date + "')");
       System.out.println(" One row inserted succesfully");
      }
      System.out.println("File imported succesfully!!!");
      break;
     case 19:
      /* Export: Retrieve name and mail address and output them to a data file */
      ResultSet rs2 = st.executeQuery("select name,mail_addr from person");
      String string = null;
      System.out.println("Enter output file name: ");
      file_name = br.readLine();
      BufferedWriter
      export = new BufferedWriter(new FileWriter("/Users/sumithkumargannarapu/Desktop/" + file_name));
      while (rs2.next()) {
       string = rs2.getString("name") + " " + rs2.getString("mail_addr");
       export.write("\n");
       export.write(string);
       export.write("\n");
       System.out.println(" One row inserted succesfully!");
      }
      System.out.println(" File exported succesfully!!!");
      export.close();
      break;
     case 20:
      //Close the statement
      st.close();
      //close the database connection
      conn.close();
      //Terminate the program
      System.exit(0);
     default:
      //default message indicates user to give a chance to enter between 1 to 20
      System.out.println("Select Options between 1-20");
    }
   }
  } catch (Exception e) {
   e.printStackTrace();
  }
 }
}