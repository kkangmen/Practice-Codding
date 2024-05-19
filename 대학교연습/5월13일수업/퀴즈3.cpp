#include <iostream>
#include <string>
using namespace std;

class Circle{
    int radius;
public:
    Circle (int radius = 0){
        this->radius = radius;
    }
    int getRadius(){
        return radius;
    }
    void setRadius(int radius){
        this->radius = radius;
    }
    double getArea(){
        return 3.14*radius*radius;
    }
};

class NamedCircle: public Circle{
    int r;
    string name;
public:
    void set(int r, string name){
        
    }
};



int main(){
    NamedCircle c[5];
    cout << "5개의 정수 반지름과 원의 이름을 입력하세요" << '\n';
    for (int i = 0; i < 5; i++){
        int r;
        string name;
        cout << i+1 << ">> ";
        cin >> r;
        getline(cin, name);
        if (r <= 0){
            cout << "다시 입력하세요" << '\n';
            i--;
            continue;
        }
        c[i].set(r, name);
    }
    cout << "가장 면적이 큰 피자는 " << biggest(c,5) << "입니다." << '\n';
    return 0;
}