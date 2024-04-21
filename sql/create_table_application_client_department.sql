CREATE TABLE department (
    idDepartment int PRIMARY KEY,
    DepartmentCity varchar(45),
    CountOfWorkers int
);

CREATE TABLE client (
    idClient int PRIMARY KEY,
    FirstName varchar(45),
    LastName varchar(45),
    Education varchar(45),
    Passport varchar(45),
    City varchar(45),
    Age varchar(45),
    Department_idDepartment int NOT NULL,
    CONSTRAINT fk_Client_Department
        FOREIGN KEY (Department_idDepartment)
        REFERENCES department (idDepartment)
);

CREATE INDEX fk_Client_Department_idx
    ON client (Department_idDepartment);

CREATE TABLE application (
    idApplication int PRIMARY KEY,
    Sum int,
    CreditState varchar(45),
    Currency varchar(45),
    Client_idClient int NOT NULL,
    CONSTRAINT fk_Application_Client1
        FOREIGN KEY (Client_idClient)
        REFERENCES client (idClient)
);

CREATE INDEX fk_Application_Client1_idx
    ON application (Client_idClient);
