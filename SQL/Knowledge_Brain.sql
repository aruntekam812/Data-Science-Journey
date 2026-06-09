CREATE DATABASE Knowledge_Brain;
use Knowledge_Brain;
-- INPUT LAYER
create table Raw_data(
   id int primary key auto_increment,
   Source Text,
   data_type Text,
   content Text,
   created_at  timestamp DEFAULT current_timestamp

);
-- CLEANING LAYER
create TABLE processed_data(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    raw_id INT,
    cleaned_content TEXT,
    null_handling_info TEXT,
    status TEXT,
    FOREIGN KEY(raw_id) REFERENCES raw_data(id)
);
-- ANALYTICAL LAYER 
CREATE TABLE insights(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    data_id INTEGER,
    insight TEXT,
    category TEXT,
    confidence REAL,
    FOREIGN KEY(data_id) REFERENCES processed_data(id)

);

-- BRAIN LAYER ⭐
CREATE TABLE knowledge_memory(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    topic TEXT,
    summary TEXT,
    tags TEXT,
    source_insight_id INTEGER,
    FOREIGN KEY(source_insight_id) REFERENCES insights(id)

);