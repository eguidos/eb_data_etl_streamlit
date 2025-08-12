def filtrar_emendas(df, 
                    uf, 
                    tipo, 
                    nome_parlamentar,
                    dt_inicio,
                    dt_fim):
    
    df_filtrado = df.copy()
    if uf != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado["uf"] == uf
        ]
    
    if tipo != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado["tipo_de_emenda"] == tipo
        ]
    if nome_parlamentar:
        df_filtrado = df_filtrado[
            df_filtrado["nome_do_autor_da_emenda"]
            .str.lower()
            .str.contains(nome_parlamentar)
        ]

    if dt_inicio != " " and dt_fim != " ":
        df_filtrado = df_filtrado[
            (df_filtrado["ano_da_emenda"] >= dt_inicio) &
            (df_filtrado["ano_da_emenda"] <= dt_fim)
        ]
    return df_filtrado