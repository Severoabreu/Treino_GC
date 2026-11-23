from repository.dao_entity import DAOEntity
from entities.entity import Entity
class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo, autor):
        if not titulo or not titulo.strip():
            raise ValueError ("O título do livro é obrigatório")
        
        novo_livro = Entity(
            titulo= titulo.strip(),
            autor= autor.strip(),
            lido= False
            )
        return  self.repository.create(novo_livro)
        # Validar dados (MUITO IMPORTANTE!!!!!)
        # Criar entidade
        # Solicitar persistência
        
        

    def list(self):
        return self.repository.find_all()

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass