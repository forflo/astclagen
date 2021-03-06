# TODO: Change all subtype_indication to optional constraint

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
            { "astType" : "Decl", "wrpType" : ["std::vector"], "name" : "declarativePart"}
            # entity_statement_part is ignored IEEE 1076.6-2004 p48
        ]
    },
    "Architecture" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "Identifier", "name" : "archName"},
            { "astType" : "Identifier", "name" : "entityName"},
            { "astType" : "Decl", "wrpType" : ["std::vector"], "name" : "declarativePart"},
            { "astType" : "ConcStmt", "wrpType" : ["std::vector"], "name" : "concStatements"},
        ]
    },
    "ConcStmt" : {"parent" : "AstNode", "members" : []},
    "SeqStmt" : {"parent" : "AstNode", "members" : []},
    "WaitStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "std::string" , "name" : "label" },
            { "astType" : "Identifier",
              "wrpType" : ["std::optional", "std::vector"],
              "name" : "waitSignals"},
            { "astType" : "Expression", "name" : "condition"},
            { "astType" : "Expression", "name" : "timeExpr"},
        ]
    },
    "IfStatement" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "Expression", "name" : "condition"},
            { "astType" : "SeqStmt",
              "wrpType" : ["std::vector"], "name" : "thenStmts"},
            { "astType" : "ElsIfBlocks",
              "wrpType" : ["std::vector"], "name" : "elsifs"},
            { "astType" : "SeqStmt",
              "wrpType" : ["std::vector"], "name" : "elseStmts"},
        ]
    },
    "ElsIfBlocks" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "Expression", "name" : "condition"},
            { "astType" : "SeqStmt",
              "wrpType" : ["std::vector"], "name" : "stmts"},
        ]
    },
    "Assertion" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "Expression", "name" : "condition"},
            { "astType" : "Expression", "name" : "reportString"},
            { "astType" : "Expression", "name" : "severity"},
        ]
    },
    "AssertConcStmt" : { "parent" : "ConcStmt", "members" : [
        { "astType" : "Assertion", "name" : "assertion"},
    ]},
    "AssertSeqStmt" : { "parent" : "SeqStmt", "members" : [
        { "astType" : "Expression", "name" : "stringExpression"},
        { "astType" : "std::string", "name" : "severity"},
    ]},
    "SeqSigAssignStmt" : {
        "parent" : "SeqStmt",
        "members" : [
            { "astType" : "Expression", "name" : "target"},
            { "astType" : "bool", "name" : "transport"},
            { "astType" : "Expression", "wrpType" : ["std::optional"],
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
            { "astType" : "bool", "name" : "guarded" },
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
    # IEEE 1076.6-2004 p71
    "Expression" : {"parent" : "AstNode", "members" : []},
    "ExpressionBinary" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "Expression", "name" : "lhs"},
            { "astType" : "Expression", "name" : "rhs"},
            # For operator reference review IEEE1076.6-2004 p72
            { "astType" : "std::string", "name" : "op"},
        ]
    },
    "ExpressionUnary" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "Expression", "name" : "operand"},
            { "astType" : "std::string", "name" : "op"},
        ]
    },
    "ExpressionName" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "Name", "name" : "name" },
        ]
    },
    "ExpressionLiteral" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "Literal", "name" : "literal" },
        ]
    },
    "ExpressionFunctionCall" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "Name", "name" : "functionName" },
            { "astType" : "ActualParameterPart", "name" : "functionName" },
        ]
    },
    "ExpressionTypeConf" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "TypeConversion", "name" : "typeConversion" },
        ]
    },
    # IEEE 1076.6 p 106. qualified_expression ::= type_mark'(expression) |...
    # This non-terminal is actually only used in the production of primary.
    "ExpressionQualifiedExpr" : {
        "parent" : "Expression",
        "members" : [
            # TODO qualified_expression
            { "astType" : "Expression", "name" : "expression" },
        ]
    },
    "ExpressionExpression" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "Expression", "name" : "expression" },
        ]
    },
    "ExpressionAggregate" : {"parent" : "Expression", "members" : [
        { "astType" : "ElementAssociation", "wrpType" : ["std::vector"],
          "name" : "elementAssociations" },
    ]},
    "ElementAssociation" : { "parent" : "AstNode", "members" : [
        { "astType" : "Choice", "wrpType" : ["std::vector"],
          "name" : "choices" },
    ]},
    # IEEE 1076.6-2004 p.94
    # choice ::= simple_expression | discrete_range | simple_name | others
    # We simplify to choice ::= expression | range
    # simple_expression produces everything in expression including simple_name
    # Maybe surprisingly, the keyword OTHERS is
    # also included as child of Expression
    # (THIS IS A SIMPLIFICATION, THE ACUTAL PARSER HAS TO UNDERSTAND!)
    "Choice" : { "parent" : "AstNode", "members" : [] },
    "ChoiceExpression" : { "parent" : "Choice", "members" : [
        { "astType" : "Expression", "name" : "expression" }
    ] },
    "ChoiceRange" : { "parent" : "Choice", "members" : [
        { "astType" : "Range", "name" : "range" }
    ] },
    "ChoiceOthers" : { "parent" : "Choice", "members" : [] },
    # Literals roughly as defined in IEEE 1076.6-2004 p 73
    "RealLiteral" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "double", "name" : "value"},
        ]
    },
    "StringLiteral" : { "parent" : "Expression", "members" : [
        { "astType" : "std::string", "name" : "value"},
    ]},
    "BitStringLiteral" : { "parent" : "Expression", "members" : [
        { "astType" : "std::string", "name" : "baseSpecifier", "allowedValues" : ["B", "O", "X"] },
        { "astType" : "std::string", "name" : "value"},
    ]},

    ## This simplification is used in order to make the abstract representation
    ## of - association_list (specifically actual_designator)
    ##    - TODO: List remaining
    ## easier to represent (especially withouth all the indirections).
    # Represents the "open" keyword
    "OpenSpecification" : { "parent" : "Expression", "members" : []},
    # Represents the "all" keyword
    "AllSpecification" : { "parent" : "Expression", "members" : []},
    # Represents the "others" keyword
    "OthersSpecification" : { "parent" : "Expression", "members" : []},


    # Subsumes IEEE 1076.6-2004 'based_literal' and 'integer'
    "IntegerLiteral" : {
        "parent" : "Expression",
        "members" : [
            { "astType" : "long", "name" : "value"},
        ]
    },
    "Decl" : { "parent" : "AstNode", "members" : [] },
    # IEEE 1076.6-2004 p.63 (a)
    "ConstantDecl" : { "parent" : "Decl", "members" : [
        # constant
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "identifierList" },
        # :
        # subtype_indication
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::vector"],
          "name" : "constraint" },
        # :=
        # init expression
        { "astType" : "Expression", "name" : "initExpression" },
    ]},
    # IEEE 1076.6-2004 p.63 (b) marks the initiation expression as ignore.
    # As a consequence, we don't include it here
    "SignalDecl" : { "parent" : "Decl", "members" : [
        # signal
        # identifier_list
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "identifierList" },
        # : subtype_indication
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::vector"],
          "name" : "constraint" },
        # signal_kind
        { "astType" : "std::string", "name" : "signalKind",
          "allowedValues" : ["register", "bus"] },
        { "astType" : "", "name" : "" },
        # := expression (marked ignore)
    ]},
    # IEEE 1076.6-2004 p.63 (c) marks the initiation expression as ignore.
    # As a consequence, we don't include it here
    "VariableDecl" : { "parent" : "Decl", "members" : [
        # variable
        # identifier_list
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "identifierList" },
        # : subtype_indication
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::optional", "std::vector"],
          "name" : "constraint" },
        # := expression (marked ignore)
    ]},
    # IEEE 1076.6-2004 p.63 (d) marks the file_declaration as ignore
    # As a consequence, we don't include it here
    # .

    # IEEE 1076.6-2004 p.66
    "AliasDecl" : { "parent" : "Decl", "members" : [
        # alias_designator ::= identifier | character_literal | operator_symbol
        # We can encode all of these productions into a std::string
        { "astType" : "std::string", "name" : "aliasDesignator" },
        # : subtype_indication
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::optional", "std::vector"],
          "name" : "constraint" },
        { "astType" : "Name", "name" : "destinationAlias" },
        # signature (IEEE 1076.6-2004 p.107)
        { "astType" : "Name", "wrpType" : ["std::optional", "std::vector"],
          "name" : "typeMarks" },
        { "astType" : "Name", "wrpType" : ["std::optional"],
          "name" : "returnTypeMark" },
    ]},

    # IEEE 1076.6-2004 p.66
    "AttributeDecl" : { "parent" : "Decl", "members" : [
        # attribute
        { "astType" : "std::string", "name" : "identifier" },
        # :
        { "astType" : "Name", "name" : "typeOrSubtypeName" },
    ]},

    # IEEE 1076.6-2004 p.64
    "InterfaceDecl" : { "parent" : "Decl", "members" : []},
    "InterfaceDeclConst" : { "parent" : "Decl", "members" : [
        # constant
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "identifiers" },
        # in
        # subtype_indication
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::optional", "std::vector"],
          "name" : "constraint" },
        { "astType" : "Name", "name" : "destinationAlias" },
        # (static) initializer expression
        { "astType" : "Expression", "name" : "initExpression" }
    ]},
    # IEEE 1076.6-2004 p.101
    "InterfaceDeclSig" : { "parent" : "Decl", "members" : [
        # signal
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "identifiers" },
        # mode
        { "astType" : "std::string", "name" : "mode",
          "allowedValues" : ["in", "out", "inout", "buffer"] },
        # subtype_indication
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::optional", "std::vector"],
          "name" : "constraint" },
        { "astType" : "Name", "name" : "destinationAlias" },
        # busflag
        { "astType" : "bool", "name" : "hasBusFlag" },
        # (static) initializer expression
        { "astType" : "Expression", "name" : "initExpression" }
    ]},
    "InterfaceDeclVar" : { "parent" : "Decl", "members" : [
        # variable
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "identifiers" },
        # mode
        { "astType" : "std::string", "name" : "mode",
          "allowedValues" : ["in", "out", "inout", "buffer"] },
        # subtype_indication
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::optional", "std::vector"],
          "name" : "constraint" },
        { "astType" : "Name", "name" : "destinationAlias" },
        # (static) initializer expression
        { "astType" : "Expression", "name" : "initExpression" }
    ]},

    # IEEE 1076.6-2004 p.66
    "ComponentDecl" : { "parent" : "Decl" , "members" : [
        # component
        { "astType" : "std::string" , "name" : "identifier" },
        # [ is ]
        { "astType" : "InterfaceDecl", "wrpType" : ["std::vector"],
          "name" : "localGenericClause" },
        # generic ( ...
        { "astType" : "InterfaceDecl", "wrpType" : ["std::vector"],
          "name" : "localGenericClauses" }, # ...)
        # port ( ...
        { "astType" : "InterfaceDecl", "wrpType" : ["std::vector"],
          "name" : "localPortClauses" }, # ...)
    ]},

    # IEEE 1076.6-2004 p 51
    # configuration id of entity_name is ... end configuration
    "ConfigDecl" : {
        "parent" : "Decl",
        "members" : [
            { "astType" : "std::string", "name" : "identifier"},
            { "astType" : "std::string", "name" : "entityName"},
            { "astType" : "ConfigDeclItem", "wrpType" : ["std::vector"],
              "name" : "declarativePart"},
            { "astType" : "BlockConfig", "name" : "blockConfiguration"}
        ]
    },
    "ConfigDeclItem" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "UseClause", "name" : "useClause"},
            { "astType" : "AttrSpec", "name" : "attributeSpecification"},
        ]
    },

    # IEEE 1076.6-2004 p.67
    "AttributeSpecification" : { "parent" : "AstNode", "members" : [
        { "astType" : "std::string", "name" : "attributeName" },
        { "astType" : "SyntaxEntitySpec", "name" : "syntaxEntitySpec" },
        { "astType" : "Expression", "name" : "expression" },
    ]},
    # IEEE 1076.6-2004 p.67
    "SyntaxEntitySpec" : { "parent" : "AstNode", "members" : [
        { "astType" : "SyntaxEntityName", "wrpType" : ["std::vector"],
          "name" : "syntaxEntities" },
        # entity_class (IEEE 1076.6-2004 p.67)
        { "astType" : "std::string", "name" : "entityClass",
          "allowedValues" : [
              "entity", "architecture", "configuration", "procedure",
              "function", "package", "type", "subtype", "constant",
              "signal", "variable", "component", "label", "literal",
              "units"
          ]
        }
    ]},
    # IEEE 1076.6 p.67
    # represents entity_name_list
    # We use a string to encode everything a entity_tag can be
    # The original productions for reference:
    # entity_name_list ::= entity_designator {, entity_designator}
    # entity_designator ::= entity_tag [signature]
    # entity_tag ::= identifier | character_literal | operator_symbol
    "SyntaxEntityName" : { "parent" : "AstNode" , "members" : [
        { "astType" : "std::string", "name" : "entity_tag" },
        { "astType" : "Signature", "wrpType" : ["std::optional"],
          "name" : "signature" }
    ]},

    # IEEE 1076.6 p.68
    # represents component_specification
    "ConfigurationSpecification" : { "parent" : "AstNode", "members" : [
        { "astType" : "ComponentSpecification", "name" : "componentName" },
        # binding_indication is inlined here
        { "astType" : "EntityAspect", "wrpType" : ["std::optional"],
          "name" : "entityAspect" },
        { "astType" : "GenericMapAspect", "wrpType" : ["std::optional"],
          "name" : "genericMapAspect" },
        { "astType" : "PortMapAspect", "wrpType" : ["std::optional"],
          "name" : "portMapAspect" },
    ]},

    # IEEE 1076.6 p.68
    # represents component_specification
    "ComponentSpecification" : { "parent" : "AstNode", "members" : [
        # simplified form from instantiation_list ::= label {, label} | others | all
        # since both keywords easily encode into this string vector
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "labelsOrOthersOrAll" },
        { "astType" : "Name", "name" : "componentName" }
    ]},

    "EntityAspect" : { "parent" : "AstNode", "members" : []},
    "EntityAspectOpen" : { "parent" : "EntityAspect", "members" : []},
    "EntityAspectEntity" : { "parent" : "EntityAspect", "members" : [
        { "astType" : "Name", "name" : "entityName" },
        { "astType" : "std::string", "wrpType" : ["std::optional"],
          "name" : "archIdentifier" },
    ]},
    "EntityAspectConfig" : { "parent" : "EntityAspect", "members" : [
        { "astType" : "Name", "name" : "configurationName" },
    ]},

    "GenericMapAspect" : { "parent" : "AstNode", "members" : [
        { "astType" : "AssociationList", "name" : "genericAssocList" },
    ]},
    "PortMapAspect" : { "parent" : "AstNode", "members" : [
        { "astType" : "AssociationList", "name" : "portAssocList" },
    ]},

    ## Simplifications used for association_list (IEEE 1076.6-2004 p.65):
    ## association_list ::= { association_element }
    ## association_element ::= [formal_part =>] actual_part
    ##   which we simplify to
    ## association_element' ::= [name =>] expr
    ## => formal_part was previously
    ##    formal_part ::= formal_designator
    ##                  | function_name ( formal_designator)
    ##                  | type_mark ( formal_designator)
    ##    formal_designator ::= name
    ##    -- simplification steps
    ##            Hence we can simplify formal_part to
    ##    formal_part' ::= name | function_name (name) | type_mark (name)
    ##            and because a function_name and a type_mark are
    ##            just names themselves.
    ##            we simplify further to
    ##    formal_part'' ::= name | name (name)
    ##            and using the fact that the rhs `name (name)`
    ##            can be expressed by
    ##            a simple indexd_name (IEEE 1076.6-2004 p.70) we finally conclude to
    ##    formal_part''' ::= name
    ##    ---------------------------
    ##
    ## => actual_part was
    ##    actual_part ::= actual_designator
    ##                  | function_name ( actual_designator )
    ##                  | type_mark ( actual_designator )
    ##    actual_designator ::= expression | name | open
    ##            using function_name == name and type_mark == name
    ##    actual_part' ::= actual_designator
    ##                  | name ( actual_designator )
    ##
    ##            and using the fact that the actual_designator can
    ##            be expressed as normal expression iff we make `open`
    ##            itself an expression (which we'll do).
    ##    actual_part' ::= expression
    ##                  | name ( expression )
    ##            which is the same as
    ##    actual_part' ::= expression
    ##    ---------------------------
    ##            since name (expression) already is an indexed_expression and thus
    ##            can be reduced to expression.
    "AssociationList" : { "parent" : "AstNode", "members" : [
        { "astType" : "AssociationElem", "wrpType" : ["std::vector"],
          "name" : "assocElementList" }
    ]},
    "AssociationElement" : { "parent" : "AstNode", "members" : [
        { "astType" : "Name", "wrpType" : ["std::optional"],
          "name" : "formalName" },
        { "astType" : "Expression", "name" : "actualExpression" }
    ]},


    ## LEFTOFF@@

    # p.104: prefix ::= name | functinon_call. Simplified to
    # prefix ::= name | expression
    "Prefix" : {"parent" : "AstNode", "members" : []},
    "PrefixName" : {"parent" : "Prefix", "members" : [
        { "astType" : "Name", "name" : "name" },
    ]},
    "PrefixCall" : {"parent" : "Prefix", "members" : [
        { "astType" : "Expression", "name" : "functionCall" },
    ]},
    # TODO: UNSIMPLIFY!
    # p 108: suffix ::= simple_name | character_literal | operator_symbol | "all"
    # simplified to suffix ::= character_string
    "Suffix" : {"parent" : "AstNode", "members" : [
        { "astType" : "std::string", "name" : "suffixString" },
    ]},
    "OperatorSymbol" : {"parent" : "AstNode", "members" : [
        { "astType" : "std::string", "name" : "operator"}
    ]},
    # p 102: name ::= simple_name | operator_symbol | selected_name
    #               | indexed_name | slice_name | attrib_name
    # simple_name and operator_symbol simplified to std::string
    "Name" : {"parent" : "AstNode", "members" : []},
    "AttributeName" : {"parent" : "Name", "members" : [
        { "astType" : "Prefix", "name" : "prefixExp" }, # TODO
        { "astType" : "Signature", "wrpType" : ["std::optional"], "name" : "prefixExp" },
        { "astType" : "std::string", "name" : "attributeName" },
        { "astType" : "Expression", "wrpType": ["std::optional"], "name" : "expression" },
    ]},
    "SelectedName" : {"parent" : "Name", "members" : [
        { "astType" : "Prefix", "name" : "prefix" },
        { "astType" : "Suffix", "name" : "suffix" },
    ]},
    # p100: IndexedName ::= prefix ( {expression}+ )
    "IndexedName" : {"parent" : "Name", "members" : [
        { "astType" : "Prefix", "name" : "prefix" },
        { "astType" : "Expression", "wrpType" : ["std::vector"], "name" : "indexExpressions" },
    ]},
    # p102: SliceName ::= prefix ( discrete_range )
    # discrete_range ::= discrete_subtype_indication | range. However IEEE 1076.6-2004
    # does not specify what discrete_subtype_indication looks like. We let
    # discrete_range be simply a range. Semantic analysis must check, that the
    # upper and lower bounds of the ranges both are discrete values
    "SliceName" : {"parent" : "Name", "members" : [
        { "astType" : "Prefix", "name" : "prefix" },
        { "astType" : "Range", "name" : "sliceRange" },
    ]},
    "OperatorName" : {"parent" : "Name", "members" : [
        { "astType" : "std::string", "name" : "operator" },
    ]},
    "SimpleName" : {"parent" : "Name", "members" : [
        { "astType" : "std::string", "name" : "identifier" },
    ]},


    # This simplifies IEEE1076.6-2004 p 98 rule 'entity_tag' and
    # 'entity_designator'
    # a string is used to represent the non-terminals simple_name
    # character_literal and operator_symbol
    "EntityDesignator" : {"parent" : "AstNode", "members" : [
        { "astType" : "std::string", "name" : "entityTag" },
        # { "astType" : "Signature", "name" : "signature" } # TODO
    ]},

    "EntityNameList" : {"parent" : "AstNode", "members" : []},
    "EntityNameListDesignators" : {"parent" : "EntityNameList", "members" : [
        { "astType" : "EntityDesignator", "wrpType" : ["std::vector"], "name" : "entityDesignators" },
    ]},
    "EntityNameListOthers" : {"parent" : "EntityNameList", "members" : []}, # represents others
    "EntityNameListAll" : {"parent" : "EntityNameList", "members" : []}, # represents all

    "EntitySpec" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "EntityNameList", "name" : "entityNameList" },
            # according to IEEE1076.6-2004 this is supposed to be a full syntax
            # intendet do be reused. However in the context of 1076.6-2004 it
            # is never used elsewhere. Hence the encoding as simple string
            # is possible. (See p 97 rule entity_class)
            { "astType" : "std::string", "name" : "entityClass" },
        ]
    },
    "" : {
        "parent" : "",
        "members" : [
            { "astType" : "", "name" : "" }
        ]
    },

    # IEEE 1076.6-2004 p 51
    # for block_specification {use_clause} {configuration_item} end for;
    "BlockConfig" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "BlockSpec", "name" : "blockSpecification" },
            { "astType" : "UseClause", "wrpType" : ["std::vector"], "name" : "useClause" },
            { "astType" : "ConfigItem", "wrpType" : ["std::vector"], "name" : "configurationItems" },
        ]
    },

    # IEEE 1076.6-2004 p 109
    # use {selected_name}+
    "UseClause" : { "parent" : "AstNode", "members" : [
        { "astType" : "SelectedName", "wrpType" : ["std::vector"], "name" : "selectedName" }
    ]},


    # Config Item
    "ConfigItem" : {
        "parent" : "AstNode",
        "members" : []
    },
    "ConfigItemBlock" : {
        "parent" : "ConfigItem",
        "members" : [
            { "astType" : "BlockConfig", "name" : "blockConfig" },
        ]
    },
    "ConfigItemCompConfig" : {
        "parent" : "ConfigItem",
        "members" : [
            { "astType" : "ComponentConfig", "name" : "blockConfig" },
        ]
    },
    # End Config Item

    # BEGIN BLOCK SPEC
    "BlockSpec" : {
        "parent" : "AstNode",
        "members" : []
    },
    "BlockSpecArchName" : {
        "parent" : "BlockSpec",
        "members" : [
            { "astType" : "std::string", "name" : "archName" },
        ]
    },
    "BlockSpecLabel" : {
        "parent" : "BlockSpec",
        "members" : [
            { "astType" : "std::string", "name" : "statementLabel" }
        ]
    },
    # IEEE p 51 says that instead of the range a simple expression could also be
    # used here. But nope. This simplification is no permanent limitation, hence
    # it is ommitted
    "BlockSpecGenerate" : {
        "parent" : "BlockSpec",
        "members" : [
            { "astType" : "std::string", "name" : "generateLabel" },
            { "astType" : "Range", "name" : "range" }
        ]
    },
    # END BLOCK SPEC

    ## Component configuration
    "ComponentConfig" : {
        "parent" : "AstNode",
        "members" : [
            { "astType" : "", "name" : "" },
            { "astType" : "BindingInd", "wrpType" :  ["std::optional"], "name" : "bindingIndication" },
            { "astType" : "BlockConfig", "wrpType" :  ["std::optional"], "name" : "blockConfiguration" },
        ]
    },

    "BindingInd" : {
        "parent" : "AstNode",
        "members" : []
    },
    "BindingIndUse" : {
        "parent" : "BindingInd",
        "members" : [ # HACK: only one member can be non-empty!
                      # 1076.6-2004 p 97 "entity_aspect"
            { "astType" : "std::string", "name" : "entityName" },
            { "astType" : "std::string", "name" : "archName" },
            { "astType" : "std::string", "name" : "configName" },
        ]
    },
    ## TODO
    "BindingIndGenMap" : {"parent" : "BindingInd", "members" : [] },
    ## TODO
    "BindingIndPortMap" : {"parent" : "BindingInd", "members" : [] },


    # IEEE 1076.6-2004 p 106: range ::= range_attribute_name
    #                                 | expression direction expression
    "Range" : { "parent" : "AstNode", "members" : [] },
    "RangeAttrib" : {
        "parent" : "Range",
        "members" : [
            { "astType" : "AttributeName", "name" : "rangeAttribute" },
        ]
    },
    "RangeDirectional" : {
        "parent" : "Range",
        "members" : [
            { "astType" : "Expression", "name" : "leftExpression" },
            { "astType" : "std::string", "name" : "direction" },
            { "astType" : "Expression", "name" : "rightExpression" }
        ]
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

    ## MARK: obsolete
    "Type" : {"parent" : "AstNode", "members" : []},
    # std_logic, integer, are considered builtIn
    "TypeBuiltIn" : {
        "parent" : "Type",
        "members" : [
            { "astType" : "std::string" , "name" : "typeName" }
        ]
    },
    ## MARK: obsolete
    "TypeArray" : {
        "parent" : "Type",
        "members" : [
            { "astType" : "Type" , "name" : "baseType" },
            { "astType" : "int",
              "wrpType" : ["std::vector"],
              "name" : "dimensions" }
        ]
    },
    ## MARK: obsolete
    "TypeArrayOneDim" : {
        "parent" : "Type",
        "members" : [
            { "astType" : "Type" , "name" : "baseType" },
            { "astType" : "int", "name" : "dimensions" }
        ]
    },
    "TypeDecl" : {"parent" : "Decl", "members" : []},
    # IEEE 1076.6-2004 p 61:
    # type_declaration ::= full_type_declaration | incomplete_type_declaration
    # incomplete_type_declaration is marked `ignore`.
    # Hence, we don't include it here
    # type identifier is type_definition;
    "TypeDeclFull" : {
        "parent" : "TypeDecl",
        "members" : [
            # IEEE 1076.6-2004 p100
            # identifier ::= basic_identifier | extended_identifier
            { "astType" : "std::string", "name" : "identifier"},
            { "astType" : "TypeDef", "name" : "typeDefinition"},
        ]
    },
    # IEEE1076.6-2004 p.62
    "TypeDeclSubtype" : {
        "parent" : "TypeDecl",
        "members" : [
            # subtype
            { "astType" : "std::string", "name" : "name"},
            # is
            { "astType" : "Name", "wrpType" : ["std::optional"], "name" : "resolutionFunctionName"},
            { "astType" : "Name", "name" : "typeMark" },
            # According to IEEE 1076.6-2004 p.62, the actual rule here would be:
            # constraint ::= range_constraint | index_constraint
            # range_constraint ::= "range" range
            # index_constraint ::= discrete_range { "," discrete_range }*
            { "astType" : "Range", "wrpType" : ["std::vector"],
              "name" : "rangeConstraint" },
            # ;
        ]
    },
    "TypeDef" : { "parent" : "AstNode", "members" : [] },
    "TypeDefEnum" : { "parent" : "TypeDef", "members" : [
        # IEEE 1076.6-2004 p.57: enumeration_literal ::= identifier | character_literal
        { "astType" : "std::string", "wrpType" : ["std::vector"], "name" : "enumLiteral" }
    ]},
    "TypeDefInteger" : { "parent" : "TypeDef", "members" : [
        { "astType" : "Range", "name" : "rangeConstraint" }
    ]},
    "TypeDefInteger" : { "parent" : "TypeDef", "members" : [
        { "astType" : "Range", "name" : "rangeConstraint" }
    ]},
    # floating_type_definition ::= range_constraint. Marked `ignore`
    "TypeDefArray" : { "parent" : "TypeDef", "members" : []},
    # IEEE 1076.6-2004 p.59
    # unconstrained_array_definition ::=
    #   array ( index_subtype_definition {, index_subtype_defintion} )
    #   of subtype_indication
    # index_subtype_definition ::= type_mark "range" "<>"
    # We simplify type_mark = name (IEEE1076-2004 p.109)
    "TypeDefArrayUnconstr" : { "parent" : "TypeDefArray", "members" : [
        # array
        # (
        { "astType" : "Name", "wrpType" : ["std::vector"], "name" : "typeMarks" },
        # .. range <>) of <subtype_indication>
        { "astType" : "Name", "wrpType" : ["std::optional"], "name" :
          "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::vector"],
          "name" : "constraint" },
    ]},
    "TypeDefArrayConstr" : { "parent" : "TypeDefArray", "members" : [
        # array
        { "astType" : "Range", "wrpType" : ["std::vector"],
          "name" : "indexConstraints" },
        # of <subtype_indication>:
        { "astType" : "Name", "wrpType" : ["std::optional"],
          "name" : "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::vector"],
          "name" : "constraint" },
    ]},

    # IEEE 1076.6-2004 p.60
    "TypeDefRecord" : { "parent" : "TypeDef", "members" : [
        # record
        { "astType" : "std::string", "wrpType" : ["std::optional"],
          "name" : "identifier" }, # element_declaration
        # end record
        { "astType" : "std::string", "wrpType" : ["std::optional"],
          "name" : "identifier" }, # element_declaration
    ]},
    # An element declaration is the part of a record defintion where a name
    # or a list of names is associated with type marks
    "ElementDeclaration" : {"parent" : "AstNode", "members" : [
        { "astType" : "std::string", "wrpType" : ["std::vector"],
          "name" : "identifierList" },
        # element_subtype_indication ::= subtype_indication
        #   (see IEEE 1076.6-2004 p.60)
        { "astType" : "Name", "wrpType" : ["std::optional"],
          "name" : "resolutionFunctionName" },
        { "astType" : "Name", "name" : "typeMark" },
        { "astType" : "Range", "wrpType" : ["std::vector"],
          "name" : "constraint" },
    ]},

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

class Wrappee:
    wrappee = None

    def __init__(self, wrappee):
        self.wrappee = wrappee

    def getWrapped(self):
        treeable = canProduceSubTree(self.wrappee)
        if treeable:
            return "std::shared_ptr<" + self.wrappee + ">"
        return self.wrappee

    def getBase(self):
        return self.wrappee

class TypeDecl:
    # True True means std::optional<std::vector<wrappee>>
    optional = False
    vector = False
    name = ""
    treeable = None
    wrappee = None # for example Expression

    def __init__(self, wrappers, wrappee, name):
        if not wrappers: wrappers = []
        if len(wrappers) > 2:
            printf("too many wrappers")
            printf("can only contain optional, vector or both")
            sys.exit(1)
        for w in wrappers:
            if w not in ["std::optional", "std::vector"]:
                print("Can only be std::optional or std::vector")
                sys.exit(1)
        if "std::optional" in wrappers: self.optional = True
        if "std::vector" in wrappers: self.vector = True
        self.treeable = canProduceSubTree(wrappee)
        self.name = name
        self.wrappee = Wrappee(wrappee)

    def maybeWrapOpt(self, string):
        return "std::optional<%(string)s>" % locals() if self.optional else string

    def maybeWrapVec(self, string):
        return "std::vector<%(string)s>" % locals() if self.vector else string

    def wrapConstRef(self, string):
        return "const " + string + " &"

    def getVarDecl(self, name):
        str = self.wrappee.getWrapped()
        return self.maybeWrapOpt(self.maybeWrapVec(str))

    def getParamDecl(self, name):
        str = self.wrappee.getWrapped()
        return self.wrapConstRef(self.maybeWrapOpt(self.maybeWrapVec(str)))

def getCloneCode(typeDecls, className):
    code = []
    copies = []
    for td in typeDecls:
        nameOrig = td.name
        nameCopy = td.name + "_copy"
        typeDecl = td.getVarDecl("")
        baseType = td.wrappee.getBase()
        copies.append(nameCopy)
        if td.treeable:
            code.append("%(typeDecl)s %(nameCopy)s;" % locals())
            if td.vector and td.optional:
                code.append("if (%(nameOrig)s.has_value()) {" % locals())
                code.append("""
                for (auto &i : *%(nameOrig)s) {
                %(nameCopy)s->push_back(
                std::dynamic_pointer_cast<%(baseType)s>(i->clone())
                );
                }
                """ % locals())
                code.append("}")
            if td.vector and not td.optional:
                code.append("""
                for (auto &i : %(nameOrig)s) {
                %(nameCopy)s.push_back(
                std::dynamic_pointer_cast<%(baseType)s>(i->clone())
                );
                }
                """ % locals())
            if not td.vector and td.optional:
                code.append("if (%(nameOrig)s.has_value()) {" % locals())
                code.append("""
                %(nameCopy)s = std::dynamic_pointer_cast<%(baseType)s>(
                (*%(nameOrig)s)->clone());
                """ % locals())
                code.append("}")
            if not td.vector and not td.optional:
                code.append("""
                %(nameCopy)s = std::dynamic_pointer_cast<%(baseType)s>(%(nameOrig)s->clone());
                """ % locals())
        else:
            code.append("%(typeDecl)s %(nameCopy)s = %(nameOrig)s;" % locals())
    return (code, copies)

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

def printTraverseTemplate(classes, superClass):
    patterns = []
    leafs = getAllLeafClasses(classes)
    for l in leafs:
        patterns.append("""some<%(l)s>(), [&](%(l)s &n){
        return v->visit(n, initial);}""" % locals())
    patterns = ",\n".join(patterns)
    print("""
    template<typename P, typename R>
    R traverse(AstVisitor<P, R> *v,
    const std::shared_ptr<%(superClass)s> &t,
    P &initial) {
    using namespace simple_match;
    using namespace simple_match::placeholders;
    return match(t,
    %(patterns)s ,
    none(),      [&]()      { return v->visitNull(initial); });
    }
    """ % locals())

def printTraverseTemplateDecl(superClass):
    print("""
    template<typename P, typename R>
    R traverse(AstVisitor<P, R>,
    const std::shared_ptr<%(superClass)s> &,
    P &);
    """ % locals())

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
        names = unifyNames(member["name"])
        toJoin = []
        for name in names:
            typeDecl = TypeDecl(wrappers, typ, name)
            toJoin.append(typeDecl.getParamDecl(name) + " " + name)
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

def printCloneImpl(typeDecls, className, superClass):
    cloneCodeTups = getCloneCode(typeDecls, className)
    print("""
    virtual std::shared_ptr<%(superClass)s> clone() override {
    """ % locals())

    print("\n".join(cloneCodeTups[0]))
    names = ",".join(cloneCodeTups[1])

    print("""
        return std::static_pointer_cast<%(superClass)s>(
           std::make_shared<%(className)s>(%(names)s)
        );
    }
    """ % locals())

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
        typeDecls = []
        typeDeclStrs = []
        for member in value["members"]:
            typ = member["astType"]
            wrappers = member.get("wrpType")
            names = unifyNames(member["name"])
            for name in names:
                typeDecl = TypeDecl(wrappers, typ, name)
                typeDecls.append(typeDecl)
                typeDeclStrs.append(typeDecl.getVarDecl(name) + " " + name + ";")
        print("\n".join(typeDeclStrs))
        # emit ctors
        printCtor(superClass, key, value)
        # emit dtors
        if isTop:
            print("virtual")
        printDtor(key, value)

        if isTop:
            printCloneProto(key)
        else:
            printCloneImpl(typeDecls, key, superClass)
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
printAbstractAstVisitor(patterns)
pE()
printTraverseTemplateDecl(superClass)
pE()
printTraverseTemplate(patterns, superClass)
printFooter()
