#include <iostream>
#include <thread>
#include <fstream>
#include <map>
#include <cstring>
#include <cmath>
#include <string>
#include <chrono>

using namespace std::chrono_literals;

void RefreshVreme(std::map<std::string, int > forecastMap)
{
    while (true)
    {
        for(auto item : forecastMap)
        {
            item.second++;
            std::cout<<  item.first<< " - "<<item.second<< std::endl;
        }
        std::this_thread :: sleep_for(2000ms);
    }
}

void function()
{
    for(int i=0; i<=400;i++)
        std::cout<<"hey ";
}
void function1()
{
    for(int i=0; i<=400;i++)
        std::cout<<"there ";
}
void FName(char s[],char id[])
{
    char *p=strtok(s," ");
    p=strtok(NULL," ");
    strcpy(id,p);
    strcat(id,"2022");
    std::cout<<id;
}

int main()
{
    std::ifstream f("data.txt");
    int dataTemp[4];
    char dataWeather[4][21];
    for(int i=0; i<3;i++)
    {
        f>>dataTemp[i];
        f>>dataWeather[i];
    }
    int id;
    std:: thread worker1 (function);
    std:: thread worker2 (function1);
    std:: thread worker3 (FName, "DavidPopovici", id);
    std::map<std::string, int> forecastMap=
    {
        {"Bucuresti",dataTemp[0]},
        {"Brasov", dataTemp[1]},
        {"Suceava", dataTemp[2]}
    };
    worker1.join();
    worker2.join();
    std::cout<<std::endl;
    worker3.join();
    return 0;
}