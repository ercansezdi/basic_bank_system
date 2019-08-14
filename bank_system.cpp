#include <iostream>
#include <ctime> // time library
#include <locale.h> // language library
#include <string> 
#include<bits/stdc++.h>  // string vector library
#include <sstream>  //sting to int library

// defines 
#define user_limit  10
#define admin_limit 1
#define no_limit 999

using namespace std;
// classes
class process_functions
{
public:
void sleep(int i)
{	
	for(int j =  0 ;j < i*500000000; j++ ){}
}
void clear_screen()
{
	system("CLS");
}
void wait()
{
	cout << "\n\n";
	system("pause");
}
}class_1;
// functions
string process(int process_no);
int admin_menu();
int user_menu(string username, string passwd);

// structes

struct users{
	string username,name,surname,passwd;
	vector <string> action; 
	int balance;
	
}user[user_limit];
struct admins{
	string username,passwd;
}admin[admin_limit];

int main()
{
	
	setlocale(LC_ALL,"Turkish"); // active of Turkish language
	
	process(1);
	// default users
	user[0].username  = "askeercan";
	user[0].name 	  = "ercan"; 
	user[0].surname   = "sezdi";
	user[0].passwd	  = "1234";
	user[0].balance   = 0;
	user[1].username  = "trforever";
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
		result = process(2);
	
		if(result == "1") // admin Menu
		{
			string usr,paswd;
			int counter = 0 ;
			class_1.clear_screen();
			cout << "Hesap Ad�n�z� Giriniz :";
			cin  >> usr;
			for(int i = 0 ; i < admin_limit ; i++)
			{
				
				if(admin[i].username == usr)
					usr = "OK";
				if(usr == "OK")
					break;
				counter++;
				
			}
			if(usr == "OK")
			{
				cout << "�ifrenizi Giriniz : ";
				cin  >> paswd;
				
				if(admin[counter].passwd == paswd)
					admin_menu();
					
				else
				{
					class_1.clear_screen();
					cout << "-!-!-!-�ifreniz Yanl�� -!-!-!-\n";	
				}
			}	
			else
			{
				class_1.clear_screen();
				cout << "-!-!-!- Hesap Ad�n�z Yanl�� -!-!-!-\n";
			}
			
			
		}
		else if(result == "2") // User Menu
		{
			string usr,paswd,yUsr;
			int counter = 0 ;
			class_1.clear_screen();
			cout << "Hesap Ad� Giriniz :";
			cin  >> usr;
			for(int i = 0 ; i < user_limit ; i++)
			{
				
				if(user[i].username == usr)
				{
					yUsr = usr;
					usr = "OK";
				}
				if(usr == "OK")
					break;
				counter++;
				
			}
			if(usr == "OK")
			{
				cout << "�ifrenizi Giriniz : ";
				cin  >> paswd;
				
				if(user[counter].passwd == paswd)
					user_menu(yUsr, paswd);
					
				else
				{
					class_1.clear_screen();
					cout << "-!-!-!- �ifreniz Yanl�� -!-!-!-\n";	
				}
			}	
			else
			{
				class_1.clear_screen();
				cout << "-!-!-!- Hesap Ad�n�z Yanl�� -!-!-!-\n";
			}
		}
		else if(result == "3") // exit
		{
			class_1.clear_screen();
			cout << "��k�� Yap�l�yor...";
			class_1.sleep(2);
			class_1.clear_screen();
			exit = 1;
		}
		else //  Error
		{
			class_1.clear_screen();
			cout << "-!-!-!- Hatal� Giri� -!-!-!-\n";
			result = process(2);
		}
	}

	return 0;
}

int admin_menu()
{	
	
	
	int exit_admin = 1;
	class_1.clear_screen();
	cout << "----- Admin Men�ye Ho�geldiniz -----" << endl << endl ;
	while(exit_admin == 1)
	{
		
		
		string process_no;
		process_no = process(3);
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
			
			cout <<  "Hesap Bilgilerini Giriniz :\n";
			cout <<  "Hesap Ad� : ";
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
				cout <<  "�ifre : ";
				cin  >>  passwd;
				
				cout << "�sim : ";
				cin  >> name; 
				
				cout << "Soyisim : ";
				cin  >> surname;
	
				user[size+1].name = name;
				user[size+1].surname = surname;
				user[size+1].balance = 0;
				user[size+1].username = username;
				user[size+1].passwd = passwd;
				class_1.clear_screen();
				cout << "Hesap Ekleniyor...";
				class_1.sleep(2);
				class_1.clear_screen();
				cout << "HEsap Eklendi.";
				class_1.sleep(1);
				class_1.clear_screen();
			}
			else
				cout << "-!-!-!- Hesap Ad� Zaten Kullan�l�yor -!-!-!-\n\n";
		}
		else if(process_no == "2")// delete user
		{
			class_1.clear_screen();
			cout << " --- Hesap silme daha eklenmedi. --- \n\n";
			class_1.sleep(2);
			class_1.clear_screen();
		}
		else if(process_no == "3") // show users
		{
			class_1.clear_screen();
			
			cout << "------------------------\n";
			for(int i = 0 ; i < user_limit ; i++)
			{
				if(user[i].username.length() != 0)
				{
					cout << "Hesap Ad�   : " << user[i].username << endl;
					cout << "�ifre       : " << user[i].passwd << endl;
					cout << "�sim        : " << user[i].name << endl;
					cout << "Soyisim     : " << user[i].surname << endl;
					cout << "Bakiye      : " << user[i].balance << " TL" << endl; 
					cout << "------------------------\n";
	 				
				}
			}
			
			class_1.wait();
			class_1.clear_screen();
		}
		else
		{
			class_1.clear_screen();
			exit_admin = 0;
		}
	}
}
string process(int process_no)
{
	//   variables
	string islem;
	
	switch(process_no)
	{
		case 1:
		{
			time_t tt;
			struct tm*ti;
			time(&tt);
			ti = localtime(&tt);
			cout << "--\tHo�geldiniz" << endl;
			cout << "--\tBank System V.0.1 " << endl;
			cout << "--\t" <<  asctime(ti);
			break;
		}
		case 2:
		{
			
			cout << "\n---------------------\n";
			cout << "1  -- > Admin Men� "  << endl;
			cout << "2  -- > Kullan�c� Men�  "  << endl;
			cout << "3  -- > ��k�� " << endl; 
			cout << "��lem Se�iniz : ";
			cout << "\n---------------------\n";
			cout << ">>"; cin >> islem;
			while(islem != "1" && islem != "2" && islem != "3" )
			{
				class_1.clear_screen();
				cout << "Hatal� Giri� :\n>> ";
				cin  >> islem;
			}
			break;
		}
		case 3:
		{
			cout << "��lem Se�iniz : \n";
			cout << "1  - > Kullan�c� Ekle \n";
			cout << "2  - > Kullan�c� Sil \n";
			cout << "3  - > Kullan�c�lar� G�ster \n";
			cout << "4  - > Admin Men�den ��k \n";
			cout << ">>";
			cin  >> islem;
			while(islem != "1" && islem != "2" && islem != "3" && islem != "4")
			{
				class_1.clear_screen();
				cout << "Hatal� Giri� :\n>> ";
				cin  >> islem;
			}
			break;
		}
		case 4:
		{
			cout << "Please select process : \n";
			cout << "1  - > Para Yat�rma \n";
			cout << "2  - > Para �ekme \n";
			cout << "3  - > Para G�nderme \n";
			cout << "4  - > Dekontlar \n";
			cout << "5  - > M��teri Bilgileri \n";
			cout << "6  - > Kullan�c� Men�den ��k \n";
			cout << ">>";
			cin  >> islem;
			while(islem != "1" && islem != "2" && islem != "3" && islem != "4" && islem != "5" && islem != "6")
			{
				class_1.clear_screen();
				cout << "Hatal� Giri� :\n>> ";
				cin  >> islem;
			}
			break;
		}
		default:
		{	
			cout << "Wrong input return False\n";
			islem = "0";
		}
			return islem;
	}
		
}
int user_menu(string username, string passwd)
{
	int exit_user = 1;
	class_1.clear_screen();
	cout << "----- Kullan�c� Men�ye Ho�geldiniz -----" << endl << endl ;
	while(exit_user == 1)
	{
		string result;
		result = process(4);
		string real_value;
		int value = 0; 
		if(result == "1") // para ekle
		{
			class_1.clear_screen();
			cout << "Yat�r�lacak Para Miktar� :";
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
						real_value = "Hesab�n�za " + real_value + " TL  geldi." ;
						user[i].action.push_back(real_value); 
						cout << "Hesab�n�za " << value << " TL  eklendi.";
						class_1.sleep(2);
						class_1.clear_screen();
					}
				}
			else
				cout << "!_!_! Hatal� Para Giri�i !_!_!";
			
		}
		else if(result == "2") // para �ek 
		{
			class_1.clear_screen();	
			cout << "�ekilecek Para Miktar�  :";
			cin  >> real_value;
			stringstream geek(real_value); 
    		geek >> value; 
			if(value > 0 )
				for(int i = 0 ; i < user_limit ; i++)
				{	
				
					if(user[i].username == username)	
					{
						if(user[i].balance > value)
						{
							class_1.clear_screen();	
							user[i].balance -= value;
							real_value = "Hesab�n�zdan " + real_value + " TL  ��kt�.";
							user[i].action.push_back(real_value); 
							cout << "Hesab�n�zdan " << value << " TL  �ekildi.";
							class_1.sleep(2);
							class_1.clear_screen();	
						}
					}
				}
			else
				cout << "!_!_! Hatal� Para Giri�i !_!_!";
		}
		else if (result == "3") // para g�nder
		{
			break;	
			
		}
		else if(result == "4") // m��teri hareketleri
		{
			class_1.clear_screen();
			cout << "---------------------\n";
			int syc = 0;
			for(int i = 0 ; i < user_limit ; i++)
			{	
				if(user[i].username == username)	
				{
					for (int j=0; j<user[i].action.size(); j++) 	
					{
						syc = 1;
        				cout << user[i].action[j] << "\n";
        			}
				}
			}
			if(syc == 0)
				cout << "��lem Bulunamad�.\n";
			cout << "---------------------\n";
			class_1.wait();
			class_1.clear_screen();
		}
		else if(result == "5")// m��teri bilgileri
		{
				for(int i = 0 ; i < user_limit ; i++)
				{	
					if(user[i].username == username)	
					{
						class_1.clear_screen();
						cout << "Kullan�c� Ad�  : " << user[i].username << endl;
						cout << "Kulan�c� �ifre : " << user[i].passwd << endl;
						cout << "�sim           : " << user[i].name << endl;
						cout << "Soyisim        : " << user[i].surname << endl;
						cout << "Bakiye         : " << user[i].balance << " TL" << endl; 	
						class_1.wait();
						class_1.clear_screen();
					}
				}
		}
		else
		{
			class_1.clear_screen();
			exit_user = 0;
		}
	}
	
	return 0;	
}

