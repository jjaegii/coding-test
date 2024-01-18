#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    vector<string> s_list;
    string tmp = "";
    for(int i = 0; i < my_string.size(); i++)
    {
        if(my_string[i] >= '0' && my_string[i] <= '9')
        {
            tmp += my_string[i];
        }
        else
        {
            if(tmp.compare("") != 0)
                s_list.push_back(tmp);
            tmp = "";
        }
    }
    if(tmp.compare("") != 0)
        s_list.push_back(tmp);
    for(int i = 0; i < s_list.size(); i++)
    {
        answer += stoi(s_list[i]);
    }
    return answer;
}