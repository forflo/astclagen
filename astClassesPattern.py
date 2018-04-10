vhdl = {
    "AstNode" : {
        "parent" : None,
        "members" : []
    },
    "Architecture" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "" }
        ]
    },
    "Entity" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "Identifier", "name" : "id" },
            { "astType" : "GenericDecl", "name" : "generics" },
            { "astType" : "PortDecl", "name" : "ports" },
            # TODO: entity_statement_part
        ]
    },
    "Architecture" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "Identifier", "name" : "archName"},
            { "astType" : "Identifier", "name" : "entityName"},
            { "astType" : "ConcStmt", "wrpType" : ["std::vector"],
              "name" : "concStatements"},
        ]
    },
    "ConcStmt" : {"parent" : "AstNode", "members" : []},
    "SeqStmt" : {"parent" : "AstNode", "members" : []},
    "WaitStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "Identifier",
              "wrpType" : ["std::optional", "std::vector"],
              "name" : "waitSignals"},
            { "astType" : "Expression", "name" : "condition"},
            { "astType" : "Expression", "name" : "timeExpr"},
        ]
    },
    "AssertStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "Expression", "name" : "stringExpression"},
            { "astType" : "std::string", "name" : "severity"},
        ]
    },
    "SeqSigAssignStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "Expression", "name" : "target"},
            { "astType" : "Boolean", "name" : "transport"},
            { "astType" : "Expression", "wrptype" : "std::optional",
              "name" : "afterTimeExpr"},
            { "astType" : "SeqSigAssignStmtAfter", "wrpType" : ["std::vector"],
              "name" : "expAfterList"},
        ]
    },
    "VarAssignStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "Expression", "name" : "target"},
            { "astType" : "Expression", "name" : "source"}
        ]
    },
    "ProcedureCallStmt" : {
        "parent" : "SeqStmt",
        "members" : []
    },
    "ProcedureCallStmtFptr" : {
        "parent" : "ProcedureCallStmt",
        "members" : [
            { "astType" : "Expression", "name" : "procedure"},
            { "astType" : "Expression",
              "wrpType" : ["std::vector"],
              "name" : "arguments"}
        ]
    },
    "ProcedureCallStmtSimple" : {
        "parent" : "ProcedureCallStmt",
        "members" : [
            { "astType" : "std::string", "name" : "procedure"},
            { "astType" : "Expression",
              "wrpType" : ["std::vector"],
              "name" : "arguments"}
        ]
    },
    "SeqSigAssignStmtAfter" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "Expression" , "name" : "expression" },
            { "astType" : "Expression" , "name" : "afterTimeExpr" },
        ]
    },
    "ProcessStmt" : {
        "parent" : "ConcStmt",
        "members" : [
            { "astType" : "std::string", "wrpType" : ["std::optional"],
              "name" : "label" },
            { "astType" : "Identifier", "wrpType" : ["std::vector"],
              "name" : "sensitivityList" },
            { "astType" : "Decl", "wrpType" : ["std::vector"],
              "name" : "declarations" },
            { "astType" : "SeqStmt", "wrpType" : ["std::vector"],
              "name" : "statements" },
        ]
    },
    "ConcSigAssign" : {"parent" : "AstNode", "members" : []},
    "ConcSigAssignSelect" : {
        "parent" : "ConcSigAssign",
        "members" : [
            { "astType" : "Expression", "name" : "selectionExpr" },
            { "astType" : "Expression", "name" : "target" },
            { "astType" : "ConcSigAssignSelectElem",
              "wrpType" : ["std::vector"],
              "name" : "selectElements" },
        ]
    },
    "ConcSigAssignSelectElem" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "Expression", "name" : "source" },
            { "astType" : "Expression", "wrpType" : ["std::optional"],
              "name" : "afterTimeExpr"},
            { "astType" : "ChoiceElem", "wrpType" : ["std::vector"],
              "name" : "choices" },
        ]
    },
    "ChoiceElem" : {
        "parent" : "AstNode",
        "members" : [] # TODO
    },
    "ConcSigAssignWhen" : {
        "parent" : "ConcSigAssign",
        "members" : [
            { "astType" : "std::string", "wrpType" : ["std::optional"],
              "name" : "label"},
            { "astType" : "Expression", "name" : "targetExp"},
            { "astType" : "ConcSigAssignWhenElem", "wrpType" : ["std::vector"],
              "name" : "whens" },
            { "astType" : "Boolean", "name" : "guarded" },
            { "astType" : "Expression", "name" : "sourceExp"},
        ]
    },
    "ConcSigAssignWhenElem" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "Expression", "name" : "sourceExp"},
            { "astType" : "Expression", "wrpType" : ["std::optional"],
              "name" : "afterTimeExpr"},
            { "astType" : "Expression", "name" : "condExp"},
        ]
    },
    "Expression" : {"parent" : "AstNode", "members" : []},
    "Decl" : {
        "parent" : "AstNode",
        "members" : []
    },
    "GenericDecl" : {
        "parent" : "Decl",
        "members" : [
            { "astType" : "GenericDeclElement", "wrpType" : ["std::vector"],
              "name" : "genericDeclElements" }
        ]
    },
    "GenericDeclElement" : {
        "parent" : "Decl",
        "members" : [
            { "astType" : "Identifier", "wrpType" : ["std::vector"],
              "name" : "identifierList"},
            { "astType" : "Type", "name" : "type"},
            { "astType" : "Expression", "wrpType" : ["std::optional"],
              "name" : "initializerExp" }
        ]
    },
    "Type" : {"parent" : "AstNode", "members" : []},
    # std_logic, integer, are considered builtIn
    "TypeBuiltIn" : {
        "parent" : "Type",
        "members" : [
            { "astType" : "std::string" , "name" : "typeName" }
        ]
    },
    "TypeArray" : {
        "parent" : "Type",
        "members" : [
            { "astType" : "Type" , "name" : "baseType" },
            { "astType" : "std::vector<int>", "name" : "dimensions" }
        ]
    },
    "TypeArrayOneDim" : {
        "parent" : "Type",
        "members" : [
            { "astType" : "Type" , "name" : "baseType" },
            { "astType" : "int", "name" : "dimensions" }
        ]
    },
    "TypeDecl" : {"parent" : "Decl", "members" : []},
    "TypeDecl" : {
        "parent" : "TypeDecl",
        "members" : [
            { "astType" : "Identifier", "name" : "name"},
            { "astType" : "Type", "name" : "type"},
        ]
    },
    # TODO
    "TypeDeclSubtype" : {
        "parent" : "TypeDecl",
        "members" : [
            { "astType" : "Identifier", "name" : "name"},
            { "astType" : "Type", "name" : "type"},
        ]
    },
    "PortDecl" : {
        "parent" : "Decl",
        "members" : []
    },
    "PortDeclElement" : {
        "parent" : "Decl",
        "members" : [
            { "astType" : "Identifier", "wrpType" : ["std::vector"],
              "name" : "portNames" },
            { "astType" : "std::string", "name" : "inOrOut"},
            { "astType" : "Type", "name" : "type" },
            { "astType" : "Expression", "wrpType" : ["std::optional"],
              "name" : "initializerExp" }
        ]
    },
    "Identifier" : { "parent" : "AstNode", "members" : [] },
    "QualifiedIdentifier" : {
        "parent" : "Identifier",
        "members" : [
            { "astType" : "std::string",
              "wrpType" : ["std::vector"],
              "name" : "qualifiedName" }
        ]
    },
    "SimpleIdentifier" : {
        "parent" : "Identifier",
        "members" : [
            { "astType" : "std::string", "name" : "id" }
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
            { "astType" : "std::string", "name" : "name" }
        ]
    },

    "Abs" : {
        "parent" : "Term",
        "members" : [
            { "astType" : "std::string", "name" : "name" },
            { "astType" : "Term", "name" : "expression" }
        ]
    },

    "App" : {
        "parent": "Term",
        "members" : [
            { "astType" : "Term", "name" : ["nameExp", "absExp"] }
        ]
    }
}

patterns = vhdl
superClass = "AstNode"
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

# breadth first traversal of `classes` using `superClass` as
# starting point. The Edges of the traversal are given by the
# parent child relationship
def getBreadthOrder(classes, superClass):
    result = []
    nextSet = []
    worklist = [superClass]
    while len(worklist) > 0:
        for i in worklist:
            result.append(i)
        for i in worklist:
            succs = []
            for c, e in classes.items():
                if i == e["parent"]:
                    succs.append(c)
            nextSet += succs
        worklist = nextSet
        nextSet = []
    return result

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
            typ = member["astType"]
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

def wrapUsingWrappers(wrappers, string):
    result = string
    if not wrappers:
        return result
    for wrapper in reversed(wrappers):
        result = "%(wrapper)s<%(result)s>" % locals()
    return result

def printCtor(superClass, className, classEntry, shared):
    print("// CTOR")
    const = "" if not shared else "const"
    alias = " &" if shared else " *"
    if len(classEntry["members"]) == 0:
        print(className + "(){}")
        return
    decls = []
    for member in classEntry["members"]:
        typ = member["astType"]
        wrappers = member.get("wrpType")
        name = member["name"]
        st = canProduceSubTree(typ) and shared
        if type(name) is list:
            toJoin = []
            for i in name:
                toJoin.append(const + " "
                              + wrapUsingWrappers(wrappers,
                                                  makeSharedWrapper(typ, st))
                              + alias + i)
            decls.append(", ".join(toJoin))
        else:
            decls.append(const + " "
                         + wrapUsingWrappers(wrappers,
                                             makeSharedWrapper(typ, st))
                         + alias + name)

    print(className + "(" + ", ".join(decls) + ") : ")
    # init list
    toJoin = []
    for member in classEntry["members"]:
        typ = member["astType"]
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

def wrapShared(name, flag):
    if flag:
        return "std::shared_ptr<" + name + ">"
    else:
        return name

def wrapIntoShared(name, superClass, flag):
    if flag:
        return "std::shared_ptr<%(superClass)s>(%(name)s)" % locals()
    else:
        return name

def printHeader():
    print("#include <memory>")
    print("#include <string>")
    print("#include <vector>")
    print("#include <optional>");
    print("#include \"simple_match/include/simple_match/simple_match.hpp\"")
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
        typ = i["astType"]
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
        return std::static_pointer_cast<%(superClass)s>(
           std::make_shared<%(className)s>(%(names)s)
        );
    }
    """ % locals())

def needsConvenientCtor(className, classEntry):
    containsSubTree = False
    for member in classEntry["members"]:
        typ = member["astType"]
        treeable = canProduceSubTree(typ)
        containsSubTree = containsSubTree or treeable
    return containsSubTree

def printClassDef():
    order = getBreadthOrder(patterns, superClass)

    for key in order:
        value = patterns[key]
        isTop = value["parent"] == None
        if isTop:
            print("class " + key + " {")
        else:
            print("class " + key + " : public " + value["parent"] + " {")
        print("public:")
        for member in value["members"]:
            typ = member["astType"]
            wrappers = member.get("wrpType")
            name = member["name"]
            treeable = canProduceSubTree(typ)
            decl = wrapShared(typ, treeable)
            decl = wrapUsingWrappers(wrappers, decl) + " "
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
