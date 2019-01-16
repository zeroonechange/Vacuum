DROP TABLE IF EXISTS price_tag;
DROP TABLE IF EXISTS msg_original;
DROP TABLE IF EXISTS msg_visited;
DROP TABLE IF EXISTS price_history;
DROP TABLE IF EXISTS record_item;

/*消息所属类型    例如 USD  GOLD*/
CREATE TABLE price_tag(
  id INT PRIMARY KEY NOT NULL,
  tag_name_cn TEXT,
  tag_name_en TEXT NOT NULL
);


/*原始消息*/
CREATE TABLE msg_original(
  tag_id INT NOT NULL,
  msg_date TEXT NOT NULL,
  msg_range TEXT,   /*例如 国内  国外*/
  msg_text TEXT
);


/*历史消息记录*/
CREATE TABLE msg_visited(
  msg_date TEXT NOT NULL,
  msg_url TEXT NOT NULL
);

/*历史价格*/
CREATE TABLE price_history(
  tag_id INT NOT NULL,
  price_date TEXT NOT NULL,
  price_op DOUBLE NOT NULL,
  price_st DOUBLE NOT NULL,
  price_max DOUBLE NOT NULL,
  price_min DOUBLE NOT NULL,
  record_ids TEXT NOT NULL
);

CREATE TABLE record_item(
  id INT PRIMARY KEY NOT NULL,
  content TEXT
);


insert into price_tag (id, tag_name_cn, tag_name_en) values (1001, '黄金', 'GOLD');