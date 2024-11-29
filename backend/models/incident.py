from utils.database import db

class Incident(db.Model):
    __tablename__ = 'incidents'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "category": self.category,
            "severity": self.severity,
            "timestamp": self.timestamp,
        }
