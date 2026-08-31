
from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import text
from database.connection import SessionLocal
from sqlalchemy.orm import Session
from calendar import datetime



router = APIRouter(
    prefix="/analitics",
    tags=["analitics"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard")
def obtener_dashboard(db: Session = Depends(get_db)):
    query = text("""
        SELECT
            total_registros,
            promedio_monto,
            pagos_realizados,
            pagos_pendientes,
            porcentaje_cumplimiento,
            total_estudiantes,
            media_estudiantes
        FROM analytics_dashboard
    """)

    result = db.execute(query).mappings().all()
    return {
        "fecha de generación": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "datos": [dict(row) for row in result],
    }