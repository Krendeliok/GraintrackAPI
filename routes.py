from fastapi import FastAPI
from api import (
    goods,
    promotion,
    reserve,
)


def route(app: FastAPI):
    app.add_api_route("/goods", goods.get_goods, methods=["GET"])
    app.add_api_route("/goods", goods.create_good, methods=["POST"])
    app.add_api_route("/goods/{good_id}", goods.delete_good, methods=["DELETE"])
    app.add_api_route("/goods/{good_id}", goods.update_good, methods=["PUT"])
    app.add_api_route("/goods/{good_id}/sell", goods.sell_good, methods=["POST"])
    app.add_api_route("/promotion", promotion.create_promotion, methods=["POST"])
    app.add_api_route("/reserve/{good_id}", reserve.reserve_good, methods=["POST"])
    app.add_api_route("/reserve/{good_id}", reserve.unreserve_good, methods=["DELETE"])
