-- Criação da tabela Cliente
CREATE TABLE cliente (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    primeiro_nome VARCHAR(50),
    ultimo_nome VARCHAR(50),
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_nascimento DATE,
    num_habilitacao INT,
    data_registro DATE,
    status_ativacao INT
);

-- Criação da tabela Veiculo
CREATE TABLE veiculo (
    veiculo_id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano INT,
    placa VARCHAR(20),
    cor VARCHAR(20),
    tipo_combustivel VARCHAR(20),
    disponivel BOOLEAN,
    valor_diaria DECIMAL(10, 2)
);

-- Criação da tabela Reserva
CREATE TABLE Reserva (
    reserva_id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    veiculo_id INT,
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
    FOREIGN KEY (veiculo_id) REFERENCES Veiculo(veiculo_id)
);

-- Criação da tabela Transacao
CREATE TABLE Transacao (
    transacao_id INT AUTO_INCREMENT PRIMARY KEY,
    reserva_id INT,
    data_hora DATETIME,
    tipo_transacao VARCHAR(20),
    metodo_pagamento VARCHAR(50),
	valor_total DECIMAL(10, 2),
    status_reserva VARCHAR(20),
    FOREIGN KEY (reserva_id) REFERENCES Reserva(reserva_id)
);
