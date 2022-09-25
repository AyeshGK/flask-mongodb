from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        student_validator= {
                "$jsonSchema": {
                "bsonType": "object",
                "title": "Student Object Validation",
                "required": [ "address", "major", "name", "year" ],
                    "properties": {
                    "name": {
                    "bsonType": "string",
                    "description": "'name' must be a string and is required"
                },
                "year": {
                    "bsonType": "int",
                    "minimum": 2017,
                    "maximum": 3017,
                    "description": "'year' must be an integer in [ 2017, 3017 ] and is required"
                },
                "gpa": {
                    "bsonType": [ "double" ],
                    "description": "'gpa' must be a double if the field exists"
                }
            }
        }
    }
        try:
            self.db.create_collection("student")
        except Exception as e:
            print("db error ::",e)
        self.db.command("collMod","student",validator=student_validator)

    def downgrade(self):
        self.db.student.drop()
