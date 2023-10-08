-- Create a new database called 'DatabaseName'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'DatabaseDQL'
)
CREATE DATABASE DatabaseDQL
GO
USE DatabaseDQL

-- Drop the table if it already exists
IF OBJECT_ID('personne', 'U') IS NOT NULL
DROP TABLE personne
GO
-- Create the table personne
CREATE TABLE personne
(
    personneId INT NOT NULL PRIMARY KEY, -- primary key column
    personneName VARCHAR(100) NOT NULL,
	personneTel VARCHAR(50) NOT NULL,
    email VARCHAR(30) NOT NULL,
	personneAddress VARCHAR(60) NOT NULL,
    age INT,
    sex VARCHAR(30),
    sitution_matrimonial VARCHAR(50)
);
GO

-- Drop the table if it already exists
IF OBJECT_ID('education', 'U') IS NOT NULL
DROP TABLE education 
GO


-- Create the table education
CREATE TABLE education (
	educationId  INT NOT NULL PRIMARY KEY,
    personneId INT FOREIGN KEY REFERENCES personne(personneId),
	graduation VARCHAR(150) NOT NULL,
	schoolOrUniversity	TEXT,
    yearOfGraduation DATE
);
GO

-- Drop the table if it already exists
IF OBJECT_ID('workExperience', 'U') IS NOT NULL
DROP TABLE workExperience 
GO

-- Create the table workExperience
CREATE TABLE workExperience (
	workExperienceId  INT NOT NULL PRIMARY KEY,
    personneId INT FOREIGN KEY REFERENCES personne(personneId),
	jobTitle VARCHAR(150) NOT NULL,
	companyName	TEXT,
    startingDate DATE,
    dateOfEnd DATE,
    dutiesAndResponsibilities TEXT,
);
GO

-- Drop the table if it already exists
IF OBJECT_ID('skills', 'U') IS NOT NULL
DROP TABLE skills 
GO

-- Create the table workExperience
CREATE TABLE skills (
	skillsId  INT NOT NULL PRIMARY KEY,
    personneId INT FOREIGN KEY REFERENCES personne(personneId),
	technicalSkills VARCHAR(150) NOT NULL,
	languageProficiency	TEXT,
    otherRelevantSkills TEXT,
);
GO

