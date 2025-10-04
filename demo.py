from jasonite import Jasonite

def main():
    db = Jasonite("demo_db.json", autosave=True)
    db.create_collection("users")

    print("=== Insert users ===")
    db.insert("users", {"id": "u1", "name": "Alice", "age": 30})
    db.insert("users", {"id": "u2", "name": "Bob", "age": 22})
    db.insert("users", {"id": "u3", "name": "Charlie", "age": 27})

    print(db.find_all("users"))

    print("\n=== Find by id ===")
    print(db.find_by_id("users", "u2"))

    print("\n=== Query with filter (age >= 25) sorted descending ===")
    res = db.find("users", {"age": {"$gte": 25}}, sort=("age", True))
    print(res)

    print("\n=== Upsert (replace or insert) ===")
    db.upsert("users", {"id": "u2", "name": "Bobby", "age": 23})
    db.upsert("users", {"id": "u4", "name": "Diana", "age": 19})
    print(db.find_all("users"))

    print("\n=== Update with find_and_modify ===")
    updated = db.find_and_modify("users", {"id": "u1"}, {"$inc": {"age": 1}, "$set": {"status": "active"}})
    print("Updated:", updated)

    print("\n=== Remove user ===")
    removed = db.find_and_remove("users", {"name": "Charlie"})
    print("Removed:", removed)

    print("\n=== Final users ===")
    print(db.find_all("users"))

if __name__ == "__main__":
    main()
