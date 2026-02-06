import logging

from sqlalchemy.orm import Session

from app.db.database import engine
from app.utils.seed_roles import seed_roles

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    with Session(engine) as session:
        seed_roles(session)
        
def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()