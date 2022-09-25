from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        try:
            self.db.create_collection("auth")
        except Exception as e:
            print("db error ::",e)
        
    def downgrade(self):
        self.db.test_collection.drop()
