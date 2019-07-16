#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

template <auto Ptr>
struct event {};
template <class EventT, class ReturnT, ReturnT EventT::*Ptr>
struct event<Ptr> {
    using event_t = EventT;
    using ret_t = ReturnT;
};

template <class Name, class T>
struct field {
    using name_t = Name;
    constexpr operator auto() { return value_; }
    T value_;
};

struct msg {
    int i;
    double d;
    float t;
};

template <class stream>
stream& operator<<(stream& s, msg& t) {
    s << t.i << '\t' << t.d << '\t' << t.t << '\n';
    return s;
}

struct trade {
    field<class price, double> price;
    field<class size, uint32_t> size;
    field<class stock_id, int> stock_id;
    field<class trade_id, int> trade_id;
    field<class num_msgs, int> num_msgs;
    field<class var_msgs, msg[0]> var_msgs;
};

template <class stream>
stream& operator<<(stream& s, trade& t) {
    s << t.price << '\t' << t.size << '\t' << t.stock_id << '\t' << t.trade_id
      << '\t' << t.num_msgs << '\n';
    for (int i = 0; i < t.num_msgs; i++) s << t.var_msgs[i];
    return s;
}

struct create {
    double price;
    uint32_t size;
    int stock_id;
    int trade_id;
    int num_msgs;
    msg var_msgs0;
    msg var_msgs1;
    msg var_msgs2;
    msg var_msgs3;
};

int main() {
    std::array<msg, 4> vm = {msg{1, 1.111, 10.1111}, msg{2, 2.2222, 20.2222},
                             msg{3, 3.3333, 30.3333}, msg{4, 4.4444, 40.4444}};
    auto in_msg = create{100.11111, 200, 1, 2, 4, vm[0], vm[1], vm[2], vm[3]};
    std::vector<int> abc = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::cout << abc[0];
    char* data = reinterpret_cast<char*>(&in_msg);

    using ev = typename event<&trade::price>::event_t;
    static_assert(std::is_same<trade, ev>::value, "failed");

    auto* t = reinterpret_cast<trade*>(data);

    auto&& [a, b, c, d, e, f] = *t;

    std::cout << *t;
    return 0;
}
