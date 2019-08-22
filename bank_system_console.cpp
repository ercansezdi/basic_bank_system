/*
@auther Ercan sezdi
@version v0.2
@date 21/08/2019
*/
#include <iostream>
#include <ctime> // time library
#include <unistd.h>
#include <string>
#include<bits/stdc++.h>  // string vector library
#include <sstream>  //sting to int library

// defines
#define user_limit  10
#define admin_limit 1

using namespace std;

// structes

struct users{
	string username,name,surname,passwd;
	vector <string> action;
	int balance;

}user[user_limit];
struct admins{
	string username,passwd;
}admin[admin_limit];

// classes
class process_functions
{
public:
void sleep(int i)
{
    for(int j= 0 ; j < 599999999*i ; j++){}
}
void clear_screen()
{
	system("clear");
}

void tire(int space)
{

  for(int i = 0; i < space ; i++)
      cout << " ";
  cout << "-\n";
}
int calcule_theBig()
{
  int syc=0;
  for(int j = 0 ; j < user_limit ; j++)
  {
      if(user[j].username != "")
          syc++;
  }
  int array[syc][4],theBig = 0;
  for(int i = 0 ; i < syc ; i++)
  {
      array[i][0] = user[i].username.length();
      array[i][1] = user[i].passwd.length();
      array[i][2] = user[i].name.length();
      array[i][3] = user[i].surname.length();

      //array[i][4] == user[i].balance.length();
  }
  for(int i = 0 ; i < syc ; i++)
  {
    for(int j = 0 ; j < 4 ; j++)
      {
        if(array[i][j] > theBig)
          theBig = array[i][j];
      }
  }
  return theBig;
}
void space(int length_string,int theBig)
{

  while(length_string < theBig)
  {
    cout << " ";
    length_string++;
  }
  cout << "-\n";

}
int user_limit_found()
{
  int lmt = 0 ;
  for(int i = 0 ; i < user_limit; i++)
  {
    if(user[i].username != "")
      lmt++;
  }
  return lmt;
}
}class_1;

// functions
string process(string process_no);
void admin_menu();
int user_menu(string username, string passwd);



int main()
{

  //class_1.clear_screen();

	process("1");
	// default users
	user[0].username  = "user_1";
	user[0].name 	  = "ercan";
	user[0].surname   = "sezdi";
	user[0].passwd	  = "1234";
	user[0].balance   = 0;
	user[1].username  = "user_2";
	user[1].name 	  = "ahmet";
	user[1].surname   = "kaya";
	user[1].passwd	  = "4321";
	user[1].balance   = 0;
	//default admin
	admin[0].username   = "admin";
	admin[0].passwd     = "admin";
	int exit = 0;
	string  result;

	while(exit != 1)
	{
		result = process("2");

		if(result == "1") // admin Menu
		{
  			string usr,paswd;
  			int counter = 0 ;
  			class_1.clear_screen();
  			cout << "Enter your account name :";
  			cin  >> usr;
  			for(int i = 0 ; i < admin_limit ; i++)
  			{
    				if(admin[i].username == usr)
    				{
      					usr = "OK";
      					break;
    				}
    				counter++;
  			}
  			if(usr == "OK")
  			{
    				cout << "Enter your password : ";
    				cin  >> paswd;

    				if(admin[counter].passwd == paswd)
    					   admin_menu();

  			    else
        				{
        					class_1.clear_screen();
        					cout << "-!-!-!-Wrong password -!-!-!-\n";
        				}
			}
			else
			{
				class_1.clear_screen();
				cout << "-!-!-!- Wrong account name -!-!-!-\n";
			}


		}
		else if(result == "2") // User Menu
		{
			string usr,paswd,yUsr;
			int counter = 0 ;
			class_1.clear_screen();
			cout << "Enter your account name :";
			cin  >> usr;
			for(int i = 0 ; i < user_limit ; i++)
			{

				if(user[i].username == usr)
				{
					yUsr = usr;
					usr = "OK";
					break;
				}
				counter++;

			}
			if(usr == "OK")
			{
				cout << "Enter your password : ";
				cin  >> paswd;

				if(user[counter].passwd == paswd)
					user_menu(yUsr, paswd);

				else
				{
					class_1.clear_screen();
					cout << "-!-!-!-Wrong password -!-!-!-\n";
				}
			}
			else
			{
				class_1.clear_screen();
				cout << "-!-!-!- Wrong account name -!-!-!-\n";
			}
		}
		else if(result == "3") // exit
		{
			class_1.clear_screen();
			cout << "Exiting ...";
			class_1.sleep(2);
			class_1.clear_screen();
			exit = 1;
		}
		else //  Error
		{
			class_1.clear_screen();
			cout << "-!-!-!- Wrong login -!-!-!-\n";
			result = process("2");
		}
	}

	return 0;
}

void admin_menu()
{

  class_1.clear_screen();
	int exit_admin = 1, theBig ;

	cout << "----- Welcome to admin menu -----" << endl << endl ;
	while(exit_admin == 1)
	{


		string process_no;
		process_no = process("3");
		if(process_no == "1") // Add user
		{
			class_1.clear_screen();
			int size = 0;
			for(int i = 0 ; i < user_limit ; i++ )
			{
				if(user[i].username.length() != 0)
					size++;
			}
			string username, passwd, name, surname, error = "0";

			cout <<  "Enter account informations :\n";
			cout <<  "Account name: ";
			cin  >>  username;
			for(int i = 0 ; i < size+1 ; i++ )
			{
				if(username == user[i].username)
				{
					error = "1";
				}
				else
				{

					if(error != "1")
						error = "0";
				}
			}
			if(error != "1")
			{
				error = "0";
				cout <<  "Password : ";
				cin  >>  passwd;

				cout << "Name : ";
				cin  >> name;

				cout << "Surname : ";
				cin  >> surname;
				user[size].name = name;
				user[size].surname = surname;
				user[size].balance = 0;
				user[size].username = username;
				user[size].passwd = passwd;
				class_1.clear_screen();
				cout << "Account added. \n";
        theBig = class_1.calcule_theBig();
			}
			else
				cout << "-!-!-!- Account name already using -!-!-!-\n\n";
		}
		else if(process_no == "2")// delete user
		{
			class_1.clear_screen();
			cout << " --- Hesap silme daha eklenmedi. --- \n\n";
		}
		else if(process_no == "3") // show users
		{
			class_1.clear_screen();
      theBig = class_1.calcule_theBig();
      theBig++;
      theBig++;

      string value = " Account ";
  			for(int i = 0 ; i < class_1.user_limit_found() ; i++)
  			{
    				if(user[i].username.length() != 0)
    				{
                for(int p = 0 ; p < 21 + theBig ; p++)
                  cout << "-";
                cout << endl;
                if((21 + theBig - 4 - value.length()) %  2 == 0) // 21 = "-  Account name  :  " -- > size
                {
                    cout << "-";
                    for(int p = 0 ; p < (21 + theBig - 4 - value.length()) / 2; p++)
                      cout << "-";
                    cout << value << i + 1<< " ";
                    for(int p = 0 ; p < (21 + theBig - 4 - value.length()) / 2 ; p++)
                      cout << "-";
                    cout << "-";
                }
                else if((21 + theBig - 4 - value.length()) %  2 == 1)
                {
                    cout << "--";
                    for(int p = 0 ; p < (21 + theBig - 4 - value.length()-1) / 2; p++)
                      cout << "-";
                    cout << value << i + 1<< " ";
                    for(int p = 0 ; p < (21 + theBig - 4 - value.length()-1)/2; p++)
                      cout << "-";
                    cout << "-";
                }
                cout << endl;
                for(int p = 0 ; p < 21 + theBig ; p++)
                  cout << "-";
                cout << endl;
              	cout << "-  Account name  :  " << user[i].username ; // 19 + string length
                class_1.space(user[i].username.length(),theBig);
      					cout << "-  Password      :  " << user[i].passwd ;
                class_1.space(user[i].passwd.length(),theBig);
      					cout << "-  Name          :  " << user[i].name;
                class_1.space(user[i].name.length(),theBig);
      					cout << "-  Surname       :  " << user[i].surname;
                class_1.space(user[i].surname.length(),theBig);

      					//cout << "- Balance        : " << user[i].balance << " TL" << endl;

    				}
  			}
        for(int p = 0 ; p < 21 + theBig ; p++)
          cout << "-";
        cout << endl;

		}
		else
		{
			class_1.clear_screen();
			exit_admin = 0;
		}
	}
}
string process(string process_no)
{
	//   variables
	string islem;
	int number;
	istringstream iss (process_no);
	iss >> number;
	switch(number)
	{
		case 1:
		{
			time_t tt;
			struct tm*ti;
			time(&tt);
			ti = localtime(&tt);

      cout << "|----------------------------------------|" << endl;
      cout << "          Basic Bank System v.01      "<< endl;
      cout << "|----------------------------------------|"<< endl;
      cout << " Mersin, Turkey "  << asctime(ti);
      cout << "|----------------------------------------|"<< endl;
			break;
		}
		case 2:
		{

			cout << "\n---------------------\n\n";
			cout << "1  -- > Admin Menu "  << endl;
			cout << "2  -- > User Menu  "  << endl;
			cout << "3  -- > Exit" << endl;
			cout << "\n---------------------\n";
			cout << ">>"; cin >> islem;
			while(islem != "1" && islem != "2" && islem != "3" )
			{
				class_1.clear_screen();
        cout << "\n---------------------\n\n";
  			cout << "1  -- > Admin Menu "  << endl;
  			cout << "2  -- > User Menu  "  << endl;
  			cout << "3  -- > Exit" << endl;
  			cout << "\n---------------------\n";
				cout << "Wrong input :\n>> ";
				cin  >> islem;
			}
			break;
		}
		case 3:
		{
			cout << "1  - > Add account \n";
			cout << "2  - > Delete account \n";
			cout << "3  - > Show accounts \n";
			cout << "4  - > Exit Admin Menu \n";
			cout << ">>";
			cin  >> islem;
			while(islem != "1" && islem != "2" && islem != "3" && islem != "4")
			{
				class_1.clear_screen();
        cout << "1  - > Add account \n";
  			cout << "2  - > Delete account \n";
  			cout << "3  - > Show accounts \n";
  			cout << "4  - > Exit Admin Menu \n";
				cout << "Wrong input :\n>> ";
				cin  >> islem;
			}
			break;
		}
		case 4:
		{
			cout << "1  - > Deposit money \n";
			cout << "2  - > Withdraw money \n";
			cout << "3  - > Transfer money \n";
			cout << "4  - > My account information \n";
			cout << "5  - > Exit user menu \n";
			cout << ">>";
			cin  >> islem;
			while(islem != "1" && islem != "2" && islem != "3" && islem != "4" && islem != "5")
			{
				class_1.clear_screen();
        cout << "1  - > Deposit money \n";
  			cout << "2  - > Withdraw money \n";
  			cout << "3  - > Transfer money \n";
  			cout << "4  - > My account information \n";
  			cout << "5  - > Exit user menu \n";
				cout << "Wrong input :\n>> ";
				cin  >> islem;
			}
			break;
		}
		default:
		{
			cout << "Wrong input return False\n";
			islem = "0";
		}

	}
	return islem;

}
int user_menu(string username, string passwd)
{
	int exit_user = 1;
	class_1.clear_screen();
	cout << "----- Welcome to user menu -----" << endl << endl ;
	while(exit_user == 1)
	{
		string result;
		result = process("4");
		string real_value;
		int value = 0;
		if(result == "1") // deposit money
		{
			class_1.clear_screen();
			cout << "How much do you wish to deposite :";
			cin  >> real_value;
			stringstream geek(real_value);
    		geek >> value;
			if(value > 0)
				for(int i = 0 ; i < user_limit ; i++)
				{
					if(user[i].username == username)
					{
						class_1.clear_screen();
						user[i].balance += value;
						real_value = "Deposit " + real_value + " TL." ;
						user[i].action.push_back(real_value);
						cout << "You have deposit " << value << " TL\n";
						class_1.sleep(2);
						class_1.clear_screen();
					}
				}
			else
				cout << "!_!_! Wrong money entry !_!_!";

		}
		else if(result == "2") // withdraw money
		{
  			class_1.clear_screen();
  			cout << "How much do you wish to withdraw  :";
  			cin  >> real_value;
  			stringstream geek(real_value);
      	geek >> value;
    		if(value > 0 )
        {
        			for(int i = 0 ; i < user_limit ; i++)
        			{
          				if(user[i].username == username)
          				{
              					if(user[i].balance > value)
              					{
                            class_1.clear_screen();
                						user[i].balance -= value;
                						real_value = "Withdrawed " + real_value + " TL\n";
                						user[i].action.push_back(real_value);
                            class_1.clear_screen();
                						cout << value << " TL has been withdrawed from your account\n";
                            class_1.sleep(2);
                            class_1.clear_screen();
            					   }
                        else
                            cout << "!_!_! Not enough balance !_!_!" << endl;
                            class_1.sleep(2);
                            class_1.clear_screen();
          				}
    				   }
        }
        else
            cout << "!_!_! Wrong money entry !_!_!";
            class_1.sleep(2);
            class_1.clear_screen();

		}
		else if (result == "3") // para gonder
		{
			class_1.clear_screen();
			string usr_name, control = "False";
			int syc = 0;
			cout << "For who do you wish to transfer to :" << endl;
			cout << ">>";
			cin  >> usr_name;
			for(int j = 0 ; j < user_limit ; j++)
			{
				if(username == user[j].username)
					break;
				syc++;
			}
			for(int i = 0 ; i < user_limit ; i++)
			{

				if(user[i].username == usr_name && usr_name != username) // True User
				{
          class_1.clear_screen();
					string real_value_recovery;
					control = "True";
					cout << "How much would like to transfer :" << endl;
					cout << ">> ";
					cin  >> real_value;
					real_value_recovery  = real_value;
					stringstream geek(real_value);
    				geek >> value;
					if(value > 0 && user[syc].balance > value)
					{
						user[i].balance += value;
						real_value = "Transferred to me from " + username  + " " + real_value + " TL ";
						user[i].action.push_back(real_value);
            class_1.clear_screen();
            cout << real_value << endl;
            class_1.sleep(2);
						class_1.clear_screen();
						for(int j = 0 ; j < user_limit ; j++)
						{
							if(username == user[j].username)
							{
								user[j].balance -= value;
								real_value = "Transferred " + usr_name + " to " + real_value_recovery + " TL";
								user[j].action.push_back(real_value);
							}
						}

					}
					else
					{
						class_1.clear_screen();
						cout << "!_!_! Not enough balance !_!_!" << endl;
						class_1.sleep(2);
						class_1.clear_screen();
					}

				}

			}
			if(control == "False")
			{
				class_1.clear_screen();
				cout << "!_!_! You entered incorrect information. !_!_!" << endl;
				class_1.sleep(2);
				class_1.clear_screen();

			}
			class_1.clear_screen();
		}
		else if(result == "4") // m��teri hareketleri
		{
			class_1.clear_screen();
      for(int i = 0 ; i < user_limit ; i++)
      {
          if(user[i].username == username)
          {
              cout << " ______________________________________________________\n";
              cout << " _____________________ User Data ______________________" << endl << endl;
              cout << "\t\tUsername   : " << user[i].username << endl;
              cout << "\t\tPassword   : " << user[i].passwd << endl;
              cout << "\t\tName       : " << user[i].name << endl;
              cout << "\t\tSurname    : " << user[i].surname << endl;
              cout << "\t\tBalance    : " << user[i].balance << " TL" << endl << endl;
          }
      }
      cout << "________________________________________________________\n";
      cout << "_____________________ Transactions _____________________" << endl << endl;
			int syc = 0;
			for(int i = 0 ; i < user_limit ; i++)
			{
				if(user[i].username == username)
				{
					for (int j=0; j<user[i].action.size(); j++)
					{
						syc = 1;
        				cout << "\t\t" <<  user[i].action[j] << "\n";
        			}
				}
			}
			if(syc == 0)
				cout << "No account information.\n";
    cout << "________________________________________________________"<<endl<<endl << endl;
    class_1.sleep(3);
    class_1.clear_screen();
		}
		else
		{
			class_1.clear_screen();
			exit_user = 0;
		}
	}

	return 0;
}
