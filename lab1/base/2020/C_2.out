Program (1)
  ExtDefList (1)
    ExtDef (1)
      Specifier (1)
        TYPE: int
      FunDec (1)
        ID: MatrixMax
        LP
        VarList (1)
          ParamDec (1)
            Specifier (1)
              TYPE: int
            VarDec (1)
              VarDec (1)
                VarDec (1)
                  ID: a
                LB
                INT: 3
                RB
              LB
              INT: 4
              RB
        RP
      CompSt (2)
        LC
        DefList (3)
          Def (3)
            Specifier (3)
              TYPE: int
            DecList (3)
              Dec (3)
                VarDec (3)
                  ID: i
                ASSIGNOP
                Exp (3)
                  INT: 0
              COMMA
              DecList (3)
                Dec (3)
                  VarDec (3)
                    ID: j
                  ASSIGNOP
                  Exp (3)
                    INT: 0
            SEMI
          DefList (4)
            Def (4)
              Specifier (4)
                TYPE: int
              DecList (4)
                Dec (4)
                  VarDec (4)
                    ID: max
                COMMA
                DecList (4)
                  Dec (4)
                    VarDec (4)
                      ID: max_i
                    ASSIGNOP
                    Exp (4)
                      INT: 0
                  COMMA
                  DecList (4)
                    Dec (4)
                      VarDec (4)
                        ID: max_j
                      ASSIGNOP
                      Exp (4)
                        INT: 0
              SEMI
        StmtList (5)
          Stmt (5)
            Exp (5)
              Exp (5)
                ID: max
              ASSIGNOP
              Exp (5)
                Exp (5)
                  Exp (5)
                    ID: a
                  LB
                  Exp (5)
                    INT: 0
                  RB
                LB
                Exp (5)
                  INT: 0
                RB
            SEMI
          StmtList (6)
            Stmt (6)
              WHILE
              LP
              Exp (6)
                Exp (6)
                  ID: i
                RELOP
                Exp (6)
                  INT: 3
              RP
              Stmt (7)
                CompSt (7)
                  LC
                  StmtList (8)
                    Stmt (8)
                      WHILE
                      LP
                      Exp (8)
                        Exp (8)
                          ID: j
                        RELOP
                        Exp (8)
                          INT: 4
                      RP
                      Stmt (9)
                        CompSt (9)
                          LC
                          StmtList (10)
                            Stmt (10)
                              IF
                              LP
                              Exp (10)
                                Exp (10)
                                  Exp (10)
                                    Exp (10)
                                      ID: a
                                    LB
                                    Exp (10)
                                      ID: i
                                    RB
                                  LB
                                  Exp (10)
                                    ID: j
                                  RB
                                RELOP
                                Exp (10)
                                  ID: max
                              RP
                              Stmt (11)
                                CompSt (11)
                                  LC
                                  StmtList (12)
                                    Stmt (12)
                                      Exp (12)
                                        Exp (12)
                                          ID: max
                                        ASSIGNOP
                                        Exp (12)
                                          Exp (12)
                                            Exp (12)
                                              ID: a
                                            LB
                                            Exp (12)
                                              ID: i
                                            RB
                                          LB
                                          Exp (12)
                                            ID: j
                                          RB
                                      SEMI
                                    StmtList (13)
                                      Stmt (13)
                                        Exp (13)
                                          Exp (13)
                                            ID: max_i
                                          ASSIGNOP
                                          Exp (13)
                                            ID: i
                                        SEMI
                                      StmtList (14)
                                        Stmt (14)
                                          Exp (14)
                                            Exp (14)
                                              ID: max_j
                                            ASSIGNOP
                                            Exp (14)
                                              ID: j
                                          SEMI
                                  RC
                            StmtList (16)
                              Stmt (16)
                                Exp (16)
                                  Exp (16)
                                    ID: j
                                  ASSIGNOP
                                  Exp (16)
                                    Exp (16)
                                      ID: j
                                    PLUS
                                    Exp (16)
                                      INT: 1
                                SEMI
                          RC
                    StmtList (18)
                      Stmt (18)
                        Exp (18)
                          Exp (18)
                            ID: i
                          ASSIGNOP
                          Exp (18)
                            Exp (18)
                              ID: i
                            PLUS
                            Exp (18)
                              INT: 1
                        SEMI
                  RC
            StmtList (20)
              Stmt (20)
                RETURN
                Exp (20)
                  INT: 0
                SEMI
        RC
