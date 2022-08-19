.headers ON
DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios(
    username TEXT,
    password varchar(32),
    level INTEGER,
    token BLOB
);

CREATE UNIQUE INDEX index_usuario ON usuarios(username);

INSERT INTO usuarios(username, password, level, token) VALUES('admin','21232f297a57a5a743894a0e4a801fc3',0,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ5ZWsiOiJhZG1pbjIwMjItMDgtMTggMTk6NTU6MDkuMDI0ODI0In0.tMYht1MODZXaXOSw2ZvC0VaCxVWVprS5UiMm6xs8kjk');
INSERT INTO usuarios(username, password, level, token) VALUES('user','ee11cbb19052e40b07aac0ca060c23ee',1, 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ5ZWsiOiJ1c2VyMjAyMi0wOC0xOCAxOTo1OToyMC45MDY4NDQifQ.7kuGeoSCYCW8ng4DTXQWFUrgyyvsZO_chd2hPZqL-AQ');

SELECT * FROM usuarios;
