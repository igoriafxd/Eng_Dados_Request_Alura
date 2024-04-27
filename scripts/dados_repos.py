import requests
import pandas as pd
import config #dados sensiveis
from math import ceil #arrendodar valor para cima


class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = config.TOKEN
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
           'X-GitHub-Api-Version': '2022-11-28'}
        
    def listar_repositorios(self):
        r = requests.get(f'{self.api_base_url}/users/{self.owner}')
        num_pages = ceil(r.json()['public_repos']/30)

        repos_list = []
        
        for page_num in range(1, num_pages):
            try:
                url_page = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url_page, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list
    
    def nomes_repositorios(self, repos_list):
        repo_names = []

        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass

        return repo_names
    
    def nomes_linguagens(self, repos_list):
        repo_language = []

        for page in repos_list:
            for repo in page:
                try:
                    repo_language.append(repo['language'])
                except:
                    pass
                
        return repo_language
    
    def cria_data_frame_linguagens(self):
        repositorios = self.listar_repositorios()
        nomes = self.nomes_repositorios(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados
    


