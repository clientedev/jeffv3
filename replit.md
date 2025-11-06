# Núcleo 1.03 - Sistema de Gestão e Prospecção de Empresas

## Visão Geral
Sistema web completo desenvolvido em Python com FastAPI para gestão e prospecção de empresas. Permite cadastro de empresas, controle de prospecções, acompanhamento de agendamentos e histórico de ligações.

## Arquitetura

### Backend
- **Framework**: FastAPI
- **Banco de Dados**: PostgreSQL
- **ORM**: SQLAlchemy
- **Autenticação**: JWT (JSON Web Token)
- **Validação**: Pydantic

### Frontend
- **Templates**: Jinja2
- **Estilização**: TailwindCSS (CDN)
- **JavaScript**: Vanilla JS com Fetch API
- **Tema**: Escuro profissional

## Estrutura do Projeto

```
.
├── backend/
│   ├── models/          # Modelos SQLAlchemy
│   │   ├── usuarios.py
│   │   ├── empresas.py
│   │   ├── prospeccoes.py
│   │   └── agendamentos.py
│   ├── routers/         # Rotas da API
│   │   ├── auth.py
│   │   ├── empresas.py
│   │   ├── prospeccoes.py
│   │   └── agendamentos.py
│   ├── schemas/         # Schemas Pydantic
│   │   ├── usuarios.py
│   │   ├── empresas.py
│   │   ├── prospeccoes.py
│   │   └── agendamentos.py
│   ├── auth/           # Segurança e autenticação
│   │   └── security.py
│   └── database.py     # Configuração do banco
├── templates/          # Templates HTML
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── empresas.html
│   ├── empresa_perfil.html
│   ├── prospeccao.html
│   └── alertas.html
├── static/            # Arquivos estáticos
│   ├── css/
│   └── js/
│       ├── auth.js
│       ├── login.js
│       ├── dashboard.js
│       ├── empresas.js
│       ├── empresa_perfil.js
│       ├── prospeccao.js
│       └── alertas.js
└── main.py           # Arquivo principal da aplicação
```

## Funcionalidades Implementadas

### 1. Autenticação e Usuários
- ✅ Tela de login e registro
- ✅ Dois tipos de usuário: Admin e Consultor
- ✅ Sessão persistente com JWT
- ✅ Logout seguro
- ✅ Controle de acesso baseado em permissões

### 2. Cadastro de Empresas
- ✅ Campos completos: empresa, CNPJ, sigla, porte, ER, carteira, endereço, etc.
- ✅ Listagem com filtros (nome, CNPJ, município, ER, carteira)
- ✅ Página de perfil com dados completos
- ✅ Histórico de prospecções por empresa
- ✅ Apenas Admin pode cadastrar empresas

### 3. Módulo de Prospecção
- ✅ Admin pode criar prospecções e atribuir a consultores
- ✅ Consultor pode registrar ligações
- ✅ Campos: data, hora, resultado, observações
- ✅ Vinculação com empresa e consultor
- ✅ Histórico completo de prospecções

### 4. Módulo de Agendamentos
- ✅ Criação de agendamentos vinculados a prospecções
- ✅ Status: pendente, realizado, vencido
- ✅ Consultor vê apenas seus agendamentos
- ✅ Admin visualiza todos os agendamentos

### 5. Módulo de Alertas
- ✅ Categorização por cores:
  - Vermelho: Agendamentos vencidos
  - Amarelo: Agendamentos de hoje
  - Verde: Agendamentos futuros
- ✅ Atualização automática
- ✅ Filtro por permissão de usuário

### 6. Interface
- ✅ Tema escuro em todas as telas
- ✅ Layout profissional com sidebar fixa
- ✅ Cabeçalho com nome do usuário e botão de logout
- ✅ Responsivo e otimizado
- ✅ Navegação intuitiva

## Como Usar

### 1. Primeiro Acesso
1. Acesse o sistema em http://localhost:5000
2. Clique em "Registre-se"
3. Crie uma conta (escolha "Administrador" para acesso completo)
4. Faça login com suas credenciais

### 2. Cadastrar Empresas (Admin)
1. No menu lateral, clique em "Empresas"
2. Clique em "+ Nova Empresa"
3. Preencha os dados da empresa
4. Clique em "Salvar Empresa"

### 3. Criar Prospecção
1. No menu lateral, clique em "Prospecções"
2. Clique em "+ Nova Prospecção"
3. Selecione a empresa e consultor (se Admin)
4. Registre a ligação com data, hora, resultado e observações
5. Clique em "Salvar Prospecção"

### 4. Criar Agendamento
1. Na lista de prospecções, clique em "Agendar"
2. Digite a data e hora do agendamento
3. Adicione observações (opcional)

### 5. Visualizar Alertas
1. No menu lateral, clique em "Alertas"
2. Veja os agendamentos categorizados por cores
3. Marque como "realizado" quando completar

## API Endpoints

### Autenticação
- `POST /api/auth/registro` - Criar nova conta
- `POST /api/auth/login` - Fazer login

### Empresas
- `GET /api/empresas` - Listar empresas (com filtros)
- `POST /api/empresas` - Criar empresa (Admin)
- `GET /api/empresas/{id}` - Obter empresa específica
- `PUT /api/empresas/{id}` - Atualizar empresa (Admin)
- `DELETE /api/empresas/{id}` - Deletar empresa (Admin)

### Prospecções
- `GET /api/prospeccoes` - Listar prospecções
- `POST /api/prospeccoes` - Criar prospecção
- `GET /api/prospeccoes/{id}` - Obter prospecção específica

### Agendamentos
- `GET /api/agendamentos` - Listar agendamentos
- `POST /api/agendamentos` - Criar agendamento
- `PUT /api/agendamentos/{id}` - Atualizar agendamento
- `GET /api/agendamentos/alertas` - Obter alertas categorizados

## Banco de Dados

### Tabelas
1. **usuarios** - Usuários do sistema (Admin/Consultor)
2. **empresas** - Cadastro de empresas
3. **prospeccoes** - Registro de prospecções e ligações
4. **agendamentos** - Agendamentos de retorno

### Relacionamentos
- Prospecção → Empresa (many-to-one)
- Prospecção → Usuário/Consultor (many-to-one)
- Agendamento → Prospecção (many-to-one)

## Tecnologias

### Python Packages
- FastAPI 0.109.0
- SQLAlchemy 2.0.25
- PostgreSQL (via psycopg2-binary)
- Pydantic 2.5.3 (com validação de email)
- python-jose (JWT)
- passlib (bcrypt para senhas)
- Jinja2 3.1.3
- Uvicorn (servidor ASGI)

## Variáveis de Ambiente (Obrigatórias)

O sistema requer as seguintes variáveis de ambiente configuradas:

- **`DATABASE_URL`** - URL de conexão PostgreSQL (obrigatório)
  - Formato: `postgresql://user:password@host:port/database`
  - No Replit, configurado automaticamente
  
- **`SESSION_SECRET`** - Chave secreta para JWT (obrigatório)
  - Deve ser uma string aleatória segura
  - No Replit, configurado automaticamente
  
**Importante**: O sistema não inicia sem estas variáveis configuradas, garantindo segurança desde o primeiro uso.

## Melhorias Futuras
- Upload de planilha Excel para cadastro em massa
- Exportação de relatórios (CSV/PDF)
- Dashboard com gráficos e estatísticas
- Notificações em tempo real
- Histórico de alterações

## Data de Criação
06 de Novembro de 2025

## Última Atualização
06 de Novembro de 2025
