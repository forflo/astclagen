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
            { "astType" : "int",
              "wrpType" : ["std::vector"],
              "name" : "dimensions" }
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
    "TypeDeclSimple" : {
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

class Graph:
    nodes = []
    edges = []
    start = None

    def invertEdges(self):
        result = []
        for edge in self.edges:
            fro = edge[0]
            to = edge[1]
            result.append((to, fro))
        self.edges = result
        return self

    # start node of this remains start node
    def mergeGraphs(self, other):
        for node in other.nodes:
            if not (node in self.nodes): self.nodes.append(node)
        for edge in other.edges:
            if not (edge in self.edges): self.edges.append(edge)
        return self

    def successors(self, node):
        result = []
        for edge in self.edges:
            fro = edge[0]
            to = edge[1]
            if fro == node and (to not in result):
                result.append(to)
        return result

    def __init__(self, nodes, edges, start):
        self.nodes = nodes
        self.edges = edges
        self.start = start

    def asDot(self):
        return printAsDot(self)

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

def getDependenceGraph(classes, superClass):
    edges = []
    classSet = classes.keys()
    for c in classSet:
        relevantTypes = []
        members = classes[c]["members"]
        for member in members:
            relevantTypes.append(member["astType"])
        for rt in relevantTypes:
            edges.append((c, rt))
    # now we have all dependency edges.
    # Now add the nodes.
    nodes = [superClass]
    for e in edges:
        nodes += e
    # deduplicate the nodes
    nodesDedup = []
    for n in nodes:
        dupe = False
        for d in nodesDedup:
            if n == d:
                dupe = True
        if not dupe:
            nodesDedup.append(n)
    # until now the superClass is a unconnected node
    # conservative assumption: everything depends on the superClass
    nodes = nodesDedup
    for node in nodes:
        if node != superClass:
            edges.append((node, superClass))
    return Graph(nodes, edges, superClass)

def getClasses(classes):
    result = []
    for cls, entry in classes.items():
        if not (cls in result): result.append(cls)
    return result

# merges the inheritance tree and the dependency tree
# into one graph. The function then sorts the graph
# topologically.
def getTopolOrder(classes, superClass):
    inhG = getInheritanceGraph(classes, superClass)
    depG = getDependenceGraph(classes, superClass)
    depG.invertEdges()
    inhG.mergeGraphs(depG)
    depthFirstTraversal(inhG)
    topSort = getTopolSort(inhG, superClass)
    # now remove all nodes that are _not_ members of the class hierarchy
    result = []
    allClasses = getClasses(classes)
    topSort = list(map(lambda x: x[0], topSort))
    for t in topSort:
        if t in allClasses: result.append(t)
    return result

def getTopolSort(graph, superClass):
    depthFirstTraversal(graph)
    if not graph.acyclic:
        print("You have cyclic dependencies in your class hierarchy!")
        print("STOP")
        sys.exit(1)
    prelim = sorted(graph.finishedAt.items(), key = lambda x : x[1])
    prelim.reverse()
    return prelim

def getInheritanceGraph(classes, superClass):
    edges = []
    nodes = []
    for cls, entry in classes.items():
        parent = entry["parent"]
        edges.append((parent, cls))
        nodes.append(cls)
        nodes.append(parent)
    return Graph(nodes, edges, superClass)

def depthFirstTraversal(graph):
    nodes = graph.nodes
    edges = graph.edges
    graph.time = 0
    graph.begunAt = {}
    graph.finishedAt = {}
    graph.acyclic = True
    graph.colors = {}
    for node in nodes:
        graph.colors[node] = "white"
    for node in nodes:
        if graph.colors[node] == "white":
            dftVisit(graph, node)

# does not detect cross and forward edges!
def dftVisit(graph, node):
    graph.colors[node] = "grey"
    graph.time = graph.time + 1
    graph.begunAt[node] = graph.time
    for succ in graph.successors(node):
        if graph.colors[succ] == "white":
            dftVisit(graph, succ)
        if graph.colors[succ] == "grey":
            graph.acyclic = False
        if graph.colors[succ] == "black":
            continue # test for forward edge
    graph.colors[node] = "black"
    graph.time = graph.time + 1
    graph.finishedAt[node] = graph.time

def printAsDot(graph):
    nodes = graph.nodes
    edges = graph.edges
    startNode = graph.start
    res = ("strict digraph G {")
    print("\"%(startNode)s\";" % locals())
    for n in nodes:
        if n: res += ("\"%(n)s\";" % locals())
    for e in edges:
        fro = e[0]
        to = e[1]
        if fro:
            res += ("\"%(fro)s\" -> \"%(to)s\";" % locals())
    res += ("}")
    return res

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

# Assumption: Every type used that is not part of the
# hierarchy in `patterns` is considered triviallyCopyable
def isTriviallyCopyable(typ):
    return not canProduceSubTree(typ)

def printCtor(superClass, className, classEntry):
    print("// CTOR")
    if len(classEntry["members"]) == 0:
        print(className + "(){}")
        return
    decls = []
    # Generate Ctor signature
    for member in classEntry["members"]:
        typ = member["astType"]
        wrappers = member.get("wrpType")
        name = unifyNames(member["name"])
        treeable = canProduceSubTree(typ)
        sharedType = makeSharedWrapper(typ, treeable)
        toJoin = []
        for i in name:
            toJoin.append("const "
                          + wrapUsingWrappers(wrappers, sharedType)
                          + "& " + i)
        decls.append(", ".join(toJoin))
    # Generate init list
    print(className + "(" + ", ".join(decls) + ") : ")
    toJoin = []
    for member in classEntry["members"]:
        typ = member["astType"]
        wrappers = member.get("wrpType")
        name = unifyNames(member["name"])
        for i in name:
            toJoin.append(i + "(" + i + ")")
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

def getCtorParams(className):
    res = []
    members = patterns[className]["members"]
    for i in members:
        name = unifyNames(i["name"])
        wrapper = i["wrpType"]
        typ = i["astType"]
        for i in name:
            res.append((i, wrapper, ))
    return res

def printCloneImpl(className, superClass):
    toNames = getCtorParams(className)
    names = ",".join(toNames)
    auto = []
    for name in toNames:
        auto.append("auto %(name)s_tmp = foo;" % locals())
    auto = "\n".join(auto)
    print("""
    virtual std::shared_ptr<%(superClass)s> clone() override {
    %(auto)s
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
    order = getTopolOrder(patterns, superClass)

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
        printCtor(superClass, key, value)
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
