hm = [
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Accounts",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts"
        ],
        "question": "How many accounts do we have?",
        "question_toks": [
            "How",
            "many",
            "accounts",
            "do",
            "we",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                  False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                  False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Accounts",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts"
        ],
        "question": "Count the number of accounts.",
        "question_toks": [
            "Count",
            "the",
            "number",
            "of",
            "accounts",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                  False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                  False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT account_id ,  customer_id ,  account_name FROM Accounts",
        "query_toks": [
            "SELECT",
            "account_id",
            ",",
            "customer_id",
            ",",
            "account_name",
            "FROM",
            "Accounts"
        ],
        "query_toks_no_value": [
            "select",
            "account_id",
            ",",
            "customer_id",
            ",",
            "account_name",
            "from",
            "accounts"
        ],
        "question": "Show ids, customer ids, names for all accounts.",
        "question_toks": [
            "Show",
            "ids",
            ",",
            "customer",
            "ids",
            ",",
            "names",
            "for",
            "all",
            "accounts",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                  False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                1,
                                  False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                  False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                3,
                                  False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT account_id ,  customer_id ,  account_name FROM Accounts",
        "query_toks": [
            "SELECT",
            "account_id",
            ",",
            "customer_id",
            ",",
            "account_name",
            "FROM",
            "Accounts"
        ],
        "query_toks_no_value": [
            "select",
            "account_id",
            ",",
            "customer_id",
            ",",
            "account_name",
            "from",
            "accounts"
        ],
        "question": "What are the account ids, customer ids, and account names for all the accounts?",
        "question_toks": [
            "What",
            "are",
            "the",
            "account",
            "ids",
            ",",
            "customer",
            "ids",
            ",",
            "and",
            "account",
            "names",
            "for",
            "all",
            "the",
            "accounts",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                  False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                1,
                                  False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                  False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                3,
                                  False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT other_account_details FROM Accounts WHERE account_name  =  \"338\"",
        "query_toks": [
            "SELECT",
            "other_account_details",
            "FROM",
            "Accounts",
            "WHERE",
            "account_name",
            "=",
            "``",
            "338",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "other_account_details",
            "from",
            "accounts",
            "where",
            "account_name",
            "=",
            "value"
        ],
        "question": "Show other account details for account with name 338.",
        "question_toks": [
            "Show",
            "other",
            "account",
            "details",
            "for",
            "account",
            "with",
            "name",
            "338",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                  False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                4,
                                  False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                      False,
                    2,
                    [
                        0,
                        [
                            0,
                            3,
                              False
                        ],
                         0
                    ],
                    "\"338\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT other_account_details FROM Accounts WHERE account_name  =  \"338\"",
        "query_toks": [
            "SELECT",
            "other_account_details",
            "FROM",
            "Accounts",
            "WHERE",
            "account_name",
            "=",
            "``",
            "338",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "other_account_details",
            "from",
            "accounts",
            "where",
            "account_name",
            "=",
            "value"
        ],
        "question": "What are the other account details for the account with the name 338?",
        "question_toks": [
            "What",
            "are",
            "the",
            "other",
            "account",
            "details",
            "for",
            "the",
            "account",
            "with",
            "the",
            "name",
            "338",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                  False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                4,
                                  False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                      False,
                    2,
                    [
                        0,
                        [
                            0,
                            3,
                              False
                        ],
                         0
                    ],
                    "\"338\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.customer_first_name ,  T2.customer_last_name ,  T2.customer_phone FROM Accounts AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T1.account_name  =  \"162\"",
        "query_toks": [
            "SELECT",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            ",",
            "T2.customer_phone",
            "FROM",
            "Accounts",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T1.account_name",
            "=",
            "``",
            "162",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            ",",
            "t2",
            ".",
            "customer_phone",
            "from",
            "accounts",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t1",
            ".",
            "account_name",
            "=",
            "value"
        ],
        "question": "What is the first name, last name, and phone of the customer with account name 162?",
        "question_toks": [
            "What",
            "is",
            "the",
            "first",
            "name",
            ",",
            "last",
            "name",
            ",",
            "and",
            "phone",
            "of",
            "the",
            "customer",
            "with",
            "account",
            "name",
            "162",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                          False,
                        2,
                        [
                            0,
                            [
                                0,
                                2,
                                  False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                              False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                  False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                  False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                  False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                  False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                      False,
                    2,
                    [
                        0,
                        [
                            0,
                            3,
                             False
                        ],
                         0
                    ],
                    "\"162\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.customer_first_name ,  T2.customer_last_name ,  T2.customer_phone FROM Accounts AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T1.account_name  =  \"162\"",
        "query_toks": [
            "SELECT",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            ",",
            "T2.customer_phone",
            "FROM",
            "Accounts",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T1.account_name",
            "=",
            "``",
            "162",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            ",",
            "t2",
            ".",
            "customer_phone",
            "from",
            "accounts",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t1",
            ".",
            "account_name",
            "=",
            "value"
        ],
        "question": "Give the full name and phone of the customer who has the account name 162.",
        "question_toks": [
            "Give",
            "the",
            "full",
            "name",
            "and",
            "phone",
            "of",
            "the",
            "customer",
            "who",
            "has",
            "the",
            "account",
            "name",
            "162",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            3,
                             False
                        ],
                         0
                    ],
                    "\"162\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Accounts AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T2.customer_first_name  =  \"Art\" AND T2.customer_last_name  =  \"Turcotte\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T2.customer_first_name",
            "=",
            "``",
            "Art",
            "''",
            "AND",
            "T2.customer_last_name",
            "=",
            "``",
            "Turcotte",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t2",
            ".",
            "customer_first_name",
            "=",
            "value",
            "and",
            "t2",
            ".",
            "customer_last_name",
            "=",
            "value"
        ],
        "question": "How many accounts does the customer with first name Art and last name Turcotte have?",
        "question_toks": [
            "How",
            "many",
            "accounts",
            "does",
            "the",
            "customer",
            "with",
            "first",
            "name",
            "Art",
            "and",
            "last",
            "name",
            "Turcotte",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Art\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Turcotte\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Accounts AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T2.customer_first_name  =  \"Art\" AND T2.customer_last_name  =  \"Turcotte\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T2.customer_first_name",
            "=",
            "``",
            "Art",
            "''",
            "AND",
            "T2.customer_last_name",
            "=",
            "``",
            "Turcotte",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t2",
            ".",
            "customer_first_name",
            "=",
            "value",
            "and",
            "t2",
            ".",
            "customer_last_name",
            "=",
            "value"
        ],
        "question": "Return the number of accounts that the customer with the first name Art and last name Turcotte has.",
        "question_toks": [
            "Return",
            "the",
            "number",
            "of",
            "accounts",
            "that",
            "the",
            "customer",
            "with",
            "the",
            "first",
            "name",
            "Art",
            "and",
            "last",
            "name",
            "Turcotte",
            "has",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Art\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Turcotte\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Accounts GROUP BY customer_id",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts",
            "GROUP",
            "BY",
            "customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts",
            "group",
            "by",
            "customer_id"
        ],
        "question": "Show all customer ids and the number of accounts for each customer.",
        "question_toks": [
            "Show",
            "all",
            "customer",
            "ids",
            "and",
            "the",
            "number",
            "of",
            "accounts",
            "for",
            "each",
            "customer",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    2,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Accounts GROUP BY customer_id",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts",
            "GROUP",
            "BY",
            "customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts",
            "group",
            "by",
            "customer_id"
        ],
        "question": "How many accounts are there for each customer id?",
        "question_toks": [
            "How",
            "many",
            "accounts",
            "are",
            "there",
            "for",
            "each",
            "customer",
            "id",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    2,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Accounts GROUP BY customer_id ORDER BY count(*) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts",
            "GROUP",
            "BY",
            "customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts",
            "group",
            "by",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "Show the customer id and number of accounts with most accounts.",
        "question_toks": [
            "Show",
            "the",
            "customer",
            "id",
            "and",
            "number",
            "of",
            "accounts",
            "with",
            "most",
            "accounts",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    2,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Accounts GROUP BY customer_id ORDER BY count(*) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Accounts",
            "GROUP",
            "BY",
            "customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "accounts",
            "group",
            "by",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "What is the customer id of the customer with the most accounts, and how many accounts does this person have?",
        "question_toks": [
            "What",
            "is",
            "the",
            "customer",
            "id",
            "of",
            "the",
            "customer",
            "with",
            "the",
            "most",
            "accounts",
            ",",
            "and",
            "how",
            "many",
            "accounts",
            "does",
            "this",
            "person",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    2,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.customer_first_name ,  T2.customer_last_name ,  T1.customer_id FROM Accounts AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id GROUP BY T1.customer_id ORDER BY count(*) ASC LIMIT 1",
        "query_toks": [
            "SELECT",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            ",",
            "T1.customer_id",
            "FROM",
            "Accounts",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "GROUP",
            "BY",
            "T1.customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "ASC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            ",",
            "t1",
            ".",
            "customer_id",
            "from",
            "accounts",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "group",
            "by",
            "t1",
            ".",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "asc",
            "limit",
            "value"
        ],
        "question": "What is the customer first, last name and id with least number of accounts.",
        "question_toks": [
            "What",
            "is",
            "the",
            "customer",
            "first",
            ",",
            "last",
            "name",
            "and",
            "id",
            "with",
            "least",
            "number",
            "of",
            "accounts",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    2,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "asc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.customer_first_name ,  T2.customer_last_name ,  T1.customer_id FROM Accounts AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id GROUP BY T1.customer_id ORDER BY count(*) ASC LIMIT 1",
        "query_toks": [
            "SELECT",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            ",",
            "T1.customer_id",
            "FROM",
            "Accounts",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "GROUP",
            "BY",
            "T1.customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "ASC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            ",",
            "t1",
            ".",
            "customer_id",
            "from",
            "accounts",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "group",
            "by",
            "t1",
            ".",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "asc",
            "limit",
            "value"
        ],
        "question": "Give the full name and customer id of the customer with the fewest accounts.",
        "question_toks": [
            "Give",
            "the",
            "full",
            "name",
            "and",
            "customer",
            "id",
            "of",
            "the",
            "customer",
            "with",
            "the",
            "fewest",
            "accounts",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    2,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "asc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers WHERE customer_id NOT IN (SELECT customer_id FROM Accounts)",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers",
            "WHERE",
            "customer_id",
            "NOT",
            "IN",
            "(",
            "SELECT",
            "customer_id",
            "FROM",
            "Accounts",
            ")"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers",
            "where",
            "customer_id",
            "not",
            "in",
            "(",
            "select",
            "customer_id",
            "from",
            "accounts",
            ")"
        ],
        "question": "Show the number of all customers without an account.",
        "question_toks": [
            "Show",
            "the",
            "number",
            "of",
            "all",
            "customers",
            "without",
            "an",
            "account",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                          True,
                    8,
                    [
                        0,
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ],
                    {
                        "from": {
                            "table_units": [
                                [
                                    "table_unit",
                                    0
                                ]
                            ],
                            "conds": []
                        },
                        "select": [
                             False,
                            [
                                [
                                    0,
                                    [
                                        0,
                                        [
                                            0,
                                            2,
                                             False
                                        ],
                                         0
                                    ]
                                ]
                            ]
                        ],
                        "where": [],
                        "groupBy": [],
                        "having": [],
                        "orderBy": [],
                        "limit":  0,
                        "intersect":  0,
                        "union":  0,
                        "except":  0
                    },
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers WHERE customer_id NOT IN (SELECT customer_id FROM Accounts)",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers",
            "WHERE",
            "customer_id",
            "NOT",
            "IN",
            "(",
            "SELECT",
            "customer_id",
            "FROM",
            "Accounts",
            ")"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers",
            "where",
            "customer_id",
            "not",
            "in",
            "(",
            "select",
            "customer_id",
            "from",
            "accounts",
            ")"
        ],
        "question": "How many customers do not have an account?",
        "question_toks": [
            "How",
            "many",
            "customers",
            "do",
            "not",
            "have",
            "an",
            "account",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                          True,
                    8,
                    [
                        0,
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ],
                    {
                        "from": {
                            "table_units": [
                                [
                                    "table_unit",
                                    0
                                ]
                            ],
                            "conds": []
                        },
                        "select": [
                             False,
                            [
                                [
                                    0,
                                    [
                                        0,
                                        [
                                            0,
                                            2,
                                             False
                                        ],
                                         0
                                    ]
                                ]
                            ]
                        ],
                        "where": [],
                        "groupBy": [],
                        "having": [],
                        "orderBy": [],
                        "limit":  0,
                        "intersect":  0,
                        "union":  0,
                        "except":  0
                    },
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_first_name ,  customer_last_name FROM Customers EXCEPT SELECT T1.customer_first_name ,  T1.customer_last_name FROM Customers AS T1 JOIN Accounts AS T2 ON T1.customer_id  =  T2.customer_id",
        "query_toks": [
            "SELECT",
            "customer_first_name",
            ",",
            "customer_last_name",
            "FROM",
            "Customers",
            "EXCEPT",
            "SELECT",
            "T1.customer_first_name",
            ",",
            "T1.customer_last_name",
            "FROM",
            "Customers",
            "AS",
            "T1",
            "JOIN",
            "Accounts",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "customer_first_name",
            ",",
            "customer_last_name",
            "from",
            "customers",
            "except",
            "select",
            "t1",
            ".",
            "customer_first_name",
            ",",
            "t1",
            ".",
            "customer_last_name",
            "from",
            "customers",
            "as",
            "t1",
            "join",
            "accounts",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id"
        ],
        "question": "Show the first names and last names of customers without any account.",
        "question_toks": [
            "Show",
            "the",
            "first",
            "names",
            "and",
            "last",
            "names",
            "of",
            "customers",
            "without",
            "any",
            "account",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except": {
                "from": {
                    "table_units": [
                        [
                            "table_unit",
                            1
                        ],
                        [
                            "table_unit",
                            0
                        ]
                    ],
                    "conds": [
                        [
                             False,
                            2,
                            [
                                0,
                                [
                                    0,
                                    5,
                                     False
                                ],
                                 0
                            ],
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ]
                },
                "select": [
                     False,
                    [
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    6,
                                     False
                                ],
                                 0
                            ]
                        ],
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    7,
                                     False
                                ],
                                 0
                            ]
                        ]
                    ]
                ],
                "where": [],
                "groupBy": [],
                "having": [],
                "orderBy": [],
                "limit":  0,
                "intersect":  0,
                "union":  0,
                "except":  0
            }
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_first_name ,  customer_last_name FROM Customers EXCEPT SELECT T1.customer_first_name ,  T1.customer_last_name FROM Customers AS T1 JOIN Accounts AS T2 ON T1.customer_id  =  T2.customer_id",
        "query_toks": [
            "SELECT",
            "customer_first_name",
            ",",
            "customer_last_name",
            "FROM",
            "Customers",
            "EXCEPT",
            "SELECT",
            "T1.customer_first_name",
            ",",
            "T1.customer_last_name",
            "FROM",
            "Customers",
            "AS",
            "T1",
            "JOIN",
            "Accounts",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "customer_first_name",
            ",",
            "customer_last_name",
            "from",
            "customers",
            "except",
            "select",
            "t1",
            ".",
            "customer_first_name",
            ",",
            "t1",
            ".",
            "customer_last_name",
            "from",
            "customers",
            "as",
            "t1",
            "join",
            "accounts",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id"
        ],
        "question": "What are the full names of customers who do not have any accounts?",
        "question_toks": [
            "What",
            "are",
            "the",
            "full",
            "names",
            "of",
            "customers",
            "who",
            "do",
            "not",
            "have",
            "any",
            "accounts",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except": {
                "from": {
                    "table_units": [
                        [
                            "table_unit",
                            1
                        ],
                        [
                            "table_unit",
                            0
                        ]
                    ],
                    "conds": [
                        [
                             False,
                            2,
                            [
                                0,
                                [
                                    0,
                                    5,
                                     False
                                ],
                                 0
                            ],
                            [
                                0,
                                2,
                                 False
                            ],
                             0
                        ]
                    ]
                },
                "select": [
                     False,
                    [
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    6,
                                     False
                                ],
                                 0
                            ]
                        ],
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    7,
                                     False
                                ],
                                 0
                            ]
                        ]
                    ]
                ],
                "where": [],
                "groupBy": [],
                "having": [],
                "orderBy": [],
                "limit":  0,
                "intersect":  0,
                "union":  0,
                "except":  0
            }
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT DISTINCT T1.customer_first_name ,  T1.customer_last_name FROM Customers AS T1 JOIN Accounts AS T2 ON T1.customer_id  =  T2.customer_id",
        "query_toks": [
            "SELECT",
            "DISTINCT",
            "T1.customer_first_name",
            ",",
            "T1.customer_last_name",
            "FROM",
            "Customers",
            "AS",
            "T1",
            "JOIN",
            "Accounts",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "distinct",
            "t1",
            ".",
            "customer_first_name",
            ",",
            "t1",
            ".",
            "customer_last_name",
            "from",
            "customers",
            "as",
            "t1",
            "join",
            "accounts",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id"
        ],
        "question": "Show distinct first and last names for all customers with an account.",
        "question_toks": [
            "Show",
            "distinct",
            "first",
            "and",
            "last",
            "names",
            "for",
            "all",
            "customers",
            "with",
            "an",
            "account",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ],
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            2,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                      True,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT DISTINCT T1.customer_first_name ,  T1.customer_last_name FROM Customers AS T1 JOIN Accounts AS T2 ON T1.customer_id  =  T2.customer_id",
        "query_toks": [
            "SELECT",
            "DISTINCT",
            "T1.customer_first_name",
            ",",
            "T1.customer_last_name",
            "FROM",
            "Customers",
            "AS",
            "T1",
            "JOIN",
            "Accounts",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "distinct",
            "t1",
            ".",
            "customer_first_name",
            ",",
            "t1",
            ".",
            "customer_last_name",
            "from",
            "customers",
            "as",
            "t1",
            "join",
            "accounts",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id"
        ],
        "question": "What are the full names of customers who have accounts?",
        "question_toks": [
            "What",
            "are",
            "the",
            "full",
            "names",
            "of",
            "customers",
            "who",
            "have",
            "accounts",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ],
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            2,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                      True,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(DISTINCT customer_id) FROM Accounts",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "DISTINCT",
            "customer_id",
            ")",
            "FROM",
            "Accounts"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "distinct",
            "customer_id",
            ")",
            "from",
            "accounts"
        ],
        "question": "How many customers have an account?",
        "question_toks": [
            "How",
            "many",
            "customers",
            "have",
            "an",
            "account",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                2,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(DISTINCT customer_id) FROM Accounts",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "DISTINCT",
            "customer_id",
            ")",
            "FROM",
            "Accounts"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "distinct",
            "customer_id",
            ")",
            "from",
            "accounts"
        ],
        "question": "Count the number of customers who hold an account.",
        "question_toks": [
            "Count",
            "the",
            "number",
            "of",
            "customers",
            "who",
            "hold",
            "an",
            "account",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        0
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                2,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers"
        ],
        "question": "How many customers do we have?",
        "question_toks": [
            "How",
            "many",
            "customers",
            "do",
            "we",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers"
        ],
        "question": "Count the number of customers.",
        "question_toks": [
            "Count",
            "the",
            "number",
            "of",
            "customers",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  customer_first_name ,  customer_last_name ,  customer_phone FROM Customers",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "customer_first_name",
            ",",
            "customer_last_name",
            ",",
            "customer_phone",
            "FROM",
            "Customers"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "customer_first_name",
            ",",
            "customer_last_name",
            ",",
            "customer_phone",
            "from",
            "customers"
        ],
        "question": "Show ids, first names, last names, and phones for all customers.",
        "question_toks": [
            "Show",
            "ids",
            ",",
            "first",
            "names",
            ",",
            "last",
            "names",
            ",",
            "and",
            "phones",
            "for",
            "all",
            "customers",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  customer_first_name ,  customer_last_name ,  customer_phone FROM Customers",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "customer_first_name",
            ",",
            "customer_last_name",
            ",",
            "customer_phone",
            "FROM",
            "Customers"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "customer_first_name",
            ",",
            "customer_last_name",
            ",",
            "customer_phone",
            "from",
            "customers"
        ],
        "question": "What are the ids, full names, and phones of each customer?",
        "question_toks": [
            "What",
            "are",
            "the",
            "ids",
            ",",
            "full",
            "names",
            ",",
            "and",
            "phones",
            "of",
            "each",
            "customer",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_phone ,  customer_email FROM Customers WHERE customer_first_name  =  \"Aniyah\" AND customer_last_name  =  \"Feest\"",
        "query_toks": [
            "SELECT",
            "customer_phone",
            ",",
            "customer_email",
            "FROM",
            "Customers",
            "WHERE",
            "customer_first_name",
            "=",
            "``",
            "Aniyah",
            "''",
            "AND",
            "customer_last_name",
            "=",
            "``",
            "Feest",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "customer_phone",
            ",",
            "customer_email",
            "from",
            "customers",
            "where",
            "customer_first_name",
            "=",
            "value",
            "and",
            "customer_last_name",
            "=",
            "value"
        ],
        "question": "What is the phone and email for customer with first name Aniyah and last name Feest?",
        "question_toks": [
            "What",
            "is",
            "the",
            "phone",
            "and",
            "email",
            "for",
            "customer",
            "with",
            "first",
            "name",
            "Aniyah",
            "and",
            "last",
            "name",
            "Feest",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                10,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Aniyah\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Feest\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_phone ,  customer_email FROM Customers WHERE customer_first_name  =  \"Aniyah\" AND customer_last_name  =  \"Feest\"",
        "query_toks": [
            "SELECT",
            "customer_phone",
            ",",
            "customer_email",
            "FROM",
            "Customers",
            "WHERE",
            "customer_first_name",
            "=",
            "``",
            "Aniyah",
            "''",
            "AND",
            "customer_last_name",
            "=",
            "``",
            "Feest",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "customer_phone",
            ",",
            "customer_email",
            "from",
            "customers",
            "where",
            "customer_first_name",
            "=",
            "value",
            "and",
            "customer_last_name",
            "=",
            "value"
        ],
        "question": "Return the phone and email of the customer with the first name Aniyah and last name Feest.",
        "question_toks": [
            "Return",
            "the",
            "phone",
            "and",
            "email",
            "of",
            "the",
            "customer",
            "with",
            "the",
            "first",
            "name",
            "Aniyah",
            "and",
            "last",
            "name",
            "Feest",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                10,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Aniyah\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Feest\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards"
        ],
        "question": "Show the number of customer cards.",
        "question_toks": [
            "Show",
            "the",
            "number",
            "of",
            "customer",
            "cards",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards"
        ],
        "question": "How many customer cards are there?",
        "question_toks": [
            "How",
            "many",
            "customer",
            "cards",
            "are",
            "there",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_id ,  customer_id ,  card_type_code ,  card_number FROM Customers_cards",
        "query_toks": [
            "SELECT",
            "card_id",
            ",",
            "customer_id",
            ",",
            "card_type_code",
            ",",
            "card_number",
            "FROM",
            "Customers_cards"
        ],
        "query_toks_no_value": [
            "select",
            "card_id",
            ",",
            "customer_id",
            ",",
            "card_type_code",
            ",",
            "card_number",
            "from",
            "customers_cards"
        ],
        "question": "Show ids, customer ids, card type codes, card numbers for all cards.",
        "question_toks": [
            "Show",
            "ids",
            ",",
            "customer",
            "ids",
            ",",
            "card",
            "type",
            "codes",
            ",",
            "card",
            "numbers",
            "for",
            "all",
            "cards",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                12,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                15,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_id ,  customer_id ,  card_type_code ,  card_number FROM Customers_cards",
        "query_toks": [
            "SELECT",
            "card_id",
            ",",
            "customer_id",
            ",",
            "card_type_code",
            ",",
            "card_number",
            "FROM",
            "Customers_cards"
        ],
        "query_toks_no_value": [
            "select",
            "card_id",
            ",",
            "customer_id",
            ",",
            "card_type_code",
            ",",
            "card_number",
            "from",
            "customers_cards"
        ],
        "question": "What are card ids, customer ids, card types, and card numbers for each customer card?",
        "question_toks": [
            "What",
            "are",
            "card",
            "ids",
            ",",
            "customer",
            "ids",
            ",",
            "card",
            "types",
            ",",
            "and",
            "card",
            "numbers",
            "for",
            "each",
            "customer",
            "card",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                12,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                15,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT date_valid_from ,  date_valid_to FROM Customers_cards WHERE card_number  =  \"4560596484842\"",
        "query_toks": [
            "SELECT",
            "date_valid_from",
            ",",
            "date_valid_to",
            "FROM",
            "Customers_cards",
            "WHERE",
            "card_number",
            "=",
            "``",
            "4560596484842",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "date_valid_from",
            ",",
            "date_valid_to",
            "from",
            "customers_cards",
            "where",
            "card_number",
            "=",
            "value"
        ],
        "question": "Show the date valid from and the date valid to for the card with card number '4560596484842'.",
        "question_toks": [
            "Show",
            "the",
            "date",
            "valid",
            "from",
            "and",
            "the",
            "date",
            "valid",
            "to",
            "for",
            "the",
            "card",
            "with",
            "card",
            "number",
            "'4560596484842",
            "'",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                16,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                17,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            15,
                             False
                        ],
                         0
                    ],
                    "\"4560596484842\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT date_valid_from ,  date_valid_to FROM Customers_cards WHERE card_number  =  \"4560596484842\"",
        "query_toks": [
            "SELECT",
            "date_valid_from",
            ",",
            "date_valid_to",
            "FROM",
            "Customers_cards",
            "WHERE",
            "card_number",
            "=",
            "``",
            "4560596484842",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "date_valid_from",
            ",",
            "date_valid_to",
            "from",
            "customers_cards",
            "where",
            "card_number",
            "=",
            "value"
        ],
        "question": "What are the valid from and valid to dates for the card with the number 4560596484842?",
        "question_toks": [
            "What",
            "are",
            "the",
            "valid",
            "from",
            "and",
            "valid",
            "to",
            "dates",
            "for",
            "the",
            "card",
            "with",
            "the",
            "number",
            "4560596484842",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                16,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                17,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            15,
                             False
                        ],
                         0
                    ],
                    "\"4560596484842\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.customer_first_name ,  T2.customer_last_name ,  T2.customer_phone FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T1.card_number  =  \"4560596484842\"",
        "query_toks": [
            "SELECT",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            ",",
            "T2.customer_phone",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T1.card_number",
            "=",
            "``",
            "4560596484842",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            ",",
            "t2",
            ".",
            "customer_phone",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t1",
            ".",
            "card_number",
            "=",
            "value"
        ],
        "question": "What is the first name, last name, and phone of the customer with card 4560596484842.",
        "question_toks": [
            "What",
            "is",
            "the",
            "first",
            "name",
            ",",
            "last",
            "name",
            ",",
            "and",
            "phone",
            "of",
            "the",
            "customer",
            "with",
            "card",
            "4560596484842",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            15,
                             False
                        ],
                         0
                    ],
                    "\"4560596484842\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.customer_first_name ,  T2.customer_last_name ,  T2.customer_phone FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T1.card_number  =  \"4560596484842\"",
        "query_toks": [
            "SELECT",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            ",",
            "T2.customer_phone",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T1.card_number",
            "=",
            "``",
            "4560596484842",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            ",",
            "t2",
            ".",
            "customer_phone",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t1",
            ".",
            "card_number",
            "=",
            "value"
        ],
        "question": "Return the full name and phone of the customer who has card number 4560596484842.",
        "question_toks": [
            "Return",
            "the",
            "full",
            "name",
            "and",
            "phone",
            "of",
            "the",
            "customer",
            "who",
            "has",
            "card",
            "number",
            "4560596484842",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                9,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            15,
                             False
                        ],
                         0
                    ],
                    "\"4560596484842\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T2.customer_first_name  =  \"Art\" AND T2.customer_last_name  =  \"Turcotte\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T2.customer_first_name",
            "=",
            "``",
            "Art",
            "''",
            "AND",
            "T2.customer_last_name",
            "=",
            "``",
            "Turcotte",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t2",
            ".",
            "customer_first_name",
            "=",
            "value",
            "and",
            "t2",
            ".",
            "customer_last_name",
            "=",
            "value"
        ],
        "question": "How many cards does customer Art Turcotte have?",
        "question_toks": [
            "How",
            "many",
            "cards",
            "does",
            "customer",
            "Art",
            "Turcotte",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Art\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Turcotte\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T2.customer_first_name  =  \"Art\" AND T2.customer_last_name  =  \"Turcotte\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T2.customer_first_name",
            "=",
            "``",
            "Art",
            "''",
            "AND",
            "T2.customer_last_name",
            "=",
            "``",
            "Turcotte",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t2",
            ".",
            "customer_first_name",
            "=",
            "value",
            "and",
            "t2",
            ".",
            "customer_last_name",
            "=",
            "value"
        ],
        "question": "Count the number of cards the customer with the first name Art and last name Turcotte has.",
        "question_toks": [
            "Count",
            "the",
            "number",
            "of",
            "cards",
            "the",
            "customer",
            "with",
            "the",
            "first",
            "name",
            "Art",
            "and",
            "last",
            "name",
            "Turcotte",
            "has",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Art\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Turcotte\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards WHERE card_type_code  =  \"Debit\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "WHERE",
            "card_type_code",
            "=",
            "``",
            "Debit",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "where",
            "card_type_code",
            "=",
            "value"
        ],
        "question": "How many debit cards do we have?",
        "question_toks": [
            "How",
            "many",
            "debit",
            "cards",
            "do",
            "we",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            14,
                             False
                        ],
                         0
                    ],
                    "\"Debit\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards WHERE card_type_code  =  \"Debit\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "WHERE",
            "card_type_code",
            "=",
            "``",
            "Debit",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "where",
            "card_type_code",
            "=",
            "value"
        ],
        "question": "Count the number of customer cards of the type Debit.",
        "question_toks": [
            "Count",
            "the",
            "number",
            "of",
            "customer",
            "cards",
            "of",
            "the",
            "type",
            "Debit",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            14,
                             False
                        ],
                         0
                    ],
                    "\"Debit\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T2.customer_first_name  =  \"Blanche\" AND T2.customer_last_name  =  \"Huels\" AND T1.card_type_code  =  \"Credit\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T2.customer_first_name",
            "=",
            "``",
            "Blanche",
            "''",
            "AND",
            "T2.customer_last_name",
            "=",
            "``",
            "Huels",
            "''",
            "AND",
            "T1.card_type_code",
            "=",
            "``",
            "Credit",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t2",
            ".",
            "customer_first_name",
            "=",
            "value",
            "and",
            "t2",
            ".",
            "customer_last_name",
            "=",
            "value",
            "and",
            "t1",
            ".",
            "card_type_code",
            "=",
            "value"
        ],
        "question": "How many credit cards does customer Blanche Huels have?",
        "question_toks": [
            "How",
            "many",
            "credit",
            "cards",
            "does",
            "customer",
            "Blanche",
            "Huels",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Blanche\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Huels\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            14,
                             False
                        ],
                         0
                    ],
                    "\"Credit\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(*) FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE T2.customer_first_name  =  \"Blanche\" AND T2.customer_last_name  =  \"Huels\" AND T1.card_type_code  =  \"Credit\"",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "T2.customer_first_name",
            "=",
            "``",
            "Blanche",
            "''",
            "AND",
            "T2.customer_last_name",
            "=",
            "``",
            "Huels",
            "''",
            "AND",
            "T1.card_type_code",
            "=",
            "``",
            "Credit",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "t2",
            ".",
            "customer_first_name",
            "=",
            "value",
            "and",
            "t2",
            ".",
            "customer_last_name",
            "=",
            "value",
            "and",
            "t1",
            ".",
            "card_type_code",
            "=",
            "value"
        ],
        "question": "Count the number of credit cards that the customer with first name Blanche and last name Huels has.",
        "question_toks": [
            "Count",
            "the",
            "number",
            "of",
            "credit",
            "cards",
            "that",
            "the",
            "customer",
            "with",
            "first",
            "name",
            "Blanche",
            "and",
            "last",
            "name",
            "Huels",
            "has",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            6,
                             False
                        ],
                         0
                    ],
                    "\"Blanche\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            7,
                             False
                        ],
                         0
                    ],
                    "\"Huels\"",
                     0
                ],
                "and",
                [
                     False,
                    2,
                    [
                        0,
                        [
                            0,
                            14,
                             False
                        ],
                         0
                    ],
                    "\"Credit\"",
                     0
                ]
            ],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Customers_cards GROUP BY customer_id",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "customer_id"
        ],
        "question": "Show all customer ids and the number of cards owned by each customer.",
        "question_toks": [
            "Show",
            "all",
            "customer",
            "ids",
            "and",
            "the",
            "number",
            "of",
            "cards",
            "owned",
            "by",
            "each",
            "customer",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Customers_cards GROUP BY customer_id",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "customer_id"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "customer_id"
        ],
        "question": "What are the different customer ids, and how many cards does each one hold?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "customer",
            "ids",
            ",",
            "and",
            "how",
            "many",
            "cards",
            "does",
            "each",
            "one",
            "hold",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Customers_cards GROUP BY customer_id ORDER BY count(*) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "What is the customer id with most number of cards, and how many does he have?",
        "question_toks": [
            "What",
            "is",
            "the",
            "customer",
            "id",
            "with",
            "most",
            "number",
            "of",
            "cards",
            ",",
            "and",
            "how",
            "many",
            "does",
            "he",
            "have",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  count(*) FROM Customers_cards GROUP BY customer_id ORDER BY count(*) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "Return the id of the customer who has the most cards, as well as the number of cards.",
        "question_toks": [
            "Return",
            "the",
            "id",
            "of",
            "the",
            "customer",
            "who",
            "has",
            "the",
            "most",
            "cards",
            ",",
            "as",
            "well",
            "as",
            "the",
            "number",
            "of",
            "cards",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T1.customer_id ,  T2.customer_first_name ,  T2.customer_last_name FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id GROUP BY T1.customer_id HAVING count(*)  >=  2",
        "query_toks": [
            "SELECT",
            "T1.customer_id",
            ",",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "GROUP",
            "BY",
            "T1.customer_id",
            "HAVING",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "2"
        ],
        "query_toks_no_value": [
            "select",
            "t1",
            ".",
            "customer_id",
            ",",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "group",
            "by",
            "t1",
            ".",
            "customer_id",
            "having",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "value"
        ],
        "question": "Show id, first and last names for all customers with at least two cards.",
        "question_toks": [
            "Show",
            "id",
            ",",
            "first",
            "and",
            "last",
            "names",
            "for",
            "all",
            "customers",
            "with",
            "at",
            "least",
            "two",
            "cards",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [
                [
                     False,
                    5,
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ],
                    2.0,
                     0
                ]
            ],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T1.customer_id ,  T2.customer_first_name ,  T2.customer_last_name FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id GROUP BY T1.customer_id HAVING count(*)  >=  2",
        "query_toks": [
            "SELECT",
            "T1.customer_id",
            ",",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "GROUP",
            "BY",
            "T1.customer_id",
            "HAVING",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "2"
        ],
        "query_toks_no_value": [
            "select",
            "t1",
            ".",
            "customer_id",
            ",",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "group",
            "by",
            "t1",
            ".",
            "customer_id",
            "having",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "value"
        ],
        "question": "What are the ids and full names of customers who hold two or more cards?",
        "question_toks": [
            "What",
            "are",
            "the",
            "ids",
            "and",
            "full",
            "names",
            "of",
            "customers",
            "who",
            "hold",
            "two",
            "or",
            "more",
            "cards",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [
                [
                     False,
                    5,
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ],
                    2.0,
                     0
                ]
            ],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T1.customer_id ,  T2.customer_first_name ,  T2.customer_last_name FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id GROUP BY T1.customer_id ORDER BY count(*) ASC LIMIT 1",
        "query_toks": [
            "SELECT",
            "T1.customer_id",
            ",",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "GROUP",
            "BY",
            "T1.customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "ASC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "t1",
            ".",
            "customer_id",
            ",",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "group",
            "by",
            "t1",
            ".",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "asc",
            "limit",
            "value"
        ],
        "question": "What is the customer id, first and last name with least number of accounts.",
        "question_toks": [
            "What",
            "is",
            "the",
            "customer",
            "id",
            ",",
            "first",
            "and",
            "last",
            "name",
            "with",
            "least",
            "number",
            "of",
            "accounts",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "asc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T1.customer_id ,  T2.customer_first_name ,  T2.customer_last_name FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id GROUP BY T1.customer_id ORDER BY count(*) ASC LIMIT 1",
        "query_toks": [
            "SELECT",
            "T1.customer_id",
            ",",
            "T2.customer_first_name",
            ",",
            "T2.customer_last_name",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "GROUP",
            "BY",
            "T1.customer_id",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "ASC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "t1",
            ".",
            "customer_id",
            ",",
            "t2",
            ".",
            "customer_first_name",
            ",",
            "t2",
            ".",
            "customer_last_name",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "group",
            "by",
            "t1",
            ".",
            "customer_id",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "asc",
            "limit",
            "value"
        ],
        "question": "Return the id and full name of the customer who has the fewest accounts.",
        "question_toks": [
            "Return",
            "the",
            "id",
            "and",
            "full",
            "name",
            "of",
            "the",
            "customer",
            "who",
            "has",
            "the",
            "fewest",
            "accounts",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ],
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            5,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                13,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                7,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    13,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "asc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code ,  count(*) FROM Customers_cards GROUP BY card_type_code",
        "query_toks": [
            "SELECT",
            "card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code"
        ],
        "question": "Show all card type codes and the number of cards in each type.",
        "question_toks": [
            "Show",
            "all",
            "card",
            "type",
            "codes",
            "and",
            "the",
            "number",
            "of",
            "cards",
            "in",
            "each",
            "type",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code ,  count(*) FROM Customers_cards GROUP BY card_type_code",
        "query_toks": [
            "SELECT",
            "card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code"
        ],
        "question": "What are the different card types, and how many cards are there of each?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "card",
            "types",
            ",",
            "and",
            "how",
            "many",
            "cards",
            "are",
            "there",
            "of",
            "each",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code FROM Customers_cards GROUP BY card_type_code ORDER BY count(*) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "card_type_code",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "What is the card type code with most number of cards?",
        "question_toks": [
            "What",
            "is",
            "the",
            "card",
            "type",
            "code",
            "with",
            "most",
            "number",
            "of",
            "cards",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code FROM Customers_cards GROUP BY card_type_code ORDER BY count(*) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "card_type_code",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code",
            "ORDER",
            "BY",
            "count",
            "(",
            "*",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code",
            "order",
            "by",
            "count",
            "(",
            "*",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "Return the code of the card type that is most common.",
        "question_toks": [
            "Return",
            "the",
            "code",
            "of",
            "the",
            "card",
            "type",
            "that",
            "is",
            "most",
            "common",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code FROM Customers_cards GROUP BY card_type_code HAVING count(*)  >=  5",
        "query_toks": [
            "SELECT",
            "card_type_code",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code",
            "HAVING",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "5"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code",
            "having",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "value"
        ],
        "question": "Show card type codes with at least 5 cards.",
        "question_toks": [
            "Show",
            "card",
            "type",
            "codes",
            "with",
            "at",
            "least",
            "5",
            "cards",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [
                [
                     False,
                    5,
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ],
                    5.0,
                     0
                ]
            ],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code FROM Customers_cards GROUP BY card_type_code HAVING count(*)  >=  5",
        "query_toks": [
            "SELECT",
            "card_type_code",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code",
            "HAVING",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "5"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code",
            "having",
            "count",
            "(",
            "*",
            ")",
            ">",
            "=",
            "value"
        ],
        "question": "What are the codes of card types that have 5 or more cards?",
        "question_toks": [
            "What",
            "are",
            "the",
            "codes",
            "of",
            "card",
            "types",
            "that",
            "have",
            "5",
            "or",
            "more",
            "cards",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [
                [
                     False,
                    5,
                    [
                        0,
                        [
                            3,
                            0,
                             False
                        ],
                         0
                    ],
                    5.0,
                     0
                ]
            ],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code ,  count(DISTINCT customer_id) FROM Customers_cards GROUP BY card_type_code",
        "query_toks": [
            "SELECT",
            "card_type_code",
            ",",
            "count",
            "(",
            "DISTINCT",
            "customer_id",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            ",",
            "count",
            "(",
            "distinct",
            "customer_id",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code"
        ],
        "question": "Show all card type codes and the number of customers holding cards in each type.",
        "question_toks": [
            "Show",
            "all",
            "card",
            "type",
            "codes",
            "and",
            "the",
            "number",
            "of",
            "customers",
            "holding",
            "cards",
            "in",
            "each",
            "type",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                13,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT card_type_code ,  count(DISTINCT customer_id) FROM Customers_cards GROUP BY card_type_code",
        "query_toks": [
            "SELECT",
            "card_type_code",
            ",",
            "count",
            "(",
            "DISTINCT",
            "customer_id",
            ")",
            "FROM",
            "Customers_cards",
            "GROUP",
            "BY",
            "card_type_code"
        ],
        "query_toks_no_value": [
            "select",
            "card_type_code",
            ",",
            "count",
            "(",
            "distinct",
            "customer_id",
            ")",
            "from",
            "customers_cards",
            "group",
            "by",
            "card_type_code"
        ],
        "question": "What are the different card type codes, and how many different customers hold each type?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "card",
            "type",
            "codes",
            ",",
            "and",
            "how",
            "many",
            "different",
            "customers",
            "hold",
            "each",
            "type",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                13,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  customer_first_name FROM Customers EXCEPT SELECT T1.customer_id ,  T2.customer_first_name FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE card_type_code  =  \"Credit\"",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "customer_first_name",
            "FROM",
            "Customers",
            "EXCEPT",
            "SELECT",
            "T1.customer_id",
            ",",
            "T2.customer_first_name",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "card_type_code",
            "=",
            "``",
            "Credit",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "customer_first_name",
            "from",
            "customers",
            "except",
            "select",
            "t1",
            ".",
            "customer_id",
            ",",
            "t2",
            ".",
            "customer_first_name",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "card_type_code",
            "=",
            "value"
        ],
        "question": "Show the customer ids and firstname without a credit card.",
        "question_toks": [
            "Show",
            "the",
            "customer",
            "ids",
            "and",
            "firstname",
            "without",
            "a",
            "credit",
            "card",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except": {
                "from": {
                    "table_units": [
                        [
                            "table_unit",
                            2
                        ],
                        [
                            "table_unit",
                            1
                        ]
                    ],
                    "conds": [
                        [
                             False,
                            2,
                            [
                                0,
                                [
                                    0,
                                    13,
                                     False
                                ],
                                 0
                            ],
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ]
                    ]
                },
                "select": [
                     False,
                    [
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    13,
                                     False
                                ],
                                 0
                            ]
                        ],
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    6,
                                     False
                                ],
                                 0
                            ]
                        ]
                    ]
                ],
                "where": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ],
                        "\"Credit\"",
                         0
                    ]
                ],
                "groupBy": [],
                "having": [],
                "orderBy": [],
                "limit":  0,
                "intersect":  0,
                "union":  0,
                "except":  0
            }
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT customer_id ,  customer_first_name FROM Customers EXCEPT SELECT T1.customer_id ,  T2.customer_first_name FROM Customers_cards AS T1 JOIN Customers AS T2 ON T1.customer_id  =  T2.customer_id WHERE card_type_code  =  \"Credit\"",
        "query_toks": [
            "SELECT",
            "customer_id",
            ",",
            "customer_first_name",
            "FROM",
            "Customers",
            "EXCEPT",
            "SELECT",
            "T1.customer_id",
            ",",
            "T2.customer_first_name",
            "FROM",
            "Customers_cards",
            "AS",
            "T1",
            "JOIN",
            "Customers",
            "AS",
            "T2",
            "ON",
            "T1.customer_id",
            "=",
            "T2.customer_id",
            "WHERE",
            "card_type_code",
            "=",
            "``",
            "Credit",
            "''"
        ],
        "query_toks_no_value": [
            "select",
            "customer_id",
            ",",
            "customer_first_name",
            "from",
            "customers",
            "except",
            "select",
            "t1",
            ".",
            "customer_id",
            ",",
            "t2",
            ".",
            "customer_first_name",
            "from",
            "customers_cards",
            "as",
            "t1",
            "join",
            "customers",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "customer_id",
            "=",
            "t2",
            ".",
            "customer_id",
            "where",
            "card_type_code",
            "=",
            "value"
        ],
        "question": "What are the ids and first names of customers who do not hold a credit card?",
        "question_toks": [
            "What",
            "are",
            "the",
            "ids",
            "and",
            "first",
            "names",
            "of",
            "customers",
            "who",
            "do",
            "not",
            "hold",
            "a",
            "credit",
            "card",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        1
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                6,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except": {
                "from": {
                    "table_units": [
                        [
                            "table_unit",
                            2
                        ],
                        [
                            "table_unit",
                            1
                        ]
                    ],
                    "conds": [
                        [
                             False,
                            2,
                            [
                                0,
                                [
                                    0,
                                    13,
                                     False
                                ],
                                 0
                            ],
                            [
                                0,
                                5,
                                 False
                            ],
                             0
                        ]
                    ]
                },
                "select": [
                     False,
                    [
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    13,
                                     False
                                ],
                                 0
                            ]
                        ],
                        [
                            0,
                            [
                                0,
                                [
                                    0,
                                    6,
                                     False
                                ],
                                 0
                            ]
                        ]
                    ]
                ],
                "where": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ],
                        "\"Credit\"",
                         0
                    ]
                ],
                "groupBy": [],
                "having": [],
                "orderBy": [],
                "limit":  0,
                "intersect":  0,
                "union":  0,
                "except":  0
            }
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT DISTINCT card_type_code FROM Customers_Cards",
        "query_toks": [
            "SELECT",
            "DISTINCT",
            "card_type_code",
            "FROM",
            "Customers_Cards"
        ],
        "query_toks_no_value": [
            "select",
            "distinct",
            "card_type_code",
            "from",
            "customers_cards"
        ],
        "question": "Show all card type codes.",
        "question_toks": [
            "Show",
            "all",
            "card",
            "type",
            "codes",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                     True,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT DISTINCT card_type_code FROM Customers_Cards",
        "query_toks": [
            "SELECT",
            "DISTINCT",
            "card_type_code",
            "FROM",
            "Customers_Cards"
        ],
        "query_toks_no_value": [
            "select",
            "distinct",
            "card_type_code",
            "from",
            "customers_cards"
        ],
        "question": "What are the different card type codes?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "card",
            "type",
            "codes",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                     True,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(DISTINCT card_type_code) FROM Customers_Cards",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "DISTINCT",
            "card_type_code",
            ")",
            "FROM",
            "Customers_Cards"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "distinct",
            "card_type_code",
            ")",
            "from",
            "customers_cards"
        ],
        "question": "Show the number of card types.",
        "question_toks": [
            "Show",
            "the",
            "number",
            "of",
            "card",
            "types",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                14,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(DISTINCT card_type_code) FROM Customers_Cards",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "DISTINCT",
            "card_type_code",
            ")",
            "FROM",
            "Customers_Cards"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "distinct",
            "card_type_code",
            ")",
            "from",
            "customers_cards"
        ],
        "question": "How many different card types are there?",
        "question_toks": [
            "How",
            "many",
            "different",
            "card",
            "types",
            "are",
            "there",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                14,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT DISTINCT transaction_type FROM Financial_Transactions",
        "query_toks": [
            "SELECT",
            "DISTINCT",
            "transaction_type",
            "FROM",
            "Financial_Transactions"
        ],
        "query_toks_no_value": [
            "select",
            "distinct",
            "transaction_type",
            "from",
            "financial_transactions"
        ],
        "question": "Show all transaction types.",
        "question_toks": [
            "Show",
            "all",
            "transaction",
            "types",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                     True,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                23,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT DISTINCT transaction_type FROM Financial_Transactions",
        "query_toks": [
            "SELECT",
            "DISTINCT",
            "transaction_type",
            "FROM",
            "Financial_Transactions"
        ],
        "query_toks_no_value": [
            "select",
            "distinct",
            "transaction_type",
            "from",
            "financial_transactions"
        ],
        "question": "What are the different types of transactions?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "types",
            "of",
            "transactions",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                     True,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                23,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(DISTINCT transaction_type) FROM Financial_Transactions",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "DISTINCT",
            "transaction_type",
            ")",
            "FROM",
            "Financial_Transactions"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "distinct",
            "transaction_type",
            ")",
            "from",
            "financial_transactions"
        ],
        "question": "Show the number of transaction types.",
        "question_toks": [
            "Show",
            "the",
            "number",
            "of",
            "transaction",
            "types",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                23,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT count(DISTINCT transaction_type) FROM Financial_Transactions",
        "query_toks": [
            "SELECT",
            "count",
            "(",
            "DISTINCT",
            "transaction_type",
            ")",
            "FROM",
            "Financial_Transactions"
        ],
        "query_toks_no_value": [
            "select",
            "count",
            "(",
            "distinct",
            "transaction_type",
            ")",
            "from",
            "financial_transactions"
        ],
        "question": "How many different types of transactions are there?",
        "question_toks": [
            "How",
            "many",
            "different",
            "types",
            "of",
            "transactions",
            "are",
            "there",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                23,
                                     True
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT avg(transaction_amount) ,  sum(transaction_amount) FROM Financial_transactions",
        "query_toks": [
            "SELECT",
            "avg",
            "(",
            "transaction_amount",
            ")",
            ",",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "FROM",
            "Financial_transactions"
        ],
        "query_toks_no_value": [
            "select",
            "avg",
            "(",
            "transaction_amount",
            ")",
            ",",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "from",
            "financial_transactions"
        ],
        "question": "What is the average and total transaction amount?",
        "question_toks": [
            "What",
            "is",
            "the",
            "average",
            "and",
            "total",
            "transaction",
            "amount",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        5,
                        [
                            0,
                            [
                                0,
                                25,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        4,
                        [
                            0,
                            [
                                0,
                                25,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT avg(transaction_amount) ,  sum(transaction_amount) FROM Financial_transactions",
        "query_toks": [
            "SELECT",
            "avg",
            "(",
            "transaction_amount",
            ")",
            ",",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "FROM",
            "Financial_transactions"
        ],
        "query_toks_no_value": [
            "select",
            "avg",
            "(",
            "transaction_amount",
            ")",
            ",",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "from",
            "financial_transactions"
        ],
        "question": "Return the average transaction amount, as well as the total amount of all transactions.",
        "question_toks": [
            "Return",
            "the",
            "average",
            "transaction",
            "amount",
            ",",
            "as",
            "well",
            "as",
            "the",
            "total",
            "amount",
            "of",
            "all",
            "transactions",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        5,
                        [
                            0,
                            [
                                0,
                                25,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        4,
                        [
                            0,
                            [
                                0,
                                25,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.card_type_code ,  count(*) FROM Financial_transactions AS T1 JOIN Customers_cards AS T2 ON T1.card_id  =  T2.card_id GROUP BY T2.card_type_code",
        "query_toks": [
            "SELECT",
            "T2.card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Financial_transactions",
            "AS",
            "T1",
            "JOIN",
            "Customers_cards",
            "AS",
            "T2",
            "ON",
            "T1.card_id",
            "=",
            "T2.card_id",
            "GROUP",
            "BY",
            "T2.card_type_code"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "financial_transactions",
            "as",
            "t1",
            "join",
            "customers_cards",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "card_id",
            "=",
            "t2",
            ".",
            "card_id",
            "group",
            "by",
            "t2",
            ".",
            "card_type_code"
        ],
        "question": "Show the card type codes and the number of transactions.",
        "question_toks": [
            "Show",
            "the",
            "card",
            "type",
            "codes",
            "and",
            "the",
            "number",
            "of",
            "transactions",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ],
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                22,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            12,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT T2.card_type_code ,  count(*) FROM Financial_transactions AS T1 JOIN Customers_cards AS T2 ON T1.card_id  =  T2.card_id GROUP BY T2.card_type_code",
        "query_toks": [
            "SELECT",
            "T2.card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Financial_transactions",
            "AS",
            "T1",
            "JOIN",
            "Customers_cards",
            "AS",
            "T2",
            "ON",
            "T1.card_id",
            "=",
            "T2.card_id",
            "GROUP",
            "BY",
            "T2.card_type_code"
        ],
        "query_toks_no_value": [
            "select",
            "t2",
            ".",
            "card_type_code",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "financial_transactions",
            "as",
            "t1",
            "join",
            "customers_cards",
            "as",
            "t2",
            "on",
            "t1",
            ".",
            "card_id",
            "=",
            "t2",
            ".",
            "card_id",
            "group",
            "by",
            "t2",
            ".",
            "card_type_code"
        ],
        "question": "What are the different card types, and how many transactions have been made with each?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "card",
            "types",
            ",",
            "and",
            "how",
            "many",
            "transactions",
            "have",
            "been",
            "made",
            "with",
            "each",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ],
                    [
                        "table_unit",
                        2
                    ]
                ],
                "conds": [
                    [
                         False,
                        2,
                        [
                            0,
                            [
                                0,
                                22,
                                 False
                            ],
                             0
                        ],
                        [
                            0,
                            12,
                             False
                        ],
                         0
                    ]
                ]
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                14,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    14,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT transaction_type ,  count(*) FROM Financial_transactions GROUP BY transaction_type",
        "query_toks": [
            "SELECT",
            "transaction_type",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Financial_transactions",
            "GROUP",
            "BY",
            "transaction_type"
        ],
        "query_toks_no_value": [
            "select",
            "transaction_type",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "financial_transactions",
            "group",
            "by",
            "transaction_type"
        ],
        "question": "Show the transaction type and the number of transactions.",
        "question_toks": [
            "Show",
            "the",
            "transaction",
            "type",
            "and",
            "the",
            "number",
            "of",
            "transactions",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                23,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    23,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT transaction_type ,  count(*) FROM Financial_transactions GROUP BY transaction_type",
        "query_toks": [
            "SELECT",
            "transaction_type",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Financial_transactions",
            "GROUP",
            "BY",
            "transaction_type"
        ],
        "query_toks_no_value": [
            "select",
            "transaction_type",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "financial_transactions",
            "group",
            "by",
            "transaction_type"
        ],
        "question": "What are the different transaction types, and how many transactions of each have taken place?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "transaction",
            "types",
            ",",
            "and",
            "how",
            "many",
            "transactions",
            "of",
            "each",
            "have",
            "taken",
            "place",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                23,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    23,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT transaction_type FROM Financial_transactions GROUP BY transaction_type ORDER BY sum(transaction_amount) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "transaction_type",
            "FROM",
            "Financial_transactions",
            "GROUP",
            "BY",
            "transaction_type",
            "ORDER",
            "BY",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "transaction_type",
            "from",
            "financial_transactions",
            "group",
            "by",
            "transaction_type",
            "order",
            "by",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "What is the transaction type that has processed the greatest total amount in transactions?",
        "question_toks": [
            "What",
            "is",
            "the",
            "transaction",
            "type",
            "that",
            "has",
            "processed",
            "the",
            "greatest",
            "total",
            "amount",
            "in",
            "transactions",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                23,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    23,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            4,
                            25,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT transaction_type FROM Financial_transactions GROUP BY transaction_type ORDER BY sum(transaction_amount) DESC LIMIT 1",
        "query_toks": [
            "SELECT",
            "transaction_type",
            "FROM",
            "Financial_transactions",
            "GROUP",
            "BY",
            "transaction_type",
            "ORDER",
            "BY",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "DESC",
            "LIMIT",
            "1"
        ],
        "query_toks_no_value": [
            "select",
            "transaction_type",
            "from",
            "financial_transactions",
            "group",
            "by",
            "transaction_type",
            "order",
            "by",
            "sum",
            "(",
            "transaction_amount",
            ")",
            "desc",
            "limit",
            "value"
        ],
        "question": "Return the type of transaction with the highest total amount.",
        "question_toks": [
            "Return",
            "the",
            "type",
            "of",
            "transaction",
            "with",
            "the",
            "highest",
            "total",
            "amount",
            "."
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                23,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    23,
                     False
                ]
            ],
            "having": [],
            "orderBy": [
                "desc",
                [
                    [
                        0,
                        [
                            4,
                            25,
                             False
                        ],
                         0
                    ]
                ]
            ],
            "limit": 1,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT account_id ,  count(*) FROM Financial_transactions GROUP BY account_id",
        "query_toks": [
            "SELECT",
            "account_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Financial_transactions",
            "GROUP",
            "BY",
            "account_id"
        ],
        "query_toks_no_value": [
            "select",
            "account_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "financial_transactions",
            "group",
            "by",
            "account_id"
        ],
        "question": "Show the account id and the number of transactions for each account",
        "question_toks": [
            "Show",
            "the",
            "account",
            "id",
            "and",
            "the",
            "number",
            "of",
            "transactions",
            "for",
            "each",
            "account"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                21,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    21,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    },
    {
        "db_id": "customers_card_transactions",
        "query": "SELECT account_id ,  count(*) FROM Financial_transactions GROUP BY account_id",
        "query_toks": [
            "SELECT",
            "account_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "FROM",
            "Financial_transactions",
            "GROUP",
            "BY",
            "account_id"
        ],
        "query_toks_no_value": [
            "select",
            "account_id",
            ",",
            "count",
            "(",
            "*",
            ")",
            "from",
            "financial_transactions",
            "group",
            "by",
            "account_id"
        ],
        "question": "What are the different account ids that have made financial transactions, as well as how many transactions correspond to each?",
        "question_toks": [
            "What",
            "are",
            "the",
            "different",
            "account",
            "ids",
            "that",
            "have",
            "made",
            "financial",
            "transactions",
            ",",
            "as",
            "well",
            "as",
            "how",
            "many",
            "transactions",
            "correspond",
            "to",
            "each",
            "?"
        ],
        "sql": {
            "from": {
                "table_units": [
                    [
                        "table_unit",
                        3
                    ]
                ],
                "conds": []
            },
            "select": [
                 False,
                [
                    [
                        0,
                        [
                            0,
                            [
                                0,
                                21,
                                 False
                            ],
                             0
                        ]
                    ],
                    [
                        3,
                        [
                            0,
                            [
                                0,
                                0,
                                 False
                            ],
                             0
                        ]
                    ]
                ]
            ],
            "where": [],
            "groupBy": [
                [
                    0,
                    21,
                     False
                ]
            ],
            "having": [],
            "orderBy": [],
            "limit":  0,
            "intersect":  0,
            "union":  0,
            "except":  0
        }
    }
]


index_s = 1
index_t = 1
source_tokenizer = {}
target_tokenizer = {}


for i in hm:
    question_toks = i["question_toks"]
    # print(query_toks)
    for j in question_toks:
        # print(j)
        
        if j not in source_tokenizer:
            source_tokenizer[j] = index_s
            index_s += 1
# print((frequency))
for i in hm:
    query_toks = i["query_toks"]
    # print(query_toks)
    for j in query_toks:
        # print(j)
        
        if j not in target_tokenizer:
            target_tokenizer[j] = index_t
            index_t += 1

# print(source_tokenizer)
# print(target_tokenizer)

##maximum output sequence length
count = []
for i in hm:
    counter = 0
    query_toks = i["question_toks"]
    for j in query_toks:
        counter+=1
    count.append(counter)
# print(max(count))




train_encoder_inputs = [example["question_toks"] for example in hm]
train_decoder_inputs = [example["query_toks"] for example in hm]

encoder_input_data_nopad = [[source_tokenizer[word] for word in sentence] for sentence in train_encoder_inputs]
# print(encoder_input_data)

decoder_input_data_nopad = [[target_tokenizer[word] for word in sentence] for sentence in train_decoder_inputs]
# print(decoder_input_data)