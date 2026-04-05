# Import MongoClient to allow the application to connect to MongoDB
from pymongo import MongoClient

class AnimalShelter(object): 
    """ Provides CRUB operations for the MongoDB animal collection with added validation and error handling """

# Initialize the database connection and verify connectivity before CRUB operations begin.
    def __init__(self, username, password):
        """ Initialize MongoDB connection and select the database and collection."""
        try:
            self.client = MongoClient('mongodb://%s:%s@localhost:27017/?authSource=aac' %(username, password))
            self.database = self.client['aac']
            self.collection = self.database['animals']
            self.client.admin.command('ping')
            print("Database connection established successfully.")
        except Exception as e:
            print(f"Database connection error: {e}")
            raise

    # Create method: inserts a new document into the animal collection after validating the input
    def create(self, data):
        """ Insert a new document into the collection ."""
        if data is None:
            raise ValueError("Data parameter is required.")

        if not isinstance(data, dict):
            raise TypeError("Data must  be provided as a dictionary.")
        # Validate incoming data before insertion and handle database errors safely
        try:
            insert_result = self.collection.insert_one(data)
            if insert_result.acknowledged:
                print(f"Record inserted successfully with id: {insert_result.inserted_id}")
                return {"success": True, "inserted_id": str(insert_result.inserted_id)}
            else:
                print("Insertion failed.")
                return {"success": False, "inserted_id": None}
        except Exception as e:
            print(f"Create operation error: {e}")
            return {"success": False, "inserted_id": None}

    # Read method: retrieves matching documents or all documents when no filter is provided
    def read(self, search_data=None):
        """Retrieve documents that match the search criteria."""
        try:
            # Validate that search_data is either a dictionary or None
            if search_data is not None and not isisnstance(search_data, dict):
                raise TypeError("search_data must be a dictionary or None.")

            # Use an empty query if no search criteria is provided
            query = search_data if search_data is not None else {}

            # Execute the query and exclude MongoDB internal _id field
            data = list(self.collection.find(query, {"_id": False}))

            # Output the number of records found
            print(f"Found {len(data)} record(s) matching your query.")
            return data

        except Exception as e:
            # Handle any errors that occur during the read
            print(f"Read operation error: {e}")
            return []

    # Update method: updates matching documents using validated search and update criteria
    def update(self, search_data, update_data):
        """Update documents that match the search criteria."""

        # Ensure both search and update data are provided
        if search_data is None or update_data is None:
            raise ValueError("Both search_data and update_data parameters are required.")

        # Validate that both inputs are dictionaries
        if not isinstance(search_data, dict) or not isinstance(update_data, dict):
            raise TypeError("search_data and update_data must both be dictionaries.")

        try:
            # Apply updates to all matching documents using MongoDB $set operator
            result = self.collection.update_many(search_data, {"$set": update_data})

            # Output how many records were updated
            print(f"Updated {result.modified_count} record(s).")

            return {"success": True, "modified_count": result.modified_count}

        except Exception as e:
            # Handle any errors during the update operation
            print(f"Update operation error: {e}")
            return {"success": False, "modified_count": 0}

    # Delete method: removes matching documents after validating the delete criteria
    def delete(self, delete_data):
        """Delete documents that match the search criteria."""

        # Ensure delete criteria is provided
        if delete_data is None:
            raise ValueError("delete_data parameter is required.")

        # Validate that delete_data is a dictionary
        if not isinstance(delete_data, dict):
            raise TypeError("delete_data must be a dictionary.")

        try:
            # Delete all documents that match the provided criteria
            result = self.collection.delete_many(delete_data)

            # Output how many records were deleted
            print(f"Deleted {result.deleted_count} record(s).")

            return {"success": True, "deleted_count": result.deleted_count}

        except Exception as e:
            # Handle any errors during the delete operation
            print(f"Delete operation error: {e}")
            return {"success": False, "deleted_count": 0}