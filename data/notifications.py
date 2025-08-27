from models.notification import Notification

account_created_notification = Notification(
    title='Account Created!',
    main='Congratulations! Your new account has been successfully created!',
    additional='You can now take advantage of member privileges '
               'to enhance your online shopping experience with us.'
)

account_deleted_notification = Notification(
    title='Account Deleted!',
    main='Your account has been permanently deleted!',
    additional='You can create new account to take advantage of member '
               'privileges to enhance your online shopping experience with us.'
)
