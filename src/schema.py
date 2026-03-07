from pydantic import (
    BaseModel,
    Field,
    AnyUrl,
    field_validator,
    model_validator,
    computed_field
)
from typing import (
    Annotated,
    Literal,
    Optional,
    List
)

class CustomerData(BaseModel):

    Age: Annotated[
        int,
        Field(
            ge=1,
            le=100,
            strict=True,
            description="Age must be greater than 0 or less than equal to 100"
        )
    ]=1
    Education: Annotated[
        int,
        Field(
            ge=0,
            le=4,
            description="Education = ('Basic':0,2n 'Cycle':1,'Graduation':2,'Master':3,'PhD':4)"
        )
    ]=0
    Marital_Status: Annotated[
        int,
        Field(
            ge=0,
            le=1,
            description="1 for married othervise 0"
        )
    ]=1
    Parental_Status: Annotated[
        int ,
        Field(
            default=0,
            ge=0,
            le=1
        )
    ]
    Children: Optional[int] = Field(ge=0,default=0,description="No. of children")
    Income: Annotated[
        float,
        Field(
            ge=1000,
            strict=True,
            description="Customer Income"
        )
    ]=1000
    Total_Spending: Annotated[
        float,
        Field(
            ge=1000,
            strict=True,
            description="Total money spending"
        )
    ]=1000
    Days_as_Customer: Annotated[
        int,
        Field(
            ge=1,
            strict=True
        )
    ]=1
    Recency: Annotated[
        int ,
        Field(
            ge=1,
            strict=True
        )
    ]=1
    Wines: Optional[float] = Field(
            ge=0,
            default=0,
            description="Total amount spend on wines in last 2 yrs"
        )
    Fruits: Optional[float] = Field(
            ge=0,
            default=0,
            description="Total amount spend on Fruits in last 2 yrs"
        )
    Meat: Optional[float] = Field(
            ge=0,
            default=0,
            description="Total amount spend on Meat in last 2 yrs"
        )
    Fish: Optional[float] = Field(
            ge=0,
            default=0,
            description="Total amount spend on Fish in last 2 yrs"
        )
    Sweets: Optional[float] = Field(
            ge=0,
            default=0,
            description="Total amount spend on Sweets in last 2 yrs"
        )
    Gold: Optional[float] = Field(
            ge=0,
            default=0,
            description="Total amount spend on Gold in last 2 yrs"
        )

    Web: Optional[int] = Field(
            ge=0,
            default=0,
            description="Number of purchase made through the company's website"
        )
    Catalog: Optional[int] = Field(
            ge=0,
            default=0,
            description="Number of purchase made using a Catalog"
        )
    Store: Optional[int] = Field(
            ge=0,
            default=0,
            description="Number of purchase made through the store"
        )
    Discount_Purchases: Optional[int] = Field(
            ge=0,
            default=0,
            description="Number of purchase made with discount"
        )
    TotalPromo: Optional[int] = Field(
            ge=0,
            default=0,
            description="Number of promotion offer customer has accepted"
        )
    NumWebVisitsMonth: Optional[int] = Field(
            ge=0,
            default=0,
            description="Number of visits to company in the last month"
        )