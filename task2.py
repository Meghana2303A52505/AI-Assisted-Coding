class Student:
    def __init__(self, name, math_score, science_score):
        self.__name = name
        self.__math_score = math_score
        self.__science_score = science_score
    
    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_math_score(self):
        return self.__math_score
    
    def get_science_score(self):
        return self.__science_score
    
    # Setter methods
    def set_name(self, name):
        self.__name = name
    
    def set_math_score(self, score):
        if 0 <= score <= 100:
            self.__math_score = score
        else:
            raise ValueError("Score must be between 0 and 100")
    
    def set_science_score(self, score):
        if 0 <= score <= 100:
            self.__science_score = score
        else:
            raise ValueError("Score must be between 0 and 100")
    
    # Derived value calculation
    def calculate_average(self):
        return (self.__math_score + self.__science_score) / 2


# Example usage
student = Student("Alice", 85, 90)
print(f"Name: {student.get_name()}")
print(f"Average Score: {student.calculate_average()}")

student.set_math_score(92)
print(f"Updated Average Score: {student.calculate_average()}")

#convert the python class into a C++ class with proper access modifiers and constructor handling and correct data types
#include <iostream>
#include <string>
#include <stdexcept>

class Student {
private:
    std::string name;
    int math_score;
    int science_score;
    
    bool isValidScore(int score) const {
        return score >= 0 && score <= 100;
    }

public:
    // Constructor
    Student(const std::string& n, int math, int science) 
        : name(n), math_score(math), science_score(science) {
        if (!isValidScore(math) || !isValidScore(science)) {
            throw std::invalid_argument("Score must be between 0 and 100");
        }
    }
    
    // Getter methods
    std::string getName() const {
        return name;
    }
    
    int getMathScore() const {
        return math_score;
    }
    
    int getScienceScore() const {
        return science_score;
    }
    
    // Setter methods
    void setName(const std::string& n) {
        name = n;
    }
    
    void setMathScore(int score) {
        if (!isValidScore(score)) {
            throw std::invalid_argument("Score must be between 0 and 100");
        }
        math_score = score;
    }
    
    void setScienceScore(int score) {
        if (!isValidScore(score)) {
            throw std::invalid_argument("Score must be between 0 and 100");
        }
        science_score = score;
    }
    
    // Derived value calculation
    double calculateAverage() const {
        return (math_score + science_score) / 2.0;
    }
};

// Example usage
int main() {
    Student student("Alice", 85, 90);
    std::cout << "Name: " << student.getName() << std::endl;
    std::cout << "Average Score: " << student.calculateAverage() << std::endl;
    
    student.setMathScore(92);
    std::cout << "Updated Average Score: " << student.calculateAverage() << std::endl;
    
    return 0;
}
