-- 创建用户表（含主键、自增、JSON 类型）
-- \c system_db;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- SERIAL 自增整数（等价于 AUTO_INCREMENT）
    name VARCHAR(50) NOT NULL,  -- 字符串，非空
    age INT CHECK (age > 0),  -- 整数，检查约束（年龄>0）
    email TEXT UNIQUE,  -- 文本，唯一约束
    tags TEXT[] , -- ARRAY,  -- 文本数组 | -- ✅ 正确：文本数组类型（替代错误的 ARRAY[TEXT]）
    info JSONB,  -- JSONB（二进制 JSON，支持索引，推荐）
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 时间戳，默认当前时间
);

-- \d users



-- 写法 1：使用 ARRAY[] 构造器（推荐，可读性高）
INSERT INTO users (name, age, email, tags, info)
VALUES (
    '张三',
    25,
    'zhangsan@test.com',
    ARRAY['Python', f'PostgreSQL'],  -- ✅ 插入数组值时用 ARRAY[]
    '{"city": "上海", "job": "工程师"}'::JSONB
);

-- 写法 2：使用花括号（字符串形式，需单引号包裹）
INSERT INTO users (name, age, email, tags)
VALUES (
    '李四',
    30,
    'lisi@test.com',
    '{"Java", "MySQL"}'  -- 等价于 ARRAY['Java', 'MySQL']
);

-- PG 标识符（表名 / 字段名）默认小写，若用大写需加双引号（不推荐）：
-- 查询数据（验证数组值）
SELECT name, tags FROM users;

SELECT * FROM users;

-- \d users