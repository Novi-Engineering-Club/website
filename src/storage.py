from abc import ABC, abstractmethod
from pathlib import Path
from werkzeug.security import safe_join

class BaseStorage(ABC):
    @abstractmethod
    def list_files(self):
        """List all available page files relative to storage root."""
        pass

    @abstractmethod
    def get_content(self, path):
        """Get content of a file."""
        pass

    @abstractmethod
    def save_content(self, path, content):
        """Save content to a file."""
        pass

    @abstractmethod
    def delete_content(self, path):
        """Delete a file."""
        pass
    
    @abstractmethod
    def exists(self, path):
        """Check if file exists."""
        pass

class FileSystemStorage(BaseStorage):
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.root_dir.mkdir(parents=True, exist_ok=True)

    def _get_full_path(self, path):
        # Ensure we don't escape the root directory
        full_path = safe_join(str(self.root_dir), str(path))
        if full_path is None:
            raise ValueError(f"Invalid path: {path}")
        return Path(full_path)

    def list_files(self):
        files = []
        for file_path in self.root_dir.rglob("*.html"):
            files.append(file_path.relative_to(self.root_dir).as_posix())
        return files

    def get_content(self, path):
        full_path = self._get_full_path(path)
        return full_path.read_text(encoding="utf-8")

    def save_content(self, path, content):
        full_path = self._get_full_path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding="utf-8")

    def delete_content(self, path):
        full_path = self._get_full_path(path)
        if full_path.exists():
            full_path.unlink()

    def exists(self, path):
        try:
            full_path = self._get_full_path(path)
            return full_path.exists()
        except ValueError:
            return False

def get_storage(storage_type="filesystem", **kwargs):
    if storage_type == "filesystem":
        return FileSystemStorage(kwargs.get("root_dir"))
    # Add other storage backends here
    raise ValueError(f"Unknown storage type: {storage_type}")
