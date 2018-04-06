vhdl = {
    "AstNode" : {
        "parent" : None,
        "members" : [
            { "cppType" : "int", "name" : "startL"},
            { "cppType" : "int", "name" : "endL"},
            { "cppType" : "int", "name" : "startCol"},
            { "cppType" : "int", "name" : "endCol"}
        ]
    },
    "Architecture" : {
        "parent" : "AstNode",
        "members" : [
            { "cppType" : "" }
        ]
    },
    "Entity" : {
        "parent" : "AstNode",
        "members" : [
            { "cppType" : "Identifier", "name" : "id" },
            { "cppType" : "GenericDecl", "name" : "generics" },
            { "cppType" : "PortDecl", "name" : "ports" },
            # TODO: entity_statement_part
        ]
    },
    "Architecture" : {
        "parent" : "AstNode",
        "members" : [
            { "cppType" : "Identifier", "name" : "archName"},
            { "cppType" : "Identifier", "name" : "entityName"},
            { "cppType" : "std::vector<ConcurrentStatement>", "name" : "concStatements"},
        ]
    },
    "ConcStmt" : {"parent" : "AstNode", "members" : []},
    "SeqStmt" : {"parent" : "AstNode", "members" : []},
    "WaitStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "cppType" : "std::optional<std::vector<Identifier>>",
              "name" : "waitSignals"},
            { "cppType" : "Expression", "name" : "condition"},
            { "cppType" : "Expression", "name" : "timeExpr"},
        ]
    },
    "AssertStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "cppType" : "Expression", "name" : "stringExpression"},
            { "cppType" : "std::string", "name" : "severity"},
        ]
    },
    "SeqSigAssignStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "cppType" : "Expression", "name" : "target"},
            { "cppType" : "Boolean", "name" : "transport"},
            { "cppType" : "std::optional<Expression>", "name" : "afterTimeExpr"},
            { "cppType" : "std::vector<SeqSigAssignStmtAfter>",
              "name" : "expAfterList"},
        ]
    },
    "VarAssignStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "cppType" : "Expression", "name" : "target"},
            { "cppType" : "Expression", "name" : "source"}
        ]
    },
    "ProcedureCallStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "cppType" : "Expression", "name" : "procedure"},
            { "cppType" : "Expression", "name" : "source"}
        ]
    },
    "SeqSigAssignStmtAfter" : {
        "parent" : "SeqStmt",
        "members" : [
            { "cppType" : "Expression" , "name" : "expression" },
            { "cppType" : "Expression" , "name" : "afterTimeExpr" },
        ]
    },
    "ProcessStmt" : {
        "parent" : "ConcStmt",
        "members" : [
            { "cppType" : "std::optional<std::string>", "name" : "label" },
            { "cppType" : "std::vector<Identifier>", "name" : "sensitivityList" },
            { "cppType" : "std::vector<Decl>", "name" : "declarations" },
            { "cppType" : "std::vector<SeqStmt>", "name" : "statements" },
        ]
    },
    "ConcSigAssign" : {"parent" : "AstNode", "members" : []},
    "ConcSigAssignSelect" : {
        "parent" : "ConcSigAssign",
        "members" : [
            { "cppType" : "Expression", "name" : "selectionExpr" },
            { "cppType" : "Expression", "name" : "target" },
            { "cppType" : "std::vector<ConcSigAssignSelectElem>",
              "name" : "selectElements" },
        ]
    },
    "ConcSigAssignSelectElem" : {
        "parent" : "AstNode",
        "members" : [
            { "cppType" : "Expression", "name" : "source" },
            { "cppType" : "std::optional<Expression>", "name" : "afterTimeExpr"},
            { "cppType" : "std::vector<ChoiceElem>", "name" : "choices" },
        ]
    },
    "ChoiceElem" : {
        "parent" : "AstNode",
        "members" : [] # TODO
    },
    "ConcSigAssignWhen" : {
        "parent" : "ConcSigAssign",
        "members" : [
            { "cppType" : "std::optional<std::string>", "name" : "label"},
            { "cppType" : "Expression", "name" : "targetExp"},
            { "cppType" : "std::vector<ConcSigAssignWhenElem>", "name" : "whens" },
            { "cppType" : "Boolean", "name" : "guarded" },
            { "cppType" : "Expression", "name" : "sourceExp"},
        ]
    },
    "ConcSigAssignWhenElem" : {
        "parent" : "AstNode",
        "members" : [
            { "cppType" : "Expression", "name" : "sourceExp"},
            { "cppType" : "std::optional<Expression>", "name" : "afterTimeExpr"},
            { "cppType" : "Expression", "name" : "condExp"},
        ]
    },
    "Decl" : {
        "parent" : "AstNode",
        "members" : []
    },
    "GenericDecl" : {
        "parent" : "Decl",
        "members" : [
            { "cppType" : "std::vector<GenericDeclElement>", "name" : "genericDeclElements" }
        ]
    },
    "GenericDeclElement" : {
        "parent" : "Decl",
        "members" : [
            { "cppType" : "std::vector<Identifier>", "name" : "identifierList"},
            { "cppType" : "Type", "name" : "type"},
            { "cppType" : "std::optional<Expression>", "name" : "initializerExp" }
        ]
    },
    "PortDecl" : {
        "parent" : "Decl",
        "members" : []
    },
    "PortDeclElement" : {
        "parent" : "Decl",
        "members" : [
            { "cppType" : "std::vector<Identifier>", "name" : "portNames" },
            { "cppType" : "std::string", "name" : "inOrOut"},
            { "cppType" : "Type", "name" : "type" },
            { "cppType" : "std::optional<Expression>", "name" : "initializerExp" }
        ]
    },
    "Identifier" : { "parent" : "AstNode", "members" : [] },
    "QualifiedIdentifier" : {
        "parent" : "Identifier",
        "members" : [
            { "cppType" : "std::vector<std::string>", "name" : "qualifiedName" }
        ]
    },
    "SimpleIdentifier" : {
        "parent" : "Identifier",
        "members" : [
            { "cppType" : "std::string", "name" : "id" }
        ]
    }
}


lam = {
    "Term" : {
        "parent" : None,
        "members" : []
    },
    "Var" : {
        "parent" : "Term",
        "members" : [
            { "cppType" : "std::string", "name" : "name" }
        ]
    },

    "Abs" : {
        "parent" : "Term",
        "members" : [
            { "cppType" : "std::string", "name" : "name" },
            { "cppType" : "Term", "name" : "expression" }
        ]
    },

    "App" : {
        "parent": "Term",
        "members" : [
            { "cppType" : "Term", "name" : ["nameExp", "absExp"] }
        ]
    }
}

patterns = lam
superClass = "Term"
classNames = list(patterns.keys())

def canProduceSubTree(typ):
    result = False
    for i in classNames:
        result = result or (i in typ)
    return result

def unifyNames(name):
    if type(name) is list:
        return name
    else:
        return [name]

def getAllLeafClasses(patterns):
    edges = []
    nodes = []
    # add all edges
    for c, e in patterns.items():
        nodes.append(c)
        edges.append((e["parent"], c))
    leafs = []
    for n in nodes:
        contained = False
        for tup in edges:
            if n == tup[0]:
                contained = True
                break;
        if not contained:
            leafs.append(n)
    return leafs

def printAbstractAstVisitor(patterns):
    visits = []
    leafs = getAllLeafClasses(patterns)
    for l in leafs:
        visits.append("virtual R visit(" + l + " v, P p) = 0;")
    visits = "\n".join(visits)
    print("""
    template<typename P, typename R> struct AstVisitor {
    public:
    %(visits)s
    virtual R visitNull(P parameter) = 0;
    };
    """ % locals())

def printTraverseTemplate(classes):
    patterns = []
    leafs = getAllLeafClasses(classes)
    for l in leafs:
        patterns.append("""some<%(l)s>(), [&](%(l)s &n){
        return v->visit(n, initial);}""" % locals())
    patterns = ",\n".join(patterns)
    print("""
    template<typename P, typename R>
    R traverse(AstVisitor<P, R> *v,
    const std::shared_ptr<Term> &t,
    P &initial) {
    using namespace simple_match;
    using namespace simple_match::placeholders;
    return match(t,
    %(patterns)s
    none(),      [&]()      { return v->visitNull(initial); });
    }
    """ % locals())

def printTraverseTemplateDecl():
    print("""
    template<typename P, typename R>
    R traverse(AstVisitor<P, R>,
    const std::shared_ptr<Term> &,
    P &);
    """)

def printSimpleMatchAdapter():
    print("namespace simple_match {")
    print("namespace customization {")
    for className, classEntry in patterns.items():
        toTie = []
        for member in classEntry["members"]:
            typ = member["cppType"]
            name = member["name"]
            # gen tie
            for i in unifyNames(name):
                toTie.append("t." + i)
        tieStr = ", ".join(toTie)
        count = len(toTie)
        # print
        print("""
        template<> struct tuple_adapter<%(className)s> {
        enum { tuple_len = %(count)s };
        template<size_t I, class T>
        static decltype(auto) get(T&& t) {
        return std::get<I>(std::tie(%(tieStr)s));}};""" % locals())
    print("}")
    print("}")

def printDtor(className, classEntry):
    print("// DTOR")
    print("~" + className + "(){}")

def makeSharedWrapper(string, flag):
    if flag:
        return "std::shared_ptr<" + string + ">"
    else:
        return string

def printCtor(superClass, className, classEntry, shared):
    print("// CTOR")
    const = "" if not shared else "const"
    alias = " &" if shared else " *"
    if len(classEntry["members"]) == 0:
        print(className + "(){}")
        return
    decls = []
    for member in classEntry["members"]:
        typ = member["cppType"]
        name = member["name"]
        st = canProduceSubTree(typ) and shared
        if type(name) is list:
            toJoin = []
            for i in name:
                toJoin.append(const + " " + makeSharedWrapper(typ, st)
                              + alias + i)
            decls.append(", ".join(toJoin))
        else:
            decls.append(const + " " + makeSharedWrapper(typ, st)
                         + alias + name)

    print(className + "(" + ", ".join(decls) + ") : ")
    # init list
    toJoin = []
    for member in classEntry["members"]:
        typ = member["cppType"]
        name = member["name"]
        if type(name) is list:
            for i in name:
                toJoin.append(i + "("
                              + wrapIntoShared(i, superClass, not shared) + ")")
        else:
            toJoin.append(name + "("
                          + wrapIntoShared(name, superClass, not shared)+ ")")
    print(", ".join(toJoin))
    print("{}")

def wrapIntoShared(name, superClass, flag):
    if flag:
        return "std::shared_ptr<%(superClass)s>(%(name)s)" % locals()
    else:
        return name

def printHeader():
    print("#include <memory>")
    print("#include <string>")
    print("#include \"simple_match.hpp\"")
    print("""
    using namespace simple_match;
    using namespace simple_match::placeholders;
    """)

def printFooter():
    print("""
    int main(void) {

    return 0;
    }
    """)

def printClassProto():
    for key, value in patterns.items():
        print ("class " + key + ";")

def printCloneProto(superClass):
    print("virtual std::shared_ptr<%(superClass)s> clone() = 0;" % locals())

def getMembersCloneExprs(className):
    res = []
    members = patterns[className]["members"]
    for i in members:
        name = i["name"]
        typ = i["cppType"]
        clone = ""
        if canProduceSubTree(typ):
            clone = "->clone()"
        if type(name) is list:
            for i in name:
                res.append(i + clone)
        else:
            res.append(name + clone)
    return res

def printCloneImpl(className, superClass):
    toNames = getMembersCloneExprs(className)
    names = ",".join(toNames)
    print("""
    virtual std::shared_ptr<%(superClass)s> clone() override {
        return std::static_pointer_cast<Term>(
           std::make_shared<%(className)s>(%(names)s)
        );
    }
    """ % locals())

def needsConvenientCtor(className, classEntry):
    containsSubTree = False
    for member in classEntry["members"]:
        typ = member["cppType"]
        treeable = canProduceSubTree(typ)
        containsSubTree = containsSubTree or treeable
    return containsSubTree

def printClassDef():
    for key, value in patterns.items():
        isTop = value["parent"] == None
        if isTop:
            print("class " + key + " {")
        else:
            print("class " + key + " : public " + value["parent"] + " {")
        print("public:")
        for member in value["members"]:
            typ = member["cppType"]
            name = member["name"]
            treeable = canProduceSubTree(typ)
            decl = ""
            if treeable:
                decl = decl + "std::shared_ptr<" + typ +  ">" + " "
            else:
                decl = decl + typ + " "
            if type(name) is list:
                decl = decl + ", ".join(name) + ";"
            else:
                decl = decl + name + ";"
            print(decl)
        # emit ctors
        printCtor(superClass, key, value, True)
        if needsConvenientCtor(key, value):
            printCtor(superClass, key, value, False)
        # emit dtors
        if isTop:
            print("virtual")
        printDtor(key, value)

        if isTop:
            printCloneProto(key)
        else:
            printCloneImpl(key, superClass)
        print("};")
        print("")

def pE():
    print("")

printHeader()
pE()
printClassProto()
pE()
printClassDef()
pE()
printSimpleMatchAdapter()
pE()
printTraverseTemplateDecl()
pE()
printTraverseTemplate(patterns)
pE()
printAbstractAstVisitor(patterns)
printFooter()
