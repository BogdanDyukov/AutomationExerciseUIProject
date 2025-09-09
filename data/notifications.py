from models.notification import Notification

account_created_notification = Notification(
    title='Account Created!',
    main_text='Congratulations! Your new account has been successfully created!',
    additional_text='You can now take advantage of member privileges '
                    'to enhance your online shopping experience with us.'
)

account_deleted_notification = Notification(
    title='Account Deleted!',
    main_text='Your account has been permanently deleted!',
    additional_text='You can create new account to take advantage of member '
                    'privileges to enhance your online shopping experience with us.'
)

order_placed_notification = Notification(
    title='Order Placed!',
    main_text='Congratulations! Your order has been confirmed!',
    additional_text=None
)
