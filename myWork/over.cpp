#include <iostream>
#include <cmath>

class Complex {
public:
    Complex(double real = 0.0, double imaginary = 0.0) : m_real(real), m_imaginary(imaginary) {}
    
    // Getters and setters
    double getReal() const { return m_real; }
    void setReal(double real) { m_real = real; }
    double getImaginary() const { return m_imaginary; }
    void setImaginary(double imaginary) { m_imaginary = imaginary; }
    
    // Overloaded operators
    Complex operator+(const Complex& other) const {
        return Complex(m_real + other.m_real, m_imaginary + other.m_imaginary);
    }
    
    Complex operator-(const Complex& other) const {
        return Complex(m_real - other.m_real, m_imaginary - other.m_imaginary);
    }
    
    Complex operator*(const Complex& other) const {
        double real = m_real * other.m_real - m_imaginary * other.m_imaginary;
        double imaginary = m_real * other.m_imaginary + m_imaginary * other.m_real;
        return Complex(real, imaginary);
    }
    
    Complex operator/(const Complex& other) const {
        double denominator = other.m_real * other.m_real + other.m_imaginary * other.m_imaginary;
        double real = (m_real * other.m_real + m_imaginary * other.m_imaginary) / denominator;
        double imaginary = (m_imaginary * other.m_real - m_real * other.m_imaginary) / denominator;
        return Complex(real, imaginary);
    }
    
    // Overloaded input and output operators
    friend std::ostream& operator<<(std::ostream& out, const Complex& c) {
        out << c.m_real << " + " << c.m_imaginary << "i";
        return out;
    }
    
    friend std::istream& operator>>(std::istream& in, Complex& c) {
        std::cout << "Real: ";
        in >> c.m_real;
        std::cout << "Imaginary: ";
        in >> c.m_imaginary;
        return in;
    }
    
private:
    double m_real;
    double m_imaginary;
};

int main() {
    Complex c1(1.0, 2.0);
    Complex c2(2.0, 3.0);
    
    Complex c3 = c1 + c2;
    std::cout << c3 << std::endl;
    
    Complex c4 = c1 - c2;
    std::cout << c4 << std::endl;
    
    Complex c5 = c1 * c2;
    std::cout << c5 << std::endl;
    
    Complex c6 = c1 / c2;
    std::cout << c6 << std::endl;
    
    Complex c7;
    std::cin >> c7;
    std::cout << "You entered: " << c7 << std::endl;
    
    return 0;
}
