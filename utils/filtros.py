def filtrar_emendas(df, 
                    uf, 
                    tipo, 
                    nome_parlamentar):
    
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
    return df_filtrado