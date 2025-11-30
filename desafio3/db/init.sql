CREATE TABLE IF NOT EXISTS mensagens (
    id SERIAL PRIMARY KEY,
    conteudo VARCHAR(255) NOT NULL
);

INSERT INTO mensagens (conteudo) VALUES
('Bem-vindo ao sistema!'),
('Mensagem registrada com sucesso.'),
('Dados carregados do PostgreSQL.');
