"""
curriculum.py
All 30 days of the backend learning roadmap.
Each day has: phase, topic_title, topic_description, daily_goal, blogs[], youtube[]
"""

PHASES = {
    1: {
        "label": "Phase 1 — Web Fundamentals (Days 1–7)",
        "color": "#EBF4FF",
        "text_color": "#1a4a7a",
    },
    2: {
        "label": "Phase 2 — FastAPI From Scratch (Days 8–18)",
        "color": "#EAFAF1",
        "text_color": "#0f5c38",
    },
    3: {
        "label": "Phase 3 — Architecture & System Design (Days 19–24)",
        "color": "#FEF9E7",
        "text_color": "#7d5a00",
    },
    4: {
        "label": "Phase 4 — Docker & GCP Deployment (Days 25–28)",
        "color": "#F4EEFF",
        "text_color": "#4a2080",
    },
    5: {
        "label": "Phase 5 — Data Engineering Integration (Days 29–30)",
        "color": "#FEF0EB",
        "text_color": "#7a2a10",
    },
}

CURRICULUM = [
    # ─────────────── PHASE 1: Web Fundamentals ───────────────
    {
        "phase": 1,
        "topic_title": "How the Internet Works — DNS, TCP/IP, Client-Server",
        "topic_description": "Before writing a single line of FastAPI, understand the physical journey of a web request: browser → DNS → IP → TCP handshake → server → response. This mental model unlocks everything else.",
        "daily_goal": "Draw a diagram of what happens between typing a URL and seeing a webpage. Explain it to yourself out loud.",
        "blogs": [
            {
                "title": "How Does the Internet Work? — MDN Web Docs",
                "url": "https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/How_does_the_Internet_work",
                "desc": "The definitive beginner-friendly explanation from Mozilla",
            },
            {
                "title": "What is DNS? How Domain Name System Works — Cloudflare",
                "url": "https://www.cloudflare.com/learning/dns/what-is-dns/",
                "desc": "Visual, clear explanation of DNS resolution",
            },
        ],
        "youtube": [
            {
                "title": "How the Internet Works in 5 Minutes — Aaron",
                "url": "https://www.youtube.com/watch?v=7_LPdttKXPc",
                "desc": "Legendary short explainer, 5 minutes, absolutely worth it",
            },
            {
                "title": "Computer Networking Full Course — freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=qiQR5rTSshw",
                "desc": "Deep dive if you want to go further into TCP/IP",
            },
        ],
    },
    {
        "phase": 1,
        "topic_title": "HTTP Deep Dive — Methods, Headers, Status Codes",
        "topic_description": "HTTP is the language of the web. GET, POST, PUT, DELETE are the verbs. Status codes (200, 404, 500) are the responses. Headers carry metadata. This is literally how your FastAPI endpoints will communicate.",
        "daily_goal": "Open browser DevTools → Network tab → visit any website. Inspect one request: see the method, headers, status code, and response body.",
        "blogs": [
            {
                "title": "An Overview of HTTP — MDN Web Docs",
                "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview",
                "desc": "The authoritative HTTP reference — bookmark this forever",
            },
            {
                "title": "HTTP in Depth — cs.fyi",
                "url": "https://cs.fyi/guide/http-in-depth",
                "desc": "Covers caching, cookies, HTTPS, connection management",
            },
            {
                "title": "HTTP Status Codes Cheat Sheet — REST API Tutorial",
                "url": "https://www.restapitutorial.com/httpstatuscodes.html",
                "desc": "Quick reference for all status codes with use cases",
            },
        ],
        "youtube": [
            {
                "title": "HTTP Crash Course & Exploration — Traversy Media",
                "url": "https://www.youtube.com/watch?v=iYM2zFP3Zn0",
                "desc": "1 hour, covers everything from methods to caching",
            },
        ],
    },
    {
        "phase": 1,
        "topic_title": "REST API Principles — The Rules of Web Communication",
        "topic_description": "REST is an architectural style, not a protocol. Six constraints define it: stateless, client-server, cacheable, uniform interface, layered system, code on demand. Understanding these prevents bad API design before it starts.",
        "daily_goal": "List the 6 REST constraints and explain each in one sentence in your own words. No copy-paste.",
        "blogs": [
            {
                "title": "REST API Best Practices — Stack Overflow Blog",
                "url": "https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/",
                "desc": "Must-read. Written by practitioners, covers naming, versioning, security",
            },
            {
                "title": "REST Endpoint Design Examples — freeCodeCamp",
                "url": "https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/",
                "desc": "Practical examples with good vs bad endpoint naming",
            },
        ],
        "youtube": [
            {
                "title": "REST API Concepts and Examples — WebConcepts",
                "url": "https://www.youtube.com/watch?v=7YcW25PHnAA",
                "desc": "Clean 8-minute explainer of REST concepts",
            },
            {
                "title": "What is a REST API? — IBM Technology",
                "url": "https://www.youtube.com/watch?v=lsMQRaeKNDk",
                "desc": "IBM's authoritative short explainer on REST",
            },
        ],
    },
    {
        "phase": 1,
        "topic_title": "How Frontend Talks to Backend — The Full Request Cycle",
        "topic_description": "User clicks button → JS fires fetch() → HTTP request hits your server → Python code runs → JSON returned → UI updates. This cycle is everything. Today you understand each step in that chain.",
        "daily_goal": "Build a 10-line HTML page with a button that calls a public API (like https://api.github.com/users/torvalds) and displays the result. No framework needed.",
        "blogs": [
            {
                "title": "REST APIs for Frontend Developers — Medium",
                "url": "https://medium.com/@devrmichael/rest-apis-for-frontend-developers-a-simple-guide-83074731e600",
                "desc": "Simple guide with examples of fetch() and axios calls",
            },
            {
                "title": "How Frontend and Backend Interact — Strapi",
                "url": "https://strapi.io/blog/how-frontend-and-backend-components-interact-in-a-full-stack-app",
                "desc": "Explains data flow, APIs, CORS, security between layers",
            },
            {
                "title": "Integrating Frontend and Backend with APIs — Medium",
                "url": "https://kapucuonur.medium.com/integrating-frontend-and-backend-with-apis-a-comprehensive-guide-9d296eef2e33",
                "desc": "Comprehensive guide with JWT integration examples",
            },
        ],
        "youtube": [
            {
                "title": "How the web works — Client server model — Academind",
                "url": "https://www.youtube.com/watch?v=zvKadd9Cybg",
                "desc": "Best visual explanation of the full request cycle",
            },
        ],
    },
    {
        "phase": 1,
        "topic_title": "JSON, APIs & Postman — Calling APIs Like a Pro",
        "topic_description": "JSON is the universal language of APIs. Postman lets you send any HTTP request manually — essential for testing your own APIs before writing frontend code. Today you become fluent in reading and constructing JSON payloads.",
        "daily_goal": "Install Postman. Call 3 different public APIs (try: OpenWeatherMap free tier, JSONPlaceholder, REST Countries). Inspect the response structure.",
        "blogs": [
            {
                "title": "Introduction to JSON — json.org",
                "url": "https://www.json.org/json-en.html",
                "desc": "Official spec — short, read the whole thing",
            },
            {
                "title": "Postman Learning Center — Getting Started",
                "url": "https://learning.postman.com/docs/getting-started/introduction/",
                "desc": "Official Postman docs — covers collections, environments, tests",
            },
        ],
        "youtube": [
            {
                "title": "Postman Beginner's Course — freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=VywxIQ2ZXw4",
                "desc": "Hands-on Postman tutorial with real API calls",
            },
            {
                "title": "What is JSON? — Fireship",
                "url": "https://www.youtube.com/watch?v=iiADhChRriM",
                "desc": "Quick 6-minute JSON explainer with examples",
            },
        ],
    },
    {
        "phase": 1,
        "topic_title": "Python Async/Await Fundamentals",
        "topic_description": "FastAPI is async-first. Without understanding async/await, you'll write blocking code that kills your API's performance. The event loop, coroutines, and I/O-bound vs CPU-bound tasks — today you build the mental model.",
        "daily_goal": "Write two versions of a function that fetches 5 URLs: one with sequential requests.get() and one with async aiohttp. Time both. See the difference.",
        "blogs": [
            {
                "title": "Async IO in Python: A Complete Walkthrough — Real Python",
                "url": "https://realpython.com/async-io-python/",
                "desc": "The most thorough async Python guide — essential reading",
            },
            {
                "title": "Python Concurrency: asyncio — Python Docs",
                "url": "https://docs.python.org/3/library/asyncio.html",
                "desc": "Official asyncio documentation with examples",
            },
        ],
        "youtube": [
            {
                "title": "Python Asyncio, Await, Async — mCoding",
                "url": "https://www.youtube.com/watch?v=t5Bo1Je9EmE",
                "desc": "Explains the event loop clearly — watch this first",
            },
            {
                "title": "Async Python — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=2IW-ZEui4h4",
                "desc": "Practical async patterns with aiohttp and asyncio",
            },
        ],
    },
    {
        "phase": 1,
        "topic_title": "Python Type Hints & Pydantic Basics",
        "topic_description": "FastAPI uses Python type hints for EVERYTHING — request validation, response schemas, documentation. Pydantic enforces types at runtime. Today you master these because you cannot use FastAPI well without them.",
        "daily_goal": "Write a Pydantic model for a 'DataPipeline' with fields: name, source_url, schedule_cron, is_active, created_at. Add validators for URL format and cron syntax.",
        "blogs": [
            {
                "title": "Python Type Checking — Real Python",
                "url": "https://realpython.com/python-type-checking/",
                "desc": "Comprehensive guide to Python's type hint system",
            },
            {
                "title": "Pydantic v2 Documentation",
                "url": "https://docs.pydantic.dev/latest/",
                "desc": "Official Pydantic docs — validators, models, field types",
            },
        ],
        "youtube": [
            {
                "title": "Pydantic Tutorial — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=Vj-iU-8_xLs",
                "desc": "Best Pydantic tutorial, covers v2 features",
            },
            {
                "title": "Python Type Hints — Corey Schafer",
                "url": "https://www.youtube.com/watch?v=QORvB-_mbZ0",
                "desc": "Clean intro to type hints from a trusted Python educator",
            },
        ],
    },
    # ─────────────── PHASE 2: FastAPI From Scratch ───────────────
    {
        "phase": 2,
        "topic_title": "FastAPI Hello World — Your First Endpoint",
        "topic_description": "Today you install FastAPI and write your first real API endpoint. You'll see the magic: automatic Swagger docs, request validation, and lightning-fast response — all in under 20 lines of code.",
        "daily_goal": "Build a FastAPI app with 3 endpoints: GET /health, GET /items/{id}, POST /items with a Pydantic body. Run it, open /docs in the browser.",
        "blogs": [
            {
                "title": "FastAPI Official Tutorial — First Steps",
                "url": "https://fastapi.tiangolo.com/tutorial/first-steps/",
                "desc": "Start here. Best written framework docs in existence",
            },
            {
                "title": "Get Started With FastAPI — Real Python",
                "url": "https://realpython.com/get-started-with-fastapi/",
                "desc": "Explains the 'why' behind FastAPI design choices",
            },
            {
                "title": "Getting Started with FastAPI — PyImageSearch",
                "url": "https://pyimagesearch.com/2025/03/17/getting-started-with-python-and-fastapi-a-complete-beginners-guide/",
                "desc": "Beginner guide covering endpoints, Pydantic, TestClient",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Full Course — freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=0sOvCWFmrtA",
                "desc": "5-hour complete course — the best free FastAPI course",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Path Parameters, Query Params & Request Body",
        "topic_description": "Three ways data comes INTO your API: path params (/users/{id}), query params (?page=2&limit=10), and request body (JSON payload in POST/PUT). Each has different use cases — today you master all three.",
        "daily_goal": "Build a /search endpoint that takes: path param for resource type, query params for pagination + filters, and a POST body for complex filter criteria.",
        "blogs": [
            {
                "title": "FastAPI Path Parameters — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/path-params/",
                "desc": "With type validation, enum types, metadata",
            },
            {
                "title": "FastAPI Query Parameters — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/query-params/",
                "desc": "Optional params, defaults, required params",
            },
            {
                "title": "FastAPI Request Body — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/body/",
                "desc": "Pydantic models as request bodies",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Path & Query Parameters — Tech With Tim",
                "url": "https://www.youtube.com/watch?v=PKoRs_jYrpQ",
                "desc": "Practical examples building a real data API",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Pydantic Models for Request & Response Schemas",
        "topic_description": "Pydantic is the backbone of FastAPI's type safety. Input validation, output serialization, nested models, optional fields, custom validators — today you go deep. This is what separates buggy APIs from reliable ones.",
        "daily_goal": "Create nested Pydantic models for a data pipeline: PipelineConfig → DataSource → ScheduleConfig → NotificationSettings. Add field validators and custom error messages.",
        "blogs": [
            {
                "title": "FastAPI Schema Extra — Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/schema-extra-example/",
                "desc": "Adding examples to your OpenAPI schema",
            },
            {
                "title": "Pydantic Field Types & Validators — Pydantic Docs",
                "url": "https://docs.pydantic.dev/latest/concepts/validators/",
                "desc": "field_validator, model_validator, custom types",
            },
        ],
        "youtube": [
            {
                "title": "Pydantic v2 Full Tutorial — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=Vj-iU-8_xLs",
                "desc": "Deep dive into Pydantic v2 with FastAPI integration",
            },
            {
                "title": "FastAPI Pydantic Models — Patrick Loeber",
                "url": "https://www.youtube.com/watch?v=rkTLZ7cCHRM",
                "desc": "Practical Pydantic patterns in FastAPI",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Database Setup — SQLAlchemy + PostgreSQL with FastAPI",
        "topic_description": "Real APIs need real databases. SQLAlchemy ORM lets you interact with PostgreSQL using Python objects instead of raw SQL. Today you set up the DB connection, create models, and run your first queries.",
        "daily_goal": "Connect FastAPI to a local PostgreSQL DB. Create a 'pipelines' table via SQLAlchemy model. Write endpoints to CREATE and READ pipeline records.",
        "blogs": [
            {
                "title": "FastAPI SQL Databases — Official Tutorial",
                "url": "https://fastapi.tiangolo.com/tutorial/sql-databases/",
                "desc": "Official guide — SQLAlchemy session, models, CRUD",
            },
            {
                "title": "SQLAlchemy ORM Tutorial — SQLAlchemy Docs",
                "url": "https://docs.sqlalchemy.org/en/20/orm/quickstart.html",
                "desc": "Modern SQLAlchemy 2.0 style — use this version",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI with SQLAlchemy & PostgreSQL — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=nC9ob8xM3c8",
                "desc": "Full setup from scratch, includes migrations",
            },
            {
                "title": "FastAPI + PostgreSQL Full Tutorial — Amigoscode",
                "url": "https://www.youtube.com/watch?v=398-BqE6gM4",
                "desc": "End-to-end tutorial with Docker for the DB",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Async Database Queries with SQLAlchemy Async",
        "topic_description": "Synchronous DB calls block your event loop — you lose all of FastAPI's async advantage. Today you migrate to AsyncSession and async queries. Your API can now handle many concurrent requests without waiting for DB.",
        "daily_goal": "Rewrite yesterday's sync DB endpoints as fully async using AsyncSession. Benchmark: run 50 concurrent requests against both versions with httpx.",
        "blogs": [
            {
                "title": "Async SQLAlchemy with FastAPI — SQLAlchemy Docs",
                "url": "https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html",
                "desc": "Official async SQLAlchemy guide — AsyncSession, async_sessionmaker",
            },
            {
                "title": "FastAPI Async SQLAlchemy — TestDriven.io",
                "url": "https://testdriven.io/blog/fastapi-sqlalchemy/",
                "desc": "Full async CRUD with PostgreSQL and Alembic migrations",
            },
        ],
        "youtube": [
            {
                "title": "Async SQLAlchemy Tutorial — Eric Roby",
                "url": "https://www.youtube.com/watch?v=SZpjzkBBnpA",
                "desc": "Covers async engine, sessions, and dependency injection",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "FastAPI Dependency Injection — The Superpower",
        "topic_description": "FastAPI's DI system is its most underrated feature. Inject DB sessions, settings, auth context, rate limiters — cleanly and testably. No global state, no hidden coupling. This is what makes FastAPI code maintainable.",
        "daily_goal": "Create 3 reusable dependencies: get_db() for DB session, get_settings() for config, get_current_user() that validates a header token. Compose them in a route.",
        "blogs": [
            {
                "title": "FastAPI Dependencies — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/dependencies/",
                "desc": "Full DI tutorial — classes, sub-dependencies, global deps",
            },
            {
                "title": "FastAPI Dependency Injection — FastAPI Best Practices",
                "url": "https://github.com/zhanymkanov/fastapi-best-practices#dependencies-cbvs",
                "desc": "Production patterns for DI from startup experience",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Dependency Injection Explained — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=C7tphtKZS8I",
                "desc": "Deep-dive into why and how to use FastAPI DI well",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Authentication — JWT Tokens & OAuth2 in FastAPI",
        "topic_description": "Every real API needs auth. JWT (JSON Web Tokens) are stateless — the server doesn't store sessions. OAuth2 password flow: user sends credentials → server issues JWT → client sends JWT in every request. Today you implement this.",
        "daily_goal": "Implement full JWT auth: /auth/login returns access + refresh tokens. Protected routes validate the JWT. /auth/refresh issues new access token. Test with Postman.",
        "blogs": [
            {
                "title": "FastAPI Security — OAuth2 with JWT — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/",
                "desc": "Official tutorial — the canonical way to do JWT in FastAPI",
            },
            {
                "title": "FastAPI JWT Auth — TestDriven.io",
                "url": "https://testdriven.io/blog/fastapi-jwt-auth/",
                "desc": "Comprehensive: access tokens, refresh tokens, logout",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI JWT Authentication — Tech With Tim",
                "url": "https://www.youtube.com/watch?v=5GxQ1rLTwaU",
                "desc": "Builds auth from scratch, explains every step",
            },
            {
                "title": "FastAPI Security Full Course — Eric Roby",
                "url": "https://www.youtube.com/watch?v=Rj01GjMhNwI",
                "desc": "Covers OAuth2, JWT, roles, and permissions",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Error Handling, Middleware & CORS",
        "topic_description": "Production APIs return structured errors, not Python tracebacks. Middleware runs on every request — logging, timing, auth checks. CORS allows your frontend domain to call your API. Today you add all three.",
        "daily_goal": "Add: (1) custom exception handler that returns {error, message, code} JSON, (2) request timing middleware that logs slow requests >500ms, (3) CORS configured for localhost:3000.",
        "blogs": [
            {
                "title": "FastAPI Error Handling — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/handling-errors/",
                "desc": "HTTPException, custom exception handlers, override defaults",
            },
            {
                "title": "FastAPI Middleware — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/middleware/",
                "desc": "Writing custom middleware, timing, logging",
            },
            {
                "title": "FastAPI CORS — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/cors/",
                "desc": "CORSMiddleware setup for frontend integration",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Middleware & Error Handling — Bitfumes",
                "url": "https://www.youtube.com/watch?v=Fp0ZBLMQWGQ",
                "desc": "Practical examples with logging and custom error responses",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Background Tasks & Webhooks in FastAPI",
        "topic_description": "Long-running jobs (scraping, data processing) shouldn't block your API response. FastAPI has built-in BackgroundTasks for lightweight jobs. Today you also build a webhook receiver — critical for receiving data from external platforms.",
        "daily_goal": "Build: (1) a /scrape endpoint that triggers a background scraping task and immediately returns {job_id}, (2) a /webhook endpoint that validates HMAC signatures and processes incoming events.",
        "blogs": [
            {
                "title": "FastAPI Background Tasks — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/background-tasks/",
                "desc": "Built-in BackgroundTasks — when to use vs Celery",
            },
            {
                "title": "FastAPI + Celery for Heavy Background Jobs — TestDriven.io",
                "url": "https://testdriven.io/blog/fastapi-and-celery/",
                "desc": "When BackgroundTasks aren't enough — Redis + Celery",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Background Tasks — Patrick Loeber",
                "url": "https://www.youtube.com/watch?v=mFBWDRxsF7g",
                "desc": "Clean examples of background tasks with status tracking",
            },
        ],
    },
    {
        "phase": 2,
        "topic_title": "Testing FastAPI — pytest + TestClient",
        "topic_description": "Untested code is broken code you haven't found yet. FastAPI's TestClient makes testing endpoints trivial. Today you write unit tests for your routes and integration tests for your DB operations. This is what separates professional from amateur.",
        "daily_goal": "Write tests for your auth endpoints: test valid login, invalid password, expired token, missing token. Aim for >80% coverage on your routes.",
        "blogs": [
            {
                "title": "FastAPI Testing — Official Docs",
                "url": "https://fastapi.tiangolo.com/tutorial/testing/",
                "desc": "TestClient, async tests, dependency overrides for mocking",
            },
            {
                "title": "Testing FastAPI Applications — TestDriven.io",
                "url": "https://testdriven.io/blog/fastapi-crud/",
                "desc": "Full CRUD app with comprehensive test coverage",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Testing Tutorial — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=UP6MfMnFHHI",
                "desc": "pytest setup, fixtures, mocking dependencies",
            },
        ],
    },
    # ─────────────── PHASE 3: Architecture & System Design ───────────────
    {
        "phase": 3,
        "topic_title": "FastAPI Project Structure — Scalable Folder Architecture",
        "topic_description": "All logic in main.py is a time bomb. Today you restructure into: routers/ (HTTP), services/ (business logic), repositories/ (DB), schemas/ (Pydantic), core/ (config). This is the pattern Netflix uses. It's the pattern you'll use.",
        "daily_goal": "Refactor your existing API into the layered structure. No route should directly touch the database. Every route calls a service. Every service calls a repository.",
        "blogs": [
            {
                "title": "FastAPI Project Structure: Production Guide — Zestminds",
                "url": "https://www.zestminds.com/blog/fastapi-project-structure/",
                "desc": "Comprehensive 2026 guide — layered + feature-based hybrid",
            },
            {
                "title": "How to Structure a Scalable FastAPI Project — FastLaunchAPI",
                "url": "https://fastlaunchapi.dev/blog/how-to-structure-fastapi",
                "desc": "Battle-tested structure with detailed explanations",
            },
            {
                "title": "FastAPI Best Practices — zhanymkanov on GitHub",
                "url": "https://github.com/zhanymkanov/fastapi-best-practices",
                "desc": "Real startup experience — the single best GitHub repo to star",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Project Structure — BugBytes",
                "url": "https://www.youtube.com/watch?v=cbASjoZZGIw",
                "desc": "Step by step refactoring a flat app to layered architecture",
            },
        ],
    },
    {
        "phase": 3,
        "topic_title": "Database Migrations with Alembic",
        "topic_description": "Your database schema will change. Alembic manages those changes as versioned migrations — like git for your database. Add a column, rename a table, add indexes — all tracked, reversible, and safe to run in production.",
        "daily_goal": "Set up Alembic for your project. Create 3 migrations: initial schema, add index on a column, add a new table. Practice: upgrade, downgrade, history.",
        "blogs": [
            {
                "title": "Alembic Tutorial — Official Docs",
                "url": "https://alembic.sqlalchemy.org/en/latest/tutorial.html",
                "desc": "Official Alembic docs — autogenerate, manual migrations",
            },
            {
                "title": "FastAPI + Alembic — TestDriven.io",
                "url": "https://testdriven.io/blog/fastapi-sqlalchemy/",
                "desc": "Full migration setup with FastAPI and PostgreSQL",
            },
        ],
        "youtube": [
            {
                "title": "Alembic Database Migrations — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=9YpFuS0f0m0",
                "desc": "Alembic from scratch with SQLAlchemy 2.0",
            },
        ],
    },
    {
        "phase": 3,
        "topic_title": "System Design Fundamentals — Scaling, Caching, Queues",
        "topic_description": "Your startup will grow. Vertical scaling (bigger machine) hits limits. Horizontal scaling (more machines) needs load balancers. Caching (Redis) reduces DB load. Message queues (Pub/Sub) decouple services. Today you build the vocabulary.",
        "daily_goal": "Draw the architecture of your current API if it needed to handle 10,000 requests/minute. Where are the bottlenecks? What would you add first?",
        "blogs": [
            {
                "title": "System Design Primer — GitHub",
                "url": "https://github.com/donnemartin/system-design-primer",
                "desc": "The most starred system design resource on GitHub. Read Part 1",
            },
            {
                "title": "Backend Web Development Complete Guide — NerdLevelTech",
                "url": "https://nerdleveltech.com/backend-web-development-the-complete-2025-guide",
                "desc": "Microservices vs monolith, async patterns, scaling decisions",
            },
        ],
        "youtube": [
            {
                "title": "System Design for Beginners — freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=i53Gi_K3o7I",
                "desc": "Complete course: load balancers, caching, databases, queues",
            },
            {
                "title": "Redis Caching Explained — Fireship",
                "url": "https://www.youtube.com/watch?v=G1rOthIU-uo",
                "desc": "When and how to use Redis for API caching",
            },
        ],
    },
    {
        "phase": 3,
        "topic_title": "API Versioning, Rate Limiting & Configuration Management",
        "topic_description": "Production APIs version their endpoints (/v1/, /v2/) so old clients don't break. Rate limiting protects against abuse. Config management keeps secrets out of code. All three are non-negotiable for a real startup API.",
        "daily_goal": "Add to your API: (1) /v1/ prefix with APIRouter versioning, (2) slowapi rate limiting (100 req/min per IP), (3) pydantic-settings loading config from .env file.",
        "blogs": [
            {
                "title": "FastAPI API Versioning Strategies",
                "url": "https://www.fastapitutorial.com/blog/api-versioning-in-fastapi/",
                "desc": "URL prefix, header-based, and router-based versioning",
            },
            {
                "title": "FastAPI Rate Limiting with slowapi — Docs",
                "url": "https://github.com/laurentS/slowapi",
                "desc": "Official slowapi docs — the standard rate limiting library for FastAPI",
            },
            {
                "title": "Pydantic Settings for Config Management",
                "url": "https://docs.pydantic.dev/latest/concepts/pydantic_settings/",
                "desc": "Environment variables, .env files, type-safe config",
            },
        ],
        "youtube": [
            {
                "title": "FastAPI Configuration with Pydantic Settings — Eric Roby",
                "url": "https://www.youtube.com/watch?v=BuBJX2savI8",
                "desc": "Environment-based config with pydantic-settings",
            },
        ],
    },
    {
        "phase": 3,
        "topic_title": "Logging, Monitoring & Observability",
        "topic_description": "If it's not logged, it didn't happen. Structured logging with structlog, request IDs for tracing, slow query detection, error alerting — production systems are blind without these. Today you instrument your API properly.",
        "daily_goal": "Add structured JSON logging to every request: method, path, status_code, duration_ms, request_id. Write a middleware that logs slow requests (>500ms) at WARN level.",
        "blogs": [
            {
                "title": "FastAPI Logging Best Practices — Better Stack",
                "url": "https://betterstack.com/community/guides/logging/fastapi/",
                "desc": "Structured logging, request IDs, log levels — comprehensive",
            },
            {
                "title": "structlog Documentation",
                "url": "https://www.structlog.org/en/stable/",
                "desc": "The best Python structured logging library",
            },
        ],
        "youtube": [
            {
                "title": "Python Logging Guide — ArjanCodes",
                "url": "https://www.youtube.com/watch?v=9L77QExPmI0",
                "desc": "Proper logging setup for Python applications",
            },
        ],
    },
    # ─────────────── PHASE 4: Docker & GCP ───────────────
    {
        "phase": 4,
        "topic_title": "Docker Fundamentals — Containerize Your FastAPI App",
        "topic_description": "Docker packages your app + all dependencies into a portable container. 'Works on my machine' stops being an excuse. Today you write a Dockerfile for your FastAPI app, build an image, and run it locally in a container.",
        "daily_goal": "Write a multi-stage Dockerfile for your FastAPI app. Stage 1: install dependencies. Stage 2: copy app code. Run it: docker build + docker run. Test all endpoints still work.",
        "blogs": [
            {
                "title": "FastAPI Docker Deployment — Official Docs",
                "url": "https://fastapi.tiangolo.com/deployment/docker/",
                "desc": "Official Dockerfile for FastAPI with uvicorn — start here",
            },
            {
                "title": "FastAPI + Docker + GCP — Towards Data Science",
                "url": "https://towardsdatascience.com/how-to-deploy-ml-solutions-with-fastapi-docker-and-gcp-de1bb8bfc59a/",
                "desc": "End-to-end: Dockerfile → local test → GCP Cloud Run",
            },
        ],
        "youtube": [
            {
                "title": "Docker for Beginners — freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=pg19Z8LL06w",
                "desc": "Complete Docker course: images, containers, compose, volumes",
            },
        ],
    },
    {
        "phase": 4,
        "topic_title": "Deploy to GCP Cloud Run — Your API Goes Live",
        "topic_description": "Cloud Run is serverless Docker on GCP — no server management, auto-scales to zero, pay per request. Perfect for a startup. Today: build image → push to Artifact Registry → deploy to Cloud Run → get a public URL.",
        "daily_goal": "Deploy your FastAPI app to Cloud Run. Get a live HTTPS URL. Test all endpoints from Postman against the live URL. Share the URL — your API is on the internet.",
        "blogs": [
            {
                "title": "How to Deploy FastAPI on Cloud Run — OneUptime",
                "url": "https://oneuptime.com/blog/post/2026-02-17-how-to-deploy-a-fastapi-application-on-cloud-run-with-automatic-api-documentation/view",
                "desc": "2026 guide with exact gcloud commands for deployment",
            },
            {
                "title": "FastAPI Docker → Cloud Run via GitHub — Medium",
                "url": "https://medium.com/@judydev/deploy-a-fastapi-docker-container-on-google-cloud-run-via-github-137d030d70a4",
                "desc": "Full deployment flow with Firestore integration",
            },
        ],
        "youtube": [
            {
                "title": "Deploy FastAPI to Cloud Run — YouTube",
                "url": "https://www.youtube.com/watch?v=mcaYN2tb7SQ",
                "desc": "2025 — uses uv, Docker, Cloud Build. Production-ready setup",
            },
        ],
    },
    {
        "phase": 4,
        "topic_title": "CI/CD with GitHub Actions + Cloud Build",
        "topic_description": "Manual deployments are error-prone. CI/CD automates: push code → tests run → Docker image builds → Cloud Run deploys. Zero manual steps. Today you set up this pipeline so deployment is just `git push`.",
        "daily_goal": "Set up a GitHub Actions workflow: on push to main → run pytest → build Docker image → push to Artifact Registry → deploy to Cloud Run. Full automation.",
        "blogs": [
            {
                "title": "CI/CD for FastAPI with Cloud Build — davidmuraya.com",
                "url": "https://davidmuraya.com/blog/fastapi-cloud-build-run-deploy-on-gcp/",
                "desc": "Step-by-step: cloudbuild.yaml, Cloud Build trigger, auto-deploy",
            },
            {
                "title": "GitHub Actions Documentation",
                "url": "https://docs.github.com/en/actions",
                "desc": "Official GitHub Actions docs — workflows, secrets, environments",
            },
        ],
        "youtube": [
            {
                "title": "GitHub Actions Full Course — TechWorld with Nana",
                "url": "https://www.youtube.com/watch?v=R8_veQiYBjI",
                "desc": "Complete GitHub Actions tutorial for backend developers",
            },
        ],
    },
    {
        "phase": 4,
        "topic_title": "GCP Services for Data Engineers — BigQuery, Pub/Sub, Cloud Storage",
        "topic_description": "As a data engineer at a startup, you'll use: Cloud Storage (data lake), BigQuery (analytics warehouse), Pub/Sub (event streaming). Today you connect your FastAPI app to these GCP services and build a data ingestion endpoint.",
        "daily_goal": "Build an endpoint that: receives JSON data → publishes to Pub/Sub topic → a subscriber writes to BigQuery. The full GCP data pipeline, triggered by your API.",
        "blogs": [
            {
                "title": "BigQuery Python Client Library — Google Docs",
                "url": "https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries",
                "desc": "Official quickstart — queries, inserts, streaming",
            },
            {
                "title": "Cloud Pub/Sub Python Guide",
                "url": "https://cloud.google.com/pubsub/docs/publish-receive-messages-client-library",
                "desc": "Publisher + subscriber with Python client library",
            },
        ],
        "youtube": [
            {
                "title": "Google Cloud for Data Engineers — Google Cloud Tech",
                "url": "https://www.youtube.com/watch?v=d3MDxC_iuaw",
                "desc": "BigQuery, Dataflow, Pub/Sub — the GCP data stack explained",
            },
        ],
    },
    # ─────────────── PHASE 5: Data Engineering Integration ───────────────
    {
        "phase": 5,
        "topic_title": "Web Scraping API — FastAPI + Playwright + Background Jobs",
        "topic_description": "Your day job: extract data from platforms via APIs and scraping. Today you wrap a Playwright scraper inside a FastAPI endpoint with background task processing, job status tracking, and results stored in your database.",
        "daily_goal": "Build a /scrape/start endpoint that accepts a URL → returns job_id. Background task scrapes the URL with Playwright → stores result in DB. /scrape/status/{job_id} returns progress.",
        "blogs": [
            {
                "title": "Web Scraping with Python — Real Python",
                "url": "https://realpython.com/python-web-scraping-practical-introduction/",
                "desc": "requests + BeautifulSoup, the foundation of Python scraping",
            },
            {
                "title": "Playwright Python Documentation",
                "url": "https://playwright.dev/python/docs/intro",
                "desc": "Official Playwright Python docs — async scraping, JavaScript-rendered pages",
            },
            {
                "title": "FastAPI + Celery Background Tasks — TestDriven.io",
                "url": "https://testdriven.io/blog/fastapi-and-celery/",
                "desc": "Production-grade background job processing with Redis",
            },
        ],
        "youtube": [
            {
                "title": "Python Web Scraping Full Course — freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=XVv6mJpFOb0",
                "desc": "Scrapy + Playwright — handles JS-rendered pages",
            },
        ],
    },
    {
        "phase": 5,
        "topic_title": "Capstone Day — Full Stack Data API + Review & What's Next",
        "topic_description": "You've come a long way. Today is integration day: build a complete mini data platform — scrape data, store it, expose it via a versioned API, auth-protected, deployed on Cloud Run, with CI/CD. Then plan your next 30 days.",
        "daily_goal": "Deploy your capstone project. Write a README with API docs. Review what was hardest. Research one advanced topic to tackle next: GraphQL, gRPC, Kubernetes, or ML model serving.",
        "blogs": [
            {
                "title": "FastAPI Production Deployment Guide 2026",
                "url": "https://www.zestminds.com/blog/fastapi-deployment-guide/",
                "desc": "Complete production checklist — Docker, GCP, Kubernetes, security",
            },
            {
                "title": "Backend Engineering in 2026 — RefonteLeaning",
                "url": "https://www.refontelearning.com/blog/backend-engineering-in-2026-top-tools-best-practices-and-career-insights",
                "desc": "What to learn next — GraphQL, gRPC, observability, AI APIs",
            },
        ],
        "youtube": [
            {
                "title": "Full FastAPI Production App — Amigoscode",
                "url": "https://www.youtube.com/watch?v=G7JsKmwrMHI",
                "desc": "Production FastAPI app with auth, DB, Docker, deployment",
            },
            {
                "title": "System Design Interview — Tech Dummies",
                "url": "https://www.youtube.com/watch?v=0163cssUxLA",
                "desc": "Design a data platform system — good capstone thinking exercise",
            },
        ],
    },
]