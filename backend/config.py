PHONE_NUMBER = 8472121483
# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('server/saving-data/fireblog/posts')
user = db.reference('users/{0}'.format(new_user.key)).get()

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())