ADD_MEMORY_TOOL = {
    "type": "function",
    "function": {
        "name": "add_memory",
        "description": "Use this function to add a new memory when the new information which does not already exist in the current memory list.",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string", "description": "Data to add to memory"}
            },
            "required": ["data"],
        },
    },
}

UPDATE_MEMORY_TOOL = {
    "type": "function",
    "function": {
        "name": "update_memory",
        "description": "Use this function to update an existing memories by IDs when new memories enhance or correct the existing memories.",
        "parameters": {
            "type": "object",
            "properties": {
                "memory_id": {
                    "type": "string",
                    "description": "memory_id of the memory to update",
                },
                "data": {
                    "type": "string",
                    "description": "Updated data for the memory",
                },
            },
            "required": ["memory_id", "data"],
        },
    },
}

DELETE_MEMORY_TOOL = {
    "type": "function",
    "function": {
        "name": "delete_memory",
        "description": "Use this function to delete a memories by IDs when new memories directly contradict or invalidate the existing memories.",
        "parameters": {
            "type": "object",
            "properties": {
                "memory_id": {
                    "type": "string",
                    "description": "memory_id of the memory to delete",
                }
            },
            "required": ["memory_id"],
        },
    },
}
