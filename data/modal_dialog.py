from models.modal_dialog import ModalDialog

checkout_modal = ModalDialog(
    title='Checkout',
    note_text='Register / Login account to proceed on checkout.',
    navigation_link_text='Register / Login',
    continue_button_text='Continue On Cart'
)

added_to_cart_modal = ModalDialog(
    title='Added!',
    note_text='Your product has been added to cart.',
    navigation_link_text='View Cart',
    continue_button_text='Continue Shopping'
)
