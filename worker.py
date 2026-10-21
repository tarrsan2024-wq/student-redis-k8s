import os
import time
import redis

# Load configurations from environment variables (Critical for Kubernetes)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def connect_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def process_next_task(r):
    try:
        # Simulate an event-driven status processing task
        r.set("worker_status", "active")
        r.incr("processed_tasks_count")
        return True
    except redis.ConnectionError:
        print("Waiting for Redis database connection...")
        return False

if __name__ == "__main__":
    print(f"Connecting to Redis host at: {REDIS_HOST}:{REDIS_PORT}")
    db = connect_redis()
    while True:
        success = process_next_task(db)
        if success:
            print("Successfully connected to cache engine! Task processed.")
        time.sleep(5)  # Run tasks continuously every 5 seconds
