DROP TABLE IF EXISTS `Contacts`;

CREATE TABLE `Contacts` (
    `contactID` INTEGER PRIMARY KEY AUTOINCREMENT,
    `firstName` TEXT NOT NULL,
    `lastName` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `phone` TEXT,
    `company` TEXT,
    `details` TEXT
);