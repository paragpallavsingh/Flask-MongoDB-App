db = db.getSiblingDB("task_db");
db.task_db.drop();

db.task_db.insertMany([
    {
        "task": "Task1",
        "result": "Make homepage",
    }, 
    {
        "task": "Task2",
        "result": "Make Tasks Page",
    }, 
    {
        "task": "Task3",
        "result": "Setup project on Github",
    }, 
]);
