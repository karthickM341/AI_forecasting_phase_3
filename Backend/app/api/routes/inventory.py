from fastapi import APIRouter

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

inventory_data = []


@router.post("/add")
def add_inventory(data: dict):

    item = {
        "id": len(inventory_data) + 1,
        "product_name": data["product_name"],
        "stock": data["stock"],
        "price": data["price"]
    }

    inventory_data.append(item)

    return {
        "message": "Inventory added successfully",
        "data": item
    }


@router.get("/")
def get_inventory():

    return {
        "inventory": inventory_data
    }


@router.get("/{item_id}")
def get_single_inventory(item_id: int):

    for item in inventory_data:

        if item["id"] == item_id:
            return item

    return {
        "message": "Item not found"
    }


@router.put("/update/{item_id}")
def update_inventory(item_id: int, data: dict):

    for item in inventory_data:

        if item["id"] == item_id:

            item["stock"] = data["stock"]
            item["price"] = data["price"]

            return {
                "message": "Inventory updated",
                "data": item
            }

    return {
        "message": "Item not found"
    }


@router.delete("/delete/{item_id}")
def delete_inventory(item_id: int):

    for item in inventory_data:

        if item["id"] == item_id:

            inventory_data.remove(item)

            return {
                "message": "Inventory deleted"
            }

    return {
        "message": "Item not found"
    }


@router.get("/analytics/summary")
def inventory_summary():

    total_items = len(inventory_data)

    total_stock = sum(
        item["stock"]
        for item in inventory_data
    )

    total_value = sum(
        item["stock"] * item["price"]
        for item in inventory_data
    )

    return {
        "total_items": total_items,
        "total_stock": total_stock,
        "total_inventory_value": total_value
    }