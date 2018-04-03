patterns = {
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
superClass = "Term"
classNames = list(patterns.keys())

def canProduceSubTree(className):
    return className in classNames

def unifyNames(name):
    if type(name) is list:
        return name
    else:
        return [name]

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

def printCtor(className, classEntry):
    print("// CTOR")
    if len(classEntry["members"]) == 0:
        print(className + "(){}")
        return
    decls = []
    for member in classEntry["members"]:
        typ = member["cppType"]
        name = member["name"]
        st = canProduceSubTree(typ)
        if type(name) is list:
            toJoin = []
            for i in name:
                toJoin.append("const " + makeSharedWrapper(typ, st) + " &" + i)
            decls.append(", ".join(toJoin))
        else:
            decls.append("const " + makeSharedWrapper(typ, st) + " &" + name)

    print(className + "(" + ", ".join(decls) + ") : ")
    # init list
    toJoin = []
    for member in classEntry["members"]:
        typ = member["cppType"]
        name = member["name"]
        if type(name) is list:
            for i in name:
                toJoin.append(i + "(" + i + ")")
        else:
            toJoin.append(name + "(" + name + ")")
    print(", ".join(toJoin))
    print("{}")

def printHeader():
    print("#include<memory>")
    print("#include<string>")

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
        printCtor(key, value)
        if isTop:
            print("virtual")
        printDtor(key, value)

        if isTop:
            printCloneProto(key)
        else:
            printCloneImpl(key, superClass)
        print("};")
        print("")

printHeader()
printClassProto()
printClassDef()

printSimpleMatchAdapter()
