Program (1)
  ExtDefList (1)
    ExtDef (1)
      Specifier (1)
        StructSpecifier (1)
          STRUCT
          Tag (1)
            ID: intset
      SEMI
    ExtDefList (2)
      ExtDef (2)
        Specifier (2)
          StructSpecifier (2)
            STRUCT
            Tag (2)
              ID: uint8_t
        SEMI
      ExtDefList (3)
        ExtDef (3)
          Specifier (3)
            StructSpecifier (3)
              STRUCT
              Tag (3)
                ID: int64_t
          SEMI
        ExtDefList (5)
          ExtDef (5)
            Specifier (5)
              StructSpecifier (5)
                STRUCT
                Tag (5)
                  ID: uint8_t
            FunDec (5)
              ID: intset_search
              LP
              VarList (5)
                ParamDec (5)
                  Specifier (5)
                    StructSpecifier (5)
                      STRUCT
                      Tag (5)
                        ID: intset
                  VarDec (5)
                    ID: is
                COMMA
                VarList (5)
                  ParamDec (5)
                    Specifier (5)
                      StructSpecifier (5)
                        STRUCT
                        Tag (5)
                          ID: int64_t
                    VarDec (5)
                      ID: value
                  COMMA
                  VarList (5)
                    ParamDec (5)
                      Specifier (5)
                        StructSpecifier (5)
                          STRUCT
                          Tag (5)
                            ID: uint32_t
                      VarDec (5)
                        ID: pos
              RP
            CompSt (5)
              LC
              DefList (6)
                Def (6)
                  Specifier (6)
                    TYPE: int
                  DecList (6)
                    Dec (6)
                      VarDec (6)
                        ID: min
                      ASSIGNOP
                      Exp (6)
                        INT: 0
                    COMMA
                    DecList (6)
                      Dec (6)
                        VarDec (6)
                          ID: max
                        ASSIGNOP
                        Exp (6)
                          Exp (6)
                            ID: intrev32ifbe
                            LP
                            Args (6)
                              Exp (6)
                                Exp (6)
                                  ID: is
                                DOT
                                ID: length
                            RP
                          MINUS
                          Exp (6)
                            INT: 1
                      COMMA
                      DecList (6)
                        Dec (6)
                          VarDec (6)
                            ID: mid
                          ASSIGNOP
                          Exp (6)
                            MINUS
                            Exp (6)
                              INT: 1
                  SEMI
                DefList (7)
                  Def (7)
                    Specifier (7)
                      StructSpecifier (7)
                        STRUCT
                        Tag (7)
                          ID: int64_t
                    DecList (7)
                      Dec (7)
                        VarDec (7)
                          ID: cur
                        ASSIGNOP
                        Exp (7)
                          MINUS
                          Exp (7)
                            INT: 1
                    SEMI
              StmtList (9)
                Stmt (9)
                  IF
                  LP
                  Exp (9)
                    Exp (9)
                      ID: intrev32ifbe
                      LP
                      Args (9)
                        Exp (9)
                          Exp (9)
                            ID: is
                          DOT
                          ID: length
                      RP
                    RELOP
                    Exp (9)
                      INT: 0
                  RP
                  Stmt (9)
                    CompSt (9)
                      LC
                      StmtList (10)
                        Stmt (10)
                          IF
                          LP
                          Exp (10)
                            ID: pos
                          RP
                          Stmt (10)
                            Exp (10)
                              Exp (10)
                                ID: pos
                              ASSIGNOP
                              Exp (10)
                                INT: 0
                            SEMI
                        StmtList (11)
                          Stmt (11)
                            RETURN
                            Exp (11)
                              INT: 0
                            SEMI
                      RC
                  ELSE
                  Stmt (12)
                    CompSt (12)
                      LC
                      StmtList (13)
                        Stmt (13)
                          IF
                          LP
                          Exp (13)
                            Exp (13)
                              ID: value
                            RELOP
                            Exp (13)
                              ID: intset_get
                              LP
                              Args (13)
                                Exp (13)
                                  ID: is
                                COMMA
                                Args (13)
                                  Exp (13)
                                    ID: max
                              RP
                          RP
                          Stmt (13)
                            CompSt (13)
                              LC
                              StmtList (14)
                                Stmt (14)
                                  IF
                                  LP
                                  Exp (14)
                                    ID: pos
                                  RP
                                  Stmt (14)
                                    Exp (14)
                                      Exp (14)
                                        ID: pos
                                      ASSIGNOP
                                      Exp (14)
                                        ID: intrev32ifbe
                                        LP
                                        Args (14)
                                          Exp (14)
                                            Exp (14)
                                              ID: is
                                            DOT
                                            ID: length
                                        RP
                                    SEMI
                                StmtList (15)
                                  Stmt (15)
                                    RETURN
                                    Exp (15)
                                      INT: 0
                                    SEMI
                              RC
                          ELSE
                          Stmt (16)
                            IF
                            LP
                            Exp (16)
                              Exp (16)
                                ID: value
                              RELOP
                              Exp (16)
                                ID: intset_get
                                LP
                                Args (16)
                                  Exp (16)
                                    ID: is
                                  COMMA
                                  Args (16)
                                    Exp (16)
                                      INT: 0
                                RP
                            RP
                            Stmt (16)
                              CompSt (16)
                                LC
                                StmtList (17)
                                  Stmt (17)
                                    IF
                                    LP
                                    Exp (17)
                                      ID: pos
                                    RP
                                    Stmt (17)
                                      Exp (17)
                                        Exp (17)
                                          ID: pos
                                        ASSIGNOP
                                        Exp (17)
                                          INT: 0
                                      SEMI
                                  StmtList (18)
                                    Stmt (18)
                                      RETURN
                                      Exp (18)
                                        INT: 0
                                      SEMI
                                RC
                      RC
                StmtList (22)
                  Stmt (22)
                    WHILE
                    LP
                    Exp (22)
                      Exp (22)
                        ID: max
                      RELOP
                      Exp (22)
                        ID: min
                    RP
                    Stmt (22)
                      CompSt (22)
                        LC
                        StmtList (23)
                          Stmt (23)
                            Exp (23)
                              Exp (23)
                                ID: mid
                              ASSIGNOP
                              Exp (23)
                                ID: shr
                                LP
                                Args (23)
                                  Exp (23)
                                    LP
                                    Exp (23)
                                      Exp (23)
                                        ID: min
                                      PLUS
                                      Exp (23)
                                        ID: max
                                    RP
                                  COMMA
                                  Args (23)
                                    Exp (23)
                                      INT: 1
                                RP
                            SEMI
                          StmtList (24)
                            Stmt (24)
                              Exp (24)
                                Exp (24)
                                  ID: cur
                                ASSIGNOP
                                Exp (24)
                                  ID: intset_get
                                  LP
                                  Args (24)
                                    Exp (24)
                                      ID: is
                                    COMMA
                                    Args (24)
                                      Exp (24)
                                        ID: mid
                                  RP
                              SEMI
                            StmtList (25)
                              Stmt (25)
                                IF
                                LP
                                Exp (25)
                                  Exp (25)
                                    ID: value
                                  RELOP
                                  Exp (25)
                                    ID: cur
                                RP
                                Stmt (25)
                                  CompSt (25)
                                    LC
                                    StmtList (26)
                                      Stmt (26)
                                        Exp (26)
                                          Exp (26)
                                            ID: min
                                          ASSIGNOP
                                          Exp (26)
                                            Exp (26)
                                              ID: mid
                                            PLUS
                                            Exp (26)
                                              INT: 1
                                        SEMI
                                    RC
                                ELSE
                                Stmt (27)
                                  IF
                                  LP
                                  Exp (27)
                                    Exp (27)
                                      ID: value
                                    RELOP
                                    Exp (27)
                                      ID: cur
                                  RP
                                  Stmt (27)
                                    CompSt (27)
                                      LC
                                      StmtList (28)
                                        Stmt (28)
                                          Exp (28)
                                            Exp (28)
                                              ID: max
                                            ASSIGNOP
                                            Exp (28)
                                              Exp (28)
                                                ID: mid
                                              MINUS
                                              Exp (28)
                                                INT: 1
                                          SEMI
                                      RC
                                  ELSE
                                  Stmt (29)
                                    CompSt (29)
                                      LC
                                      StmtList (30)
                                        Stmt (30)
                                          Exp (30)
                                            ID: break
                                          SEMI
                                      RC
                        RC
                  StmtList (34)
                    Stmt (34)
                      IF
                      LP
                      Exp (34)
                        Exp (34)
                          ID: value
                        RELOP
                        Exp (34)
                          ID: cur
                      RP
                      Stmt (34)
                        CompSt (34)
                          LC
                          StmtList (35)
                            Stmt (35)
                              IF
                              LP
                              Exp (35)
                                ID: pos
                              RP
                              Stmt (35)
                                Exp (35)
                                  Exp (35)
                                    ID: pos
                                  ASSIGNOP
                                  Exp (35)
                                    ID: mid
                                SEMI
                            StmtList (36)
                              Stmt (36)
                                RETURN
                                Exp (36)
                                  INT: 1
                                SEMI
                          RC
                      ELSE
                      Stmt (37)
                        CompSt (37)
                          LC
                          StmtList (38)
                            Stmt (38)
                              IF
                              LP
                              Exp (38)
                                ID: pos
                              RP
                              Stmt (38)
                                Exp (38)
                                  Exp (38)
                                    ID: pos
                                  ASSIGNOP
                                  Exp (38)
                                    ID: min
                                SEMI
                            StmtList (39)
                              Stmt (39)
                                RETURN
                                Exp (39)
                                  INT: 0
                                SEMI
                          RC
              RC
