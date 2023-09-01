Program (39)
  ExtDefList (39)
    ExtDef (39)
      Specifier (39)
        StructSpecifier (39)
          STRUCT
          Tag (39)
            ID: liststar
      FunDec (39)
        ID: listDup
        LP
        VarList (39)
          ParamDec (39)
            Specifier (39)
              StructSpecifier (39)
                STRUCT
                Tag (39)
                  ID: liststar
            VarDec (39)
              ID: orig
        RP
      CompSt (40)
        LC
        DefList (41)
          Def (41)
            Specifier (41)
              StructSpecifier (41)
                STRUCT
                Tag (41)
                  ID: liststar
            DecList (41)
              Dec (41)
                VarDec (41)
                  ID: copy
            SEMI
          DefList (42)
            Def (42)
              Specifier (42)
                StructSpecifier (42)
                  STRUCT
                  Tag (42)
                    ID: listIter
              DecList (42)
                Dec (42)
                  VarDec (42)
                    ID: iter
              SEMI
            DefList (43)
              Def (43)
                Specifier (43)
                  StructSpecifier (43)
                    STRUCT
                    Tag (43)
                      ID: listNodestar
                DecList (43)
                  Dec (43)
                    VarDec (43)
                      ID: node
                SEMI
        StmtList (45)
          Stmt (45)
            IF
            LP
            Exp (45)
              Exp (45)
                LP
                Exp (45)
                  Exp (45)
                    ID: copy
                  ASSIGNOP
                  Exp (45)
                    ID: listCreate
                    LP
                    RP
                RP
              RELOP
              Exp (45)
                ID: NULL
            RP
            Stmt (46)
              RETURN
              Exp (46)
                ID: NULL
              SEMI
          StmtList (47)
            Stmt (47)
              Exp (47)
                Exp (47)
                  Exp (47)
                    ID: copy
                  DOT
                  ID: dup
                ASSIGNOP
                Exp (47)
                  Exp (47)
                    ID: orig
                  DOT
                  ID: dup
              SEMI
            StmtList (48)
              Stmt (48)
                Exp (48)
                  Exp (48)
                    Exp (48)
                      ID: copy
                    DOT
                    ID: free
                  ASSIGNOP
                  Exp (48)
                    Exp (48)
                      ID: orig
                    DOT
                    ID: free
                SEMI
              StmtList (49)
                Stmt (49)
                  Exp (49)
                    Exp (49)
                      Exp (49)
                        ID: copy
                      DOT
                      ID: match
                    ASSIGNOP
                    Exp (49)
                      Exp (49)
                        ID: orig
                      DOT
                      ID: match
                  SEMI
                StmtList (50)
                  Stmt (50)
                    Exp (50)
                      ID: listRewind
                      LP
                      Args (50)
                        Exp (50)
                          ID: orig
                        COMMA
                        Args (50)
                          Exp (50)
                            ID: ref
                            LP
                            Args (50)
                              Exp (50)
                                ID: iter
                            RP
                      RP
                    SEMI
                  StmtList (51)
                    Stmt (51)
                      WHILE
                      LP
                      Exp (51)
                        Exp (51)
                          LP
                          Exp (51)
                            Exp (51)
                              ID: node
                            ASSIGNOP
                            Exp (51)
                              ID: listNext
                              LP
                              Args (51)
                                Exp (51)
                                  ID: ref
                                  LP
                                  Args (51)
                                    Exp (51)
                                      ID: iter
                                  RP
                              RP
                          RP
                        RELOP
                        Exp (51)
                          ID: NULL
                      RP
                      Stmt (51)
                        CompSt (51)
                          LC
                          DefList (52)
                            Def (52)
                              Specifier (52)
                                StructSpecifier (52)
                                  STRUCT
                                  Tag (52)
                                    ID: voidstart
                              DecList (52)
                                Dec (52)
                                  VarDec (52)
                                    ID: value
                              SEMI
                          StmtList (54)
                            Stmt (54)
                              IF
                              LP
                              Exp (54)
                                Exp (54)
                                  ID: copy
                                DOT
                                ID: dup
                              RP
                              Stmt (54)
                                CompSt (54)
                                  LC
                                  StmtList (55)
                                    Stmt (55)
                                      Exp (55)
                                        Exp (55)
                                          ID: value
                                        ASSIGNOP
                                        Exp (55)
                                          ID: dup
                                          LP
                                          Args (55)
                                            Exp (55)
                                              ID: copy
                                            COMMA
                                            Args (63)
                                              Exp (63)
                                                Exp (63)
                                                  ID: node
                                                DOT
                                                ID: value
                                          RP
                                      SEMI
                                    StmtList (64)
                                      Stmt (64)
                                        IF
                                        LP
                                        Exp (64)
                                          Exp (64)
                                            ID: value
                                          RELOP
                                          Exp (64)
                                            ID: NULL
                                        RP
                                        Stmt (64)
                                          CompSt (64)
                                            LC
                                            StmtList (65)
                                              Stmt (65)
                                                Exp (65)
                                                  ID: listRelease
                                                  LP
                                                  Args (65)
                                                    Exp (65)
                                                      ID: copy
                                                  RP
                                                SEMI
                                              StmtList (66)
                                                Stmt (66)
                                                  RETURN
                                                  Exp (66)
                                                    ID: NULL
                                                  SEMI
                                            RC
                                  RC
                              ELSE
                              Stmt (69)
                                Exp (69)
                                  Exp (69)
                                    ID: value
                                  ASSIGNOP
                                  Exp (69)
                                    Exp (69)
                                      ID: node
                                    DOT
                                    ID: value
                                SEMI
                            StmtList (70)
                              Stmt (70)
                                IF
                                LP
                                Exp (70)
                                  Exp (70)
                                    ID: listAddNodeTail
                                    LP
                                    Args (70)
                                      Exp (70)
                                        ID: copy
                                      COMMA
                                      Args (70)
                                        Exp (70)
                                          ID: value
                                    RP
                                  RELOP
                                  Exp (70)
                                    ID: NULL
                                RP
                                Stmt (70)
                                  CompSt (70)
                                    LC
                                    StmtList (71)
                                      Stmt (71)
                                        Exp (71)
                                          ID: listRelease
                                          LP
                                          Args (71)
                                            Exp (71)
                                              ID: copy
                                          RP
                                        SEMI
                                      StmtList (72)
                                        Stmt (72)
                                          RETURN
                                          Exp (72)
                                            ID: NULL
                                          SEMI
                                    RC
                          RC
                    StmtList (75)
                      Stmt (75)
                        RETURN
                        Exp (75)
                          ID: copy
                        SEMI
        RC
