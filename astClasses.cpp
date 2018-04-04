#include <memory>
#include <string>
#include <iostream>
#include <simple_match/include/simple_match/simple_match.hpp>

class Term;
class Var;
class Abs;
class App;

class Term {
  public:
    // CTOR
    Term() {}
    virtual
        // DTOR
        ~Term() {}
    virtual std::shared_ptr<Term> clone() = 0;
};

class Var : public Term {
  public:
    std::string name;
    // CTOR
    Var(const std::string &name) : name(name) {}
    // DTOR
    ~Var() {}

    virtual std::shared_ptr<Term> clone() override {
        return std::static_pointer_cast<Term>(std::make_shared<Var>(name));
    }
};

class Abs : public Term {
  public:
    std::string name;
    std::shared_ptr<Term> expression;
    // CTOR
    Abs(const std::string &name, const std::shared_ptr<Term> &expression)
        : name(name), expression(expression) {}
    Abs(const std::string &name, Term *expression)
        : name(name), expression(std::shared_ptr<Term>(expression)) {}
    // DTOR
    ~Abs() {}

    virtual std::shared_ptr<Term> clone() override {
        return std::static_pointer_cast<Term>(
            std::make_shared<Abs>(name, expression->clone()));
    }
};

class App : public Term {
  public:
    std::shared_ptr<Term> nameExp, absExp;
    // CTOR
    App(const std::shared_ptr<Term> &nameExp,
        const std::shared_ptr<Term> &absExp)
        : nameExp(nameExp), absExp(absExp) {}
    App(Term *nameExp, Term *absExp)
        : nameExp(std::shared_ptr<Term>(nameExp))
        , absExp(std::shared_ptr<Term>(absExp)) {}
    // DTOR
    ~App() {}

    virtual std::shared_ptr<Term> clone() override {
        return std::static_pointer_cast<Term>(
            std::make_shared<App>(nameExp->clone(), absExp->clone()));
    }
};

namespace simple_match {
namespace customization {

template <> struct tuple_adapter<Var> {
    enum { tuple_len = 1 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.name));
    }
};

template <> struct tuple_adapter<Abs> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.name, t.expression));
    }
};

template <> struct tuple_adapter<App> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.nameExp, t.absExp));
    }
};
} // namespace customization
} // namespace simple_match

std::string toStr(const std::shared_ptr<Term> &t);
std::string toStr2(const std::shared_ptr<Term> &t);
void createDestroy(void);

// interface
template<typename P, typename R> struct AstVisitor {
public:
    virtual R visit(Var v, P parameter) = 0;
    virtual R visit(App a, P parameter) = 0;
    virtual R visit(Abs ab, P parameter) = 0;
    virtual R visitNull(P parameter) = 0;
};

template<typename P, typename R>
R traverse(AstVisitor<P, R>,
           const std::shared_ptr<Term> &,
           P &);

template<typename P, typename R>
R traverse(AstVisitor<P, R> *v,
           const std::shared_ptr<Term> &t,
           P &initial) {
    using namespace simple_match;
    using namespace simple_match::placeholders;
    return match(t,
                 some<Var>(), [&](Var &n){ return v->visit(n, initial); },
                 some<Abs>(), [&](Abs &n){ return v->visit(n, initial); },
                 some<App>(), [&](App &n){ return v->visit(n, initial); },
                 none(),      [&]()      { return v->visitNull(initial); });
}

struct Context {
    void incCount(void) {
        (this->i)++;
    }
private:
    int i = 0;
};

class MyVisitor : public AstVisitor<Context, std::string> {
public:
    MyVisitor() {}
    ~MyVisitor() {}
    std::string visit(Var v, Context parameter) override {
        parameter.incCount();
        return v.name;
    }

    std::string visit(App a, Context parameter) override {
        parameter.incCount();
        return "(" + traverse(this, a.nameExp, parameter) + " "
            + traverse(this, a.absExp, parameter) + ") (geil)";
    }

    std::string visit(Abs v, Context parameter) override {
        parameter.incCount();
        return "\\" + v.name + " -> (geil) "
            + traverse<Context, std::string>(this, v.expression, parameter);
    }

    std::string visitNull(Context) override {
        return "";
    }
};

int main(void) {
    // create a test tree for \x -> (\y -> x y)
    Term *t = new Abs("x", new Abs("y", new App(new Var("x"), new Var("y)"))));
    std::shared_ptr<Term> c1 = t->clone();
    std::shared_ptr<Term> c2 = t->clone();

    std::cout << toStr(c1) << std::endl;
    std::cout << toStr(c2) << std::endl;
    std::cout << toStr2(c2) << std::endl;

    MyVisitor *my = new MyVisitor();
    Context c = Context();
    std::cout << traverse(my, c1, c) << std::endl;

    while(1) {
        createDestroy();
    }

    return 0;
}

void createDestroy(void) {
    Term *t = new Abs("x", new Abs("y", new App(new Var("x"), new Var("y)"))));
    std::shared_ptr<Term> c1 = std::shared_ptr<Term>(t);
}

std::string toStr(const std::shared_ptr<Term> &t) {
    using namespace simple_match;
    using namespace simple_match::placeholders;
    return match(t,
                 some<Var>(), [](Var &v){ return v.name; },
                 some<Abs>(), [](Abs &a){
                     return
                         "\\" + a.name + " -> "
                         + toStr(a.expression);
                 },
                 some<App>(), [](App &a){
                     return "(" + toStr(a.nameExp)
                         + " " + toStr(a.absExp) + ")";
                 },
                 none(), []() { return std::string(""); });
}

std::string toStr2(const std::shared_ptr<Term> &t) {
    using namespace simple_match;
    using namespace simple_match::placeholders;
    return match(t,
                 some<Var>(ds(_x)), [](auto &n){ return n; },
                 some<Abs>(ds(_x, _x)), [](auto &n, auto &t){
                     return "\\" + n + " -> " + toStr(t);
                 },
                 some<App>(ds(_x, _x)), [](auto &a, auto &b){
                     return "(" + toStr(a) + " " + toStr(b) + ")";
                 },
                 none(), []() { return std::string(""); });
}
