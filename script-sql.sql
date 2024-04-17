CREATE TABLE cliente (
    cpf VARCHAR(11) PRIMARY KEY, 
    primeiro_nome VARCHAR(50),
    sobrenome VARCHAR(255),
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_nascimento DATE,
    num_habilitacao VARCHAR(30),
    data_registro DATE
);

CREATE TABLE veiculo (
    veiculo_id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano INT,
    placa VARCHAR(20),
    categoria VARCHAR(20),
    cor VARCHAR(20),
    tipo_combustivel VARCHAR(20),
    disponivel CHAR(1) 
    valor_diaria DECIMAL(10,2),
);

CREATE TABLE reserva (
    reserva_id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id VARCHAR(11),
    veiculo_id INT,
    data_reserva DATE,
    data_inicio DATE,
    data_fim DATE,
    valor_total DECIMAL(10,2),
    -- Definir chaves estrangeiras
    FOREIGN KEY (cliente_id) REFERENCES cliente(cpf),
    FOREIGN KEY (veiculo_id) REFERENCES veiculo(veiculo_id)
);