import fakeredis
from worker import process_next_task

def test_worker_task_processing():
    # Use fakeredis to isolate testing from a real running database instance
    mock_redis = fakeredis.FakeRedis(decode_responses=True)
    
    # Run the worker process logic once
    result = process_next_task(mock_redis)
    
    # Assert conditions match expected outcomes
    assert result is True
    assert mock_redis.get("worker_status") == "active"
    assert mock_redis.get("processed_tasks_count") == "1"
