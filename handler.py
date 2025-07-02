import runpod
import time
def handler(job):
    """
    This is a simple handler that takes a name as input and returns a greeting.
    The job parameter contains the input data in job["input"]
    """
    job_input = job["input"]
    
    # Get the name from the input, default to "World" if not provided
    name = job_input.get("name", "World")

    for update_number in range(0, 3):
        time.sleep(10)  # Simulate a long-running task
        runpod.serverless.progress_update(job, f"Update {update_number}/3")
    # Return a greeting message
    return f"Hello, {name}! Welcome to RunPod Serverless! How are you doing?"

# Start the serverless function
runpod.serverless.start({"handler": handler})
