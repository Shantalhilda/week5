-- Active: 1729094293979@@127.0.0.1@3306@army
create table units(
    unit_id INT,
    unit_name VARCHAR(45),
    unit_type VARCHAR(45),
    _location VARCHAR(45),
    primary key (unit_id)
);

create table missions(
    Mission_id INT,
    M_name VARCHAR(45),
    M_type VARCHAR(45),
    Start_Date VARCHAR(45),
    End_Date VARCHAR(45),
    unit_id INT,
    primary key (Mission_id),
    foreign key (unit_id) references units(unit_id)
);

create table Soldiers(
    Soldier_ID INT,
    First_Name VARCHAR(45),
    Last_Name VARCHAR(45),
    _Level VARCHAR(45),
    date_of_birth DATE,
    unit_id INT,
    primary key (Soldier_ID),
    foreign key (unit_id) references units(unit_id)
);
DESCRIBE units;

create table Equipments(
    Eqt_ID INT,
    Eqt_Name VARCHAR(45),
    Quantity INT,
    unit_id INT,
    primary key (Eqt_ID),
    foreign key (unit_id) references units(unit_id)
);

insert into units VALUES
(1001 , 'Squad', 'engineering' , 'Jinja'),
(1002 , 'Corps', 'Armored' , 'Kampala'),
(1003 , 'Brigade' , 'fire' ,' mukono');


INSERT INTO missions VALUES
(101, 'Gulfwar', 'offensive', '02/03/20', '05/03/20', 1001),
(102, 'Panamawar', 'Defensive', '17/12/20', '20/12/20', 1002),
(103, 'Vietnam', 'Surveillance', '12/04/19', '20/04/19',1003);


INSERT INTO Soldiers VALUES
(001, 'john', 'wasswa', 'General', '2004-03-12', 1001),
(002, 'sam', 'kitale', 'Specialist', '2003-03-18', 1002),
(003, 'laura', 'kibwezi', 'Commander', '1999-02-19', 1003);


INSERT INTO Equipments VALUES
(101, 'weapons', 100, 1001),
(102, 'ammunition', 500, 1002),
(103, 'powder', 100,1003 );







select*from Equipments ; 