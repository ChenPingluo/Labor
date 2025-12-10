# Labor Education Management System

这是一个基于 Flask (后端) 和 Vue 3 (前端) 的全栈管理系统。

## 项目结构

- `backend/`: Flask 后端代码
- `frontend/`: Vue 3 + Vite 前端代码
- `labor_core/`: Rust 高性能计算核心模块

## 快速开始

### 1. 后端环境配置 (Backend & Rust Core)

**注意**：本项目使用了 Rust 编写高性能计算模块。
- **运行原理**：Rust 代码会被编译为 Python 的扩展模块（`.pyd` 或 `.so`），直接在 Python 进程中加载运行，**无需**单独启动 Rust 服务或进程。
- **编译要求**：首次安装时，系统必须安装 Rust 编译器 (Cargo)。

确保你已经安装了 Python 3.8+ 和 [Rust 工具链](https://rustup.rs/)。

```bash
# 1. 进入后端目录
cd backend

# 2. 创建虚拟环境 (可选，但推荐)
python -m venv venv

# Windows 激活虚拟环境
.\venv\Scripts\activate
# Linux/Mac 激活虚拟环境
source venv/bin/activate

# 3. 安装依赖 (已包含 maturin 构建工具)
pip install -r requirements.txt

# 4. 编译并安装 Rust 核心模块
# 这一步会将 Rust 代码编译并安装到当前的 Python 虚拟环境中
cd ../labor_core
maturin develop
cd ../backend

# 5. 数据库迁移

# 初始化数据库表结构
flask db upgrade

# 6. 创建管理员账号
# 默认账号: admin / 密码: admin
python create_admin.py

# 7. 启动后端服务
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
4. **多语言支持**：系统支持中文和英文切换，可在页面右上角进行设置。

## 技术栈

- **后端**: Python, Flask, SQLAlchemy, Flask-Migrate, Flask-JWT-Extended
- **高性能计算核心**: Rust, PyO3, Maturin
- **前端**: Vue 3, Vite, Vue Router, Axios, Vue I18n
- **数据库**: SQLite (默认), 可配置为 PostgreSQL/MySQL

## 注意事项

- 如果遇到跨域问题 (CORS)，请确保后端 `app/__init__.py` 中已正确配置 `CORS(app)`。
- 生产环境部署请使用 Gunicorn (Linux) 或 Waitress (Windows) 作为 WSGI 服务器，并构建前端静态资源 (`npm run build`)。
- 未进行单元测试和功能测试，代码可能有漏洞
