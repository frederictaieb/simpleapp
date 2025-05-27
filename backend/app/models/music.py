from sqlmodel import Field, SQLModel

class MusicBase(SQLModel):
    title: str = Field(index=True)
    artist: str = Field(index=True)
    album: str = Field(index=True)

class Music(MusicBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class MusicCreate(MusicBase):
    pass

class MusicUpdate(SQLModel):  # Tous les champs sont optionnels pour une mise à jour
    title: str | None = None
    artist: str | None = None
    album: str | None = None
