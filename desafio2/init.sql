CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10,2) NOT NULL
);

INSERT INTO produtos (nome, preco) VALUES
('Teclado Mecânico', 350.00),
('Mouse Gamer', 199.90),
('Monitor 27"', 1299.00);
