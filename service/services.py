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

    def get(self, livro_id):
        livro = self.repository.find_by_id(livro_id)
        if livro is None:
            raise ValueError("Registro não encontrado")
        return livro

    def update(self, livro_id, titulo, autor):
        livro_existente = self.get(livro_id)
        
        if not titulo or not titulo.strip():
            raise ValueError("O titulo do livro e obrigatorio.")
        
        livro_existente.titulo = titulo.strip()
        livro_existente.autor = autor.strip()
        
        self.repository.update(livro_existente)

    def delete(self, task_id):
        pass