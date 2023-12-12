from stripe._api_resource import APIResource
from stripe._list_object import ListObject
from stripe._stripe_object import StripeObject
from typing import TypeVar

T = TypeVar("T", bound=StripeObject)

# TODO(major): 1704 - remove this class and all internal usages. `.list` is already inlined into the resource classes.
# Although we should inline .auto_paging_iter into the resource classes as well.


class ListableAPIResource(APIResource[T]):
    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject[T]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__,)
            )

        return result
