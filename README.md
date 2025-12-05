# Labor Education Management System

这是一个基于 Flask (后端) 和 Vue 3 (前端) 的全栈管理系统。

## 项目结构

- `backend/`: Flask 后端代码
- `frontend/`: Vue 3 + Vite 前端代码

## 快速开始

### 1. 后端环境配置 (Backend)

确保你已经安装了 Python 3.8+。

```bash
# 1. 进入后端目录
cd backend

# 2. 创建虚拟环境 (可选，但推荐)
python -m venv venv

# Windows 激活虚拟环境
.\venv\Scripts\activate
# Linux/Mac 激活虚拟环境
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 数据库迁移
# 初始化数据库表结构
flask db upgrade

# 5. 创建管理员账号
# 默认账号: admin / 密码: admin
python create_admin.py

# 6. 启动后端服务
# Windows PowerShell
$env:FLASK_APP="app"
$env:FLASK_ENV="development"
flask run

# 或者 CMD
set FLASK_APP=app
set FLASK_ENV=development
flask run

# Linux/Mac
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

后端服务默认运行在 `http://127.0.0.1:5000`。

### 2. 前端环境配置 (Frontend)

确保你已经安装了 Node.js (推荐 v16+)。

```bash
# 1. 进入前端目录
cd frontend

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run dev
```

前端服务启动后，通常运行在 `http://localhost:5173` (具体看终端输出)。

## 使用说明

1. 打开浏览器访问前端地址 (如 `http://localhost:5173`)。
2. 使用默认管理员账号登录：
   - **用户名**: `admin`
   - **密码**: `admin`
3. 登录后即可进行商品管理、仓库管理、库存流水记录及财务管理等操作。

## 技术栈

- **后端**: Python, Flask, SQLAlchemy, Flask-Migrate, Flask-JWT-Extended
- **前端**: Vue 3, Vite, Vue Router, Axios
- **数据库**: SQLite (默认), 可配置为 PostgreSQL/MySQL

## 注意事项

- 如果遇到跨域问题 (CORS)，请确保后端 `app/__init__.py` 中已正确配置 `CORS(app)`。
- 生产环境部署请使用 Gunicorn (Linux) 或 Waitress (Windows) 作为 WSGI 服务器，并构建前端静态资源 (`npm run build`)。
- 未进行单元测试和功能测试，代码可能有漏洞
