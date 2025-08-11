from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, float]

    def get_check(
            self,
            name: str,
            products: dict[str, float],
            products_expense: float
    ) -> str:
        check_builder = [
            datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"),
            f"\nThanks, {name}, for your purchase!\nYou have bought:\n",
        ]
        for key in self.products:
            price = products[key] * self.products[key]
            if price == round(price):
                price = round(price)
            check_builder.append(
                f"{products[key]} {key}s for "
                f"{price} dollars\n"
            )
        check_builder.append(
            f"Total cost is {products_expense} dollars\nSee you again!"
        )
        return "".join(check_builder)
