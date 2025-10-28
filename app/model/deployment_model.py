from datetime import datetime
from . import db

class Deployment(db.Model):
    """Deployment model for storing Kubernetes deployment configurations"""
    __tablename__ = 'deployments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    image = db.Column(db.String(255), nullable=False)
    namespace = db.Column(db.String(100), default='default')
    tier = db.Column(db.Integer)
    ports = db.Column(db.String(255))  # Stored as comma-separated values
    yaml_content = db.Column(db.Text)  # Store the generated YAML
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def to_dict(self):
        """Convert deployment object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'namespace': self.namespace,
            'tier': self.tier,
            'ports': self.ports,
            'yaml_content': self.yaml_content,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Deployment {self.name}>'

class Service(db.Model):
    """Service model for storing Kubernetes service configurations"""
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    namespace = db.Column(db.String(100), default='default')
    tier = db.Column(db.String(50))
    port = db.Column(db.Integer)
    target_port = db.Column(db.Integer)
    node_port = db.Column(db.Integer)
    service_type = db.Column(db.String(50), default='NodePort')
    yaml_content = db.Column(db.Text)  # Store the generated YAML
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    created_by_user = db.relationship('User', backref='services', lazy=True)
    
    def to_dict(self):
        """Convert service object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'namespace': self.namespace,
            'tier': self.tier,
            'port': self.port,
            'target_port': self.target_port,
            'node_port': self.node_port,
            'service_type': self.service_type,
            'yaml_content': self.yaml_content,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Service {self.name}>'
