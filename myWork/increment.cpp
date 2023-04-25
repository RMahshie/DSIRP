#include <iostream>
using namespace std;

struct Time {
    int hour, minute;
    double second;
};

void increment(Time& time, double secs)
{
    time.second += secs;

    while (time.second >= 60.0) {
        time.second -= 60.0;
        time.minute += 1;
    }
    while (time.minute >= 60) {
        time.minute -= 60;
        time.hour += 1;
    }
}

double convert_to_seconds(const Time& t)
{
    int minutes = t.hour * 60 + t.minute;
    double seconds = minutes * 60 + t.second;

    return seconds;
}



Time make_time(double secs)
{
    Time time;
    time.hour = int(secs / 3600.0);
    secs -= time.hour * 3600.0;
    time.minute = int(secs / 60.0);
    secs -= time.minute * 60;
    time.second = secs;

    return time;
}

void print_time(Time& t) {
    cout << t.hour << ":" << t.minute << ":" << t.second << endl;
}

int main() {
	Time time = {4, 5, 6};
	double seconds = convert_to_seconds(time);
	seconds += 300;
	time = make_time(seconds);
	print_time(time);
	return 0;
	

}
