FROM python:3.12.8-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /srv
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app ./app
RUN useradd --create-home --uid 10001 service && mkdir -p /data/cache && chown -R service /data
USER service

# Persistent Tavily response cache, and the archive (/data/archive.sqlite) that keeps every cached response
# after the cache's TTL removes it (mount a volume here to keep both across restarts)
ENV TAVILY_CACHE_DIR=/data/cache
VOLUME ["/data"]

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import sys, urllib.request; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=4).status == 200 else 1)"

# Keys come from the environment (SERVICE_API_KEY, TAVILY_API_KEY, OPENAI_API_KEY); see .env.example.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2", "--no-server-header"]
