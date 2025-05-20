def get_random_english_concepts_connected_by_relation(conn, relation, sample_size=10):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM english_edges WHERE relation = %s ORDER BY random() LIMIT %s;""",
                (relation, sample_size))

    edges = cur.fetchall()
    cur.close()

    return [(edge[2], edge[3]) for edge in edges]


def get_unique_random_english_concepts_connected_by_relation(conn, relation, sample_size=10):
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM english_edges e1
    WHERE relation = %s
    AND NOT EXISTS (
        SELECT 1
        FROM english_edges e2
        WHERE e1.arg1 = e2.arg1
        AND e1.arg2 = e2.arg2
        AND e2.relation <> %s
    )
    ORDER BY random()
    LIMIT %s;
  """, (relation, relation, sample_size))

    edges = cur.fetchall()
    cur.close()

    return [(edge[2], edge[3]) for edge in edges]


def check_if_edge_exists(conn, relation, arg1, arg2):
    cur = conn.cursor()

    cur.execute("""SELECT EXISTS (SELECT 1 FROM english_edges WHERE relation = %s AND arg1 = %s AND arg2 = %s);""",
                (relation, arg1, arg2))

    exists = cur.fetchone()
    cur.close()

    return exists[0]
