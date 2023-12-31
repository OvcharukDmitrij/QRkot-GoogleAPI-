from typing import Optional, List, Dict

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        """Получение id проекта по его имени."""

        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()

        return db_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[Dict[str, str]]:
        projects = await session.execute(
            select(CharityProject).where(CharityProject.fully_invested)
        )

        close_projects = [
            {
                'name': project.name,
                'period': project.close_date - project.create_date,
                'description': project.description,
            } for project in projects.scalars().all()
        ]

        close_projects = sorted(close_projects, key=lambda x: x['period'])
        return close_projects


charityproject_crud = CRUDCharityProject(CharityProject)
