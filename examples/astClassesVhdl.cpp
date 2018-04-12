#include "simple_match/include/simple_match/simple_match.hpp"
#include <memory>
#include <iostream>
#include <sstream>
#include <optional>
#include <string>
#include <vector>

using namespace simple_match;
using namespace simple_match::placeholders;

class AstNode;
class Architecture;
class Entity;
class ConcStmt;
class SeqStmt;
class WaitStmt;
class IfStatement;
class ElsIfBlocks;
class AssertStmt;
class SeqSigAssignStmt;
class VarAssignStmt;
class ProcedureCallStmt;
class ProcedureCallStmtFptr;
class ProcedureCallStmtSimple;
class SeqSigAssignStmtAfter;
class ProcessStmt;
class ConcSigAssign;
class ConcSigAssignSelect;
class ConcSigAssignSelectElem;
class ChoiceElem;
class ConcSigAssignWhen;
class ConcSigAssignWhenElem;
class Expression;
class ExpressionBinary;
class ExpressionUnary;
class Integer;
class Decl;
class GenericDecl;
class GenericDeclElement;
class Type;
class TypeBuiltIn;
class TypeArray;
class TypeArrayOneDim;
class TypeDecl;
class TypeDeclSimple;
class TypeDeclSubtype;
class PortDecl;
class PortDeclElement;
class Identifier;
class QualifiedIdentifier;
class SimpleIdentifier;

class AstNode {
  public:
    // CTOR
    AstNode() {}
    virtual
        // DTOR
        ~AstNode() {}
    virtual std::shared_ptr<AstNode> clone() = 0;
};

class Identifier : public AstNode {
  public:
    // CTOR
    Identifier() {}
    // DTOR
    ~Identifier() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(
            std::make_shared<Identifier>());
    }
};

class SimpleIdentifier : public Identifier {
  public:
    std::string id;
    // CTOR
    SimpleIdentifier(const std::string &id) : id(id) {}
    // DTOR
    ~SimpleIdentifier() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::string id_copy = id;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<SimpleIdentifier>(id_copy));
    }
};

class QualifiedIdentifier : public Identifier {
  public:
    std::vector<std::string> qualifiedName;
    // CTOR
    QualifiedIdentifier(const std::vector<std::string> &qualifiedName)
        : qualifiedName(qualifiedName) {}
    // DTOR
    ~QualifiedIdentifier() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::vector<std::string> qualifiedName_copy = qualifiedName;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<QualifiedIdentifier>(qualifiedName_copy));
    }
};

class Type : public AstNode {
  public:
    // CTOR
    Type() {}
    // DTOR
    ~Type() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(std::make_shared<Type>());
    }
};

class TypeArrayOneDim : public Type {
  public:
    std::shared_ptr<Type> baseType;
    int dimensions;
    // CTOR
    TypeArrayOneDim(const std::shared_ptr<Type> &baseType,
                    const int &dimensions)
        : baseType(baseType), dimensions(dimensions) {}
    // DTOR
    ~TypeArrayOneDim() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Type> baseType_copy;

        baseType_copy = std::dynamic_pointer_cast<Type>(baseType->clone());

        int dimensions_copy = dimensions;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<TypeArrayOneDim>(baseType_copy, dimensions_copy));
    }
};

class TypeArray : public Type {
  public:
    std::shared_ptr<Type> baseType;
    std::vector<int> dimensions;
    // CTOR
    TypeArray(const std::shared_ptr<Type> &baseType,
              const std::vector<int> &dimensions)
        : baseType(baseType), dimensions(dimensions) {}
    // DTOR
    ~TypeArray() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Type> baseType_copy;

        baseType_copy = std::dynamic_pointer_cast<Type>(baseType->clone());

        std::vector<int> dimensions_copy = dimensions;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<TypeArray>(baseType_copy, dimensions_copy));
    }
};

class TypeBuiltIn : public Type {
  public:
    std::string typeName;
    // CTOR
    TypeBuiltIn(const std::string &typeName) : typeName(typeName) {}
    // DTOR
    ~TypeBuiltIn() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::string typeName_copy = typeName;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<TypeBuiltIn>(typeName_copy));
    }
};

class Decl : public AstNode {
  public:
    // CTOR
    Decl() {}
    // DTOR
    ~Decl() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(std::make_shared<Decl>());
    }
};

class PortDecl : public Decl {
  public:
    // CTOR
    PortDecl() {}
    // DTOR
    ~PortDecl() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(std::make_shared<PortDecl>());
    }
};

class TypeDecl : public Decl {
  public:
    // CTOR
    TypeDecl() {}
    // DTOR
    ~TypeDecl() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(std::make_shared<TypeDecl>());
    }
};

class TypeDeclSubtype : public TypeDecl {
  public:
    std::shared_ptr<Identifier> name;
    std::shared_ptr<Type> type;
    // CTOR
    TypeDeclSubtype(const std::shared_ptr<Identifier> &name,
                    const std::shared_ptr<Type> &type)
        : name(name), type(type) {}
    // DTOR
    ~TypeDeclSubtype() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Identifier> name_copy;

        name_copy = std::dynamic_pointer_cast<Identifier>(name->clone());

        std::shared_ptr<Type> type_copy;

        type_copy = std::dynamic_pointer_cast<Type>(type->clone());

        return std::static_pointer_cast<AstNode>(
            std::make_shared<TypeDeclSubtype>(name_copy, type_copy));
    }
};

class TypeDeclSimple : public TypeDecl {
  public:
    std::shared_ptr<Identifier> name;
    std::shared_ptr<Type> type;
    // CTOR
    TypeDeclSimple(const std::shared_ptr<Identifier> &name,
                   const std::shared_ptr<Type> &type)
        : name(name), type(type) {}
    // DTOR
    ~TypeDeclSimple() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Identifier> name_copy;

        name_copy = std::dynamic_pointer_cast<Identifier>(name->clone());

        std::shared_ptr<Type> type_copy;

        type_copy = std::dynamic_pointer_cast<Type>(type->clone());

        return std::static_pointer_cast<AstNode>(
            std::make_shared<TypeDeclSimple>(name_copy, type_copy));
    }
};

class Expression : public AstNode {
  public:
    // CTOR
    Expression() {}
    // DTOR
    ~Expression() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(
            std::make_shared<Expression>());
    }
};

class PortDeclElement : public Decl {
  public:
    std::vector<std::shared_ptr<Identifier>> portNames;
    std::string inOrOut;
    std::shared_ptr<Type> type;
    std::optional<std::shared_ptr<Expression>> initializerExp;
    // CTOR
    PortDeclElement(
        const std::vector<std::shared_ptr<Identifier>> &portNames,
        const std::string &inOrOut, const std::shared_ptr<Type> &type,
        const std::optional<std::shared_ptr<Expression>> &initializerExp)
        : portNames(portNames), inOrOut(inOrOut), type(type),
          initializerExp(initializerExp) {}
    // DTOR
    ~PortDeclElement() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::vector<std::shared_ptr<Identifier>> portNames_copy;

        for (auto &i : portNames) {
            portNames_copy.push_back(
                std::dynamic_pointer_cast<Identifier>(i->clone()));
        }

        std::string inOrOut_copy = inOrOut;
        std::shared_ptr<Type> type_copy;

        type_copy = std::dynamic_pointer_cast<Type>(type->clone());

        std::optional<std::shared_ptr<Expression>> initializerExp_copy;
        if (initializerExp.has_value()) {

            initializerExp_copy = std::dynamic_pointer_cast<Expression>(
                (*initializerExp)->clone());
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<PortDeclElement>(portNames_copy, inOrOut_copy,
                                              type_copy, initializerExp_copy));
    }
};

class GenericDeclElement : public Decl {
  public:
    std::vector<std::shared_ptr<Identifier>> identifierList;
    std::shared_ptr<Type> type;
    std::optional<std::shared_ptr<Expression>> initializerExp;
    // CTOR
    GenericDeclElement(
        const std::vector<std::shared_ptr<Identifier>> &identifierList,
        const std::shared_ptr<Type> &type,
        const std::optional<std::shared_ptr<Expression>> &initializerExp)
        : identifierList(identifierList), type(type),
          initializerExp(initializerExp) {}
    // DTOR
    ~GenericDeclElement() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::vector<std::shared_ptr<Identifier>> identifierList_copy;

        for (auto &i : identifierList) {
            identifierList_copy.push_back(
                std::dynamic_pointer_cast<Identifier>(i->clone()));
        }

        std::shared_ptr<Type> type_copy;

        type_copy = std::dynamic_pointer_cast<Type>(type->clone());

        std::optional<std::shared_ptr<Expression>> initializerExp_copy;
        if (initializerExp.has_value()) {

            initializerExp_copy = std::dynamic_pointer_cast<Expression>(
                (*initializerExp)->clone());
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<GenericDeclElement>(identifierList_copy, type_copy,
                                                 initializerExp_copy));
    }
};

class GenericDecl : public Decl {
  public:
    std::vector<std::shared_ptr<GenericDeclElement>> genericDeclElements;
    // CTOR
    GenericDecl(const std::vector<std::shared_ptr<GenericDeclElement>>
                    &genericDeclElements)
        : genericDeclElements(genericDeclElements) {}
    // DTOR
    ~GenericDecl() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::vector<std::shared_ptr<GenericDeclElement>>
            genericDeclElements_copy;

        for (auto &i : genericDeclElements) {
            genericDeclElements_copy.push_back(
                std::dynamic_pointer_cast<GenericDeclElement>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<GenericDecl>(genericDeclElements_copy));
    }
};

class Integer : public Expression {
  public:
    long value;
    // CTOR
    Integer(const long &value) : value(value) {}
    // DTOR
    ~Integer() {}

    virtual std::shared_ptr<AstNode> clone() override {

        long value_copy = value;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<Integer>(value_copy));
    }
};

class ExpressionUnary : public Expression {
  public:
    std::shared_ptr<Expression> operand;
    std::string op;
    // CTOR
    ExpressionUnary(const std::shared_ptr<Expression> &operand,
                    const std::string &op)
        : operand(operand), op(op) {}
    // DTOR
    ~ExpressionUnary() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> operand_copy;

        operand_copy = std::dynamic_pointer_cast<Expression>(operand->clone());

        std::string op_copy = op;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ExpressionUnary>(operand_copy, op_copy));
    }
};

class ExpressionBinary : public Expression {
  public:
    std::shared_ptr<Expression> lhs;
    std::shared_ptr<Expression> rhs;
    std::string op;
    // CTOR
    ExpressionBinary(const std::shared_ptr<Expression> &lhs,
                     const std::shared_ptr<Expression> &rhs,
                     const std::string &op)
        : lhs(lhs), rhs(rhs), op(op) {}
    // DTOR
    ~ExpressionBinary() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> lhs_copy;

        lhs_copy = std::dynamic_pointer_cast<Expression>(lhs->clone());

        std::shared_ptr<Expression> rhs_copy;

        rhs_copy = std::dynamic_pointer_cast<Expression>(rhs->clone());

        std::string op_copy = op;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ExpressionBinary>(lhs_copy, rhs_copy, op_copy));
    }
};

class ConcSigAssignWhenElem : public AstNode {
  public:
    std::shared_ptr<Expression> sourceExp;
    std::optional<std::shared_ptr<Expression>> afterTimeExpr;
    std::shared_ptr<Expression> condExp;
    // CTOR
    ConcSigAssignWhenElem(
        const std::shared_ptr<Expression> &sourceExp,
        const std::optional<std::shared_ptr<Expression>> &afterTimeExpr,
        const std::shared_ptr<Expression> &condExp)
        : sourceExp(sourceExp), afterTimeExpr(afterTimeExpr), condExp(condExp) {
    }
    // DTOR
    ~ConcSigAssignWhenElem() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> sourceExp_copy;

        sourceExp_copy =
            std::dynamic_pointer_cast<Expression>(sourceExp->clone());

        std::optional<std::shared_ptr<Expression>> afterTimeExpr_copy;
        if (afterTimeExpr.has_value()) {

            afterTimeExpr_copy = std::dynamic_pointer_cast<Expression>(
                (*afterTimeExpr)->clone());
        }
        std::shared_ptr<Expression> condExp_copy;

        condExp_copy = std::dynamic_pointer_cast<Expression>(condExp->clone());

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ConcSigAssignWhenElem>(
                sourceExp_copy, afterTimeExpr_copy, condExp_copy));
    }
};

class ChoiceElem : public AstNode {
  public:
    // CTOR
    ChoiceElem() {}
    // DTOR
    ~ChoiceElem() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ChoiceElem>());
    }
};

class ConcSigAssignSelectElem : public AstNode {
  public:
    std::shared_ptr<Expression> source;
    std::optional<std::shared_ptr<Expression>> afterTimeExpr;
    std::vector<std::shared_ptr<ChoiceElem>> choices;
    // CTOR
    ConcSigAssignSelectElem(
        const std::shared_ptr<Expression> &source,
        const std::optional<std::shared_ptr<Expression>> &afterTimeExpr,
        const std::vector<std::shared_ptr<ChoiceElem>> &choices)
        : source(source), afterTimeExpr(afterTimeExpr), choices(choices) {}
    // DTOR
    ~ConcSigAssignSelectElem() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> source_copy;

        source_copy = std::dynamic_pointer_cast<Expression>(source->clone());

        std::optional<std::shared_ptr<Expression>> afterTimeExpr_copy;
        if (afterTimeExpr.has_value()) {

            afterTimeExpr_copy = std::dynamic_pointer_cast<Expression>(
                (*afterTimeExpr)->clone());
        }
        std::vector<std::shared_ptr<ChoiceElem>> choices_copy;

        for (auto &i : choices) {
            choices_copy.push_back(
                std::dynamic_pointer_cast<ChoiceElem>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ConcSigAssignSelectElem>(
                source_copy, afterTimeExpr_copy, choices_copy));
    }
};

class ConcSigAssign : public AstNode {
  public:
    // CTOR
    ConcSigAssign() {}
    // DTOR
    ~ConcSigAssign() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ConcSigAssign>());
    }
};

class ConcSigAssignWhen : public ConcSigAssign {
  public:
    std::optional<std::string> label;
    std::shared_ptr<Expression> targetExp;
    std::vector<std::shared_ptr<ConcSigAssignWhenElem>> whens;
    bool guarded;
    std::shared_ptr<Expression> sourceExp;
    // CTOR
    ConcSigAssignWhen(
        const std::optional<std::string> &label,
        const std::shared_ptr<Expression> &targetExp,
        const std::vector<std::shared_ptr<ConcSigAssignWhenElem>> &whens,
        const bool &guarded, const std::shared_ptr<Expression> &sourceExp)
        : label(label), targetExp(targetExp), whens(whens), guarded(guarded),
          sourceExp(sourceExp) {}
    // DTOR
    ~ConcSigAssignWhen() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::optional<std::string> label_copy = label;
        std::shared_ptr<Expression> targetExp_copy;

        targetExp_copy =
            std::dynamic_pointer_cast<Expression>(targetExp->clone());

        std::vector<std::shared_ptr<ConcSigAssignWhenElem>> whens_copy;

        for (auto &i : whens) {
            whens_copy.push_back(
                std::dynamic_pointer_cast<ConcSigAssignWhenElem>(i->clone()));
        }

        bool guarded_copy = guarded;
        std::shared_ptr<Expression> sourceExp_copy;

        sourceExp_copy =
            std::dynamic_pointer_cast<Expression>(sourceExp->clone());

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ConcSigAssignWhen>(label_copy, targetExp_copy,
                                                whens_copy, guarded_copy,
                                                sourceExp_copy));
    }
};

class ConcSigAssignSelect : public ConcSigAssign {
  public:
    std::shared_ptr<Expression> selectionExpr;
    std::shared_ptr<Expression> target;
    std::vector<std::shared_ptr<ConcSigAssignSelectElem>> selectElements;
    // CTOR
    ConcSigAssignSelect(
        const std::shared_ptr<Expression> &selectionExpr,
        const std::shared_ptr<Expression> &target,
        const std::vector<std::shared_ptr<ConcSigAssignSelectElem>>
            &selectElements)
        : selectionExpr(selectionExpr), target(target),
          selectElements(selectElements) {}
    // DTOR
    ~ConcSigAssignSelect() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> selectionExpr_copy;

        selectionExpr_copy =
            std::dynamic_pointer_cast<Expression>(selectionExpr->clone());

        std::shared_ptr<Expression> target_copy;

        target_copy = std::dynamic_pointer_cast<Expression>(target->clone());

        std::vector<std::shared_ptr<ConcSigAssignSelectElem>>
            selectElements_copy;

        for (auto &i : selectElements) {
            selectElements_copy.push_back(
                std::dynamic_pointer_cast<ConcSigAssignSelectElem>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ConcSigAssignSelect>(
                selectionExpr_copy, target_copy, selectElements_copy));
    }
};

class SeqStmt : public AstNode {
  public:
    // CTOR
    SeqStmt() {}
    // DTOR
    ~SeqStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(std::make_shared<SeqStmt>());
    }
};

class ElsIfBlocks : public AstNode {
  public:
    std::shared_ptr<Expression> condition;
    std::vector<std::shared_ptr<SeqStmt>> stmts;
    // CTOR
    ElsIfBlocks(const std::shared_ptr<Expression> &condition,
                const std::vector<std::shared_ptr<SeqStmt>> &stmts)
        : condition(condition), stmts(stmts) {}
    // DTOR
    ~ElsIfBlocks() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> condition_copy;

        condition_copy =
            std::dynamic_pointer_cast<Expression>(condition->clone());

        std::vector<std::shared_ptr<SeqStmt>> stmts_copy;

        for (auto &i : stmts) {
            stmts_copy.push_back(
                std::dynamic_pointer_cast<SeqStmt>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ElsIfBlocks>(condition_copy, stmts_copy));
    }
};

class SeqSigAssignStmtAfter : public SeqStmt {
  public:
    std::shared_ptr<Expression> expression;
    std::shared_ptr<Expression> afterTimeExpr;
    // CTOR
    SeqSigAssignStmtAfter(const std::shared_ptr<Expression> &expression,
                          const std::shared_ptr<Expression> &afterTimeExpr)
        : expression(expression), afterTimeExpr(afterTimeExpr) {}
    // DTOR
    ~SeqSigAssignStmtAfter() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> expression_copy;

        expression_copy =
            std::dynamic_pointer_cast<Expression>(expression->clone());

        std::shared_ptr<Expression> afterTimeExpr_copy;

        afterTimeExpr_copy =
            std::dynamic_pointer_cast<Expression>(afterTimeExpr->clone());

        return std::static_pointer_cast<AstNode>(
            std::make_shared<SeqSigAssignStmtAfter>(expression_copy,
                                                    afterTimeExpr_copy));
    }
};

class ProcedureCallStmt : public SeqStmt {
  public:
    // CTOR
    ProcedureCallStmt() {}
    // DTOR
    ~ProcedureCallStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ProcedureCallStmt>());
    }
};

class ProcedureCallStmtSimple : public ProcedureCallStmt {
  public:
    std::string procedure;
    std::vector<std::shared_ptr<Expression>> arguments;
    // CTOR
    ProcedureCallStmtSimple(
        const std::string &procedure,
        const std::vector<std::shared_ptr<Expression>> &arguments)
        : procedure(procedure), arguments(arguments) {}
    // DTOR
    ~ProcedureCallStmtSimple() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::string procedure_copy = procedure;
        std::vector<std::shared_ptr<Expression>> arguments_copy;

        for (auto &i : arguments) {
            arguments_copy.push_back(
                std::dynamic_pointer_cast<Expression>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ProcedureCallStmtSimple>(procedure_copy,
                                                      arguments_copy));
    }
};

class ProcedureCallStmtFptr : public ProcedureCallStmt {
  public:
    std::shared_ptr<Expression> procedure;
    std::vector<std::shared_ptr<Expression>> arguments;
    // CTOR
    ProcedureCallStmtFptr(
        const std::shared_ptr<Expression> &procedure,
        const std::vector<std::shared_ptr<Expression>> &arguments)
        : procedure(procedure), arguments(arguments) {}
    // DTOR
    ~ProcedureCallStmtFptr() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> procedure_copy;

        procedure_copy =
            std::dynamic_pointer_cast<Expression>(procedure->clone());

        std::vector<std::shared_ptr<Expression>> arguments_copy;

        for (auto &i : arguments) {
            arguments_copy.push_back(
                std::dynamic_pointer_cast<Expression>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ProcedureCallStmtFptr>(procedure_copy,
                                                    arguments_copy));
    }
};

class VarAssignStmt : public SeqStmt {
  public:
    std::shared_ptr<Expression> target;
    std::shared_ptr<Expression> source;
    // CTOR
    VarAssignStmt(const std::shared_ptr<Expression> &target,
                  const std::shared_ptr<Expression> &source)
        : target(target), source(source) {}
    // DTOR
    ~VarAssignStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> target_copy;

        target_copy = std::dynamic_pointer_cast<Expression>(target->clone());

        std::shared_ptr<Expression> source_copy;

        source_copy = std::dynamic_pointer_cast<Expression>(source->clone());

        return std::static_pointer_cast<AstNode>(
            std::make_shared<VarAssignStmt>(target_copy, source_copy));
    }
};

class SeqSigAssignStmt : public SeqStmt {
  public:
    std::shared_ptr<Expression> target;
    bool transport;
    std::optional<std::shared_ptr<Expression>> afterTimeExpr;
    std::vector<std::shared_ptr<SeqSigAssignStmtAfter>> expAfterList;
    // CTOR
    SeqSigAssignStmt(
        const std::shared_ptr<Expression> &target, const bool &transport,
        const std::optional<std::shared_ptr<Expression>> &afterTimeExpr,
        const std::vector<std::shared_ptr<SeqSigAssignStmtAfter>> &expAfterList)
        : target(target), transport(transport), afterTimeExpr(afterTimeExpr),
          expAfterList(expAfterList) {}
    // DTOR
    ~SeqSigAssignStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> target_copy;

        target_copy = std::dynamic_pointer_cast<Expression>(target->clone());

        bool transport_copy = transport;
        std::optional<std::shared_ptr<Expression>> afterTimeExpr_copy;
        if (afterTimeExpr.has_value()) {

            afterTimeExpr_copy = std::dynamic_pointer_cast<Expression>(
                (*afterTimeExpr)->clone());
        }
        std::vector<std::shared_ptr<SeqSigAssignStmtAfter>> expAfterList_copy;

        for (auto &i : expAfterList) {
            expAfterList_copy.push_back(
                std::dynamic_pointer_cast<SeqSigAssignStmtAfter>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<SeqSigAssignStmt>(target_copy, transport_copy,
                                               afterTimeExpr_copy,
                                               expAfterList_copy));
    }
};

class AssertStmt : public SeqStmt {
  public:
    std::shared_ptr<Expression> stringExpression;
    std::string severity;
    // CTOR
    AssertStmt(const std::shared_ptr<Expression> &stringExpression,
               const std::string &severity)
        : stringExpression(stringExpression), severity(severity) {}
    // DTOR
    ~AssertStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> stringExpression_copy;

        stringExpression_copy =
            std::dynamic_pointer_cast<Expression>(stringExpression->clone());

        std::string severity_copy = severity;

        return std::static_pointer_cast<AstNode>(
            std::make_shared<AssertStmt>(stringExpression_copy, severity_copy));
    }
};

class IfStatement : public SeqStmt {
  public:
    std::shared_ptr<Expression> condition;
    std::vector<std::shared_ptr<SeqStmt>> thenStmts;
    std::vector<std::shared_ptr<ElsIfBlocks>> elsifs;
    std::vector<std::shared_ptr<SeqStmt>> elseStmts;
    // CTOR
    IfStatement(const std::shared_ptr<Expression> &condition,
                const std::vector<std::shared_ptr<SeqStmt>> &thenStmts,
                const std::vector<std::shared_ptr<ElsIfBlocks>> &elsifs,
                const std::vector<std::shared_ptr<SeqStmt>> &elseStmts)
        : condition(condition), thenStmts(thenStmts), elsifs(elsifs),
          elseStmts(elseStmts) {}
    // DTOR
    ~IfStatement() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Expression> condition_copy;

        condition_copy =
            std::dynamic_pointer_cast<Expression>(condition->clone());

        std::vector<std::shared_ptr<SeqStmt>> thenStmts_copy;

        for (auto &i : thenStmts) {
            thenStmts_copy.push_back(
                std::dynamic_pointer_cast<SeqStmt>(i->clone()));
        }

        std::vector<std::shared_ptr<ElsIfBlocks>> elsifs_copy;

        for (auto &i : elsifs) {
            elsifs_copy.push_back(
                std::dynamic_pointer_cast<ElsIfBlocks>(i->clone()));
        }

        std::vector<std::shared_ptr<SeqStmt>> elseStmts_copy;

        for (auto &i : elseStmts) {
            elseStmts_copy.push_back(
                std::dynamic_pointer_cast<SeqStmt>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(std::make_shared<IfStatement>(
            condition_copy, thenStmts_copy, elsifs_copy, elseStmts_copy));
    }
};

class WaitStmt : public SeqStmt {
  public:
    std::optional<std::vector<std::shared_ptr<Identifier>>> waitSignals;
    std::shared_ptr<Expression> condition;
    std::shared_ptr<Expression> timeExpr;
    // CTOR
    WaitStmt(const std::optional<std::vector<std::shared_ptr<Identifier>>>
                 &waitSignals,
             const std::shared_ptr<Expression> &condition,
             const std::shared_ptr<Expression> &timeExpr)
        : waitSignals(waitSignals), condition(condition), timeExpr(timeExpr) {}
    // DTOR
    ~WaitStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::optional<std::vector<std::shared_ptr<Identifier>>>
            waitSignals_copy;
        if (waitSignals.has_value()) {

            for (auto &i : *waitSignals) {
                waitSignals_copy->push_back(
                    std::dynamic_pointer_cast<Identifier>(i->clone()));
            }
        }
        std::shared_ptr<Expression> condition_copy;

        condition_copy =
            std::dynamic_pointer_cast<Expression>(condition->clone());

        std::shared_ptr<Expression> timeExpr_copy;

        timeExpr_copy =
            std::dynamic_pointer_cast<Expression>(timeExpr->clone());

        return std::static_pointer_cast<AstNode>(std::make_shared<WaitStmt>(
            waitSignals_copy, condition_copy, timeExpr_copy));
    }
};

class ConcStmt : public AstNode {
  public:
    // CTOR
    ConcStmt() {}
    // DTOR
    ~ConcStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        return std::static_pointer_cast<AstNode>(std::make_shared<ConcStmt>());
    }
};

class ProcessStmt : public ConcStmt {
  public:
    std::optional<std::string> label;
    std::vector<std::shared_ptr<Identifier>> sensitivityList;
    std::vector<std::shared_ptr<Decl>> declarations;
    std::vector<std::shared_ptr<SeqStmt>> statements;
    // CTOR
    ProcessStmt(const std::optional<std::string> &label,
                const std::vector<std::shared_ptr<Identifier>> &sensitivityList,
                const std::vector<std::shared_ptr<Decl>> &declarations,
                const std::vector<std::shared_ptr<SeqStmt>> &statements)
        : label(label), sensitivityList(sensitivityList),
          declarations(declarations), statements(statements) {}
    // DTOR
    ~ProcessStmt() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::optional<std::string> label_copy = label;
        std::vector<std::shared_ptr<Identifier>> sensitivityList_copy;

        for (auto &i : sensitivityList) {
            sensitivityList_copy.push_back(
                std::dynamic_pointer_cast<Identifier>(i->clone()));
        }

        std::vector<std::shared_ptr<Decl>> declarations_copy;

        for (auto &i : declarations) {
            declarations_copy.push_back(
                std::dynamic_pointer_cast<Decl>(i->clone()));
        }

        std::vector<std::shared_ptr<SeqStmt>> statements_copy;

        for (auto &i : statements) {
            statements_copy.push_back(
                std::dynamic_pointer_cast<SeqStmt>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(
            std::make_shared<ProcessStmt>(label_copy, sensitivityList_copy,
                                          declarations_copy, statements_copy));
    }
};

class Entity : public AstNode {
  public:
    std::shared_ptr<Identifier> id;
    std::shared_ptr<GenericDecl> generics;
    std::shared_ptr<PortDecl> ports;
    // CTOR
    Entity(const std::shared_ptr<Identifier> &id,
           const std::shared_ptr<GenericDecl> &generics,
           const std::shared_ptr<PortDecl> &ports)
        : id(id), generics(generics), ports(ports) {}
    // DTOR
    ~Entity() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Identifier> id_copy;

        id_copy = std::dynamic_pointer_cast<Identifier>(id->clone());

        std::shared_ptr<GenericDecl> generics_copy;

        generics_copy =
            std::dynamic_pointer_cast<GenericDecl>(generics->clone());

        std::shared_ptr<PortDecl> ports_copy;

        ports_copy = std::dynamic_pointer_cast<PortDecl>(ports->clone());

        return std::static_pointer_cast<AstNode>(
            std::make_shared<Entity>(id_copy, generics_copy, ports_copy));
    }
};

class Architecture : public AstNode {
  public:
    std::shared_ptr<Identifier> archName;
    std::shared_ptr<Identifier> entityName;
    std::vector<std::shared_ptr<ConcStmt>> concStatements;
    // CTOR
    Architecture(const std::shared_ptr<Identifier> &archName,
                 const std::shared_ptr<Identifier> &entityName,
                 const std::vector<std::shared_ptr<ConcStmt>> &concStatements)
        : archName(archName), entityName(entityName),
          concStatements(concStatements) {}
    // DTOR
    ~Architecture() {}

    virtual std::shared_ptr<AstNode> clone() override {

        std::shared_ptr<Identifier> archName_copy;

        archName_copy =
            std::dynamic_pointer_cast<Identifier>(archName->clone());

        std::shared_ptr<Identifier> entityName_copy;

        entityName_copy =
            std::dynamic_pointer_cast<Identifier>(entityName->clone());

        std::vector<std::shared_ptr<ConcStmt>> concStatements_copy;

        for (auto &i : concStatements) {
            concStatements_copy.push_back(
                std::dynamic_pointer_cast<ConcStmt>(i->clone()));
        }

        return std::static_pointer_cast<AstNode>(std::make_shared<Architecture>(
            archName_copy, entityName_copy, concStatements_copy));
    }
};

namespace simple_match {
namespace customization {

template <> struct tuple_adapter<AstNode> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<Architecture> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.archName, t.entityName, t.concStatements));
    }
};

template <> struct tuple_adapter<Entity> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.id, t.generics, t.ports));
    }
};

template <> struct tuple_adapter<ConcStmt> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<SeqStmt> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<WaitStmt> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.waitSignals, t.condition, t.timeExpr));
    }
};

template <> struct tuple_adapter<IfStatement> {
    enum { tuple_len = 4 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.condition, t.thenStmts, t.elsifs, t.elseStmts));
    }
};

template <> struct tuple_adapter<ElsIfBlocks> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.condition, t.stmts));
    }
};

template <> struct tuple_adapter<AssertStmt> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.stringExpression, t.severity));
    }
};

template <> struct tuple_adapter<SeqSigAssignStmt> {
    enum { tuple_len = 4 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.target, t.transport, t.afterTimeExpr, t.expAfterList));
    }
};

template <> struct tuple_adapter<VarAssignStmt> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.target, t.source));
    }
};

template <> struct tuple_adapter<ProcedureCallStmt> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<ProcedureCallStmtFptr> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.procedure, t.arguments));
    }
};

template <> struct tuple_adapter<ProcedureCallStmtSimple> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.procedure, t.arguments));
    }
};

template <> struct tuple_adapter<SeqSigAssignStmtAfter> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.expression, t.afterTimeExpr));
    }
};

template <> struct tuple_adapter<ProcessStmt> {
    enum { tuple_len = 4 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.label, t.sensitivityList, t.declarations, t.statements));
    }
};

template <> struct tuple_adapter<ConcSigAssign> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<ConcSigAssignSelect> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.selectionExpr, t.target, t.selectElements));
    }
};

template <> struct tuple_adapter<ConcSigAssignSelectElem> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.source, t.afterTimeExpr, t.choices));
    }
};

template <> struct tuple_adapter<ChoiceElem> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<ConcSigAssignWhen> {
    enum { tuple_len = 5 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.label, t.targetExp, t.whens, t.guarded, t.sourceExp));
    }
};

template <> struct tuple_adapter<ConcSigAssignWhenElem> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.sourceExp, t.afterTimeExpr, t.condExp));
    }
};

template <> struct tuple_adapter<Expression> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<ExpressionBinary> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.lhs, t.rhs, t.op));
    }
};

template <> struct tuple_adapter<ExpressionUnary> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.operand, t.op));
    }
};

template <> struct tuple_adapter<Integer> {
    enum { tuple_len = 1 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.value));
    }
};

template <> struct tuple_adapter<Decl> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<GenericDecl> {
    enum { tuple_len = 1 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.genericDeclElements));
    }
};

template <> struct tuple_adapter<GenericDeclElement> {
    enum { tuple_len = 3 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.identifierList, t.type, t.initializerExp));
    }
};

template <> struct tuple_adapter<Type> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<TypeBuiltIn> {
    enum { tuple_len = 1 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.typeName));
    }
};

template <> struct tuple_adapter<TypeArray> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.baseType, t.dimensions));
    }
};

template <> struct tuple_adapter<TypeArrayOneDim> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.baseType, t.dimensions));
    }
};

template <> struct tuple_adapter<TypeDecl> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<TypeDeclSimple> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.name, t.type));
    }
};

template <> struct tuple_adapter<TypeDeclSubtype> {
    enum { tuple_len = 2 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.name, t.type));
    }
};

template <> struct tuple_adapter<PortDecl> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<PortDeclElement> {
    enum { tuple_len = 4 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(
            std::tie(t.portNames, t.inOrOut, t.type, t.initializerExp));
    }
};

template <> struct tuple_adapter<Identifier> {
    enum { tuple_len = 0 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie());
    }
};

template <> struct tuple_adapter<QualifiedIdentifier> {
    enum { tuple_len = 1 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.qualifiedName));
    }
};

template <> struct tuple_adapter<SimpleIdentifier> {
    enum { tuple_len = 1 };
    template <size_t I, class T> static decltype(auto) get(T &&t) {
        return std::get<I>(std::tie(t.id));
    }
};
} // namespace customization
} // namespace simple_match

template <typename P, typename R> struct AstVisitor {
  public:
    virtual R visit(Architecture v, P p) = 0;
    virtual R visit(Entity v, P p) = 0;
    virtual R visit(WaitStmt v, P p) = 0;
    virtual R visit(IfStatement v, P p) = 0;
    virtual R visit(ElsIfBlocks v, P p) = 0;
    virtual R visit(AssertStmt v, P p) = 0;
    virtual R visit(SeqSigAssignStmt v, P p) = 0;
    virtual R visit(VarAssignStmt v, P p) = 0;
    virtual R visit(ProcedureCallStmtFptr v, P p) = 0;
    virtual R visit(ProcedureCallStmtSimple v, P p) = 0;
    virtual R visit(SeqSigAssignStmtAfter v, P p) = 0;
    virtual R visit(ProcessStmt v, P p) = 0;
    virtual R visit(ConcSigAssignSelect v, P p) = 0;
    virtual R visit(ConcSigAssignSelectElem v, P p) = 0;
    virtual R visit(ChoiceElem v, P p) = 0;
    virtual R visit(ConcSigAssignWhen v, P p) = 0;
    virtual R visit(ConcSigAssignWhenElem v, P p) = 0;
    virtual R visit(ExpressionBinary v, P p) = 0;
    virtual R visit(ExpressionUnary v, P p) = 0;
    virtual R visit(Integer v, P p) = 0;
    virtual R visit(GenericDecl v, P p) = 0;
    virtual R visit(GenericDeclElement v, P p) = 0;
    virtual R visit(TypeBuiltIn v, P p) = 0;
    virtual R visit(TypeArray v, P p) = 0;
    virtual R visit(TypeArrayOneDim v, P p) = 0;
    virtual R visit(TypeDeclSimple v, P p) = 0;
    virtual R visit(TypeDeclSubtype v, P p) = 0;
    virtual R visit(PortDecl v, P p) = 0;
    virtual R visit(PortDeclElement v, P p) = 0;
    virtual R visit(QualifiedIdentifier v, P p) = 0;
    virtual R visit(SimpleIdentifier v, P p) = 0;
    virtual R visitNull(P parameter) = 0;
};

template <typename P, typename R>
R traverse(AstVisitor<P, R>, const std::shared_ptr<AstNode> &, P &);

template <typename P, typename R>
R traverse(AstVisitor<P, R> *v, const std::shared_ptr<AstNode> &t, P &initial) {
    using namespace simple_match;
    using namespace simple_match::placeholders;
    return match(
        t, some<Architecture>(),
        [&](Architecture &n) { return v->visit(n, initial); }, some<Entity>(),
        [&](Entity &n) { return v->visit(n, initial); }, some<WaitStmt>(),
        [&](WaitStmt &n) { return v->visit(n, initial); }, some<IfStatement>(),
        [&](IfStatement &n) { return v->visit(n, initial); },
        some<ElsIfBlocks>(),
        [&](ElsIfBlocks &n) { return v->visit(n, initial); },
        some<AssertStmt>(), [&](AssertStmt &n) { return v->visit(n, initial); },
        some<SeqSigAssignStmt>(),
        [&](SeqSigAssignStmt &n) { return v->visit(n, initial); },
        some<VarAssignStmt>(),
        [&](VarAssignStmt &n) { return v->visit(n, initial); },
        some<ProcedureCallStmtFptr>(),
        [&](ProcedureCallStmtFptr &n) { return v->visit(n, initial); },
        some<ProcedureCallStmtSimple>(),
        [&](ProcedureCallStmtSimple &n) { return v->visit(n, initial); },
        some<SeqSigAssignStmtAfter>(),
        [&](SeqSigAssignStmtAfter &n) { return v->visit(n, initial); },
        some<ProcessStmt>(),
        [&](ProcessStmt &n) { return v->visit(n, initial); },
        some<ConcSigAssignSelect>(),
        [&](ConcSigAssignSelect &n) { return v->visit(n, initial); },
        some<ConcSigAssignSelectElem>(),
        [&](ConcSigAssignSelectElem &n) { return v->visit(n, initial); },
        some<ChoiceElem>(), [&](ChoiceElem &n) { return v->visit(n, initial); },
        some<ConcSigAssignWhen>(),
        [&](ConcSigAssignWhen &n) { return v->visit(n, initial); },
        some<ConcSigAssignWhenElem>(),
        [&](ConcSigAssignWhenElem &n) { return v->visit(n, initial); },
        some<ExpressionBinary>(),
        [&](ExpressionBinary &n) { return v->visit(n, initial); },
        some<ExpressionUnary>(),
        [&](ExpressionUnary &n) { return v->visit(n, initial); },
        some<Integer>(), [&](Integer &n) { return v->visit(n, initial); },
        some<GenericDecl>(),
        [&](GenericDecl &n) { return v->visit(n, initial); },
        some<GenericDeclElement>(),
        [&](GenericDeclElement &n) { return v->visit(n, initial); },
        some<TypeBuiltIn>(),
        [&](TypeBuiltIn &n) { return v->visit(n, initial); }, some<TypeArray>(),
        [&](TypeArray &n) { return v->visit(n, initial); },
        some<TypeArrayOneDim>(),
        [&](TypeArrayOneDim &n) { return v->visit(n, initial); },
        some<TypeDeclSimple>(),
        [&](TypeDeclSimple &n) { return v->visit(n, initial); },
        some<TypeDeclSubtype>(),
        [&](TypeDeclSubtype &n) { return v->visit(n, initial); },
        some<PortDecl>(), [&](PortDecl &n) { return v->visit(n, initial); },
        some<PortDeclElement>(),
        [&](PortDeclElement &n) { return v->visit(n, initial); },
        some<QualifiedIdentifier>(),
        [&](QualifiedIdentifier &n) { return v->visit(n, initial); },
        some<SimpleIdentifier>(),
        [&](SimpleIdentifier &n) { return v->visit(n, initial); }, none(),
        [&]() { return v->visitNull(initial); });
}

std::string prettyPrint(const std::shared_ptr<AstNode> &t) {
    using namespace simple_match;
    using namespace simple_match::placeholders;
    return match(t,
                 some<ExpressionBinary>(ds(_x, _x, _x)),
                 [](auto &lhs, auto &rhs, auto &op){
                     return prettyPrint(lhs) + op + prettyPrint(rhs);},
                 some<ExpressionUnary>(ds(_x, _x)),
                 [](auto &operand, auto &op){
                     return prettyPrint(operand) + op;},
                 some<Integer>(ds(_x)),
                 [](auto &value){
                     std::string out;
                     auto toLong = std::stringstream();
                     toLong << value;
                     toLong >> out;
                     return out;},
                 some<IfStatement>(ds(_x, _x, _x, _x)),
                 [](auto &a,auto &then,auto &,auto &){
                     auto result = std::string("");
                     for (auto &i : then) {
                         result += prettyPrint(i);
                     }
                     return "if(" + prettyPrint(a) + ") then "
                         + result + "end if;";
                 },
                 none(), [](){return std::string("");});
}

int main(void) {
    // represents the expression (10+12) * (5+15)
    auto expr = std::make_shared<ExpressionBinary>
        (std::make_shared<ExpressionBinary>
         (std::make_shared<Integer>(10),
          std::make_shared<Integer>(12),
          "+"),
         std::make_shared<ExpressionBinary>
         (std::make_shared<Integer>(5),
          std::make_shared<Integer>(15),
          "+"),
         "*");

    std::cout << prettyPrint(expr) << std::endl;
}
