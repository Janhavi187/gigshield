"""
GigShield — AI-Powered Parametric Insurance Platform
FastAPI Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Route imports (to be implemented)
# from app.api import auth, user, policy, claims, analytics

app = FastAPI(
    title="GigShield API",
    description="AI-Powered Parametric Insurance for Gig Workers",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
# app.include_router(auth.router,     prefix="/api/auth",      tags=["Auth"])
# app.include_router(user.router,     prefix="/api/user",      tags=["User"])
# app.include_router(policy.router,   prefix="/api/policy",    tags=["Policy"])
# app.include_router(claims.router,   prefix="/api/claims",    tags=["Claims"])
# app.include_router(analytics.router,prefix="/api/analytics", tags=["Analytics"])


@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "message": "GigShield API is running 🛡️"}


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}
