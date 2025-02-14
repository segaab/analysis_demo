import modal
from env_config import env
from utils.token_validator import TokenValidator

def setup_modal():
    """
    Set up Modal authentication and configuration
    Returns True if successful, False otherwise
    """
    try:
        # Validate tokens first
        if not TokenValidator.validate_modal_token(
            env.MODAL_TOKEN_ID,
            env.MODAL_TOKEN_SECRET
        ):
            raise ValueError("Invalid Modal token format")

        # Initialize Modal client
        modal.setup(
            token_id=env.MODAL_TOKEN_ID,
            token_secret=env.MODAL_TOKEN_SECRET
        )
        return True
    except Exception as e:
        logger.error(f"Error setting up Modal: {e}")
        return False

if __name__ == "__main__":
    # Run setup when script is executed directly
    if setup_modal():
        print("Modal setup successful!")
    else:
        print("Modal setup failed!") 