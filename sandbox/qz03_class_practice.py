"""A class written for example for QZ03."""

from __future__ import annotations


class ChristmasTreeFarm:
    """Represents a Christmas Tree Farm as a class."""

    plots: list[int]
    
    def __init__(self, plots: int, initial_planting: int):
        """Initializes."""
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        
        while i < plots:
            self.plots.append(0)
            i += 1

    def plant(self, planted: int) -> None:
        """Plants or uproots a tree."""
        self.plots[planted] = 1

    def growth(self) -> None:
        """Growing."""
        for trees in self.plots:
            if trees > 0:
                trees += 1
    
    def harvest(self, replant: bool) -> int:
        """HArvesting."""
        result: int = 0
        for trees in self.plots:
            if trees >= 5:
                if replant:
                    trees = 1
                else:
                    trees = 0
                result += 1
                
        return result

    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Adding."""
        r_size: int = len(self.plots) + len(rhs.plots)
        r_plantings: int = 0

        for trees in self.plots:
            if trees >= 1:
                r_plantings += 1

        for trees in rhs.plots:
            if trees >= 1:
                r_plantings += 1

        result: ChristmasTreeFarm = ChristmasTreeFarm(r_size, r_plantings)
        return result


class Course:
    """Models UNC course."""
    name: str
    level: int
    prerequisites: list[str]
    
    def is_valid_course(self, prereq: str) -> bool:
        """Is it valid?"""
        result: bool = False
        if self.level >= 400:
            for classes in self.prerequisites:
                if classes == prereq:
                    result = True
        return result
                    

def find_courses(courses: list[Course], search: str) -> list[str]:
    """Finds courses."""
    result: list[str] = []
    for course in courses:
        if course.level >= 400:
            if search in course.prerequisites:
                result.append(course.name)

    return result