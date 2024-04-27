from dados_repos import DadosRepositorios

amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_data_frame_linguagens()
#print(ling_mais_usadas_amzn)
netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_data_frame_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_data_frame_linguagens()

apple_rep = DadosRepositorios('apple')
ling_mais_usadas_apple = apple_rep.cria_data_frame_linguagens()

# Salvando os dados 

ling_mais_usadas_amzn.to_csv('./external_data/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('./external_data/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('./external_data/linguagens_spotify.csv')
ling_mais_usadas_apple.to_csv('./external_data/linguagens_apple.csv')

