# Api Information

## Description

### Directories
- `api/` - Contains the API code
- `models/` - Contains the models for DB
- `services/` - Contains the API logic


### Methods
- `api/goods.py`:
    - `get_goods` - Return list of goods
    - `delete_good` - Delete good by id
    - `update_good` - Update a good`s fields by id
    - `create_good` - Create a new good
    - `sell_good` - Sell a good by id
- `api/promotion.py`:
    - `create_promotion` - Create a new promotion
- `api/reserve.py`:
    - `reserve_good` - Reserve a good by user
    - `unreserve_good` - Delete a reservation by id

### Swagger is available at `/docs`