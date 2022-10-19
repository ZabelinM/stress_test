#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>


int func(std::vector<int> &data){
    return *std::min_element(data.begin(), data.end());
}

int main() {
    std::string gen_path = "input.txt";
    std::string out_path = "out1.txt";

    std::ifstream fin;
    std::ofstream fout;

    fout.open(out_path);
    fin.open(gen_path);

//    read data
    std::string strdata;
    std::getline(fin, strdata);
    std::vector<int> data;
    std::stringstream iss(strdata);
    int num;
    while (iss >> num){
        data.push_back(num);
    }

//    algo working
    int res = func(data);
    fout << std::to_string(res);


    fin.close();
    fout.close();

    return 0;
}