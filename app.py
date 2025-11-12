from app import app, config

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app", 
        host=config.HOST, 
        port=config.PORT,
        log_level=config.LOG_LEVEL,
        reload=config.RELOAD
    )