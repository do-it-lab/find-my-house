"""

"""


class HousingItem(object):
    """

    create_at: 수집일자
    site_id: 수집 사이트 ID
    item_id: 매물 ID
    item_register_date: 매물 등록일자
    item_type: 매물 유형 {아파트, 단독}
    selling_type: 거래 유형 {매매, 전세, 월세}
    price: 매매가
    deposit: 보증금
    monthly_fee: 월세
    yearly_fee: 년세
    exclusive_area: 전용면적
    common_area: 공용면적
    num_of_room: 방 개수
    num_of_toilet: 욕실 개수
    built_date: 준공년도
    num_of_layer: 층 수
    direction: 방향
    special_type: 구조 {복층, 주방 분리}
    loan: 융자
    num_of_household: 세대 수
    monthly_utility: 관리비
    parking_available: 주차 여부
    lat: 위도
    lng: 경도
    description: 기타 설명
    title: 매물 제

    """

    def __init__(self):

        self.create_at = ""
        self.site_id = ""
        self.item_id = ""
        self.item_register_date = ""
        self.item_type = ""
        self.selling_type = ""
        self.price = 0
        self.deposit = 0
        self.monthly_fee = 0
        self.yearly_fee = 0
        self.exclusive_area = 0.0
        self.common_area = 0.0
        self.num_of_room = 0
        self.num_of_toilet = 0
        self.built_date = ""
        self.num_of_layer = 0
        self.direction = ""
        self.special_type = ""
        self.loan = 0
        self.num_of_household = 0
        self.monthly_utility = 0
        self.parking_available = 0
        self.lat = 0.0
        self.lng = 0.0
        self.description = ""
        self.title = ""
