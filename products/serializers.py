from rest_framework import serializers

from .models import Menu, Item, Tag

class ItemSerializer(serializers.ModelSerializer):
    name   = serializers.CharField(max_length=50)
    size   = serializers.CharField(max_length=10)
    price  = serializers.IntegerField(default=0)
    isSold = serializers.BooleanField(default=False)
    
    class Meta:
        model  = Item
        fields = ['id', 'name', 'size', 'price', 'isSold', 'menu']

    def validate(self, value):
        if value not in [Item.L, Item.M, Item.S]:
            raise Exception("value Error")

        return value

    def to_representation(self, instance):
        return {
            'id'    : instance.id,
            'name'  : instance.name,
            'size'  : instance.size,
            'price' : instance.price,
            'isSold': instance.isSold,
            'menuid': instance.menu_id,
        }

class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)

    class Meta:
        model  = Tag
        fields = ['id', 'name', 'type', 'menu']

    def to_representation(self, instance):
        return {
            'id'     : instance.id,
            'name'   : instance.name,
            'type'   : instance.type,
            'menuid' : instance.menu_id,
        }

class MenuSerializer(serializers.ModelSerializer):
    category    = serializers.CharField(max_length=30)
    name        = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=200)
    isSold      = serializers.BooleanField(default=False)
    badge       = serializers.CharField(max_length=8)
    items       = ItemSerializer(required=False, many=True)
    tags        = TagSerializer(required=False, many=True)

    class Meta:
        model = Menu
        fields = ['id', 'category', 'name', 'description', 'isSold', 'badge', 'items', 'tags' ]

    def validate_categoty(self, value):
        if value not in [Menu.SALAD, Menu.MILK, Menu.EGG]:
            raise Exception("value Error")
        
        return value

    def validate_badge(self, value):
        if value not in [Menu.NEW, Menu.OLD]:
            raise Exception("value Error")
    
        return value

    def create(self, validated_data):
        items    = validated_data.pop('items', None)
        tags     = validated_data.pop('tags', None)
        instance = super().create(validated_data)

        if items:
            items_instance = []
            for item_dict in items:
                items_instance.append(
                    Item(
                        name=item_dict.get('name'),
                        size=item_dict.get('size'),
                        price=item_dict.get('price', 0),
                        isSold=item_dict.get('isSold', False),
                        menu=instance
                    )
                )
            Item.objects.bulk_create(items_instance, batch_size=10)

        if tags:
            tags_instance = []
            for tag_dict in tags:
                tags_instance.append(
                    Tag(
                        name=tag_dict.get('name'),
                        type=tag_dict.get('type'),
                        menu=instance
                    )
                )
            Tag.objects.bulk_create(tags_instance, batch_size=10)
        return instance

    def to_representation(self, instance):
        return {
            'id'         : instance.id,
            'category'   : instance.category,
            'name'       : instance.name,
            'description': instance.description,
            'isSold'     : instance.isSold,
            'badge'      : instance.badge,
            'items'      : ItemSerializer(instance.item_set.all(), many=True).data,
            'tags'       : TagSerializer(instance.tag_set.all(), many=True).data,
        }