from sqlalchemy.orm import Session
from app.enums.role_enum import RoleEnum
from app.models.role import Role


def seed_roles(db: Session):
    # for role in RoleEnum:
    #     exists = db.query(Role).filter_by(name=role.value).first()
    #     if not exists:
    #         db.add(Role(name=role.value))
    # db.commit()
    
    role_names = [r.value for r in RoleEnum]
    
    try:
        from sqlalchemy.dialects.postgresql import insert
        statement = insert(Role.__tablename__).values([{"name": name} for name in role_names])
        statement = statement.on_conflict_do_nothing(index_elements=["name"])
        db.execute(statement)
        db.commit()
        return db.query(Role).filter(Role.name.in_(role_names)).all()
    except Exception:
        db.rollback()
        existing = {row[0] for row in db.query(Role.name).filter(Role.name.in_(role_names)).all()}
        to_create = [Role(name=n) for n in role_names if n not in existing]
        if to_create:
            db.add_all(to_create)
            try:
                db.commit()
            except Exception:
                db.rollback()
                raise
        return db.query(Role).filter(Role.name.in_(role_names)).all()